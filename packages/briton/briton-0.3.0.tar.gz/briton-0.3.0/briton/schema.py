import json
import random
import string
import time
from json import JSONDecodeError
from typing import (
    Any,
    AsyncGenerator,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Union,
    cast,
)

import openai.types.chat.chat_completion as chat_completion
import openai.types.chat.chat_completion_chunk as chat_completion_chunk
from fastapi import HTTPException
from jinja2.exceptions import TemplateError
from openai.types.chat import ChatCompletion, ChatCompletionChunk
from openai.types.chat.chat_completion_message import ChatCompletionMessage
from openai.types.chat.chat_completion_message_tool_call import (
    ChatCompletionMessageToolCall,
    Function,
)
from openai.types.completion_usage import CompletionUsage
from pydantic import BaseModel, Field, ValidationError, model_validator
from transformers import PreTrainedTokenizerFast


class ModelInput(BaseModel):
    """This class mirrors the `CompletionCreateParamsBase` in the `openai-python` repository.

    However, that class is a TypedDict rather than a pydantic model, so we redefine it here
    to take advantage of pydantic's validation features. In addition, we define helper methods
    to get the formatted prompt, tools to use, and response format to adhere to.

    Unsupported parameters:
    - https://platform.openai.com/docs/api-reference/chat/create#chat-create-store
      - OpenAI platform specific
    - https://platform.openai.com/docs/api-reference/chat/create#chat-create-metadata
      - OpenAI platform specific
    - https://platform.openai.com/docs/api-reference/chat/create#chat-create-frequency_penalty
      - Frequency penalty is not currently passed through to briton
    - https://platform.openai.com/docs/api-reference/chat/create#chat-create-logit_bias
      - User provided logit biasing is not implemented
    - https://platform.openai.com/docs/api-reference/chat/create#chat-create-logprobs
      - Returning log probabilities is not implemented
    - https://platform.openai.com/docs/api-reference/chat/create#chat-create-top_logprobs
      - Returning log probabilities is not implemented
    - https://platform.openai.com/docs/api-reference/chat/create#chat-create-n
      - Multiple generation is not implemented
    - https://platform.openai.com/docs/api-reference/chat/create#chat-create-service_tier
      - OpenAI platform specific
    - https://platform.openai.com/docs/api-reference/chat/create#chat-create-stop
      - Stop words are not implemented
    - https://platform.openai.com/docs/api-reference/chat/create#chat-create-user
      - OpenAI platform specific
    - https://platform.openai.com/docs/api-reference/chat/create#chat-create-function_call
      - Deprecated
    - https://platform.openai.com/docs/api-reference/chat/create#chat-create-functions
      - Deprecated
    """

    class Tool(BaseModel):
        """An element in the top level `tools` field."""

        class Function(BaseModel):
            name: str
            description: str
            parameters: Dict[str, Any]  # `parameters` holds the json schema
            return_: Optional[Dict[str, Any]] = Field(None, alias="return")

        type: Literal["function"]
        function: Function

        @property
        def json_schema(self) -> Dict[str, Any]:
            return {
                "type": "object",
                "properties": {
                    "name": {"const": self.function.name},
                    "parameters": self.function.parameters,
                },
                "required": ["name", "parameters"],
            }

    class ToolChoice(BaseModel):
        """The top level `tool_choice` field."""

        class FunctionChoice(BaseModel):
            name: str

        type: Literal["function"]
        function: FunctionChoice

    class SchemaResponseFormat(BaseModel):
        """The top level `response_format` field."""

        class JsonSchema(BaseModel):
            """`schema_` holds the actual json schema"""

            schema_: Dict[str, Any] = Field(..., alias="schema")

        type: Literal["json_schema"]
        json_schema: JsonSchema

    class JsonResponseFormat(BaseModel):
        type: Literal["json_object"]

    class TextResponseFormat(BaseModel):
        type: Literal["text"]

    class StreamOptions(BaseModel):
        """The top level `stream_options` field."""

        include_usage: bool

    model: Optional[str] = Field("")

    # TODO: Define `Message` objects to mirror `ChatCompletionMessageParam` for validation
    messages: Optional[List[Dict[str, Any]]] = Field(None)
    prompt_: Optional[str] = Field(None, min_length=1, alias="prompt")

    max_tokens_: Optional[int] = Field(None, alias="max_tokens")
    max_completion_tokens: Optional[int] = Field(None)

    stream: Optional[bool] = Field(False)
    stream_options: Optional[StreamOptions] = Field(None)

    seed_: Optional[int] = Field(None, alias="seed")
    random_seed: Optional[int] = Field(None)

    frequency_penalty: Optional[float] = Field(0)
    presence_penalty: Optional[float] = Field(0)
    length_penalty: Optional[float] = Field(None)

    temperature: Optional[float] = Field(1)
    top_p_: Optional[float] = Field(1, alias="top_p")
    runtime_top_p: Optional[float] = Field(None)
    top_k_: Optional[int] = Field(None, alias="top_k")
    runtime_top_k: Optional[int] = Field(None)

    response_format: Optional[
        Union[SchemaResponseFormat, JsonResponseFormat, TextResponseFormat]
    ] = Field(None)
    tools_: Optional[List[Tool]] = Field(None, alias="tools")
    tool_choice: Optional[Union[Literal["none", "required", "auto"], ToolChoice]] = Field(None)
    parallel_tool_calls: Optional[bool] = Field(True)

    beam_width: Optional[Literal[1]] = Field(None)

    end_id: Optional[int] = Field(None)
    pad_id: Optional[int] = Field(None)

    _generated_seed: Optional[int] = None

    @model_validator(mode="after")
    def messages_not_empty(cls, values):
        messages = values.messages
        if messages is not None and len(messages) == 0:
            raise ValueError("`messages` cannot be empty.")
        return values

    @model_validator(mode="after")
    def oneof_messages_and_prompt_set(cls, values):
        prompt = values.prompt_
        messages = values.messages
        if prompt is None and messages is None:
            raise ValueError("One of `prompt` or `messages` must be specified.")
        if prompt is not None and messages is not None:
            raise ValueError("Only one of `prompt` and `messages` can be specified.")
        return values

    @model_validator(mode="after")
    def max_tokens_and_max_completion_tokens_not_set(cls, values):
        max_tokens = values.max_tokens_
        max_completion_tokens = values.max_completion_tokens
        if max_tokens is not None and max_completion_tokens is not None:
            raise ValueError(
                "Only one of `max_tokens` and `max_completion_tokens` can be specified."
            )
        return values

    @model_validator(mode="after")
    def tools_valid(cls, values):
        tools = values.tools_
        tool_choice = values.tool_choice
        if tools is not None and tool_choice is None:
            values.tool_choice = "auto"
        if tools is not None and len(tools) == 0 and tool_choice != "none":
            raise ValueError("`tools` cannot be empty.")
        if isinstance(tool_choice, cls.ToolChoice) and tool_choice.function.name not in [
            tool.function.name for tool in tools
        ]:
            raise ValueError("`tool_choice` not in `tools`.")
        return values

    @model_validator(mode="after")
    def tools_not_used_with_prompt(cls, values):
        prompt = values.prompt_
        tool_choice = values.tool_choice
        if prompt is not None and tool_choice is not None and tool_choice != "none":
            raise ValueError("`tool_choice` cannot be used with `prompt`.")
        return values

    @model_validator(mode="after")
    def tools_not_used_with_response_format(cls, values):
        response_format = values.response_format
        tool_choice = values.tool_choice
        if response_format is not None and tool_choice is not None and tool_choice != "none":
            raise ValueError("`tools` cannot be used with `response_format`.")
        return values

    @model_validator(mode="after")
    def adjust_temperature_for_greedy_decoding(cls, values):
        if values.temperature == 0:
            values.temperature = 0.01
            values.top_k_ = 0
            values.top_p_ = 0.0
        return values

    @property
    def force_tools(self) -> Optional[bool]:
        if self.tool_choice is not None and self.tool_choice != "none":
            return self.tool_choice == "required" or isinstance(self.tool_choice, self.ToolChoice)
        return None

    @property
    def tools(self) -> Optional[List[Tool]]:
        """Returns the tools to use, dependent on tool_choice."""
        if self.tool_choice is not None and self.tool_choice != "none":
            if self.tools_ is None:
                raise ValueError("`tools` must be specified with `tool_choice`.")
            if isinstance(self.tool_choice, self.ToolChoice):
                return [
                    tool
                    for tool in self.tools_
                    if tool.function.name == self.tool_choice.function.name
                ]
            return self.tools_
        return None

    @property
    def _tool_dicts(self) -> Optional[List[Dict[str, Any]]]:
        """Convenience property to get all tools as plain dicts."""
        return (
            [tool.model_dump(by_alias=True) for tool in self.tools]
            if self.tools is not None
            else None
        )

    @property
    def output_json_schema(self) -> Optional[Dict[str, Any]]:
        """Creates the output json schema based on the response format or tools."""
        if isinstance(self.response_format, self.SchemaResponseFormat):
            return self.response_format.json_schema.schema_
        if isinstance(self.response_format, self.TextResponseFormat):
            return None
        if isinstance(self.response_format, self.JsonResponseFormat):
            return {}
        tools = self.tools
        if tools is not None:
            schema = {
                "type": "array",
                "items": {"anyOf": [tool.json_schema for tool in tools]},
                "minItems": 1,
            }
            if self.parallel_tool_calls == False:
                schema["maxItems"] = 1
            return schema
        return None

    @property
    def max_tokens(self) -> Optional[int]:
        """`max_tokens` was deprecated in favor of `max_completion_tokens`"""
        return self.max_tokens_ if self.max_tokens_ is not None else self.max_completion_tokens

    @property
    def top_p(self) -> Optional[float]:
        """`top_p` was previously named `runtime_top_p` in briton"""
        return self.top_p_ if self.top_p_ is not None else self.runtime_top_p

    @property
    def top_k(self) -> Optional[int]:
        """`top_k` was previously named `runtime_top_k` in briton"""
        return self.top_k_ if self.top_k_ is not None else self.runtime_top_k

    @property
    def seed(self) -> int:
        """`seed` was previously named `random_seed` in briton"""
        if self.seed_ is not None:
            return self.seed_
        if self.random_seed is not None:
            return self.random_seed
        if self._generated_seed is None:
            self._generated_seed = random.randint(-(2**63), 2**63 - 1)
        return self._generated_seed

    @property
    def include_stream_usage(self) -> bool:
        return self.stream_options is not None and self.stream_options.include_usage

    @property
    def combined_messages(self) -> List[Dict[str, Any]]:
        """Combine consecutive user messages into a single message to avoid chat template errors."""
        if not self.messages:
            return []

        combined_messages = []
        current_user_message = None

        for message in self.messages:
            if message["role"] == "user":
                if current_user_message:
                    # OpenAI combines user messages with a space and newline
                    current_user_message["content"] += f" \n{message['content']}"
                else:
                    current_user_message = message.copy()
            else:
                if current_user_message:
                    combined_messages.append(current_user_message)
                    current_user_message = None
                combined_messages.append(message)

        if current_user_message:
            combined_messages.append(current_user_message)

        return combined_messages

    def prompt(self, tokenizer: PreTrainedTokenizerFast) -> str:
        """Calculate text prompt from model_input.

        Prompt may be supplied in the input as such or as messages. If messages
        are supplied, they are used to generate the prompt using chat template.
        """
        if self.prompt_ is None:
            if self.messages is None:
                raise ValueError("`messages` must be specified.")
            return cast(
                str,
                tokenizer.apply_chat_template(
                    conversation=self.combined_messages,
                    tools=self._tool_dicts,
                    tokenize=False,
                    add_generation_prompt=True,
                ),
            )
        return self.prompt_


class ModelInputWithoutTools(ModelInput):
    """Input class for models that don't support function calling."""

    @model_validator(mode="after")
    def tools_not_used(cls, values):
        if values.tools is not None:
            raise ValueError("This model does not support `tools`.")
        return values


def get_prompt(model_input: ModelInput, tokenizer: PreTrainedTokenizerFast) -> str:
    try:
        return model_input.prompt(tokenizer)
    except (ValueError, TemplateError) as e:
        raise HTTPException(status_code=400, detail=str(e))


def validate_model_input(model_input: Dict[str, Any], supports_tools: bool = True) -> ModelInput:
    try:
        if supports_tools:
            return ModelInput(**model_input)
        else:
            return ModelInputWithoutTools(**model_input)
    except (ValueError, ValidationError) as e:
        raise HTTPException(status_code=400, detail=str(e))


def update_raw_model_input(model_input: Dict[str, Any], validated_input: ModelInput) -> None:
    """Updates the `model_input` dictionary with values from the `validated_input` object.

    This is need in cases where 1) the field names different between the spec and briton
    and 2) where we override values (in the case of `seed` or `temperature`).

    Parameters:
    - model_input (Dict[str, Any]): The raw model input.
    - validated_input (ModelInput): The validated model input.
    """
    if validated_input.max_tokens is not None:
        model_input["max_tokens"] = validated_input.max_tokens
    if validated_input.top_k is not None:
        model_input["runtime_top_k"] = validated_input.top_k
    if validated_input.top_p is not None:
        model_input["runtime_top_p"] = validated_input.top_p
    if validated_input.temperature is not None:
        model_input["temperature"] = validated_input.temperature
    model_input["random_seed"] = validated_input.seed


def _load_content_json(content: str) -> Any:
    """Safely load the content json from the input text."""
    try:
        return json.loads(content)
    except JSONDecodeError:
        raise HTTPException(status_code=400, detail="Tool call was cut off by max_tokens.")


def _generate_tool_call_id():
    """Mistral expects a length 9 alphanumeric id"""
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(9))


def _create_tool_calls(content: str) -> List[ChatCompletionMessageToolCall]:
    content_json = _load_content_json(content)
    tool_calls = []
    for briton_fn in content_json:
        fn = Function(name=briton_fn["name"], arguments=str(briton_fn["parameters"]))
        tool_call = ChatCompletionMessageToolCall(
            id=_generate_tool_call_id(), function=fn, type="function"
        )
        tool_calls.append(tool_call)
    return tool_calls


def create_completion(
    req_id: str,
    model: str,
    input_text: str,
    eos_token: str,
    tool_token: str,
    prompt_tokens: Optional[int] = None,
    completion_tokens: Optional[int] = None,
) -> ChatCompletion:
    created = int(time.time())
    finish_reason = "stop" if input_text.endswith(eos_token) else "length"
    content = input_text.removesuffix(eos_token)
    tool_calls = None
    if content.startswith(tool_token):
        content = content.removeprefix(tool_token)
        tool_calls = _create_tool_calls(content)
        content = None
    message = ChatCompletionMessage(content=content, role="assistant", tool_calls=tool_calls)
    choice = chat_completion.Choice(finish_reason=finish_reason, index=0, message=message)
    usage = None
    if prompt_tokens is not None and completion_tokens is not None:
        usage = CompletionUsage(
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=prompt_tokens + completion_tokens,
        )
    return ChatCompletion(
        id=req_id,
        choices=[choice],
        created=created,
        model=model,
        object="chat.completion",
        usage=usage,
    )


def _make_sse_chunk(chunk: ChatCompletionChunk) -> str:
    return f"data: {chunk.model_dump_json()}\n\n"


# It's the responsibility of the caller to pass the full content
def _create_tool_call_deltas(
    content: str,
) -> List[chat_completion_chunk.ChoiceDeltaToolCall]:
    content_json = _load_content_json(content)
    tool_call_deltas = []
    for i, briton_fn in enumerate(content_json):
        fn = chat_completion_chunk.ChoiceDeltaToolCallFunction(
            name=briton_fn["name"], arguments=str(briton_fn["parameters"])
        )
        tool_call_delta = chat_completion_chunk.ChoiceDeltaToolCall(
            index=i, id=_generate_tool_call_id(), function=fn, type="function"
        )
        tool_call_deltas.append(tool_call_delta)
    return tool_call_deltas


def _create_completion_chunk(
    id: str,
    created: int,
    model: str,
    content: Optional[str] = None,
    role: Optional[Literal["system", "user", "assistant", "tool"]] = None,
    finish_reason: Optional[
        Literal["stop", "length", "tool_calls", "content_filter", "function_call"]
    ] = None,
    tool_calls: Optional[List[chat_completion_chunk.ChoiceDeltaToolCall]] = None,
    usage: Optional[CompletionUsage] = None,
) -> ChatCompletionChunk:
    delta = chat_completion_chunk.ChoiceDelta(content=content, role=role, tool_calls=tool_calls)
    choice = chat_completion_chunk.Choice(index=0, delta=delta, finish_reason=finish_reason)
    return ChatCompletionChunk(
        id=id,
        choices=[choice],
        created=created,
        model=model,
        object="chat.completion.chunk",
        usage=usage,
    )


async def create_completion_chunks(
    req_id: str,
    model: str,
    input_text: AsyncGenerator[str, None],
    eos_token: str,
    tool_token: str,
    prompt_tokens: Optional[int] = None,
    completion_tokens_fn: Optional[Callable[[], int]] = None,
) -> AsyncGenerator[str, None]:
    created = int(time.time())
    start_chunk = _create_completion_chunk(
        id=req_id, created=created, model=model, content="", role="assistant"
    )
    is_first_iter = True
    delta = None
    async for delta in input_text:
        if is_first_iter:
            if delta.startswith(tool_token):
                break
            is_first_iter = False
            yield _make_sse_chunk(start_chunk)
        content = delta.removesuffix(eos_token)
        if len(content) == 0:
            continue  # Don't send empty chunks
        chunk = _create_completion_chunk(id=req_id, created=created, model=model, content=content)
        yield _make_sse_chunk(chunk)

    # Handle function call case
    if is_first_iter and delta is not None and delta.startswith(tool_token):
        full_text = delta.removeprefix(tool_token)
        async for delta in input_text:
            full_text += delta
        tool_calls = _create_tool_call_deltas(full_text.removesuffix(eos_token))
        chunk = _create_completion_chunk(
            id=req_id, created=created, model=model, tool_calls=tool_calls
        )
        yield _make_sse_chunk(start_chunk)
        yield _make_sse_chunk(chunk)
        finish_reason = "tool_calls"
    else:
        finish_reason = "stop" if delta is not None and delta.endswith(eos_token) else "length"
    end_chunk = _create_completion_chunk(
        id=req_id, created=created, model=model, finish_reason=finish_reason
    )
    yield _make_sse_chunk(end_chunk)
    if prompt_tokens is not None and completion_tokens_fn is not None:
        completion_tokens = completion_tokens_fn()
        usage = CompletionUsage(
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=prompt_tokens + completion_tokens,
        )
        usage_chunk = _create_completion_chunk(id=req_id, created=created, model=model, usage=usage)
        yield _make_sse_chunk(usage_chunk)
    yield "data: [DONE]\n\n"

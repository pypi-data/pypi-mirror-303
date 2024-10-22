# TODO(pankaj) Pick this from truss constants, once a small lib is extracted out of truss.
OPENAI_COMPATIBLE_TAG = "openai-compatible"
DEFAULT_BRITON_PORT = 50051
DEFAULT_TP_COUNT = 1

# Use a directory that can be picked up by baseten-fs, if enabled
FSM_CACHE_DIR = "/cache/model/fsm_cache"

DEFAULT_MAX_FSM_WORKERS = 10

TOOL_CALL_IDS = {
    "llama": 128010,
    "mistral": 5,
}

TOOL_CALL_TOKENS = {
    "llama": "<|python_tag|>",
    "mistral": "[TOOL_CALLS]",
}


MODEL_INPUT_TO_BRITON_FIELD = {
    "max_tokens": "request_output_len",
    "beam_width": "beam_width",
    "repetition_penalty": "repetition_penalty",
    "presence_penalty": "presence_penalty",
    "temperature": "temperature",
    "length_penalty": "len_penalty",
    "end_id": "end_id",
    "pad_id": "pad_id",
    "runtime_top_k": "runtime_top_k",
    "runtime_top_p": "runtime_top_p",
    "random_seed": "random_seed",
}

# Briton startup
# Briton inference request creation

import abc
import atexit
import os
import signal
import subprocess
import threading
import time
from pathlib import Path
from typing import Any, Optional

import grpc
from huggingface_hub import snapshot_download

from briton.flags import TRUSS_DEVELOPMENT_MODE
from briton.fs import is_local_path
from briton.network import is_port_available
from briton.proto import BritonStub
from briton.tokenizer import serialize_added_tokens_to_config


BRITON_CONFIG_FILENAME = "briton_config.pbtxt"
BRITON_STARTUP_CHECK_FREQUENCY_SECS = 1
BRITON_MONITOR_FREQUENCY_SECS = 1


class BritonInteractor(abc.ABC):
    @abc.abstractmethod
    def hf_download(self, repo_id: str, local_dir: Path, hf_token: Optional[str] = None):
        pass

    @abc.abstractmethod
    def load(
        self,
        model_name: str,
        engine_path: str,
        hf_tokenizer: str,
        work_dir: Path,
        fsm_cache_dir: str,
        kv_cache_free_gpu_mem_fraction: float,
        port: int,
        added_tokens: list,
        max_num_tokens: Optional[int],
        enable_chunked_context: bool = False,
        hf_token: Optional[str] = None,
        tp_count: Optional[int] = 1,
    ):
        pass

    @abc.abstractmethod
    def create_grpc_stub(self, port: int) -> Any:
        pass


class BritonInteractorImpl(BritonInteractor):
    def hf_download(self, repo_id: str, local_dir: Path, hf_token: Optional[str] = None):
        snapshot_download(repo_id, local_dir=local_dir, token=hf_token)

    def load(self, *args, **kwargs):
        return load_briton(*args, **kwargs)

    def create_grpc_stub(self, port: int) -> BritonStub:
        channel = grpc.aio.insecure_channel(f"localhost:{port}")
        return BritonStub(channel)


def load_briton(
    model_name: str,
    engine_path: str,
    hf_tokenizer: str,
    work_dir: Path,
    fsm_cache_dir: str,
    kv_cache_free_gpu_mem_fraction: float,
    port: int,
    added_tokens: list,
    max_num_tokens: Optional[int],
    enable_chunked_context: bool = False,
    hf_token: Optional[str] = None,
    tp_count: Optional[int] = 1,
):
    """Starts a Briton server for a given model type.

    TODO: Document the parameters.
    """
    if TRUSS_DEVELOPMENT_MODE:
        # Loading models (via Briton) can be slow. In development mode we reuse existing
        # Briton servers. If the port is occupied we assume one is running and we don't
        # start a new one.
        if not is_port_available(port):
            return

    # TODO(pankaj) Use this after debugging an issue we ran into with this.
    # Pass tokenizer file to Briton for the rust tokenizer.
    if is_local_path(hf_tokenizer):
        hf_tokenizer = str(Path(hf_tokenizer) / "tokenizer.json")

    config_str = f"""
        engine_path: "{engine_path}"
        hf_tokenizer: "{hf_tokenizer}"
        kv_cache_free_gpu_mem_fraction: {kv_cache_free_gpu_mem_fraction}
        enable_kv_cache_reuse: true
        enable_chunked_context: {enable_chunked_context}
        port: {port}
        fsm_cache_dir: "{fsm_cache_dir}"
    """
    if max_num_tokens is not None:
        config_str += f"\nmax_num_tokens: {max_num_tokens}"
    # Pass added tokens to Briton for the rust tokenizer.
    if len(added_tokens) > 0:
        config_str += "\n" + "\n".join(serialize_added_tokens_to_config(added_tokens))

    work_dir.mkdir(parents=True, exist_ok=True)
    config_pbtxt_path = (work_dir / BRITON_CONFIG_FILENAME).resolve()
    config_pbtxt_path.write_text(config_str)
    briton_env = os.environ.copy()
    if hf_token is not None:
        briton_env["HF_ACCESS_TOKEN"] = hf_token
        briton_env["HF_TOKEN"] = hf_token
    briton_process = _start_briton(config_pbtxt_path, tp_count, briton_env)
    while is_port_available(port):
        print(f"Waiting for Briton {model_name} to start")
        time.sleep(BRITON_STARTUP_CHECK_FREQUENCY_SECS)

    briton_monitor_thread = threading.Thread(target=_briton_monitor, args=(briton_process,))
    briton_monitor_thread.daemon = True
    briton_monitor_thread.start()


def _briton_monitor(briton_process):
    while True:
        if briton_process.poll() is not None:
            print(
                f"Briton process has exited with code {briton_process.returncode}, exiting truss server"
            )
            pid = os.getpid()
            os.kill(pid, signal.SIGKILL)
        time.sleep(BRITON_MONITOR_FREQUENCY_SECS)


def _start_briton(config_pbtxt_path, tp_count, briton_env):
    if tp_count is None or tp_count == 1:
        briton_process = subprocess.Popen(
            ["Briton", "--config", str(config_pbtxt_path)], env=briton_env
        )
    else:
        briton_process = subprocess.Popen(
            [
                "mpirun",
                "--allow-run-as-root",
                "-n",
                f"{tp_count}",
                "Briton",
                "--config",
                str(config_pbtxt_path),
            ],
            env=briton_env,
        )
    atexit.register(_cleanup_subprocess, briton_process)
    return briton_process


def _cleanup_subprocess(proc):
    print("Cleaning up: terminating the subprocess")
    try:
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)  # Terminate the subprocess group
    except Exception as e:
        print(f"Failed to terminate subprocess: {e}")

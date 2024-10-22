import os
import psutil
import signal


def kill_current_process_and_children():
    current_process = psutil.Process(os.getpid())

    for child in current_process.children(recursive=True):
        os.kill(child.pid, signal.SIGKILL)

    os.kill(os.getpid(), signal.SIGKILL)

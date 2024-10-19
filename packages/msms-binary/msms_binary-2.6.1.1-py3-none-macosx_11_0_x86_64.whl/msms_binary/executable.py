import os
import subprocess
from os import PathLike
from pathlib import Path

BIN_DIR = Path(__file__).parent / "bin"
if os.name == "nt":
    MSMS_BIN_PATH = BIN_DIR / "msms.exe"
else:
    MSMS_BIN_PATH = BIN_DIR / "msms"


def run_msms(*args, **kwargs):
    if len(args) > 0:
        cmd_args = args[0]
        args = args[1:]
    else:
        cmd_args = None

    if cmd_args is None or (isinstance(cmd_args, str) and cmd_args == ""):
        return subprocess.run(MSMS_BIN_PATH, *args, **kwargs)
    elif isinstance(cmd_args, (str, bytes, PathLike)):
        return subprocess.run([MSMS_BIN_PATH, cmd_args], *args, **kwargs)
    return subprocess.run([MSMS_BIN_PATH, *cmd_args], *args, **kwargs)


def popen_msms(
    *args,
    **kwargs,
):
    if len(args) > 0:
        cmd_args = args[0]
        args = args[1:]
    else:
        cmd_args = None

    if cmd_args is None or (isinstance(cmd_args, str) and cmd_args == ""):
        return subprocess.Popen(MSMS_BIN_PATH, *args, **kwargs)
    elif isinstance(cmd_args, (str, bytes, PathLike)):
        return subprocess.Popen([MSMS_BIN_PATH, cmd_args], *args, **kwargs)
    return subprocess.Popen([MSMS_BIN_PATH, *cmd_args], *args, **kwargs)

import subprocess
from pathlib import Path
from typing import (
    Any,
    Callable,
    Generic,
    TypeVar,
)

# https://stackoverflow.com/questions/59717828/copy-type-signature-from-another-function
# Needed to make subprocess.Popen or subprocess.run wrappers without modifying the signature
_F = TypeVar("_F", bound=Callable[..., Any])

# NOTE: it will return None and make the resulting function uncallable.
# Only use in TYPE_CHECKING block
class CopySignature(Generic[_F]):
    def __init__(self, target: _F) -> None: ...
    def __call__(self, wrapped: Callable[..., Any]) -> _F: ...

MSMS_BIN_PATH: Path

@CopySignature(subprocess.run)
def run_msms(
    *args,
    **kwargs,
): ...
@CopySignature(subprocess.Popen)
def popen_msms(
    *args,
    **kwargs,
): ...

"""
pyimportcheck.core.logger - Logger primitives
"""
__all__ = [
    'log_error',
    'log_warning',
    'log_info',
]
import sys

#---
# Public
#---

def log_error(text: str, end: str = '\n') -> None:
    """ display error """
    print(f"\033[31m[ERROR] {text}\033[0m", end=end, file=sys.stderr)

def log_warning(text: str, end: str = '\n') -> None:
    """ display warning """
    print(f"\033[33m[WARNING] {text}\033[0m", end=end)

def log_info(text: str, end: str = '\n') -> None:
    """ display info """
    print(text, end=end)

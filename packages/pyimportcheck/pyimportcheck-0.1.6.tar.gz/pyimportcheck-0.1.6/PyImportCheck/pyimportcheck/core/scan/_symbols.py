"""
pyimportcheck.core.scan._symbols    - analyse symbol declarations
"""
__all__ = [
    'pic_scan_symbols',
    'pic_scan_symbol_add',
]
from typing import Any
import re

from pyimportcheck.core._logger import (
    log_error,
    log_warning,
)
from pyimportcheck.core.scan.types import (
    PicScannedFile,
    PicScannedSymbol,
    PicScannedSymbolType,
)

#---
# Internals
#---

def _pic_scan_symbol_var(file_info: PicScannedFile, stream: Any) -> None:
    """ analyse variable symbols
    """
    matcher = re.compile(
        flags   = re.MULTILINE,
        pattern = r"^(?P<var>([a-zA-Z0-9_]+( )*=(?!=)( )*)+)",
    )
    for sym_record in matcher.finditer(stream):
        lineno = stream[:sym_record.start()].count('\n')
        for sym in sym_record['var'].split('='):
            if not (sym := sym.strip()):
                continue
            pic_scan_symbol_add(
                file_info   = file_info,
                lineno      = lineno,
                symname     = sym,
                symtype     = PicScannedSymbolType.VAR,
            )

def _pic_scan_symbol_func(file_info: PicScannedFile, stream: Any) -> None:
    """ analyse function symbols
    """
    matcher = re.compile(
        flags   = re.MULTILINE,
        pattern = r"^def( )+(?P<symbol>([a-zA-Z0-9_]+))( )*\(",
    )
    for sym in matcher.finditer(stream):
        pic_scan_symbol_add(
            file_info   = file_info,
            lineno      = stream[:sym.start()].count('\n'),
            symname     = sym['symbol'],
            symtype     = PicScannedSymbolType.FUNC,
        )

def _pic_scan_symbol_class(file_info: PicScannedFile, stream: Any) -> None:
    """ analyse class symbols
    """
    matcher = re.compile(
        flags   = re.MULTILINE,
        pattern = r"^class( )+(?P<symbol>([a-zA-Z0-9_]+))( )*\(",
    )
    for sym in matcher.finditer(stream):
        pic_scan_symbol_add(
            file_info   = file_info,
            lineno      = stream[:sym.start()].count('\n'),
            symname     = sym['symbol'],
            symtype     = PicScannedSymbolType.CLASS,
        )

#---
# Public
#---

def pic_scan_symbols(
    file_info:  PicScannedFile,
    stream: Any,
) -> None:
    """ analyse symbol declarations
    """
    _pic_scan_symbol_func(file_info, stream)
    _pic_scan_symbol_var(file_info, stream)
    _pic_scan_symbol_class(file_info, stream)

def pic_scan_symbol_add(
    file_info:  PicScannedFile,
    lineno:     int,
    symname:    str,
    symtype:    PicScannedSymbolType,
) -> None:
    """ add symbol information into the internal dictionary
    """
    if symname == '*':
        log_warning(
            f"{file_info.relpath}:{lineno}: avoid using '*' import"
        )
        return
    if symname in file_info.symbols:
        log_error(
            f"{file_info.relpath}:{lineno + 1}: symbol '{symname}' already "
            'exists, the symbol will be ignored'
        )
        return
    file_info.symbols[symname] = PicScannedSymbol(
        lineno  = lineno + 1,
        name    = symname,
        type    = symtype,
    )

"""
pyimportcheck.core.scan._imports    - analyse import statements
"""
__all__ = [
    'pic_scan_imports',
    'pic_scan_import_add',
]
from typing import Any
import re

from pyimportcheck.core._logger import log_warning
from pyimportcheck.core.scan._symbols import pic_scan_symbol_add
from pyimportcheck.core.scan.types import (
    PicScannedFile,
    PicScannedImport,
    PicScannedSymbolType,
    PicScannedImportType,
)

#---
# Internals
#---

def _pic_scan_check_from_multiline(
    file_info: PicScannedFile,
    stream: Any,
    package: str,
) -> None:
    """ check multilined `from` imports

    @notes
    - check only `from <package> import (<symbols>, ...)`
    - register imports information
    - register implicit symbols information
    """
    matcher = re.compile(
        flags   = re.MULTILINE,
        pattern = \
            rf"^from (?P<path>{package}(\.[a-zA-Z0-9_]+)*) import "
            '\\(( )*(#.*(?=\n))?'
            '(?P<workaround>(\n)?)'
            '(?P<sym>(( )*[a-zA-Z0-9_\\*]+(,)?( )*(#.*(?=\n))?[ \n]*)+)'
            '\\)',
    )
    for imp in matcher.finditer(stream):
        lineno = stream[:imp.start()].count('\n')
        pic_scan_import_add(
            file_info   = file_info,
            lineno      = lineno,
            imppath     = imp['path'],
            imptype     = PicScannedImportType.FROM,
        )
        if imp['workaround']:
            lineno = lineno + 1
        for symbol in imp['sym'].split('\n'):
            symbol = symbol.split('#')[0].strip()
            for sym in symbol.split(','):
                sym = sym.strip()
                if not sym:
                    continue
                pic_scan_symbol_add(
                    file_info   = file_info,
                    lineno      = lineno,
                    symname     = sym,
                    symtype     = PicScannedSymbolType.IMPORT,
                )
            lineno = lineno + 1

def _pic_scan_check_from_inline(
    file_info: PicScannedFile,
    stream: Any,
    package: str,
) -> None:
    """ check inlined `from` import

    @notes
    - check only `from <package> import <symbols>`
    - register imports information
    - register implicit symbols information
    """
    matcher = re.compile(
        flags   = re.MULTILINE,
        pattern = \
            rf"^from (?P<path>{package}(\.[a-zA-Z0-9_]+)*) import "
            '(?P<sym>[a-zA-Z0-9_\\*]+(,( )*[a-zA-Z0-9_\\*]+( )*)*)'
            '([ \t]*(#.*))?$',
    )
    for imp in matcher.finditer(stream):
        lineno = stream[:imp.start()].count('\n')
        pic_scan_import_add(
            file_info   = file_info,
            lineno      = lineno,
            imppath     = imp['path'],
            imptype     = PicScannedImportType.FROM_INLINE,
        )
        for symbol in imp['sym'].split(','):
            pic_scan_symbol_add(
                file_info   = file_info,
                lineno      = lineno,
                symname     = symbol.strip(),
                symtype     = PicScannedSymbolType.IMPORT,
            )

def _pic_scan_check_raw(
    file_info: PicScannedFile,
    stream: Any,
    package: str,
) -> None:
    """ check raw import statements

    @notes
    - check only `import <package statement>`
    - register imports information
    - display warning
    """
    matcher = re.compile(
        flags   = re.MULTILINE,
        pattern = rf"^import (?P<path>{package}(\.[a-z_0-9]+)*)",
    )
    for imp in matcher.finditer(stream):
        log_warning(
            f"{file_info.relpath}:{imp.start()}: avoid using raw "
            '`import`, prefer using `from ... import ...` instead'
        )
        pic_scan_import_add(
            file_info   = file_info,
            lineno      = stream[:imp.start()].count('\n'),
            imppath     = imp['path'],
            imptype     = PicScannedImportType.RAW,
        )

#---
# Public
#---

def pic_scan_imports(
    file_info: PicScannedFile,
    stream: Any,
    package: str,
) -> None:
    """ analyse import statements

    @notes
    - check for raw imports (`import <package>`)
    - analyse fragmented imports (`from <package> import ...`)
    """
    _pic_scan_check_raw(file_info, stream, package)
    _pic_scan_check_from_inline(file_info, stream, package)
    _pic_scan_check_from_multiline(file_info, stream, package)

def pic_scan_import_add(
    file_info:  PicScannedFile,
    lineno:     int,
    imppath:    str,
    imptype:    PicScannedImportType,
) -> None:
    """ add new import information
    """
    file_info.imports.append(
        PicScannedImport(
            lineno      = lineno + 1,
            import_path = imppath,
            type        = imptype,
        )
    )

"""
pyimportcheck.core.scan._exports    - analyse the `__all__` declaration
"""
__all__ = [
    'pic_scan_exports',
]
from typing import Any
import re

from pyimportcheck.core._logger import log_warning
from pyimportcheck.core.scan.types import (
    PicScannedFile,
    PicScannedExport,
)

#---
# Public
#---

def pic_scan_exports(
    file_info: PicScannedFile,
    stream: Any,
) -> None:
    """ analyse `__all__` declaration

    @notes
    - fetch all exposed symbols
    - generate warning if it uses "(" instead of "["
    """
    matcher = re.compile(
        flags   = re.MULTILINE,
        pattern = \
            '^__all__( )+=( )*(?P<enclose>[\\[\\(])'
            '(?P<workaround>(\n)?)'
            '(?P<raw>('
            '( )*[\'"][A-Za-z0-9_]+[\'"](,)?'
            '( )*(#.*(?=\n))?[ \n]*)*'
            ')'
            '[ \n]*[\\]\\)]',
    )
    for symbols in matcher.finditer(stream):
        lineno = stream[:symbols.start()].count('\n')
        if symbols['enclose'] == '(':
            log_warning(
                f"{file_info.path}:{lineno}: the `__all__` declaration "
                'should use square brackets for declaration as implicitly '
                'described in the PEP-8'
            )
        if symbols['workaround']:
            lineno = lineno + 1
        for symbol in symbols['raw'].split('\n'):
            symbol = symbol.split('#')[0].strip()
            for sym in symbol.split(','):
                if not (sym := sym.strip()):
                    continue
                sym = sym.replace('\'', '')
                sym = sym.replace('"', '')
                file_info.exports.append(
                    PicScannedExport(
                        lineno  = lineno + 1,
                        name    = sym,
                    )
                )
            lineno = lineno + 1

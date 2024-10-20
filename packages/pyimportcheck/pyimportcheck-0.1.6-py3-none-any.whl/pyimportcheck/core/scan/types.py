"""
pyimportcheck.core.scan.types   - glossary of all scanner types
"""
# use this magical import to enable partially initialised classes needed by
# the `PicScannedModule` which can store other modules' information
from __future__ import annotations

__all__ = [
    'PicScannedFile',
    'PicScannedModule',
    'PicScannedSymbol',
    'PicScannedImport',
    'PicScannedExport',
    'PicScannedSymbolType',
    'PicScannedImportType',
]
from typing import Dict, Union, List
from dataclasses import dataclass
from pathlib import Path
from enum import Enum

from pyimportcheck.core._utils import PicDebugClass

#---
# Public
#---

class PicScannedSymbolType(Enum):
    """ symbol type """
    IMPORT  = 'import'
    FUNC    = 'function'
    VAR     = 'var'
    CLASS   = 'class'

@dataclass
class PicScannedSymbol(PicDebugClass):
    """ symbol information """
    lineno: int
    name:   str
    type:   PicScannedSymbolType

class PicScannedImportType(Enum):
    """ import type """
    RAW         = 'raw'
    FROM        = 'from'
    FROM_INLINE = 'from-inline'

@dataclass
class PicScannedImport(PicDebugClass):
    """ import information """
    lineno:      int
    import_path: str
    type:        PicScannedImportType

    @property
    def name(self) -> str:
        """ shortcut to fetch the import name """
        return self.import_path.rsplit('.', maxsplit=1)[-1]

@dataclass
class PicScannedExport(PicDebugClass):
    """ scanned export symbol information """
    lineno: int
    name:   str

@dataclass
class PicScannedFile(PicDebugClass):
    """ scanned python file information """
    path:       Path
    relpath:    Path
    symbols:    Dict[str,PicScannedSymbol]
    exports:    List[PicScannedExport]
    imports:    List[PicScannedImport]

    @property
    def name(self) -> str:
        """ shortcut to fetch the package name """
        return self.path.stem

@dataclass
class PicScannedModule(PicDebugClass):
    """ scanned module information """
    name:           str
    path:           Path
    relpath:        Path
    modules:        Dict[str,Union[PicScannedModule,PicScannedFile]]

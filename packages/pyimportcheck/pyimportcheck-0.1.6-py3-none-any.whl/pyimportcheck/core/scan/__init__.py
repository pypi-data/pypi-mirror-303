"""
pyimportcheck.core.scan   - static code scanner
"""
__all__ = [
    'pic_scan_package',
    'PicScannedFile',
    'PicScannedSymbol',
    'PicScannedImport',
    'PicScannedExport',
    'PicScannedModule',
    'PicScannedSymbolType',
    'PicScannedImportType',
]
from typing import Union
from dataclasses import dataclass
from pathlib import Path
import re

from pyimportcheck.core.scan._imports import pic_scan_imports
from pyimportcheck.core.scan._exports import pic_scan_exports
from pyimportcheck.core.scan._symbols import pic_scan_symbols
from pyimportcheck.core.scan.types import (
    PicScannedModule,
    PicScannedFile,
    PicScannedSymbol,
    PicScannedExport,
    PicScannedImport,
    PicScannedSymbolType,
    PicScannedImportType,
)
from pyimportcheck.core._logger import (
    log_warning,
    log_error,
)

#---
# Internals
#---

def _pic_analyse_file(
    fileinfo:   PicScannedFile,
    package:    str
) -> PicScannedFile:
    """ load the file and manually parse it
    """
    with open(fileinfo.path, 'r', encoding='utf-8') as filestream:
        mfile = filestream.read()
        pic_scan_imports(fileinfo, mfile, package)
        pic_scan_symbols(fileinfo, mfile)
        pic_scan_exports(fileinfo, mfile)
    return fileinfo

def _pic_analyse_package(
    module:      PicScannedModule,
    package:     str,
    base_prefix: Path
) -> PicScannedModule:
    """ recursively scan package folders
    """
    for filepath in module.path.iterdir():
        if filepath.name in ['__pycache__', 'py.typed']:
            continue
        if filepath.name.startswith('.'):
            continue
        if filepath.is_dir():
            module.modules[filepath.name] = _pic_analyse_package(
                PicScannedModule(
                    name    = filepath.name,
                    path    = filepath,
                    relpath = filepath.resolve().relative_to(base_prefix),
                    modules = {},
                ),
                package,
                base_prefix,
            )
            continue
        if not filepath.name.endswith('.py'):
            log_warning(f"file '{str(filepath)}' is not a valid")
            continue
        module.modules[filepath.stem] = _pic_analyse_file(
            fileinfo    = PicScannedFile(
                path    = filepath,
                relpath = filepath.resolve().relative_to(base_prefix),
                symbols = {},
                exports = [],
                imports = [],
            ),
            package     = package,
        )
    return module

#---
# Public
#---

def pic_scan_package(
    prefix: Path,
) -> Union[PicScannedModule,PicScannedFile]:
    """ package scanner
    """
    prefix = prefix.resolve()
    if prefix.is_dir():
        return _pic_analyse_package(
            module      = PicScannedModule(
                name    = prefix.name,
                path    = prefix.resolve(),
                relpath = prefix.relative_to(prefix.parent),
                modules = {},
            ),
            package     = prefix.name,
            base_prefix = prefix.parent,
        )
    if not prefix.name.endswith('.py'):
        log_warning(f"file '{str(prefix)}' is not a valid")
    return _pic_analyse_file(
        fileinfo    = PicScannedFile(
            path    = prefix,
            relpath = prefix.resolve().relative_to(prefix.parent),
            symbols = {},
            exports = [],
            imports = [],
        ),
        package     = prefix.name,
    )

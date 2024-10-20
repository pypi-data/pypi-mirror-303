"""
pyimportcheck.cli   - Crupy CLI entry
"""
__all__ = [
    'pyimportcheck_cli_entry',
]
from typing import NoReturn, Optional
from pathlib import Path
import sys

import click

from pyimportcheck.core.scan import pic_scan_package
from pyimportcheck.core.detect import pic_detect_all
from pyimportcheck.core.output import (
    pic_output_stdout,
    pic_output_json,
)

#---
# Public
#---

@click.command('pyimportcheck')
@click.argument(
    'package_prefix_list',
    required    = True,
    metavar     = 'PATHFILE',
    type        = click.Path(
        exists      = True,
        file_okay   = True,
        dir_okay    = True,
        path_type   = Path,
    ),
    nargs       = -1,
)
@click.option(
    '-j', '--json', 'json_output',
    required    = False,
    metavar     = 'OUTPUT_FILENAME',
    help        = 'enable JSON output',
    type        = click.Path(
        exists      = False,
        file_okay   = True,
        dir_okay    = False,
        path_type   = Path,
    ),
)
@click.option(
    '--json-only', 'json_output_only',
    required    = False,
    metavar     = 'OUTPUT_FILENAME',
    help        = 'enable JSON output only',
    type        = click.Path(
        exists      = False,
        file_okay   = True,
        dir_okay    = False,
        path_type   = Path,
    ),
)
@click.version_option(message='%(version)s')
def pyimportcheck_cli_entry(
    package_prefix_list:    list[Path],
    json_output:            Optional[Path],
    json_output_only:       Optional[Path],
) -> NoReturn:
    """ Python circular import detector
    """
    ret = 0
    for package_prefix in package_prefix_list:
        info = pic_scan_package(package_prefix)
        report = pic_detect_all(info)
        if not json_output_only:
            ret += pic_output_stdout(package_prefix, report)
        if json_output:
            ret += pic_output_json(json_output, package_prefix, report)
        if json_output_only:
            ret += pic_output_json(json_output_only, package_prefix, report)
    sys.exit(ret)

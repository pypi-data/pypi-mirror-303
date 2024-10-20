"""
pyimportcheck.core.output.json  - JSON output
"""
__all__ = [
    'pic_output_json',
]
from pathlib import Path
import json

from pyimportcheck.core.detect import PicDetectReport
from pyimportcheck.core._logger import log_warning

#---
# Public
#---

def pic_output_json(
    pathname:       Path,
    package_prefix: Path,
    report:         PicDetectReport,
) -> int:
    """ export the report in a JSON file
    """
    output = {}
    if pathname.exists():
        with open(pathname, 'r', encoding = 'utf8') as outfd:
            output = json.load(outfd)
    if str(package_prefix) in output:
        log_warning(
            f"output '{str(pathname)}' already export "
            f"'{str(package_prefix)}' (update)"
        )
    output[str(package_prefix)] = report.export_json()
    with open(pathname, 'w', encoding = 'utf8') as outfd:
        json.dump(output, outfd)
    return report.error + report.warning

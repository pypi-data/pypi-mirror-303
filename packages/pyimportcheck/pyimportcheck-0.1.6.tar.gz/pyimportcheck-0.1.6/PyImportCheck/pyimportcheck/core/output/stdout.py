"""
pyimportcheck.core.stdout   - display the report in stdout
"""
__all__ = [
    'pic_output_stdout',
]
import sys
from pathlib import Path

from pyimportcheck.core.detect import PicDetectReport
from pyimportcheck.core._logger import (
    log_error,
    log_warning,
    log_info,
)

#---
# Public
#---

def pic_output_stdout(package_prefix: Path, report: PicDetectReport) -> int:
    """ display the report in stdout and return the exit status
    """
    if report.error > 0 or report.warning > 0:
        print(f"-=== {str(package_prefix)} ===-", file=sys.stderr)
    # (todo) waiting notification rework planned for `v0.2.0`
    for notif_list in report.notifications.values():
        for notif in notif_list:
            log = log_error if notif.type == 'error' else log_warning
            log(notif.log)
    if report.error > 0 or report.warning > 0:
        log_info('==========================')
        error = 'error' if report.error == 1 else 'errors'
        warning = 'warning' if report.warning == 1 else 'warnings'
        log_error(f"Detected {report.error} {error}")
        log_warning(f"Detected {report.warning} {warning}")
    return report.error + report.warning

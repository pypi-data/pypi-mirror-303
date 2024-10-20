"""
pyimportcheck.core.detect._import   - check module validity
"""
__all__ = [
    'pic_detect_module_invalid',
]
from typing import List, Union

from pyimportcheck.core.detect.types import PicDetectNotification
from pyimportcheck.core.scan import (
    PicScannedModule,
    PicScannedFile,
)

#---
# Internals
#---

def _pic_generate_notification(
    module: PicScannedModule,
) -> PicDetectNotification:
    """ generate a notification
    """
    return PicDetectNotification(
        type    = 'error',
        path    = module.path,
        log     = f"{module.relpath}: missing critical `__init__.py` file",
    )

def _pic_detect_module_invalid(
    current: PicScannedModule,
) -> List[PicDetectNotification]:
    """ check missing `__init__.py` file
    """
    notifications: List[PicDetectNotification] = []
    if '__init__' not in current.modules:
        notifications.append(_pic_generate_notification(current))
    for module_info in current.modules.values():
        if isinstance(module_info, PicScannedModule):
            notifications += _pic_detect_module_invalid(module_info)
    return notifications

#---
# Public
#---

def pic_detect_module_invalid(
    current: Union[PicScannedModule,PicScannedFile],
) -> List[PicDetectNotification]:
    """ check missing `__init__.py` file
    """
    if isinstance(current, PicScannedFile):
        return []
    return _pic_detect_module_invalid(current)

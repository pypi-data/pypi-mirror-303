"""
pyimportcheck.core.detect._exports  - check missing / bad `__all__` symbol
"""
__all__ = [
    'pic_detect_exports_mistake',
]
from typing import Dict, List, Any, Union

from pyimportcheck.core.detect.types import PicDetectNotification
from pyimportcheck.core.scan import (
    PicScannedModule,
    PicScannedFile,
    PicScannedSymbolType,
)

#---
# Internals
#---

def _pic_generate_notification(
    notif_type: str,
    info:       PicScannedFile,
    log:        str,
) -> PicDetectNotification:
    """ generate a notification
    """
    return PicDetectNotification(
        type    = notif_type,
        path    = info.path,
        log     = f"{info.relpath}:{log}",
    )

def _pic_check_missing_export(
    info: PicScannedFile,
) -> List[PicDetectNotification]:
    """ check missing `__all__` declaration
    """
    if '__all__' not in info.symbols:
        if not info.symbols:
            return []
        log  = ' missing the `__all__` symbol, which can be declared as '
        log += 'follows:\n'
        log += '>>> __all__ = [\n'
        for sym in info.symbols.keys():
            if not sym.startswith('_'):
                log += f">>>     '{sym}',\n"
        log += '>>> ]'
        return [
            _pic_generate_notification(
                notif_type  = 'warning',
                info        = info,
                log         = log,
            ),
        ]
    return []

def _pic_check_mismatched_export(
    info: PicScannedFile,
) -> List[PicDetectNotification]:
    """ check mismatched `__all__` declaration

    @notes
    - check that no private symbols have been exported
    - check if one symbol has been exported multiple times
    - check that exported symbols exist
    """
    notifications = []
    expected_exports: Dict[str,Any] = {}
    for syminfo in info.symbols.values():
        if not syminfo.name.startswith('_'):
            expected_exports[syminfo.name] = 0
    for exp in info.exports:
        if exp.name in expected_exports:
            if expected_exports[exp.name] > 0:
                notifications.append(
                    _pic_generate_notification(
                        notif_type  = 'warning',
                        info        = info,
                        log         = \
                            f"{exp.lineno}: symbol '{exp.name}' has "
                            'already been exported, you can remove this '
                            'line',
                    ),
                )
            expected_exports[exp.name] += 1
            continue
        if exp.name in info.symbols:
            notifications.append(
                _pic_generate_notification(
                    notif_type  = 'warning',
                    info        = info,
                    log         = \
                        f"{exp.lineno}: symbol '{exp.name}' should not "
                        'be exported',
                ),
            )
            continue
        notifications.append(
            _pic_generate_notification(
                notif_type  = 'error',
                info        = info,
                log         = \
                    f"{exp.lineno}: exported symbol '{exp.name}' does "
                    'not exist',
            ),
        )
    for expname, expcnt in expected_exports.items():
        if expcnt != 0:
            continue
        if info.symbols[expname].type == PicScannedSymbolType.IMPORT:
            continue
        notifications.append(
            _pic_generate_notification(
                notif_type  = 'warning',
                info        = info,
                log         = f" missing exported symbol '{expname}'",
            ),
        )
    return notifications

def _pic_check_export_validity(
    info: PicScannedFile,
) -> List[PicDetectNotification]:
    """ check `__all__` declaration

    @notes
    - special check performed on `__main__.py` file which should not have an
        `__all__` declaration
    """
    if info.path.name == '__main__.py':
        notifications = []
        if '__all__' in info.symbols:
            notifications.append(
                _pic_generate_notification(
                    notif_type  = 'warning',
                    info        = info,
                    log         = \
                        f"{info.symbols['__all__'].lineno}: "
                        'You can remove the `__all__` declaration since '
                        'this magic file should not export symbols',
                ),
            )
            notifications += _pic_check_mismatched_export(info)
        return notifications
    if notifications := _pic_check_missing_export(info):
        return notifications
    if notifications := _pic_check_mismatched_export(info):
        return notifications
    return []

def _pic_detect_exports_mistake(
    current: PicScannedModule,
) -> List[PicDetectNotification]:
    """ check missing / bad `__all__` declaration
    """
    notifications: List[PicDetectNotification] = []
    for _, module_info in current.modules.items():
        if isinstance(module_info, PicScannedModule):
            notifications += _pic_detect_exports_mistake(module_info)
            continue
        notifications += _pic_check_export_validity(module_info)
    return notifications

#---
# Public
#---

def  pic_detect_exports_mistake(
    current: Union[PicScannedModule,PicScannedFile],
) -> List[PicDetectNotification]:
    """ check missing / bad `__all__` declaration
    """
    if isinstance(current, PicScannedFile):
        return _pic_check_export_validity(current)
    return _pic_detect_exports_mistake(current)

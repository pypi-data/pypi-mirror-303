"""
pyimportcheck.core.detect.types - all exposed types used by the detector
"""
__all__ = [
    'PicDetectReport',
    'PicDetectNotification',
]
from typing import List, Dict, Any
from dataclasses import dataclass
from pathlib import Path

from pyimportcheck.core._utils import PicDebugClass

#---
# Public
#---

@dataclass
class PicDetectNotification(PicDebugClass):
    """ warning / error information """
    type:   str
    path:   Path
    log:    str

@dataclass
class PicDetectReport(PicDebugClass):
    """ report of all detected information
    """
    notifications:   Dict[str,List[PicDetectNotification]]

    def __count_notification_type(self, notif_type: str) -> int:
        """ count the number of `notif_type` notifications
        """
        counter = 0
        for notifs in self.notifications.values():
            counter += sum(x.type == notif_type for x in notifs)
        return counter

    @property
    def error(self) -> int:
        """ return the number of errors in the notification list """
        return self.__count_notification_type('error')

    @property
    def warning(self) -> int:
        """ return the number of warnings in the notification list """
        return self.__count_notification_type('warning')

    def export_json(self) -> Dict[str,Any]:
        """ export to JSON
        """
        outinfo: Dict[str,Any] = {
            'version': 1,
            'total' : {
                'all' : self.error + self.warning,
                'error': self.error,
                'warning': self.warning,
            },
            'notifications': [],
        }
        for notif_list in self.notifications.values():
            for notif in notif_list:
                outinfo['notifications'].append({
                    'type': notif.type,
                    'path': str(notif.path),
                    'log': notif.log,
                })
        return outinfo

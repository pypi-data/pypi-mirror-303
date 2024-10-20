"""
pyimportcheck.core.detect._circular - detect circular import
"""
__all__ = [
    'pic_detect_circular_import',
]
from typing import List, Union, cast

from pyimportcheck.core.exception import PicException
from pyimportcheck.core.detect.types import PicDetectNotification
from pyimportcheck.core.scan import (
    PicScannedModule,
    PicScannedImport,
    PicScannedFile,
)

#---
# Internals
#---

def _pic_generate_notification(
    root_module_info:       PicScannedModule,
    target_file_info:       PicScannedFile,
    circular_import_list:   List[List[Union[str,int]]],
) -> PicDetectNotification:
    """ generate the notification

    @notes
    - since all imports `lineno` refer to corresponding parent imports,
        we need to perform a weird iteration on the circular import list
        to properly generate correct information
    """
    last_import_path = circular_import_list[-1][0]
    error  = f"({str(target_file_info.relpath)}) "
    for circular_imp in circular_import_list:
        import_path = cast(str, circular_imp[0])
        impinfo = _pic_find_fileinfo(
            root_module_info        = root_module_info,
            target_import_path      = import_path,
            target_import_lineno    = -1,
        )
        if impinfo.name == '__init__':
            if not import_path.endswith('__init__'):
                import_path = f"{import_path}.__init__"
        if circular_imp[0] == last_import_path:
            circular_import_list[-1][1] = circular_imp[1]
        error += f"{import_path}:{circular_imp[1]} -> "
    error += '...'
    return PicDetectNotification(
        type    = 'error',
        path    = target_file_info.path,
        log     = error,
    )

def _pic_generate_raise_log(
    module_info:    PicScannedModule,
    import_path:    str,
    import_lineno:  int,
    log:            str,
) -> PicException:
    """ generate exception information
    """
    return PicException(
        f"{module_info.relpath}:{import_lineno}: unable to import "
        f"'{import_path}', {log}",
    )

def _pic_find_fileinfo(
    root_module_info:     PicScannedModule,
    target_import_path:   str,
    target_import_lineno: int,
) -> PicScannedFile:
    """ resolve manual import path

    @notes
    - if the last part of the `current_import_info.import_path` is a module
        then it will automatically try to find the associated `__init__.py`
        file
    """
    target: Union[PicScannedModule,PicScannedFile] = root_module_info
    for shard in target_import_path.split('.')[1:]:
        if isinstance(target, PicScannedFile):
            raise _pic_generate_raise_log(
                module_info     = root_module_info,
                import_path     = target_import_path,
                import_lineno   = target_import_lineno,
                log             = \
                    f"because '{target.name}' is a file, but it should be "
                    'a module',
            )
        if shard not in target.modules:
            raise _pic_generate_raise_log(
                module_info     = root_module_info,
                import_path     = target_import_path,
                import_lineno   = target_import_lineno,
                log             = \
                    f"unable to find the '{shard}' file information",
            )
        target = target.modules[shard]
    if isinstance(target, PicScannedModule):
        if '__init__' not in target.modules:
            raise _pic_generate_raise_log(
                module_info     = root_module_info,
                import_path     = target_import_path,
                import_lineno   = target_import_lineno,
                log             = \
                    'unable to find the \'__init__.py\' file information '
                    'required to analyse the module (note that all files '
                    'inside this module will be skipped until the file is'
                    'added)',
            )
        target = target.modules['__init__']
    assert isinstance(target, PicScannedFile)
    return target

def _pic_search_circular_import(
    root_module_info:    PicScannedModule,
    current_import_info: PicScannedImport,
    import_history_list: List[List[Union[str,int]]],
) -> List[List[Union[str,int]]]:
    """ resolve a package and avoid circular import

    @notes
    - if a circular dependency has been detected, the import history
        will be returned, otherwise an empty list will be returned instead
    """
    if import_history_list:
        import_history_list[-1][1] = current_import_info.lineno
    for import_info in import_history_list[:-1]:
        if import_info[0] == current_import_info.import_path:
            import_history_list.append(
                [current_import_info.import_path, -1],
            )
            return import_history_list
    target = _pic_find_fileinfo(
        root_module_info        = root_module_info,
        target_import_path      = current_import_info.import_path,
        target_import_lineno    = current_import_info.lineno,
    )
    for next_import in target.imports:
        valid = _pic_search_circular_import(
            root_module_info    = root_module_info,
            current_import_info = next_import,
            import_history_list = \
                import_history_list + [
                    [current_import_info.import_path, -1]
                ],
        )
        if valid:
            return valid
    return []

def _pic_check_file(
    root_module_info:    PicScannedModule,
    current_file_info:   PicScannedFile,
    current_import_path: str,
) -> List[PicDetectNotification]:
    """ analyse file (check circular import)
    """
    notifications: List[PicDetectNotification] = []
    for imp in current_file_info.imports:
        try:
            circular_import_list = _pic_search_circular_import(
                root_module_info    = root_module_info,
                current_import_info = imp,
                import_history_list = [[current_import_path, -1]],
            )
        except PicException as err:
            notifications.append(
                PicDetectNotification(
                    type    = 'error',
                    path    = current_file_info.path,
                    log     = str(err),
                ),
            )
            continue
        if not circular_import_list:
            continue
        notifications.append(
            _pic_generate_notification(
                root_module_info     = root_module_info,
                target_file_info     = current_file_info,
                circular_import_list = circular_import_list,
            ),
        )
    return notifications

def _pic_check_module(
    root_module_info: PicScannedModule,
    current_module_info: PicScannedModule,
    import_prefix: str,
) -> List[PicDetectNotification]:
    """ recursively resolve all dependencies
    """
    notifications: List[PicDetectNotification] = []
    for module, module_info in current_module_info.modules.items():
        if isinstance(module_info, PicScannedModule):
            notifications += _pic_check_module(
                root_module_info    = root_module_info,
                current_module_info = module_info,
                import_prefix       = f"{import_prefix}.{module}",
            )
            continue
        notifications += _pic_check_file(
            root_module_info    = root_module_info,
            current_file_info   = module_info,
            current_import_path = f"{import_prefix}.{module}",
        )
    return notifications

#---
# Public
#---

def pic_detect_circular_import(
    root_module_info: Union[PicScannedModule,PicScannedFile],
) -> List[PicDetectNotification]:
    """ try to detect circular import
    """
    if isinstance(root_module_info, PicScannedFile):
        return []
    return _pic_check_module(
        root_module_info,
        root_module_info,
        root_module_info.name,
    )

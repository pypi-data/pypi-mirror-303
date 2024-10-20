"""
pyimportcheck.core.utils    - small utilities
"""
__all__ = [
    'PicDebugClass',
]
from typing import Any

#---
# Public
#---

# allow "too few public methods" and "too many return statements"
# pylint: disable=locally-disabled,R0903,R0911

class PicDebugClass():
    """ provide class pretty print
    """

    #---
    # Internals
    #---

    def __display_field(
        self,
        field_name:     str,
        field_data:     Any,
        indent:         int = 0,
        dict_special:   bool = False,
    ) -> str:
        """ handle each supported type
        """
        margin = ' ' * (indent * 4)
        if dict_special:
            field_name = f"'{field_name}'\t:"
        else:
            field_name = f"{field_name}\t="
        if isinstance(field_data, (int, str)):
            return f"{margin}{field_name} {field_data}\n"
        if isinstance(field_data, (list, tuple)):
            content = f"{margin}{field_name} "
            if not field_data:
                return content + '[],\n'
            content += margin + '[\n'
            for data in field_data:
                content += f"{margin}    {data},\n"
            content += f"{margin}],\n"
            return content
        if isinstance(field_data, dict):
            content = f"{margin}{field_name} "
            if not field_data:
                return content + '{},\n'
            content += margin + '{\n'
            for item_name, item_data in field_data.items():
                content += self.__display_field(
                    field_name      = item_name,
                    field_data      = item_data,
                    indent          = indent + 1,
                    dict_special    = True,
                )
            content += margin + '},\n'
            return content
        if not getattr(field_data, 'debug_show', None):
            content = f"{margin}{field_name} {field_data}\n"
            return content
        content  = f"{margin}{field_name} "
        content += f"{field_data.debug_show(indent + 1).strip()}\n"
        return content

    #---
    # Public
    #---

    def debug_show(self, indent: int = 0) -> str:
        """ use magical class information for pretty print

        @notes
        - only the strict minimum has been supported for now
        - only used in `core/scan/types.py` and `core/detect/types.py`
        """
        margin = ' ' * (indent * 4)
        content = f"{margin}{self.__class__.__name__}(\n"
        for attr_name, attr_data in self.__dict__.items():
            content += self.__display_field(
                field_name  = attr_name,
                field_data  = attr_data,
                indent      = indent + 1,
            )
        content += f"{margin})"
        return content

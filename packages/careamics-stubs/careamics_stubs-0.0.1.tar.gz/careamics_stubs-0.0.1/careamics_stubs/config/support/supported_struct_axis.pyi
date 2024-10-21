from careamics.utils import BaseEnum as BaseEnum

class SupportedStructAxis(str, BaseEnum):
    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'
    NONE = 'none'

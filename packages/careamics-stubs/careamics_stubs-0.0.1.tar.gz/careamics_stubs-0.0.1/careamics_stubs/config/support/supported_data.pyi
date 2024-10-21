from careamics.utils import BaseEnum as BaseEnum

class SupportedData(str, BaseEnum):
    ARRAY = 'array'
    TIFF = 'tiff'
    CUSTOM = 'custom'
    @classmethod
    def get_extension_pattern(cls, data_type: str | SupportedData) -> str: ...
    @classmethod
    def get_extension(cls, data_type: str | SupportedData) -> str: ...

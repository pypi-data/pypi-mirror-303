from careamics.utils import BaseEnum as BaseEnum

class SupportedArchitecture(str, BaseEnum):
    UNET = 'UNet'
    LVAE = 'LVAE'
    CUSTOM = 'custom'

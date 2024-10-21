from careamics.utils import BaseEnum as BaseEnum

class SupportedPixelManipulation(str, BaseEnum):
    UNIFORM = 'uniform'
    MEDIAN = 'median'

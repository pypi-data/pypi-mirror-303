from careamics.utils import BaseEnum as BaseEnum

class SupportedAlgorithm(str, BaseEnum):
    N2V = 'n2v'
    CARE = 'care'
    N2N = 'n2n'
    MUSPLIT = 'musplit'
    DENOISPLIT = 'denoisplit'
    CUSTOM = 'custom'

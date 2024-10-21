from careamics.utils import BaseEnum as BaseEnum

class SupportedTransform(str, BaseEnum):
    XY_FLIP = 'XYFlip'
    XY_RANDOM_ROTATE90 = 'XYRandomRotate90'
    N2V_MANIPULATE = 'N2VManipulate'
    NORMALIZE = 'Normalize'

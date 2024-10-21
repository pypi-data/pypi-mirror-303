from careamics.utils import BaseEnum as BaseEnum

class SupportedOptimizer(str, BaseEnum):
    ADAM = 'Adam'
    ADAMAX = 'Adamax'
    SGD = 'SGD'

class SupportedScheduler(str, BaseEnum):
    REDUCE_LR_ON_PLATEAU = 'ReduceLROnPlateau'
    STEP_LR = 'StepLR'

from careamics.utils import BaseEnum as BaseEnum

class SupportedActivation(str, BaseEnum):
    NONE = 'None'
    SIGMOID = 'Sigmoid'
    SOFTMAX = 'Softmax'
    TANH = 'Tanh'
    RELU = 'ReLU'
    LEAKYRELU = 'LeakyReLU'
    ELU = 'ELU'

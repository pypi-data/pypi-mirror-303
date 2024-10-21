from careamics.utils import BaseEnum as BaseEnum

class SupportedLoss(str, BaseEnum):
    MSE = 'mse'
    MAE = 'mae'
    N2V = 'n2v'
    MUSPLIT = 'musplit'
    DENOISPLIT = 'denoisplit'
    DENOISPLIT_MUSPLIT = 'denoisplit_musplit'

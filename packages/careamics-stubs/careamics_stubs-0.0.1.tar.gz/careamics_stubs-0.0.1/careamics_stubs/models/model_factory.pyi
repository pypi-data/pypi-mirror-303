import torch
from _typeshed import Incomplete
from careamics.config.architectures import CustomModel as CustomModel, LVAEModel as LVAEModel, UNetModel as UNetModel, get_custom_model as get_custom_model
from careamics.config.support import SupportedArchitecture as SupportedArchitecture
from careamics.models.unet import UNet as UNet
from careamics.utils import get_logger as get_logger

logger: Incomplete

def model_factory(model_configuration: UNetModel | LVAEModel | CustomModel) -> torch.nn.Module: ...

from .eegnet import EEGNet
from .lenet import LeNetPro
from .simple_cnn import AttentionCNN, VerySimpleCNN
from .simple_rnn import CRNN
from .tcn import TemporalConvNet

__all__ = [
    "EEGNet",
    "LeNetPro",
    "VerySimpleCNN",
    "CRNN",
    "TemporalConvNet",
    "AttentionCNN",
]

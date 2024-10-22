import numpy as np
import matplotlib.pyplot as plt
import math
import os
import torch
import pickle
from argparse import ArgumentParser
from torch import optim

from . import models
from . import utils as ut
from . import datasets as dt
from . import data_utils as dtul
from . import grid_predictor as grid
from .paths import get_paths
from . import losses as lo

from .dataloader import *
from .trainer_helper import *
from .eval_helper import *
from .trainer import *


def main():
    parser = make_args_parser()
    args = parser.parse_args()

    trainer = Trainer(args, console=True)
    trainer.run_train()
    trainer.run_eval_final()

    val_preds = trainer.run_eval_spa_enc_only(
        eval_flag_str="LocEnc ", load_model=True)

import tensorflow as tf
from tensorflow.keras import callbacks

from base.trainer import BaseTrainer


class ReduceLROnPlateauTrainer(BaseTrainer):
    def __init__(self, config, model, data):
        super().__init__(config, model, data)
        self.init_callbacks()

    def log_lr(self, epoch):
        tf.summary.scalar("learning_rate", data=self.model.model.optimizer.lr, step=epoch)

    def init_callbacks(self):
        self.callbacks.append(callbacks.ReduceLROnPlateau(**self.config.trainer.reduce_lr_on_plateau))
        if self.config.trainer.tensorboard_enabled:
            self.callbacks.append(callbacks.LambdaCallback(
                on_epoch_begin=lambda epoch, loss: self.log_lr(epoch)
            ))

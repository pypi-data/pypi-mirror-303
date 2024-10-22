import numpy as np


class MeanSquaredError:
    def __call__(self, y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)

    def gradient(self, y_true, y_pred):
        return 2 * (y_pred - y_true) / y_true.size


class CrossEntropyLoss:
    def __call__(self, y_true, y_pred):
        epsilon = 1e-12
        y_pred = np.clip(y_pred, epsilon, 1. - epsilon)
        return -np.sum(y_true * np.log(y_pred)) / y_true.shape[0]

    def gradient(self, y_true, y_pred):
        epsilon = 1e-12
        y_pred = np.clip(y_pred, epsilon, 1. - epsilon)
        return - (y_true / y_pred) / y_true.shape[0]


class HingeLoss:
    def __call__(self, y_true, y_pred):
        return np.mean(np.maximum(0, 1 - y_true * y_pred))

    def gradient(self, y_true, y_pred):
        return np.where(y_true * y_pred < 1, -y_true, 0)

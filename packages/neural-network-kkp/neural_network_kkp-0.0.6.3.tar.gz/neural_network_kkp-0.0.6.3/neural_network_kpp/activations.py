import numpy as np


class ReLU:
    def __call__(self, z):
        return np.maximum(0, z)

    @staticmethod
    def derivative(z):
        derivative = np.ones_like(z)
        derivative[z <= 0] = 0
        return derivative


class Sigmoid:
    def __call__(self, z):
        return 1 / (1 + np.exp(-z))

    @staticmethod
    def derivative(z):
        sigmoid = 1 / (1 + np.exp(-z))
        return sigmoid * (1 - sigmoid)


class Tanh:
    def __call__(self, z):
        return np.tanh(z)

    @staticmethod
    def derivative(z):
        return 1 - np.tanh(z) ** 2

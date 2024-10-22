import numpy as np
from .activations import ReLU, Sigmoid, Tanh


class DenseLayer:
    def __init__(self, input_size, output_size, activation_func, weights_initializer='random',
                 biases_initializer='ones', learning_rate=0.01):
        self.activation_func = activation_func
        self.learning_rate = learning_rate

        if weights_initializer == 'random':
            self.weights = np.random.randn(input_size, output_size) * 0.01
        elif weights_initializer == 'xavier':
            self.weights = np.random.randn(input_size, output_size) * np.sqrt(1 / input_size)
        elif weights_initializer == 'he':
            self.weights = np.random.randn(input_size, output_size) * np.sqrt(2 / input_size)
        elif weights_initializer == 'normal':
            self.weights = np.random.normal(0, 1, (input_size, output_size))
        else:
            raise ValueError(f"Unknown weights initializer: {weights_initializer}")

        if biases_initializer == 'zeros':
            self.biases = np.zeros((1, output_size))
        elif biases_initializer == 'ones':
            self.biases = np.ones((1, output_size))
        elif biases_initializer == 'normal':
            self.biases = np.random.normal(0, 1, (1, output_size))
        else:
            raise ValueError(f"Unknown biases initializer: {biases_initializer}")

    def forward(self, inputs):
        self.inputs = inputs
        self.z = np.dot(inputs, self.weights) + self.biases
        self.a = self.activation_func(self.z)
        return self.a

    def backward(self, grad_output):
        grad_activation = self.activation_func.derivative(self.z)
        grad_input = np.dot(grad_output * grad_activation, self.weights.T)
        grad_weights = np.dot(self.inputs.T, grad_output * grad_activation)
        grad_biases = np.sum(grad_output * grad_activation, axis=0, keepdims=True)
        self.weights -= self.learning_rate * grad_weights
        self.biases -= self.learning_rate * grad_biases

        return grad_input

    def update_weights(self, learning_rate):
        self.weights -= learning_rate * self.grad_weights
        self.biases -= learning_rate * self.grad_biases


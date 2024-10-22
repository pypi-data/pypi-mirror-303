class NeuralNetwork:
    def __init__(self):
        self.layers = []

    def add_layer(self, layer):
        self.layers.append(layer)

    def forward(self, X):
        output = X
        for layer in self.layers:
            output = layer.forward(output)
        return output

    def backward(self, X, y, loss_func):
        output = self.forward(X)
        loss_gradient = loss_func.gradient(y, output)
        for layer in reversed(self.layers):
            loss_gradient = layer.backward(loss_gradient)
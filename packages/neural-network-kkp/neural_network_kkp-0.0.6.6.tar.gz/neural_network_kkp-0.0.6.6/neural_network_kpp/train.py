
def train(network, x, y, loss_func, epochs, learning_rate=0.01):
    for epoch in range(epochs):
        network.backward(x, y, loss_func)
        for layer in network.layers:
            if hasattr(layer, 'update_weights'):
                layer.update_weights(learning_rate)
        loss_value = loss_func(y, network.forward(x))
        predicted_output = network.forward(x)
        print(f"Эпоха {epoch + 1}/{epochs}, Потеря: {loss_value:.4f}, Предсказанное значение: {predicted_output.flatten()}")

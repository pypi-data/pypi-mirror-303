import numpy as np


def train(network, x, y, loss_func, epochs, learning_rate=0.01):
    for epoch in range(epochs):
        # Обратное распространение ошибки
        network.backward(x, y, loss_func)
        # Обновление весов (добавьте здесь шаг, если слои имеют метод для обновления параметров)
        for layer in network.layers:
            if hasattr(layer, 'update_weights'):
                layer.update_weights(learning_rate)
        # Вычисление потерь
        loss_value = loss_func(y, network.forward(x))
        print(f"Эпоха {epoch + 1}/{epochs}, Потеря: {loss_value:.4f}")

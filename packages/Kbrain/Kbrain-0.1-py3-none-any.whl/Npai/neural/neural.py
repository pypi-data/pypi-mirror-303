import numpy as np
import pickle
from Kbrain.layer.layer import Dense


class NeuralNetwork:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_derivative = None

    def add(self, layer):
        self.layers.append(layer)

    def set_loss(self, loss, loss_derivative):
        self.loss = loss
        self.loss_derivative = loss_derivative

    def forward(self, inputs):
        for layer in self.layers:
            inputs = layer.forward(inputs)
        return inputs

    def backward(self, dvalues):
        for layer in reversed(self.layers):
            dvalues = layer.backward(dvalues)
        return dvalues

    def train(self, X, y, epochs=1000, lr=0.01):
        for epoch in range(epochs):
            # Forward pass
            output = self.forward(X)

            # Compute loss (Mean Squared Error in this case)
            loss = self.loss(y, output)

            # Backward pass
            dvalues = self.loss_derivative(y, output)
            self.backward(dvalues)

            # Update weights and biases
            for layer in self.layers:
                if isinstance(layer, Dense):
                    layer.update(lr)

            # Print loss every 100 epochs
            if epoch % 100 == 0:
                print(f'Epoch {epoch}, Loss: {loss}')

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def mse_derivative(y_true, y_pred):
    return 2 * (y_pred - y_true) / y_true.size


def bce_loss(y_true, y_pred):
    # 예방 조치: log(0)을 피하기 위해 y_pred를 근사
    y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)

    # BCE 손실 계산
    bce = - np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

    return bce

def bce_derivative(y_true, y_pred):
    return - (y_true / y_pred - (1 - y_true) / (1 - y_pred))

def load_model(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
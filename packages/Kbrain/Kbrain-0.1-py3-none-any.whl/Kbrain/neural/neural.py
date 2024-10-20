import numpy as np

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

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def mse_derivative(y_true, y_pred):
    return 2 * (y_pred - y_true) / y_true.size

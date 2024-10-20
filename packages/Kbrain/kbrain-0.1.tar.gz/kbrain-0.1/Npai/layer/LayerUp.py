import numpy as np

from Kbrain import Dense as Kdense

class Dense(Kdense):
    def __init__(self, input_size, output_size):
        super().__init__(
            input_size=input_size,
            output_size=output_size
        )

class ConvLayer:
    def __init__(self, num_filters, filter_size, input_shape, stride=1, padding=0):
        self.num_filters = num_filters
        self.filter_size = filter_size
        self.input_shape = input_shape
        self.stride = stride
        self.padding = padding

        # Initialize weights and biases
        self.weights = np.random.randn(num_filters, input_shape[2], filter_size, filter_size)
        self.biases = np.zeros((num_filters,))

    def forward(self, input_data):
        self.input_data = input_data

        num_filters, channels, filter_size, _ = self.weights.shape
        _, input_height, input_width, input_channels = input_data.shape

        output_height = (input_height - filter_size + 2 * self.padding) // self.stride + 1
        output_width = (input_width - filter_size + 2 * self.padding) // self.stride + 1

        output_data = np.zeros((input_data.shape[0], output_height, output_width, num_filters))

        for batch_idx in range(input_data.shape[0]):
            for fh in range(output_height):
                for fw in range(output_width):
                    for f in range(num_filters):
                        # Calculate the receptive field
                        h_start = fh * self.stride
                        h_end = h_start + filter_size
                        w_start = fw * self.stride
                        w_end = w_start + filter_size

                        receptive_field = input_data[batch_idx, h_start:h_end, w_start:w_end, :]
                        output_data[batch_idx, fh, fw, f] = np.sum(receptive_field * self.weights[f]) + self.biases[f]

        return output_data

    def backward(self, dL_dy):
        batch_size, output_height, output_width, num_filters = dL_dy.shape
        _, input_height, input_width, input_channels = self.input_data.shape
        _, filter_size, _, _ = self.weights.shape

        dL_dw = np.zeros_like(self.weights)
        dL_db = np.sum(dL_dy, axis=(0, 1, 2))  # 편향에 대한 그래디언트 계산

        dL_dx = np.zeros_like(self.input_data)

        for batch_idx in range(batch_size):
            for fh in range(output_height):
                for fw in range(output_width):
                    for f in range(num_filters):
                        h_start = fh * self.stride
                        h_end = h_start + filter_size
                        w_start = fw * self.stride
                        w_end = w_start + filter_size

                        dL_dw[f] += dL_dy[batch_idx, fh, fw, f] * self.input_data[batch_idx, h_start:h_end,
                                                                  w_start:w_end, :]
                        dL_dx[batch_idx, h_start:h_end, w_start:w_end, :] += dL_dy[batch_idx, fh, fw, f] * self.weights[
                            f]

        return dL_dx, dL_dw, dL_db


class RecurrentLayer:
    def __init__(self, input_size, hidden_size, activation='tanh'):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.activation = activation

        # Initialize weights and biases
        self.Wxh = np.random.randn(input_size, hidden_size)
        self.Whh = np.random.randn(hidden_size, hidden_size)
        self.bh = np.zeros((1, hidden_size))

        self.hidden_state = hidden_size

    def forward(self, input_data, initial_hidden_state):
        self.input_data = input_data
        self.initial_hidden_state = initial_hidden_state

        batch_size, seq_length, input_size = input_data.shape
        hidden_state = np.zeros((batch_size, seq_length + 1, self.hidden_size))
        hidden_state[:, 0, :] = initial_hidden_state

        for t in range(seq_length):
            xt = input_data[:, t, :]
            ht_prev = hidden_state[:, t, :]

            ht = np.tanh(np.dot(xt, self.Wxh) + np.dot(ht_prev, self.Whh) + self.bh)
            hidden_state[:, t + 1, :] = ht

        return hidden_state[:, 1:, :]  # Return all but the initial hidden state

    def backward(self, dL_dhidden):
        batch_size, seq_length, hidden_size = dL_dhidden.shape
        _, input_size = self.input_data.shape

        dL_dWxh = np.zeros_like(self.Wxh)
        dL_dWhh = np.zeros_like(self.Whh)
        dL_dbh = np.zeros_like(self.bh)

        dL_dxt = np.zeros_like(self.input_data)
        dL_dh_prev = np.zeros((batch_size, hidden_size))

        for t in reversed(range(seq_length)):
            dL_dht = dL_dhidden[:, t, :] + dL_dh_prev

            dL_dz = dL_dht * (1 - np.tanh(self.hidden_state[:, t, :]) ** 2)
            dL_dWxh += np.dot(self.input_data[:, t, :].T, dL_dz)
            dL_dWhh += np.dot(self.hidden_state[:, t - 1, :].T, dL_dz)
            dL_dbh += np.sum(dL_dz, axis=0, keepdims=True)

            dL_dxt[:, t, :] = np.dot(dL_dz, self.Wxh.T)
            dL_dh_prev = np.dot(dL_dz, self.Whh.T)

        return dL_dxt, dL_dWxh, dL_dWhh, dL_dbh

class Layer:
    def __init__(self, mode):
        self.mode = mode
    def forward(self, inputs):
        if self.mode == "relu":
            return self.relu_forward(inputs)
        if self.mode == "sigmoid":
            return self.sigmoid_forward(inputs)
        if self.mode == "softmax":
            return self.softmax_forward(inputs)

    def backward(self, dvalues):
        if self.mode == "relu":
            return self.backward(dvalues)
        if self.mode == "sigmoid":
            return self.backward(dvalues)
        if self.mode == "softmax":
            return self.backward(dvalues)

    def relu_forward(self, inputs):
        self.inputs = inputs
        self.output = np.maximum(0, inputs)
        return self.output

    def relu_backward(self, dvalues):
        self.dinputs = dvalues.copy()
        self.dinputs[self.inputs <= 0] = 0
        return self.dinputs

    def sigmoid_forward(self, inputs):
        self.inputs = inputs
        self.output = 1 / (1 + np.exp(-inputs))
        return self.output

    def sigmoid_backward(self, dvalues):
        self.dinputs = dvalues * (self.output * (1 - self.output))
        return self.dinputs

    def softmax_forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        self.output = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        return self.output

    def softmax_backward(self, dvalues):
        self.dinputs = dvalues
        return self.dinputs

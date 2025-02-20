import numpy as np 

np.random.seed(42)

X = [[1.0, 2.0, 3.0, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8]]


class LayersDense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = LayersDense(4, 5)
layer2 = LayersDense(5, 5)
layer3 = LayersDense(5, 2)


layer1.forward(X)
layer2.forward(layer1.output)
layer3.forward(layer2.output)
print(layer3.output)

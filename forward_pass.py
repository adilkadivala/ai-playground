import numpy as np

def relu(z):
    return np.maximum(0, z)

def forward_pass(x, W1, b1, W2, b2):
    z1 = (W1 @ x) + b1
    a1 = relu(z1)
    z2 = (W2 @ a1) + b2
    # No activation on the final layer here; raw score (e.g. for regression)
    return z2

# A tiny 2-input, 3-hidden-unit, 1-output network
W1 = np.array([[1.0, -1.0], [0.5, 0.5], [-1.0, 1.0]])
b1 = np.array([0.0, 0.0, 0.0])
W2 = np.array([[1.0, 1.0, 1.0]])
b2 = np.array([0.0])
x = np.array([1.0, 0.0])

print(forward_pass(x, W1, b1, W2, b2))
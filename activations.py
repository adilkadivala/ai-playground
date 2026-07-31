import numpy as np

def softmax(z, axis=-1):
    z = z - np.max(z, axis=axis, keepdims=True)
    # stability shift
    e = np.exp(z)
    return e / np.sum(e, axis=axis, keepdims=True)

def leaky_relu(z, alpha=0.01):
    return np.where(z >= 0, z, alpha * z)

def leaky_relu_grad(z, alpha=0.01):
    return np.where(z >= 0, 1.0, alpha)
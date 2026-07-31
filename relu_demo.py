import numpy as np

def relu(z):
    return np.maximum(0, z)
def relu_grad(z):
    return (z > 0).astype(float)

z = np.array([-3.0, -1.5, -0.2, -5.0, 3.0]) 
print("activations:", relu(z))
print("gradients: ", relu_grad(z))
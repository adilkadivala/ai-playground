import numpy as np

def softmax(z):
    z_shifted = z - np.max(z)
    exp_z = np.exp(z_shifted)
    return exp_z / np.sum(exp_z)

logits = np.array([2.0, 1.0, 0.1])

print(softmax(logits))
print("sums to:", softmax(logits).sum())
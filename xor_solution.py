import numpy as np

def step(z):
    return (z >= 0).astype(float)

# Hand-picked weights (not learned here, just to show representability)

W1 = np.array([[1.0, 1.0], [1.0, 1.0]])
b1 = np.array([-0.5, -1.5])
W2 = np.array([[1.0, -1.0]])
b2 = np.array([-0.5])

def xor_net(x):
    a1 = step(W1 @ x + b1)
    return step(W2 @ a1 + b2)

for x1 in [0, 1]:
    for x2 in [0, 1]:
        x = np.array([x1, x2])
        print(x1, x2, "->", int(xor_net(x)[0]))
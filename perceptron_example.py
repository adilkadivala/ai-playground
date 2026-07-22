def perceptron(x1, x2, w1=3.0, w2=-2.0, b=-1.0):
    z = w1 * x1 + w2 * x2 + b
    return 1 if z >= 0 else 0

# High credit score, low debt -> approve
print(perceptron(0.9, 0.1))
# z = 2.7 - 0.2 - 1 = 1.5 -> 1

# Low credit score, high debt -> deny
print(perceptron(0.2, 0.8))
# z = 0.6 - 1.6 - 1 = -2.0 -> 0
"""
Tiny training loop — student demo (no frameworks).
Idea: learn w and b so that prediction ≈ true target for one example.

Model:  y_hat = w * x + b
Loss:   |y_hat - y_true|   (simple absolute error)
Update: nudge w and b opposite to how they affect the error (hand-simple rule)
"""

# --- one training example ---
x = 2.0          # input
y_true = 10.0    # what we want the model to output

# --- start with "wrong" weights (guesses) ---
w = 1.0
b = 0.0
learning_rate = 0.1

print("Goal: make prediction close to", y_true, "when x =", x)
print("Start: w =", w, "b =", b)
print("-" * 40)

for step in range(20):
    # 1) FORWARD PASS — prediction
    y_hat = w * x + b

    # 2) LOSS — how wrong?
    loss = abs(y_hat - y_true)

    # 3) Simple slopes (for this tiny linear model)
    #    If prediction is too high, we want to decrease w and b.
    #    If prediction is too low, we want to increase w and b.
    error = y_hat - y_true          # positive => too high
    # slope of (w*x+b) vs w is x; vs b is 1
    grad_w = error * x              # direction for w
    grad_b = error * 1              # direction for b

    # 4) GRADIENT DESCENT UPDATE
    w = w - learning_rate * grad_w
    b = b - learning_rate * grad_b

    print(f"step {step:2d} | pred={y_hat:7.3f} | loss={loss:7.3f} | w={w:7.3f} | b={b:7.3f}")

print("-" * 40)
print("Done. Prediction should be near", y_true)
print("Final: w =", round(w, 3), "b =", round(b, 3))

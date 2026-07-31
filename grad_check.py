import numpy as np

def grad_check(f, x, analytic_grad, eps=1e-5, tol=1e-6):
    """f: scalar fn of vector x. analytic_grad: your computed gradient."""
    num = np.zeros_like(x, dtype=float)
    for i in range(x.size):
        xp, xm = x.copy(), x.copy()
        xp[i] += eps
        xm[i] -= eps
        num[i] = (f(xp) - f(xm)) / (2 * eps)
    # central difference
    rel = np.abs(num - analytic_grad) / (np.abs(num) + np.abs(analytic_grad) + 1e-12)
    return rel.max(), rel.max() < tol
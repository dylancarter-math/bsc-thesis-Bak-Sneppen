import numpy as np
from scipy.optimize import minimize_scalar, brentq

# Critical value
PHI_C = 0.7491

# Computed lower bound from proof section
def P(L, p):
    q = 1 - p
    a = 2*q**3/3 + 4*q**2/3 + 2*q - 6
    return np.exp(a*L) * (np.exp(L*q**2/3) - 1)**2 * (np.exp(L*q**3/3) - 1)**4

# Computes supremum of P(L, p) over L
def P_max(p):
    res = minimize_scalar(lambda L: -P(L, p), bounds=(1e-6, 500), method='bounded')
    return -res.fun, res.x

# Solve for p* such that P_max(p*) = PHI_C
p_star = brentq(lambda p: P_max(p)[0] - PHI_C, 1e-5, 0.1)

# Corresponding optimal length L
L_hat  = P_max(p_star)[1]

print(f"p*    = {p_star:.6f} < p_c")
print(f"L_hat = {L_hat:.4f}")
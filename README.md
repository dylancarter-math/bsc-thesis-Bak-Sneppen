# Discrete Bak-Sneppen Model

**Author:** D. Carter  
**Supervisors:** Dr. R. Szabo, Prof. dr. J.P. Trapman  

This repository contains the code and supplementary materials for my Bachelor's thesis: *"Bounds for the discrete Bak-Sneppen model"* (June 2026).

---

## Overview

The **discrete Bak-Sneppen model** is an interacting particle system where $N$ species arranged on a ring have binary fitness values (0 or 1). At each step:

1. A zero-fitness species is chosen uniformly at random (or any species if all are ones).
2. That species and its two neighbours are updated with new Bernoulli($p$) fitness values.

The key question is the value of a **critical probability** $p_c$:

- For $p < p_c$ : zeros survive with positive density in the stationary distribution.
- For $p > p_c$: the system converges to the all-ones state.

This thesis establishes both rigorous upper and lower bounds for $p_c$ and provides numerical simulations to support the findings.

---

## Repository Contents

| File | Description |
|------|-------------|
| `BachelorsThesis.pdf` | Full thesis document with theoretical proofs, simulation results, and conclusions. |
| `BakSnepp_Simulation.ipynb` | Python script with discrete Bak-Sneppen simulations for various $p$ and system sizes $N$. |
| `Numerical_LowerBound.py` | Numerical optimization to compute the lower bound $p_c > 0.00138$ using oriented percolation comparison. |

---

## Simulation Details

- **State space:** {0,1}<sup>N</sup> on a 1D ring with periodic boundary conditions.
- **Update rule:** Bernoulli(p) resampling of a chosen zero (or random if none) and its two neighbours.
- **Measured quantity:** Stationary fraction of zeros $$Z = \frac{1}{N} \sum_i \mathbf{1}_{\{X_i = 0\}}$$.
- **Burn-in:** First 20–40% of iterations discarded before averaging.

### Example Results

| p | Stationary zero density N = 10000 |
|--------|-------------------------------------------|
| 0.0005 | 0.99924 |
| 0.001  | 0.99857 |
| 0.002  | 0.99696 |

These confirm zero survival for small $p$, consistent with the theoretical lower bound.

For larger $p$ (e.g., $p = 0.36, 0.37, 0.38$), the zero density drops sharply, suggesting a critical value near $p_c \approx 0.365$.

---

## Key Theoretical Results

### Upper Bound

For $p > p^* $, where $p^\ast$ is the unique positive solution of

$$
p^5 + 4p^4 + 2p^3 + 3p^2 = 1,
$$

the stationary probability of a species being in state 1 satisfies

$$
\pi^{(N)}(p) \to 1 \quad \text{as } N \to \infty.
$$

Thus,
$p_c \leq p^* \approx 0.45\ldots$.

### Lower Bound

Using a graphical representation and comparison with oriented percolation (with critical probability
$\phi_c < 0.72599$
),
numerical optimization yields $p_c > 0.00138$.

We prove that for sufficiently small $p$, zeros survive in the stationary distribution with positive density.

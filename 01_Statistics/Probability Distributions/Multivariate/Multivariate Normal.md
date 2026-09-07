## Overview
* **Type:** Continuous (Multivariate)
* **Key Intuition:** Jointly normal random variables with linear dependence captured by a covariance matrix
* **Example Use Cases:**
    * Modeling correlated measurement errors
    * Multivariate regression and Gaussian processes
    * Prior distributions over vectors in Bayesian models

---

## Mathematical Definition

### Notation
$\mathbf{X} \sim \mathcal{N}_d(\boldsymbol{\mu}, \boldsymbol{\Sigma})$

where
$$\boldsymbol{\mu} =
\begin{pmatrix}
\mu_1 \\ \mu_2 \\ \vdots \\ \mu_d
\end{pmatrix},
\qquad
\boldsymbol{\Sigma} =
\begin{pmatrix}
\sigma_{11} & \sigma_{12} & \cdots & \sigma_{1d} \\
\sigma_{21} & \sigma_{22} & \cdots & \sigma_{2d} \\
\vdots      & \vdots      & \ddots & \vdots      \\
\sigma_{d1} & \sigma_{d2} & \cdots & \sigma_{dd}
\end{pmatrix}$$

with $\boldsymbol{\Sigma}$ symmetric and positive definite.

### Probability Density Function (PDF)
> $$f(\mathbf{x}) =
\frac{1}{(2\pi)^{d/2} |\boldsymbol{\Sigma}|^{1/2}}
\exp\!\left(
-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^\top
\boldsymbol{\Sigma}^{-1}
(\mathbf{x}-\boldsymbol{\mu})
\right)$$

### Cumulative Distribution Function (CDF)
> No closed-form expression for $d>1$

---

## Parameters & Support
* **Parameters:**
    * $\boldsymbol{\mu} \in \mathbb{R}^d$: Mean vector
    * $\boldsymbol{\Sigma} \in \mathbb{R}^{d \times d}$: Covariance matrix (symmetric, positive definite)
    * $d \in \mathbb{N}$: Dimension of the random vector

* **Support:** $\mathbf{x} \in \mathbb{R}^d$

---

## Key Properties

| Property                   | Formula / Description                                                                                                                                    |
| :------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mean ($E[\mathbf{X}]$)** | $\boldsymbol{\mu}$                                                                                                                                       |
| **Covariance**             | $\boldsymbol{\Sigma}$                                                                                                                                    |
| **Mode**                   | $\boldsymbol{\mu}$                                                                                                                                       |
| **Marginals**              | Any subset is multivariate normal                                                                                                                        |
| **Conditionals**           | Normal with affine mean, reduced covariance                                                                                                              |
| **Affine Transform**       | $A\mathbf{X}+b \sim \mathcal{N}(A\boldsymbol{\mu}+b,\;A\boldsymbol{\Sigma}A^\top)$                                                                       |
| **Quadratic Form**         | $(\mathbf{X}-\boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1} (\mathbf{X}-\boldsymbol{\mu}) \sim \chi^2_d$                                                |
| **Fisher Information**     | $\mathcal{I}(\boldsymbol{\mu})=\boldsymbol{\Sigma}^{-1}$ (known $\boldsymbol{\Sigma}$)                                                                   |
| **MLE**                    | $\hat{\boldsymbol{\mu}}=\bar{\mathbf{X}},\;\hat{\boldsymbol{\Sigma}}=\frac{1}{n}\sum(\mathbf{X}_i-\bar{\mathbf{X}})(\mathbf{X}_i-\bar{\mathbf{X}})^\top$ |

---

## Relationships to Other Distributions
* **[[Normal]]:** Special case when $d = 1$
---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.multivariate_normal`
* **R:** `mvtnorm::dmvnorm`, `rmvnorm`

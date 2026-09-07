## Overview
* **Type:** Continuous (Multivariate)
* **Key Intuition:** Distribution over probability vectors; conjugate prior for the [[Categorical]] distribution
* **Example Use Cases:**
    * Prior over class probabilities in Bayesian classification


---

## Mathematical Definition

### Notation
$\boldsymbol{P} \sim Dir(\boldsymbol{\alpha})$

where $\boldsymbol{\alpha} = (\alpha_1, \alpha_2, \dots, \alpha_K)$ with $\alpha_i > 0$.

### Probability Density Function (PDF)
> $$f(\boldsymbol{p}) = \frac{1}{B(\boldsymbol{\alpha})}
\prod_{i=1}^{K} p_i^{\alpha_i - 1}$$

where
> $$B(\boldsymbol{\alpha}) = \frac{\prod_{i=1}^{K} \Gamma(\alpha_i)}{\Gamma\!\left(\sum_{i=1}^{K} \alpha_i\right)}$$

---

## Parameters & Support
* **Parameters:**
    * $\alpha_i$: Concentration parameter for category $i$
    * $\alpha_0 = \sum_{i=1}^K \alpha_i$: Total concentration

* **Support:**  
$\boldsymbol{p} = (p_1, \dots, p_K)$ such that $p_i \ge 0$ and $\sum_{i=1}^K p_i = 1$

---

## Key Properties

| Property                         | Formula                                                                 |
| :------------------------------- | :---------------------------------------------------------------------- |
| **Mean ($E[p_i]$)**              | $\displaystyle \frac{\alpha_i}{\alpha_0}$                               |
| **Mode**                         | $\displaystyle \frac{\alpha_i - 1}{\alpha_0 - K}$ (if all $\alpha_i > 1$) |
| **Variance ($Var(p_i)$)**        | $\displaystyle \frac{\alpha_i(\alpha_0 - \alpha_i)}{\alpha_0^2(\alpha_0 + 1)}$ |
| **Covariance ($Cov(p_i,p_j)$)**  | $\displaystyle -\frac{\alpha_i\alpha_j}{\alpha_0^2(\alpha_0 + 1)}$      |
| **Entropy**                      | No simple closed form                                                   |
| **Fisher Information**           | Known in closed form; involves trigamma functions                       |
| **Jeffreys Prior**               | $\displaystyle \prod_{i=1}^K p_i^{-1/2}$ (improper on simplex)           |
| **MAP Estimator**                | $\displaystyle \frac{\alpha_i - 1}{\alpha_0 - K}$                       |

---

## Relationships to Other Distributions
* **[[Beta]]:** Special case with $K = 2$
* **[[Categorical]]:** Conjugate prior for categorical

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.dirichlet`
* **R:** `ddirichlet`, `rdirichlet` (package `MCMCpack`)

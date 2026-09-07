## Overview
* **Type:** Discrete (Multivariate)
* **Key Intuition:** Distribution over category counts when $n$ independent draws are each made from a [[Categorical]] distribution; the multivariate generalization of the [[Binomial]]
* **Example Use Cases:**
    * Word counts across vocabulary categories in a document
    * Counts of outcomes in $n$ rolls of a $K$-sided die
    * Vote tallies across $K$ candidates from $n$ voters

---

## Mathematical Definition

### Notation
$\mathbf{X} \sim \text{Mult}(n, \boldsymbol{p})$

where $\boldsymbol{p} = (p_1, p_2, \dots, p_K)$ with $p_i \ge 0$ and $\sum_{i=1}^K p_i = 1$.

### Probability Mass Function (PMF)
> $$P(\mathbf{X} = \mathbf{x}) = \binom{n}{x_1,\, x_2,\, \dots,\, x_K} \prod_{i=1}^{K} p_i^{x_i}
= \frac{n!}{\prod_{i=1}^K x_i!} \prod_{i=1}^{K} p_i^{x_i}$$

---

## Parameters & Support
* **Parameters:**
    * $n \in \mathbb{N}$: Total number of trials
    * $p_i$: Probability of category $i$, with $p_i \ge 0$
    * $K \in \mathbb{N}$: Number of categories

* **Support:**
$\mathbf{x} = (x_1, \dots, x_K)$ with $x_i \in \{0, 1, \dots, n\}$ and $\sum_{i=1}^K x_i = n$

---

## Key Properties

| Property                            | Formula                                                                              |
| :---------------------------------- | :----------------------------------------------------------------------------------- |
| **Mean ($E[X_i]$)**                 | $\displaystyle n p_i$                                                                |
| **Mode**                            | $\displaystyle \lfloor (n+K-1)\,p_i \rfloor$ or $\lceil (n+K-1)\,p_i \rceil - 1$   |
| **Variance ($Var(X_i)$)**           | $\displaystyle n p_i (1 - p_i)$                                                      |
| **Covariance ($Cov(X_i, X_j)$)**   | $\displaystyle -n p_i p_j \quad (i \ne j)$                                           |
| **MGF**                             | $\displaystyle \left(\sum_{i=1}^K p_i e^{t_i}\right)^n$                             |
| **Entropy**                         | No simple closed form in general                                                     |
| **MLE ($\hat{p}_i$)**               | $\displaystyle \frac{x_i}{n}$ (observed relative frequency)                          |

---

## Relationships to Other Distributions
* **[[Binomial]]:** Special case with $K = 2$; $X_1 \sim Bin(n, p_1)$
* **[[Categorical]]:** Special case when $n = 1$

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.multinomial`
* **R:** `dmultinom`, `rmultinom`

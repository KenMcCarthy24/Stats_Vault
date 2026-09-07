![[Categorical_pmf.svg]]
## Overview
* **Type:** Discrete
* **Key Intuition:** Single draw from a finite set of categories, each with its own probability
* **Example Use Cases:**
    * Outcome of a biased die roll
    * Survey response chosen from a fixed list of options

---

## Mathematical Definition

### Notation
$X \sim Cat(\boldsymbol{p})$

where $\boldsymbol{p} = (p_1, p_2, \dots, p_K)$ and $\sum_{i=1}^K p_i = 1$.

### Probability Mass (PMF)
> $$P(X = i) = p_i \quad \text{for } i = 1, \dots, K$$

### Cumulative Distribution Function (CDF)
> $$F(i) = P(X \le i) = \sum_{j=1}^{i} p_j$$  
*(Requires an ordering of categories)*

---

## Parameters & Support
* **Parameters:**
    * $p_i$: Probability of category $i$, with $p_i \ge 0$
    * $K$: Number of categories

* **Support:** $x \in \{1, 2, \dots, K\}$

---

## Key Properties

| Property                | Formula                                                        |
| :---------------------- | :------------------------------------------------------------- |
| **Mean ($E[X]$)**       | $\displaystyle \sum_{i=1}^K i\,p_i$ *(index-dependent)*        |
| **Median**              | Not uniquely defined                                           |
| **Mode**                | $\displaystyle \arg\max_i p_i$                                 |
| **Variance ($Var(X)$)** | $\displaystyle \sum_{i=1}^K i^2 p_i - \left(\sum_{i=1}^K i p_i\right)^2$ |
| **Skewness**            | Depends on category ordering                                   |
| **Kurtosis**            | Depends on category ordering                                   |
| **Fisher Information**  | $\displaystyle \text{diag}\!\left(\frac{1}{p_1}, \dots, \frac{1}{p_K}\right)$ (with constraint $\sum p_i = 1$) |
| **Jeffreys Prior**      | $\displaystyle \prod_{i=1}^K p_i^{-1/2}$                       |
| **MLE**                 | $\displaystyle \hat{p}_i = \mathbb{1}\{X=i\}$ (single draw)    |

---

## Relationships to Other Distributions
* **[[Bernoulli]]:** Special case with $K = 2$
* **[[Multinomial]]:** Generalisation to $n$ independent draws
* **[[Dirichlet]]:** Bayesian Conjugate prior for $\boldsymbol{p}$

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.multinomial` (with `n=1`)
* **R:** `dcat` (package `extraDistr`), `rmultinom` (with `size = 1`)

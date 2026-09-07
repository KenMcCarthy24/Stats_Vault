![[Bernoulli_pmf.svg]]
## Overview
* **Type:** Discrete
* **Key Intuition:** Single binary event with probability $p$
* **Example Use Cases:**
    * Probability of getting heads on a single coin flip
    * Probability of testing positive for a disease
    * Probability it will rain today

---

## Mathematical Definition

### Notation
$X \sim Bern(p)$

### Probability Mass Function (PMF)
> $$f(k; p) = p^k(1-p)^{1-k}$$


---

## Parameters & Support
* **Parameters:**
    * $p$: Probability of event
* **Support:** $x \in \{0, 1\}$
* Often also use $q=1-p$

---

## Key Properties

| Property                | Formula                             |
| :---------------------- | :---------------------------------- |
| **Mean ($E[X]$)**       | $p$                                 |
| **Variance ($Var(X)$)** | $pq$                                |
| **Fisher Information**  | $\displaystyle\frac{1}{pq}$         |
| **Jefferys Prior**      | $\displaystyle \frac{1}{\sqrt{pq}}$ |
| **MLE**                 | $\bar{X}$                           |

---

## Relationships to Other Distributions
* **[[Binomial]]:** Special case of Binomial when n=1
* **[[Beta]]**: Bayesian Conjugate Prior

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.bernoulli`
* **R:** `dbern`, `pbern`, `qbern`, `rbern`

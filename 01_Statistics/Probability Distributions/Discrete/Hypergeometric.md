![[Hypergeometric_pmf.svg]]
## Overview
* **Type:** Discrete
* **Key Intuition:** Number of successes observed when drawing a fixed-size sample **without replacement** from a finite population
* **Example Use Cases:**
    * Number of red balls drawn from an urn without replacement
    * Number of defective items in a quality-control sample
    * Card problems (e.g., number of Hearts in a 5-card hand)

---

## Mathematical Definition

### Notation
$X \sim Hypergeom(N, K, n)$

### Probability Mass (PMF)
> $$P(X = k) = \frac{\binom{K}{k}\binom{N-K}{\,n-k\,}}{\binom{N}{n}}$$

### Cumulative Distribution Function (CDF)
> $$F(k) = P(X \le k) = \sum_{j=0}^{k} \frac{\binom{K}{j}\binom{N-K}{\,n-j\,}}{\binom{N}{n}}$$

---

## Parameters & Support
* **Parameters:**
    * $N$: Population size
    * $K$: Number of successes in the population
    * $n$: Sample size (draws without replacement)

* **Support:**  
  $$k \in \{\max(0, n-(N-K)), \dots, \min(n, K)\}$$

---

## Key Properties

| Property                | Formula                                                                 |
| :---------------------- | :---------------------------------------------------------------------- |
| **Mean ($E[X]$)**       | $\displaystyle n\frac{K}{N}$                                            |
| **Median**              | No closed form                                                          |
| **Mode**                | $\displaystyle \left\lfloor \frac{(n+1)(K+1)}{N+2} \right\rfloor$        |
| **Variance ($Var(X)$)** | $\displaystyle n\frac{K}{N}\left(1-\frac{K}{N}\right)\frac{N-n}{N-1}$    |
| **Skewness**            | $\displaystyle \frac{(N-2K)\sqrt{N-1}(N-2n)}{\sqrt{nK(N-K)(N-n)}(N-2)}$   |
| **Kurtosis**            | $\displaystyle \text{(complicated; rarely used in practice)}$          |
| **Fisher Information**  | Not typically expressed in closed form                                  |
| **Jeffreys Prior**      | No simple closed form                                                    |
| **MLE**                 | $\displaystyle \hat{K} \approx \frac{N}{n}\bar{X}$                      |

---

## Relationships to Other Distributions
* **[[Binomial]]:** Limit as $N \to \infty$ with $\frac{K}{N} \to p$

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.hypergeom`
* **R:** `dhyper`, `phyper`, `qhyper`, `rhyper`

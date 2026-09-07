![[Geometric_pmf.svg]]
## Overview
* **Type:** Discrete
* **Key Intuition:** Number of successive [[Bernoulli]] trials with probability $p$ until first success
* **Example Use Cases:**
    * Number of Tails flipped on a fair coin until first Heads
    * Number of customers contacted until a single sale is made

---

## Mathematical Definition

### Notation
$X \sim Geom(p)$

### Probability Mass (PMF)
> $$f(k;p) = p(1-p)^{k-1}$$

### Cumulative Distribution Function (CDF)
> $$F(k;p) = P(X \le k) = 1-(1-p)^k$$

---

## Parameters & Support
* **Parameters:**
    * $p$: Probability of success $p$ of each trial

* **Support:** $x \in \{1, 2, 3, \dots\}$

---

## Key Properties

| Property                | Formula                                            |
| :---------------------- | :------------------------------------------------- |
| **Mean ($E[X]$)**       | $\displaystyle\frac{1}{p}$                         |
| **Median**              | $$\left\lceil \frac{-1}{log_2(1-p)} \right\rceil$$ |
| **Mode**                | $1$                                                |
| **Variance ($Var(X)$)** | $$\frac{1-p}{p^2}$$                                |
| **Skewness**            | $$\frac{2-p}{\sqrt{1-p}}$$                         |
| **Kurtosis**            | $$9 + \frac{p^2}{1-p}$$                            |
| **Fisher Information**  | $$\frac{1}{p^2(1-p)}$$                             |
| **Jefferys Prior**      | $$\frac{1}{p\sqrt{1-p}}$$                          |
| **MLE**                 | $$\frac{1}{\bar{X}}$$                              |


---

## Relationships to Other Distributions
* **[[Negative Binomial]]:** Special case of Negative Binomial when $r=1$.
	* Sum of $r$ independent geometric random variables is $NB(r, p)$
* **[[Beta]]**: Bayesian Conjugate prior for $p$

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.geom`
* **R:** `dgeom`, `pgeom`, `qgeom`, `rgeom`

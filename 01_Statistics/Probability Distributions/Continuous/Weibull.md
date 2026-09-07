![[Weibull_pdf.svg]]
## Overview
* **Type:** Continuous
* **Key Intuition:** Flexible lifetime distribution capturing increasing, constant, or decreasing hazard rates. Generalization of the [[Exponential]] distribution.
* **Example Use Cases:**
    * Time-to-failure and reliability modeling
    * Survival analysis and hazard-rate modeling
    * Modeling wind speeds, material strength, and aging processes

---

## Mathematical Definition

### Notation
$X \sim \mathrm{Weibull}(k, \lambda)$

where $k$ is the **shape** and $\lambda$ is the **scale**.

### Probability Density Function (PDF)
$$f(x) = \frac{k}{\lambda}\left(\frac{x}{\lambda}\right)^{k-1}
\exp\!\left[-\left(\frac{x}{\lambda}\right)^k\right], \qquad x \ge 0$$

### Cumulative Distribution Function (CDF)
> $$F(x) = 1 - \exp\!\left[-\left(\frac{x}{\lambda}\right)^k\right]$$

---

## Parameters & Support
* **Parameters:**
    * $k > 0$: Shape parameter  
        * $k < 1$: Decreasing hazard  
        * $k = 1$: Constant hazard  
        * $k > 1$: Increasing hazard
    * $\lambda > 0$: Scale parameter

* **Support:** $x \in [0,\infty)$

---

## Key Properties

| Property                | Formula                                                                                                                     |
| :---------------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| **Mean ($E[X]$)**       | $\displaystyle \lambda\,\Gamma\!\left(1+\frac{1}{k}\right)$                                                                 |
| **Median**              | $\displaystyle \lambda(\log 2)^{1/k}$                                                                                       |
| **Mode**                | $\displaystyle \lambda\left(\frac{k-1}{k}\right)^{1/k}$ (for $k>1$)                                                         |
| **Variance ($Var(X)$)** | $\displaystyle \lambda^2\!\left[\Gamma\!\left(1+\frac{2}{k}\right)- \Gamma^2\!\left(1+\frac{1}{k}\right)\right]$            |

---

## Relationships to Other Distributions
* **[[Exponential]]:** When $k = 1$,  $X \sim \text{Exp}(1/\lambda)$

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.weibull_min`
* **R:** `dweibull`, `pweibull`, `qweibull`, `rweibull`

![[Normal_pdf.svg]]
**Note**: Also commonly referred to as **Gaussian**
## Overview
* **Type:** Continuous
* **Key Intuition:** Symmetric, bell-shaped distribution describing natural variation around a mean
* **Example Use Cases:**
    * Measurement noise and errors
    * Heights, test scores, and other approximately symmetric biological or social variables
    * Limiting distribution of sums/averages via the Central Limit Theorem

---

## Mathematical Definition

### Notation
$X \sim \mathcal{N}(\mu, \sigma^2)$

### Probability Density Function (PDF)
> $$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}
> \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

### Cumulative Distribution Function (CDF)
> $$F(x) = P(X \le x) = \Phi\!\left(\frac{x-\mu}{\sigma}\right)$$

where $\Phi(\cdot)$ is the standard normal ($\mathcal{N}(0, 1)$) CDF, which is a common enough to have its own symbol.

---

## Parameters & Support
* **Parameters:**
    * $\mu$: Mean (location)
    * $\sigma^2$: Variance (scale), with $\sigma > 0$

* **Support:** $x \in (-\infty, \infty)$

---

## Key Properties

| Property                | Formula                                                                                         |
| :---------------------- | :---------------------------------------------------------------------------------------------- |
| **Mean ($E[X]$)**       | $\displaystyle \mu$                                                                             |
| **Median**              | $\displaystyle \mu$                                                                             |
| **Mode**                | $\displaystyle \mu$                                                                             |
| **Variance ($Var(X)$)** | $\displaystyle \sigma^2$                                                                        |
| **Skewness**            | $0$                                                                                             |
| **Kurtosis**            | $3$ (excess kurtosis $0$)                                                                       |
| **Entropy**             | $\displaystyle \tfrac{1}{2}\log(2\pi e\sigma^2)$                                                |
| **Fisher Information**  | $\displaystyle \mathcal{I}(\mu)=\frac{1}{\sigma^2},\;\mathcal{I}(\sigma^2)=\frac{1}{2\sigma^4}$ |
| **MLE**                 | $\displaystyle \hat{\mu}=\bar{X},\;\hat{\sigma}^2=\frac{1}{n}\sum (X_i-\bar{X})^2$              |


---

## Relationships to Other Distributions
* **Standard Normal:** Special case with $\mu=0$, $\sigma^2=1$
* **[[Chi-Squared]]:** Sum of squared standard normals
* **[[Student-t]]:** Normal with unknown variance integrated out
* **[[Lognormal]]:** Exponential of a normal random variable

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.norm`
* **R:** `dnorm`, `pnorm`, `qnorm`, `rnorm`

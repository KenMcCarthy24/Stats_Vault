![[Lognormal_pdf.svg]]
## Overview
* **Type:** Continuous
* **Key Intuition:** Distribution of a positive random variable whose logarithm is normally distributed
* **Example Use Cases:**
    * Asset prices and returns over long horizons
    * Income and wealth distributions
    * Biological measurements constrained to be positive (e.g., cell sizes)

---

## Mathematical Definition

### Notation
$X \sim \text{LogNormal}(\mu, \sigma^2)$  

Equivalently,
$$\log X \sim \mathcal{N}(\mu, \sigma^2)$$

### Probability Density Function (PDF)
> $$f(x) = \frac{1}{x\sigma\sqrt{2\pi}}
> \exp\!\left(-\frac{(\log x - \mu)^2}{2\sigma^2}\right), \quad x>0$$

### Cumulative Distribution Function (CDF)
> $$F(x) = P(X \le x) = \Phi\!\left(\frac{\log x - \mu}{\sigma}\right), \quad x>0$$

where $\Phi(\cdot)$ is the standard normal CDF.

---

## Parameters & Support
* **Parameters:**
    * $\mu$: Mean of $\log X$
    * $\sigma^2$: Variance of $\log X$, with $\sigma > 0$

* **Support:** $x \in (0, \infty)$

---

## Key Properties

| Property                | Formula                                                                                                   |
| :---------------------- | :-------------------------------------------------------------------------------------------------------- |
| **Mean ($E[X]$)**       | $\displaystyle e^{\mu + \sigma^2/2}$                                                                      |
| **Median**              | $\displaystyle e^{\mu}$                                                                                   |
| **Mode**                | $\displaystyle e^{\mu - \sigma^2}$                                                                        |
| **Variance ($Var(X)$)** | $\displaystyle (e^{\sigma^2}-1)e^{2\mu+\sigma^2}$                                                         |
| **Skewness**            | $\displaystyle (e^{\sigma^2}+2)\sqrt{e^{\sigma^2}-1}$                                                     |
| **Kurtosis**            | $\displaystyle e^{4\sigma^2}+2e^{3\sigma^2}+3e^{2\sigma^2}-6$                                             |
| **Fisher Information**  | $\displaystyle \mathcal{I}(\mu)=\frac{1}{\sigma^2},\;\mathcal{I}(\sigma^2)=\frac{1}{2\sigma^2}$           |
| **MLE**                 | $\displaystyle \hat{\mu}=\frac{1}{n}\sum \log X_i,\;\hat{\sigma}^2=\frac{1}{n}\sum(\log X_i-\hat{\mu})^2$ |


---

## Relationships to Other Distributions
* **[[Normal]]:** Logarithm of a lognormal is normal

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.lognorm` (parameterized by `s=\sigma`, `scale=e^{\mu}`)
* **R:** `dlnorm`, `plnorm`, `qlnorm`, `rlnorm`

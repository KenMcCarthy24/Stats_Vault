![[ChiSquared_pdf.svg]]
## Overview
* **Type:** Continuous
* **Key Intuition:** Distribution of the sum of squares of $n$ independent standard normal random variables
* **Example Use Cases:**
    * Variance estimation in normal models
    * Goodness-of-fit tests (e.g. Pearson’s $\chi^2$ test)
    * Likelihood ratio tests and inference on dispersion

---

## Mathematical Definition

### Notation
$X \sim \chi^2_k$

### Probability Density Function (PDF)
> $$f(x) = \frac{1}{2^{k/2}\Gamma(k/2)} x^{\frac{k}{2}-1} e^{-x/2}, \quad x > 0$$

### Cumulative Distribution Function (CDF)
> $$F(x) = P(X \le x)
> = \frac{\gamma\!\left(\frac{k}{2}, \frac{x}{2}\right)}{\Gamma\!\left(\frac{k}{2}\right)}$$

where $\Gamma(\cdot)$ is the gamma function and  $\gamma(\cdot,\cdot)$ is the lower incomplete gamma function.

---

## Parameters & Support
* **Parameters:**
    * $k$: [[Degrees of Freedom]] ($n > 0$)

* **Support:** $x \in (0, \infty)$

---

## Key Properties

| Property                | Formula                                                                                                                                       |
| :---------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mean ($E[X]$)**       | $\displaystyle k$                                                                                                                             |
| **Median**              | $\displaystyle k\!\left(1 - \frac{2}{9k}\right)^3$ (approx.)                                                                                  |
| **Mode**                | $\displaystyle \max(k-2, 0)$                                                                                                                  |
| **Variance ($Var(X)$)** | $\displaystyle 2k$                                                                                                                            |
| **Skewness**            | $\displaystyle \sqrt{\frac{8}{k}}$                                                                                                            |
| **Kurtosis**            | $\displaystyle 3 + \frac{12}{k}$                                                                                                              |
| **Entropy**             | $\displaystyle \frac{k}{2} + \log\!\left(2\Gamma\!\left(\frac{k}{2}\right)\right) + \left(1-\frac{k}{2}\right)\psi\!\left(\frac{k}{2}\right)$ |

$\psi(\cdot)$ is the digamma function 

---

## Relationships to Other Distributions
* **[[Gamma]]:** $\chi^2_k \equiv \text{Gamma}\!\left(\frac{k}{2}, \frac{1}{2}\right)$
* **[[Normal]]:** Sum of squares of $n$ independent $\mathcal{N}(0,1)$ variables
* **[[Student-t]]:** Ratio of a normal and the square root of a scaled $\chi^2$
* **[[F-distribution]]:** Ratio of scaled chi-squared variables

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.chi2`
* **R:** `dchisq`, `pchisq`, `qchisq`, `rchisq`

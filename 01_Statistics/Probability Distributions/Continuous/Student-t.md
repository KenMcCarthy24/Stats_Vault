![[Student_t_pdf.svg]]
## Overview
* **Type:** Continuous
* **Key Intuition:** Symmetric, heavy-tailed distribution that arises when estimating a normal mean with unknown variance
* **Example Use Cases:**
    * Small-sample inference for a population mean
    * Hypothesis testing and confidence intervals (Student’s *t*-tests)
    * Robust alternative to the normal when variance is uncertain

---

## Mathematical Definition

### Notation
$X \sim t_\nu$

where $\nu$ is the number of degrees of freedom.

### Probability Density Function (PDF)
> $$f(x)
 = \frac{\Gamma\!\left(\frac{\nu+1}{2}\right)}
 {\sqrt{\nu\pi}\,\Gamma\!\left(\frac{\nu}{2}\right)}
 \left(1 + \frac{x^2}{\nu}\right)^{-\frac{\nu+1}{2}},
 \quad x \in \mathbb{R}$$

### Cumulative Distribution Function (CDF)
> $$F(x) = P(X \le x)$$  
> *(No closed form; expressed via the regularized incomplete beta function)*

---

## Parameters & Support
* **Parameters:**
    * $\nu$: Degrees of freedom ($\nu > 0$)

* **Support:** $x \in (-\infty, \infty)$

---

## Key Properties

| Property                | Formula / Value                                                                         |
| :---------------------- | :-------------------------------------------------------------------------------------- |
| **Mean ($E[X]$)**       | $0$ for $\nu > 1$                                                                       |
| **Median**              | $0$                                                                                     |
| **Mode**                | $0$                                                                                     |
| **Variance ($Var(X)$)** | $\displaystyle \frac{\nu}{\nu-2}$ for $\nu > 2$                                         |
| **Skewness**            | $0$ for $\nu > 3$                                                                       |
| **Kurtosis**            | $\displaystyle 3 + \frac{6}{\nu-4}$ for $\nu > 4$                                       |

---

## Relationships to Other Distributions
* **[[Normal]]:** Limit as $\nu \to \infty$
* **[[Chi-Squared]]:** If $Z \sim \mathcal{N}(0,1)$ and $U \sim \chi^2_\nu$ are independent, then  
  $\displaystyle \frac{Z}{\sqrt{U/\nu}} \sim t_\nu$
* **[[F-distribution]]:** $t_\nu^2 \sim F_{1,\nu}$

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.t`
* **R:** `dt`, `pt`, `qt`, `rt`

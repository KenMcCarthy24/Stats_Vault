![[F_dist_pdf.svg]]
## Overview
* **Type:** Continuous
* **Key Intuition:** Distribution of the ratio of two independent scaled [[Chi-Squared]] random variables; compares relative variances
* **Example Use Cases:**
    * Testing equality of variances
    * ANOVA and regression F-tests
    * Comparing nested linear models

---

## Mathematical Definition

### Notation
$X \sim F_{d_1, d_2}$

where $d_1$ and $d_2$ are the numerator and denominator degrees of freedom.

### Probability Density Function (PDF)
> $$f(x)
= \frac{\Gamma\!\left(\frac{d_1+d_2}{2}\right)}
{\Gamma\!\left(\frac{d_1}{2}\right)\Gamma\!\left(\frac{d_2}{2}\right)}
\left(\frac{d_1}{d_2}\right)^{\frac{d_1}{2}}
\frac{x^{\frac{d_1}{2}-1}}
{\left(1+\frac{d_1}{d_2}x\right)^{\frac{d_1+d_2}{2}}},
\quad x > 0$$

### Cumulative Distribution Function (CDF)
> $$F(x) = P(X \le x)$$  
> *(Expressed via the regularized incomplete beta function)*

---

## Parameters & Support
* **Parameters:**
    * $d_1$: Numerator [[Degrees of Freedom]] ($d_1 > 0$)
    * $d_2$: Denominator [[Degrees of Freedom]] ($d_2 > 0$)

* **Support:** $x \in (0, \infty)$

---

## Key Properties

| Property                | Formula / Value                                                           |
| :---------------------- | :------------------------------------------------------------------------ |
| **Mean ($E[X]$)**       | $\displaystyle \frac{d_2}{d_2-2}$ for $d_2 > 2$                           |
| **Median**              | No closed form                                                            |
| **Mode**                | $\displaystyle \frac{(d_1-2)d_2}{d_1(d_2+2)}$ for $d_1 > 2$               |
| **Variance ($Var(X)$)** | $\displaystyle\frac{2d_2^2(d_1+d_2-2)}{d_1(d_2-2)^2(d_2-4)}$for $d_2 > 4$ |

---

## Relationships to Other Distributions
* **[[Chi-Squared]]:** If $U_1 \sim \chi^2_{d_1}$ and $U_2 \sim \chi^2_{d_2}$ independently, then  
  $(U_1/d_1)/(U_2/d_2) \sim F_{d_1,d_2}$
* **[[Student-t]]:** $t_\nu^2 \sim F_{1,\nu}$

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.f`
* **R:** `df`, `pf`, `qf`, `rf`

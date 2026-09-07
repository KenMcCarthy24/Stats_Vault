![[Gamma_pdf.svg]]
## Overview
* **Type:** Continuous
* **Key Intuition:** Flexible, positive-valued distribution for waiting times, rates, and scale-like uncertainty
* **Example Use Cases:**
    * Waiting time until $k$ events occur in a [[Poisson]] process
    * Conjugate Prior distribution for [[Poisson]] or [[Exponential]] rate parameters
    * Modeling right-skewed, positive data (e.g. rainfall, lifetimes)

---

## Mathematical Definition

### Notation
$X \sim \mathrm{Gamma}(\alpha, \lambda)$

*(Shape–rate parameterization)*

### Probability Density Function (PDF)
> $$f(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\lambda x}, \qquad x \ge 0$$

### Cumulative Distribution Function (CDF)
> $$F(x) = \frac{\gamma(\alpha, \lambda x)}{\Gamma(\alpha)}$$

where $\gamma(\cdot,\cdot)$ is the lower incomplete gamma function.

---

## Parameters & Support
* **Parameters:**
    * $\alpha > 0$: Shape parameter
    * $\lambda > 0$: Rate parameter

* **Support:** $x \in [0,\infty)$

---

## Key Properties

| Property                | Formula                                                                                                                 |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| **Mean ($E[X]$)**       | $\displaystyle \frac{\alpha}{\lambda}$                                                                                    |
| **Median**              | No closed form                                                                                                          |
| **Mode**                | $\displaystyle \frac{\alpha-1}{\lambda}$ (for $\alpha>1$)                                                                 |
| **Variance ($Var(X)$)** | $\displaystyle \frac{\alpha}{\lambda^2}$                                                                                  |
| **Skewness**            | $\displaystyle \frac{2}{\sqrt{\alpha}}$                                                                                 |
| **Kurtosis**            | $\displaystyle 3 + \frac{6}{\alpha}$                                                                                    |
| **Fisher Information**  | $\displaystyle\begin{pmatrix}\psi'(\alpha) & -\frac{1}{\lambda} \\-\frac{1}{\lambda} & \frac{\alpha}{\lambda^2}\end{pmatrix}$ |
| **Jeffreys Prior**      | $\displaystyle \propto \sqrt{\det \mathcal{I}(\alpha,\lambda)}$                                                           |
| **MLE**                 | $\hat{\lambda} = \frac{\alpha}{\bar{X}}$ (given $\alpha$);<br>$\hat{\alpha}$ numeric                                      |

---

## Relationships to Other Distributions
* **[[Exponential]]:** Special case with $\alpha = 1$
* **[[Chi-Squared]]:** Special case with $\alpha = \nu/2$, $\lambda = 1/2$
* **[[Poisson]]:** Waiting time until the $\alpha$-th event in a Poisson process with rate $\lambda = \lambda$
* **Erlang:** Integer-valued shape parameter $\alpha$

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.gamma` *(uses shape–scale; scale = $1/\lambda$)*
* **R:** `dgamma`, `pgamma`, `qgamma`, `rgamma`

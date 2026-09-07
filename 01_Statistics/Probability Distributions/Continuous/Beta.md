![[Beta_pdf.svg]]
## Overview
* **Type:** Continuous
* **Key Intuition:** Flexible distribution on $[0,1]$ for modeling probabilities and proportions
* **Example Use Cases:**
    * Prior distribution for a [[Bernoulli]], [[Geometric]], or [[Binomial]] success probability
    * Modeling proportions or rates bounded between 0 and 1

---

## Mathematical Definition

### Notation
$X \sim \mathrm{Beta}(\alpha, \beta)$

### Probability Density Function (PDF)
> $$f(x) = \frac{1}{B(\alpha,\beta)} x^{\alpha-1}(1-x)^{\beta-1}, \qquad 0 \le x \le 1$$

where
> $$B(\alpha,\beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$$

### Cumulative Distribution Function (CDF)
> $$F(x) = I_x(\alpha,\beta)$$

where $I_x(\alpha,\beta)$ is the regularized incomplete beta function.

---

## Parameters & Support
* **Parameters:**
    * $\alpha > 0$: Shape (pseudo-count of successes)
    * $\beta > 0$: Shape (pseudo-count of failures)

* **Support:** $x \in [0,1]$

---

## Key Properties

| Property                | Formula                                                                                                                                                       |
| :---------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Mean ($E[X]$)**       | $\displaystyle \frac{\alpha}{\alpha+\beta}$                                                                                                                   |
| **Median**              | No closed form (≈ $\frac{\alpha-\tfrac13}{\alpha+\beta-\tfrac23}$ for large $\alpha,\beta$)                                                                   |
| **Mode**                | $\displaystyle \frac{\alpha-1}{\alpha+\beta-2}$ (for $\alpha,\beta>1$)                                                                                        |
| **Variance ($Var(X)$)** | $\displaystyle \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$                                                                                          |
| **Skewness**            | $\displaystyle \frac{2(\beta-\alpha)\sqrt{\alpha+\beta+1}}{(\alpha+\beta+2)\sqrt{\alpha\beta}}$                                                               |
| **Kurtosis**            | $\displaystyle 3 + \frac{6[(\alpha-\beta)^2(\alpha+\beta+1)-\alpha\beta(\alpha+\beta+2)]}{\alpha\beta(\alpha+\beta+2)(\alpha+\beta+3)}$                       |
| **Entropy**             | $\displaystyle \log B(\alpha,\beta) - (\alpha-1)\psi(\alpha) - (\beta-1)\psi(\beta) + (\alpha+\beta-2)\psi(\alpha+\beta)$                                     |
| **Fisher Information**  | $\displaystyle\begin{pmatrix}\psi'(\alpha)-\psi'(\alpha+\beta) & -\psi'(\alpha+\beta) \\-\psi'(\alpha+\beta) & \psi'(\beta)-\psi'(\alpha+\beta)\end{pmatrix}$ |
| **Jeffreys Prior**      | $\displaystyle \propto \sqrt{\det \mathcal{I}(\alpha,\beta)}$                                                                                                 |
| **MLE**                 | No closed form (numerical optimization)                                                                                                                       |

---

## Relationships to Other Distributions
* **[[Continuous Uniform]]:** Special case with $\alpha=\beta=1$ has distribution $U(0, 1)$
* **[[Bernoulli]] / [[Geometric]] / [[Binomial]]:** Conjugate prior for success probability $p$
* **[[Dirichlet]]:** Multivariate generalization of Beta

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.beta`
* **R:** `dbeta`, `pbeta`, `qbeta`, `rbeta`

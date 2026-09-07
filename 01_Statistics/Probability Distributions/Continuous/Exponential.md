![[Exponential_pdf.svg]]
## Overview
* **Type:** Continuous
* **Key Intuition:** Waiting time until the first event in a Poisson process with constant rate $\lambda$. Time to events or time between events. 
* **Example Use Cases:**
    * Time until the next customer arrives
    * Lifetime of a component with constant hazard rate
    * Inter-arrival times in queueing systems

---

## Mathematical Definition

### Notation
$X \sim \text{Exp}(\lambda)$

### Probability Density Function (PDF)
> $$f(x) = \lambda e^{-\lambda x}, \quad x \ge 0$$

### Cumulative Distribution Function (CDF)
> $$F(x) = P(X \le x) = 1 - e^{-\lambda x}$$

---

## Parameters & Support
* **Parameters:**
    * $\lambda$: Rate parameter, $\lambda > 0$

* **Support:** $x \in [0, \infty)$

---

## Key Properties

| Property                | Formula                                           |
| :---------------------- | :------------------------------------------------ |
| **Mean ($E[X]$)**       | $\displaystyle \frac{1}{\lambda}$                 |
| **Median**              | $\displaystyle \frac{\ln 2}{\lambda}$             |
| **Mode**                | $0$                                               |
| **Variance ($Var(X)$)** | $\displaystyle \frac{1}{\lambda^2}$               |
| **Skewness**            | $2$                                               |
| **Kurtosis**            | $9$                                               |
| **Fisher Information**  | $\displaystyle \frac{1}{\lambda^2}$               |
| **Jeffreys Prior**      | $\displaystyle \frac{1}{\lambda}$                 |
| **MLE**                 | $\displaystyle \hat{\lambda} = \frac{1}{\bar{X}}$ |


---

## Relationships to Other Distributions
* **[[Geometric]]:** Discrete analogue (waiting time in Bernoulli trials)
* **[[Gamma]]:**
	* Special case with shape parameter $k = 1$.
	* Bayesian conjugate Prior for $\lambda$.
	* If $X_i \sim \text{Exp}(\lambda)$ then the sample mean $\bar X\sim \Gamma(n, n\lambda)$
* **[[Weibull]]:** Generalization with non-constant hazard rate
* **[[Poisson]]:** Inter-arrival times in a Poisson process are exponential

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.expon` (parameterized by scale $= 1/\lambda$)
* **R:** `dexp`, `pexp`, `qexp`, `rexp`

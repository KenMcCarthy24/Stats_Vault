
---

## Overview
* **Type:** [Discrete / Continuous]
* **Key Intuition:** [e.g., Number of successes in $n$ trials, time between events, etc.]
* **Example Use Cases:**
    * [Example 1]
    * [Example 2]

---

## Mathematical Definition

### Notation
$X \sim \text{Dist}(\theta_1, \theta_2)$

### Probability Mass/Density Function (PMF / PDF)
> $$f(x) = \dots \text{ for } x \in \text{Support}$$

### Cumulative Distribution Function (CDF)
> $$F(x) = P(X \le x) = \dots$$

---

## Parameters & Support
* **Parameters:**
    * $\theta_1$: [Description, e.g., probability of success $p$]
    * $\theta_2$: [Description, e.g., number of trials $n$]
* **Support:** $x \in \{ \dots \}$ or $[ \dots ]$

---

## Key Properties

| Property                | Formula   |
| :---------------------- | :-------- |
| **Mean ($E[X]$)**       | $$\dots$$ |
| **Median**              | $$\dots$$ |
| **Mode**                | $$\dots$$ |
| **Variance ($Var(X)$)** | $$\dots$$ |
| **Skewness**            | $$\dots$$ |
| **Kurtosis**            | $$\dots$$ |
| **Fisher Information**  | $$\dots$$ |
| **Jefferys Prior**      | $$\dots$$ |
| **MLE**                 | $$\dots$$ |


---

## Relationships to Other Distributions
* **[Distribution A]:** [e.g., If $n=1$, Binomial becomes Bernoulli.]
* **[Distribution B]:** [e.g., Normal is the limit of Poisson as $\lambda \to \infty$.]

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.[dist_name]`
* **R:** `d[name]`, `p[name]`, `q[name]`, `r[name]`

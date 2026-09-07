![[Discrete_Uniform_pmf.svg]]
## Overview
* **Type:** Discrete
* **Key Intuition:** All outcomes in a finite set are equally likely
* **Example Use Cases:**
    * Rolling a fair die
    * Selecting an integer uniformly at random from a fixed range
    * Randomized assignment with equal probability across options

---

## Mathematical Definition

### Notation
$X \sim Unif(a, b)$

where $a, b \in \mathbb{Z}$ and $a \le b$.

### Probability Mass (PMF)
> $$P(X = x) = \frac{1}{b-a+1}, \quad x = a, a+1, \dots, b$$

### Cumulative Distribution Function (CDF)
> $$F(x) = P(X \le x) =
\begin{cases}
0, & x < a \\
\displaystyle \frac{\lfloor x \rfloor - a + 1}{b-a+1}, & a \le x \le b \\
1, & x \ge b
\end{cases}$$

---

## Parameters & Support
* **Parameters:**
    * $a$: Lower bound (integer)
    * $b$: Upper bound (integer)

* **Support:** $x \in \{a, a+1, \dots, b\}$

---

## Key Properties

| Property                | Formula                                                             |
| :---------------------- | :------------------------------------------------------------------ |
| **Mean ($E[X]$)**       | $\displaystyle \frac{a+b}{2}$                                       |
| **Median**              | $\displaystyle \frac{a+b}{2}$                                       |
| **Mode**                | Not unique (all values equally likely)                              |
| **Variance ($Var(X)$)** | $\displaystyle \frac{(b-a+1)^2 - 1}{12}$                            |
| **Skewness**            | $0$                                                                 |
| **Kurtosis**            | $\displaystyle -\frac{6}{5}\cdot\frac{(b-a)^2+2(b-a)}{(b-a+1)^2-1}$ |
| **Fisher Information**  | $0$ (no unknown continuous parameter)                               |
| **Jeffreys Prior**      | Not applicable                                                      |
| **MLE**                 | $\hat{a} = \min(X),\ \hat{b} = \max (X)$                            |

---

## Relationships to Other Distributions
* **[[Continuous Uniform]]:** Continuous analogue on an interval
* **[[Categorical]]:** Special case with equal category probabilities

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.randint`
* **R:** `dunif`, `punif`, `qunif`, `runif` (with integer support)

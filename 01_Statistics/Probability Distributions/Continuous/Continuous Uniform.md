![[Continuous_Uniform_pdf.svg]]
## Overview
* **Type:** Continuous
* **Key Intuition:** All values in a bounded interval are equally likely
* **Example Use Cases:**
    * Random number generation on a fixed interval
    * Modeling complete ignorance over a bounded range

---

## Mathematical Definition

### Notation
$X \sim Unif(a, b)$

where $a < b$ and $a, b \in \mathbb{R}$.

### Probability Density (PDF)
> $$f(x) = \frac{1}{b-a}, \quad a \le x \le b$$

### Cumulative Distribution Function (CDF)
> $$F(x) = P(X \le x) =
\begin{cases}
0, & x < a \\
\displaystyle \frac{x-a}{b-a}, & a \le x \le b \\
1, & x > b
\end{cases}$$

---

## Parameters & Support
* **Parameters:**
    * $a$: Lower bound
    * $b$: Upper bound

* **Support:** $x \in [a, b]$

---

## Key Properties

| Property                | Formula                                 |
| :---------------------- | :-------------------------------------- |
| **Mean ($E[X]$)**       | $\displaystyle \frac{a+b}{2}$           |
| **Median**              | $\displaystyle \frac{a+b}{2}$           |
| **Mode**                | Not unique (all values equally likely)  |
| **Variance ($Var(X)$)** | $\displaystyle \frac{(b-a)^2}{12}$      |
| **Skewness**            | $0$                                     |
| **Execess Kurtosis**    | $\displaystyle -\frac{6}{5}$            |
| **Fisher Information**  | $0$ (for known bounds)                  |
| **Jeffreys Prior**      | Not well-defined for $(a,b)$            |
| **MLE**                 | $\hat{a} = \min(X),\ \hat{b} = \max(X)$ |

---

## Relationships to Other Distributions
* **[[Discrete Uniform]]:** Discrete analogue on a finite set

---

## Notes & Implementation (Python/R)
* **Scipy:** `scipy.stats.uniform`
* **R:** `dunif`, `punif`, `qunif`, `runif`

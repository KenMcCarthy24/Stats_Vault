A probability distribution is a mathematical function that describes the probability of all possible outcomes of a [[Random Variable]].

The **Support** of a random variable $X$ is the set of all real values that $X$ can take with nonzero probability.

### General Requirements
In order to be a valid probability distribution a function must:
* Be non-negative over its support (so negative probabilities are impossible)
* Have a total probability (by sum or by integral) of 1 (meaning that something has to happen)

Probability distributions are often parametrized by a set of one or more parameters $\{\theta_1, \theta_2, \dots\}$, that define the unique shape of the distribution.

---

## Types of Distributions

### [[Discrete Probability Distributions]]
Relates to random variables that take values in a countable set (e.g., $\{0,1,2,\dots\}$).
* Defined by the **Probability Mass Function (PMF)**.
* Expectation and variance are calculated via **summation**.

### [[Continuous Probability Distributions]]
Relates to random variables with values in an uncountable set (e.g., intervals on the real line $\mathbb{R}$).
* Defined by the **Probability Density Function (PDF)**.
* Expectation and variance are calculated via **integration**.

### [[Joint and Multivariate Distributions]]
Relates to scenarios involving multiple variables ($X, Y$) or random vectors ($\mathbf{X}$) in multidimensional space ($\mathbb{R}^n$).
* Covers **Joint PDFs** and Double Integrals.
* Describes relationships between variables using **Covariance** and **Covariance Matrices**. A probability distribution is a mathematical function that describes the probability of all possible outcomes of a Random Variable.
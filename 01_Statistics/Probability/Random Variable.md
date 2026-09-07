A **random variable** is a function that assigns a real number to each outcome of a random experiment.

$$
X:\Omega \rightarrow \mathbb{R}
$$

Where:
- $\Omega$ is the **sample space** (set of all outcomes)
- $\omega \in \Omega$ is a particular outcome
- $X(\omega)$ is the value of the random variable for that outcome

Types:
- **Discrete:** $X$ takes values in a countable set (e.g., $\{0,1,2,\dots\}$)
	- [[Bernoulli]], [[Binomial]], [[Categorical]], [[Discrete Uniform]], [[Geometric]], [[Hypergeometric]], [[Negative Binomial]], [[Poisson]]
- **Continuous:** $X$ takes values in an interval (e.g., $[0,1]$)
	- [[Beta]], [[Chi-Squared]], [[Continuous Uniform]], [[Exponential]], [[F-distribution]], [[Gamma]], [[Lognormal]], [[Normal]], [[Student-t]], [[Weibull]]
- **Multivariate:** $X = (X_1,\dots,X_n)$ takes values in $\mathbb{R}^n$, representing multiple random variables jointly. Can be discrete or continuous.
	- [[Multivariate Normal]], [[Dirichlet]]

(lists not comprehensive)

Every random variable follows a [[Probability Distribution]] describing the probability of each of its possible values.

Examples:
- Coin toss: $X=1$ for heads, $X=0$ for tails ([[Bernoulli]])
- Dice roll: $X \in \{1,\dots,6\}$ ([[Discrete Uniform]])
- Pick a real number in $[0,1]$: $X \in [0,1]$ ([[Continuous Uniform]])

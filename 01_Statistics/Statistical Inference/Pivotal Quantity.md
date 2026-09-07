Let $X = (X_1, X_2, \dots, X_n)$ be a random sample from a distribution involving an unknown parameter $\theta$. A random variable $Q$ is a pivotal quantity if:

1. It is a function of both the data $X$ and the unknown parameter $\theta$.
   $$Q = g(X, \theta)$$
2. Its probability distribution **does not depend** on $\theta$ (or any other unknown parameters).
## Common Examples

| Parameter           | Assumptions        | Pivotal Quantity ($Q$)                    | Distribution of $Q$          |
| :------------------ | :----------------- | :---------------------------------------- | :--------------------------- |
| Mean $\mu$          | $\sigma^2$ known   | $\frac{\bar{X} - \mu}{\sigma / \sqrt{n}}$ | $\mathcal{N}(0, 1)$          |
| Mean $\mu$          | $\sigma^2$ unknown | $\frac{\bar{X} - \mu}{s / \sqrt{n}}$      | $t_{n-1}$ (Student's t)      |
| Variance $\sigma^2$ | Normal pop.        | $\frac{(n-1)S^2}{\sigma^2}$               | $\chi^2_{n-1}$ (Chi-squared) |

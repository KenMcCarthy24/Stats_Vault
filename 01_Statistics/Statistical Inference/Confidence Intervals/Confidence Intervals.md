A confidence interval for a population parameter $\theta$ is a range of values, computed from sample data $X$, that is intended to contain the true value of $\theta$ with a specified level of confidence. It is constructed using a **significance level** $\alpha$, which represents the probability that the interval procedure fails to capture the true parameter. Equivalently, the interval is often described by its **confidence level** $1-\alpha$ (or $100(1-\alpha)$ as a a percent), which is the long-run proportion of such intervals that would contain $\theta$.

For example, $\alpha = 0.05$ corresponds to a 95% confidence interval based on a sample $X$. This means that if samples were repeatedly drawn in the same way and a 95% confidence interval was constructed from each one, about 95% of those intervals would contain the true population parameter $\theta$, while about 5% would not.

Common Pitfall: This does **NOT** mean that a single 95% confidence interval is 95% likely to contain $\theta$.

Specific Examples: [[CI For Mean]], [[CI For Difference In Means]], [[CI For Proportions]], [[CI For Difference In Proportions]], [[CI For Variance]], [[CI For Variance Ratio]]

# General Procedure:
Below is a general procedure (called the **Pivotal Quantity Method**) used to find a $100(1-\alpha)\%$ confidence interval for an arbitrary parameter $\theta$ based on data $X_1...X_n$:
1. Choose a [[Pivotal Quantity]] $Q$ that is a function of the unknown parameter $\theta$ and the sample data $X$. Its distribution $D$ must **not** depend on $\theta$.
   $$Q = g(X, \theta) \sim D$$
2. Choose critical values $d_1, d_2$ from the distribution $D$ such that they bound the probability $1-\alpha$. (Note: Usually so there is $\alpha/2$ probability in each tail)
   $$P(d_1 \leq Q \leq d_2)=1-\alpha$$
3. Set up the inequality based on the probability statement
   $$d_1 \leq g(X, \theta) \leq d_2$$
4. Get the confidence interval by algebraically manipulating the inequality to isolate $\theta$ in the center
   $$CI_{low} \leq \theta \leq CI_{high}$$

$d_1$ can be set to the minimum possible parameter value in order to make $CI_{high}$ an upper bound for $\theta$

$d_2$ can be set to the maximum possible parameter value in order to make $CI_{low}$ a lower bound for $\theta$

---

> [!example]- Example: [[Exponential]] Confidence Interval
> $X_1...X_n \sim \text{Exp}(\lambda)$. What is a $100(1-\alpha)\%$ confidence interval for $\lambda$.
> 
> It is known that in the case $\bar X \sim \Gamma(n, n\lambda)$. However this is not a pivotal quantity as the distribution depends on $\lambda$. To make it a pivotal quantity take advantage of the property of [[Gamma]] distributions that for some constant c.
> $$c\Gamma(a, b) = \Gamma(a, \frac{b}{c})$$
> So a pivotal quantity $Q$ can be obtained by multiplying the sample mean $\bar X$ by $\lambda$. 
> $$Q = \lambda \bar X \sim \Gamma(n, n)$$
> Now choose the critical values as $\Gamma_{\frac{\alpha}{2}}$ and $\Gamma_{1-\frac{\alpha}{2}}$ as the values along the $\Gamma(n, n)$ distribution that bound $\frac{\alpha}{2}$ and $1-\frac{\alpha}{2}$ probability area to the left respectively. $1-\alpha$ probability between them.
> 
> Set up the inequality.
> $$\Gamma_{\frac{\alpha}{2}} \leq \lambda \bar X \leq \Gamma_{1-\frac{\alpha}{2}}$$
> And manipulate so that $\lambda$ is isolated in the center to get the confidence interval:
> $$\frac{\Gamma_{\frac{\alpha}{2}}}{\bar X} \leq  \lambda \leq \frac{\Gamma_{1-\frac{\alpha}{2}}}{\bar X}$$
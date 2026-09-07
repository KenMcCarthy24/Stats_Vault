Given a [[Hypothesis Test]]
$$H_0: \theta \in \Theta_0$$
$$H_1:\theta \in \Theta_1$$
where $\Theta$ is the parameter space — the set of all possible values of the parameter $\theta$ and $\Theta_0$  and $\Theta_1$ are disjoint subsets of $\Theta$. The **Power Function** is the function that describes how the [[Power of a Test]] changes as the true population parameter $\theta$ changes within the parameter space $\Theta$. Denoted as:
$$\gamma(\theta) = P(\text{Reject } H_0;\theta)$$
As the true parameter $\theta$ moves further away from the null hypothesis space $\Theta_0$, the power function increases; meaning it gets more likely to accurately reject the null hypothesis. On the other hand, the power function is low when $\theta$ is close to $\Theta_0$.

As the sample size $n \rightarrow \infty$, $\gamma(\theta) \rightarrow 1$ for $\theta \in \Theta_1$. Visually, the curve becomes steeper, approaching a step function at the boundary of $\Theta_0$.

# Relationship to Errors

The probability of committing a [[Errors in Hypothesis Testing|Type I Error]] $\alpha$ — or the probability of rejecting $H_0$ when it is true — is the maximum value of the power function when $\theta \in \Theta_0$. If the null hypothesis only covers a single point $\theta_0$ (e.g. $\theta=2$), then $\alpha$ is just the power function evaluated at that point $\gamma(\theta_0)$.
$$\alpha = \max_{\theta \in \Theta_0}\gamma(\theta)$$
The probability of committing a [[Errors in Hypothesis Testing#Type II Error ($ beta$) False Negative|Type II Error]] — or the probability of failing to reject $H_0$ when it is false — for a given $\theta$ can be described by the function. 
$$\beta(\theta) = 1 - \gamma(\theta)$$
The worst case probability of a type II error can be found by maximizing this function over $\Theta_1$.
$$\beta_{max} = \max_{\theta \in \Theta_1}\beta(\theta)$$
An ideal test will have:
* $\gamma(\theta)$ close to 0 when $\theta \in \Theta_0$
* $\gamma(\theta)$ close to 1 when $\theta \in \Theta_1$

---

> [!example]-
> 
> Given The Hypothesis Test:
> $$H_0: \mu=0$$
> $$H_1: \mu > 0$$
> Imagine performing an upper-tailed [[Hypothesis Test For Mean#Z-Test For Mean|Z-test for the Mean]] with:
> 
> * Level of significance $\alpha=0.05$
> * Sample size: $n=36$
> * Known Variance: $\sigma^2=10$
> 
> Derive the power function $\gamma(\mu)$ and plot it from $\mu=-1$ to $\mu=2$
> 
> ---
> Start by calculating the critical value $c$ on the null hypothesis curve $N(0, 10)$. This is the area that cuts off $\alpha$ to the right. Know that on a standard normal $N(0,1)$, that the critical value is:
> $$z_{0.05} = \frac{c-\mu_0}{\sigma/\sqrt n}$$
> so:
> $$c = \mu_0 + \frac{z_{0.05} \sigma}{\sqrt n} = 0 + \frac{(1.645)(\sqrt{10})}{6}=0.867$$
> Now the power function is the area to the right of the alternate hypothesis curve $N(\mu, 10)$ for different values of $\mu$. This is best represented using the Standard Normal CDF, $\Phi(z)$:
> $$
> \begin{split}
> \gamma(\mu) &= P(X > c | \mu) \\
> &= P\left(Z > \frac{c - \mu}{\sigma/\sqrt{n}}\right) \\
> &= 1 - \Phi\left( \frac{0.867 - \mu}{0.527} \right)
> \end{split}
> $$
> Plot:
> ![[power_example_plot.svg]]
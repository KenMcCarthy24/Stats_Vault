The bias of an [[Estimators|Estimator]] $\hat{\theta}$ is defined as the difference between the expectation value of the estimator and the true parameter $\theta$.
$$\text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta$$

A parameter is said to be **Unbiased** if it has a bias of zero, meaning $E[\hat{\theta}] = \theta$. It is generally preferable for an estimator to be unbiased, although a biased estimator may still be used if, for example:
* No unbiased estimator exists
* Unbiased estimator is computationally harder to compute
* A biased estimator leads to a lower variance (see [[Bias-Variance Tradeoff]])

> [!example]- Example: Bias of [[Sample Mean]] $\bar{X}$
> 
> Let $X = [x_1, x_2, \dots, x_n]$ be an iid random sample from some distribution with true mean $\mu$. What is the bias of the sample mean $\bar{X}$?
> 
> Since each $x_i$ is drawn from a population with mean $\mu$, then $E[x_i] = \mu$ for all $x_i$
> 
> $$E[\bar{X}] = E[\frac{1}{n}\sum_{i=1}^n x_i] = \frac{1}{n}\sum_{i=1}^nE[x_i] = \frac{1}{n}\sum_{i=1}^n \mu = \frac{1}{n} n\mu = \mu$$
> 
> So $E[\bar{X}] = \mu$, meaning the bias is 0 and that $\bar{X}$ is an unbiased estimator for $\mu$ for any arbitrary distribution.

> [!example]- Example: Bias of [[Sample Variance and Standard Deviation|Sample Variance]] $\hat{\sigma}^2$
> 
> Let $X = [x_1, x_2, \dots, x_n]$ be an iid random sample from some distribution with true mean $\mu$. What is the bias of the sample variance $\hat{\sigma}^2$?
> 
> $$E[\hat{\sigma}^2] = E[\frac{1}{n}\sum_{i=1}^n(x_i - \bar{X})^2] = \dots = \frac{n-1}{n}\sigma^2$$
> 
> So the bias is $\text{Bias}(\hat{\sigma}^2) = E[\hat{\sigma}^2] - \sigma^2 = \frac{-\sigma^2}{n}$. This means that this estimator tends to underestimate the true variance.
> 
> An unbiased estimator for variance is given by $\displaystyle S^2 = \frac{n}{n-1}\hat{\sigma}^2$, where
> $$E[S^2] = E[\frac{1}{n-1}\sum_{i=1}^n(x_i - \bar{X})^2] = \dots = \sigma^2$$
> 
> so the bias is 0. This is called **Bessel's Correction**
> 
> $\hat{\sigma}^2$ is often called the **Biased Sample Variance** while $S^2$ is the **Unbiased Sample Variance**. 


The calculation of a $100(1-\alpha)\%$ [[Confidence Intervals|confidence interval]] for the variance, based on independent [[Normal]] samples $X_1...X_n \sim N(\mu, \sigma^2)$, is done in one of three ways, depending on the desired bounds of the confidence interval. A confidence interval for the standard deviation $\sigma$ is simply the square root of the confidence interval for the variance. 

All depend on the fact that the following [[Pivotal Quantity]] follows a [[Chi-Squared]] distribution with $n-1$ [[Degrees of Freedom]]
$$\frac{(n-1)s^2}{\sigma^2} \sim \chi^2_{n-1}$$
Where $s^2$ is the [[Sample Variance and Standard Deviation|unbiased sample variance]].

Note: this is only true for normally distributed data and will not be valid for data from other distributions.

---
# Method 1: The Two-Sided Interval
This is the most common method, used to estimate the variance with precision on both sides.

This confidence interval is defined by the critical values $\chi^2_{1-\alpha/2, n-1}$ (small value) and $\chi^2_{\alpha/2, n-1}$ (large value), which capture between them the central $(1-\alpha)$ area of the chi squared distribution. This is expressed by the inequality:
$$\chi^2_{1-\frac{\alpha}{2}, n-1} < \frac{(n-1)s^2}{\sigma^2} < \chi^2_{\frac{\alpha}{2}, n-1}$$

Solving the inequality for $\sigma^2$  gives the interval:
$$\frac{(n-1)s^2}{\chi^2_{\alpha/2, n-1}} \le \sigma^2 \le \frac{(n-1)s^2}{\chi^2_{1-\alpha/2, n-1}}$$

---
# Method 2: One Sided Upper Bound Interval
This method is used to determine an upper bound on the variance, setting the lower bound to zero.

This confidence interval is defined by the critical value $\chi^2_{1-\alpha, n-1}$, which captures to the right of it the upper $(1-\alpha)$ area of the chi squared distribution. This is expressed by the inequality:
$$\chi^2_{1-\alpha, n-1} < \frac{(n-1)s^2}{\sigma^2} < \infty$$

Solving the inequality for $\sigma^2$ gives the interval:
$$0 \le \sigma^2 \le \frac{(n-1)s^2}{\chi^2_{1-\alpha, n-1}}$$

---
# Method 3: One Sided Lower Bound Interval
This method is used to determine a lower bound on the variance, setting the upper bound to infinity.

This confidence interval is defined by the critical value $\chi^2_{\alpha, n-1}$ (a large value), which captures to the left of it the lower $(1-\alpha)$ area of the chi squared distribution. This is expressed by the inequality:
$$0 < \frac{(n-1)s^2}{\sigma^2} < \chi^2_{\alpha, n-1}$$

Solving the inequality for $\sigma^2$ gives the interval:
$$\frac{(n-1)s^2}{\chi^2_{\alpha, n-1}} \le \sigma^2 < \infty$$
---

> [!example]-
> A manufacturing plant must ensure that the true standard deviation of rod diameters does not exceed 5 mm. Based on historical data, rod diameters are assumed to follow a Normal distribution.
> 
> A sample of 100 rods is collected, yielding a sample standard deviation of $s=4.1$ mm. Calculate a 95% One-Sided Upper Confidence Interval to verify the process meets specifications.
> 
> Using Method 2 (One-Sided Upper Bound), we identify the critical value for $\alpha=0.05$ and $df=n-1=99$:
> $$\chi^2_{1-\alpha, n-1} = \chi^2_{0.95, 99} = 77.046$$
> 
> The 95% confidence interval for the variance is calculated as:
> $$CI
> =\left[0, \frac{(n-1)s^2}{\chi^2_{1-\alpha, n-1}}\right]
> =\left[0, \frac{(99)(4.1)^2}{77.046}\right]$$
> Result: $[0, 21.6]$
> 
> The upper bound for the standard deviation is $\sqrt{21.6}=4.64$ mm. Since this upper bound (4.64 mm) is less than the maximum tolerance (5 mm), there is statistical evidence at the 95% confidence level that the process variation is within limits.



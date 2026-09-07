The calculation of a $100(1-\alpha)\%$ [[Confidence Intervals|confidence interval]] for the ratio of two variances $\displaystyle \frac{\sigma_2^2}{\sigma_1^2}$, based on  two independent [[Normal]] samples $X_{1,1}, \dots, X_{1,n_1} \sim N(\mu_1,\sigma_1^2)$ and $X_{2,1}, \dots, X_{2,n_2} \sim N(\mu_2, \sigma_2^2)$ is done as follows.

---

For each variance, the following [[Pivotal Quantity]] follows a [[Chi-Squared]] distribution with $n-1$ [[Degrees of Freedom]]
$$\frac{(n-1)s^2}{\sigma^2} \sim \chi^2(n-1)$$
Where $s^2$ is the [[Sample Variance and Standard Deviation|unbiased sample variance]].

Define a new pivotal quantity $F$ as the ratio of these quantities for each variance divided by their degrees of freedom. Since $F$ is the ratio of two Chi-Squared random variables divided by their degrees of freedom, $F$ will follow the [[F-distribution]].
$$\frac{\left[\frac{(n_1-1)s_1^2}{(n_1-1)\sigma_1^2}\right]}{\left[\frac{(n_2-1)s_2^2}{(n_2-1)\sigma_2^2}\right]} = \frac{\sigma_2^2s_1^2}{\sigma_1^2s_2^2} \sim F(n_1-1, n_2-1)$$

This confidence interval is defined by the critical values $F_{1-\frac{\alpha}{2}, n_1-1, n_2-1}$  and $F_{\frac{\alpha}{2}, n_1-1, n_2-1}$, which capture between them the central $(1-\alpha)$ area of the **F distribution**. This is expressed by the inequality:
$$F_{1-\frac{\alpha}{2}, n_1-1, n_2-1} < \frac{\sigma_2^2s_1^2}{\sigma_1^2s_2^2} < F_{\frac{\alpha}{2}, n_1-1, n_2-1}$$

Solving the inequality for the variance ratio $\frac{\sigma_2^2}{\sigma_1^2}$ gives the interval:
$$\left(\frac{s_2^2}{s_1^2}\right)F_{1-\frac{\alpha}{2}, n_1-1, n_2-1} < \frac{\sigma_2^2}{\sigma_1^2} < \left(\frac{s_2^2}{s_1^2}\right)F_{\frac{\alpha}{2}, n_1-1, n_2-1}$$

A confidence interval for the standard deviation ratio $\frac{\sigma_2}{\sigma_1}$ is simply the square root of the variance ratio confidence interval.

---

> [!example]-
> Students from two classes took the same exam.
> * Class 1 had $n_1=18$ students with a sample variance $s_1^2=15.3$
> * Class 2 had $n_2=15$ students with a sample variance $s_2^2=19.7$
> 
> Calculate a 99% confidence interval for the variance ratio $\frac{\sigma_2^2}{\sigma_1^2}$. 
> 
> Here $n_1-1=17$ and $n_2-1=14$, and:
> * $F_{0.995, 17, 14} \approx 0.2601$
> * $F_{0.005, 17, 14} \approx 4.1592$
> 
> The 99% confidence interval for the variance is calculated as:
> $$\left[\left(\frac{s_2^2}{s_1^2}\right)F_{1-\frac{\alpha}{2}, n_1-1, n_2-1}, \left(\frac{s_2^2}{s_1^2}\right)F_{\frac{\alpha}{2}, n_1-1, n_2-1}\right]$$
> 
> $$ = \left[\left(\frac{19.7}{15.3}\right)0.2601, \left(\frac{19.7}{15.3}\right)4.1592\right]$$
> 
> Result: $[0.3349, 5.3553]$
> 
> Note this interval does include 1 so it is plausible at the 99% confidence level that the variances are equal.

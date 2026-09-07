Given a random sample $\vec X = X_1 ... X_n$ with some unknown population parameter $\theta$ that were sampled from some known pdf $f(x;\theta)$, the Generalized Likelihood Ratio test is a method of performing a [[Hypothesis Test]] for when other methods don't exist or are impractical. Given the full parameter space $\Theta$ and the disjoint subspaces $\Theta_0$ and $\Theta_1 = \Theta \setminus \Theta_0$, the test is structured as:
$$H_0: \theta \in \Theta_0$$
$$H_1: \theta \in \Theta_1$$

The Likelihood ratio $\lambda_{LR}$ is given by:
$$\lambda_{LR} = \frac{L(\vec X;\hat \theta_0)}{L(\vec X; \hat \theta)}$$
Where:
* $L(\vec X; \theta)$ is the likelihood function
	* $\displaystyle L(\vec X; \theta) = \prod_{i=1}^n f(x_i;\theta)$
* $\hat \theta$ is the [[Maximum Likelihood Estimation|Maximum Likelihood Estimator]] of $\theta$.
* $\hat \theta_0$ is the restricted MLE, or the MLE if the null hypothesis $H_0$ is assumed true.

In the general case, the exact sampling distribution of $\lambda_{LR}$ is unknown, making it impossible to calculate critical values or p-values for hypothesis testing. However, at large sample sizes, an approximate distribution can be found.

# Wilks' Theorem
Wilks' Theorem states that at a sufficiently large sample size (Rule of Thumb $n > 50$), the sampling distribution of the test statistic approaches a [[Chi-Squared]] distribution.

Because the restricted maximum likelihood $L(\hat \theta_0)$ cannot exceed the unrestricted global maximum likelihood $L(\hat \theta)$, the ratio is always bounded:
$$0 \le \lambda_{LR} \le 1$$
Consequently, the natural log $\ln(\lambda_{LR})$ is always negative (or zero). Multiplying by $-2$ ensures the test statistic is positive, which is required for a Chi-Squared distribution.

$$\chi^2 = -2\ln(\lambda_{LR}) \sim \chi^2_{df}$$

Degrees of Freedom ($df$):
The degrees of freedom are calculated as the difference in dimensionality between the full parameter space and the restricted parameter space.

$$df = \text{dim}(\Theta) - \text{dim}(\Theta_0)$$

* **$\text{dim}(\Theta)$:** The number of free parameters in the full, unrestricted model.
* **$\text{dim}(\Theta_0)$:** The number of free parameters remaining after assuming $H_0$ is true.

*Practical Rule:* $df$ is simply equal to the **number of independent parameters fixed** by the null hypothesis $H_0$.

> [!Warning] 
> Wilks' Theorem does not hold if the parameter $\theta$ defines the bounds of the pdf support (the range where probability > 0), such as in the [[Continuous Uniform]] distribution.

---

> [!example]- Example 1
> An engineer is testing the lifespan of a new specific type of lightbulb. They assume that the bulb lifespans follow an [[Exponential]] distribution with an unknown rate parameter $\lambda$.
> 
> A random sample of **$n = 100$** bulbs is run to failure. The calculated sample mean of their lifespans is **$\bar{X} = 1.8$ years**.
> 
> The historic rate parameter for this type of bulb is $\lambda = 0.5$ (corresponding to a mean life of 2 years). Perform a Generalized Likelihood Ratio Test at $\alpha = 0.05$ to determine if the new bulbs deviate from this standard.
> 
> Hypotheses:
> $$H_0: \lambda = 0.5$$
> $$H_1: \lambda \neq 0.5$$
> The MLE for $\lambda$ is:
> $$\hat \lambda = \frac{1}{\bar X} = \frac{1}{1.8} = \frac{5}{9}$$
> This is a simple hypothesis so the restrained MLE is just just:
> $$\hat \lambda_0 = \lambda_0 = 0.5$$
> 
> The Likelihood Ratio is:
> $$\lambda_{LR} = \frac{L(\vec X;\hat \theta_0)}{L(\vec X; \hat \theta)} = \frac{\displaystyle \prod_{i=1}^n\hat\lambda_0e^{-\hat\lambda_0x_i}}{\displaystyle \prod_{i=1}^n\hat\lambda e^{-\hat\lambda x_i}} = \frac{\hat\lambda_0^ne^{-n\hat\lambda_0\bar X}}{\hat\lambda^n e^{-n\hat\lambda\bar{X}}}$$
> 
> The sample size of $n=100$ is large enough for Wilks' Theorem to be used to approximate the test statistic sampling distribution as a Chi-Squared. $H_0$ fixes one parameter so $df = 1$.
> 
> The test statistic is:
> $$
> \begin{split}
> \chi^2 = -2\ln(\lambda_{LR}) &= -2\ln(\frac{\hat\lambda_0^ne^{-n\hat\lambda_0\bar X}}{\hat\lambda^n e^{-n\hat\lambda\bar{X}}}) \\
> &=-2\left[n\ln(\hat\lambda_0) -n\hat\lambda_0\bar X - n\ln(\hat\lambda) + n\hat\lambda\bar X\right] \\
> &= -2n\left[\ln(\frac{\hat\lambda_0}{\hat\lambda}) + \bar X(\hat\lambda - \hat\lambda_0)\right] \\
> &= 1.072
> \end{split}
> $$
> 
> Using a Chi-Squared Distribution with 1 degrees of freedom $\chi^2_{1}$, this leads to a p-value of:
> $$p = P(\chi^2>1.072) = 0.3004$$
> $p > \alpha$ so the null hypothesis cannot be rejected, meaning there is not significant evidence that the lifespans of the new bulbs deviate from the previous standard.
![[glrt_example_1.svg]]

> [!example]- Example 2
> A pharmaceutical company produces tablets that must adhere to strict quality control standards for both weight and consistency. They assume the tablet weights follow a [[Normal]] Distribution $N(\mu, \sigma^2)$.
> 
> A random sample of **$n = 50$** tablets is weighed. The calculated sample mean is **$\bar{X} = 10.2$ mg** and the sample variance is **$s^2 = 1.5$ mg²**.
> 
> The required standard for these tablets is a mean weight of $\mu = 10$ mg and a variance of $\sigma^2 = 1$. Perform a Generalized Likelihood Ratio Test at $\alpha = 0.05$ to determine if the batch meets the standard.
> 
> Hypotheses:
> $$H_0: \mu = 10, \sigma^2 = 1$$
> $$H_1: \mu \neq 10, \sigma^2 \neq 1$$
> 
> The unrestricted MLEs for a Normal distribution are the sample mean and the sample variance:
> $$\hat \mu = \bar{X} = 10.2$$
> $$\hat \sigma^2 = s^2 = 1.5$$
> 
> The null hypothesis fixes both parameters, so the restricted MLEs are:
> $$\hat \mu_0 = 10$$
> $$\hat \sigma^2_0 = 1$$
> 
> The Likelihood function for the Normal distribution is:
> $$L(\mu, \sigma^2) = (2\pi\sigma^2)^{-n/2} \exp\left(-\frac{1}{2\sigma^2}\sum_{i=1}^n(x_i - \mu)^2\right)$$
> 
> Substituting the MLEs into the ratio $\lambda_{LR} = \frac{L(\hat \mu_0, \hat \sigma^2_0)}{L(\hat \mu, \hat \sigma^2)}$ and simplifying the algebra yields the test statistic formula:
> 
> $$
> \chi^2 = -2\ln(\lambda_{LR}) = n \left[ \frac{S^2}{\hat\sigma^2_0} - 1 - \ln\left(\frac{S^2}{\hat\sigma^2_0}\right) + \frac{(\bar{X}-\hat\mu_0)^2}{\hat\sigma^2_0} \right] = 6.725
> $$
> 
> The sample size of $n=50$ is large enough for Wilks' Theorem to be used to approximate the test statistic sampling distribution as a Chi-Squared. $H_0$ fixes two parameters ($\mu$ and $\sigma^2$) so $df = 2$.
> 
> Using a Chi-Squared Distribution with 2 degrees of freedom $\chi_2^2$, this leads to a p-value of:
> $$p = P(\chi^2>6.725) = 0.035$$
> $p < \alpha$ so the null hypothesis can be rejected, meaning there is significant evidence that the tablets deviate from the required standards (either in mean weight, consistency, or both).![[glrt_example_2.svg]]
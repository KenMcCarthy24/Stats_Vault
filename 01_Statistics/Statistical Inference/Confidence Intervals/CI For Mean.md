
The calculation of a $100(1-\alpha)\%$ [[Confidence Intervals|confidence interval]] for the population mean $\mu$, based on a sample $X_1, \dots, X_n$, typically follows one of two methods. The choice depends on the sample size $n$ and whether the population variance $\sigma^2$ is known or unknown.

---

# Z-Interval
This method is used when the population variance $\sigma^2$ is known or when the sample size is large ($n \geq 30$). This approach can be used with data that follows any [[Probability Distribution]] so long as the sample size is large. 

According to the [[Central Limit Theorem]], the [[Pivotal Quantity]] $Z$ follows a standard normal distribution:
$$Z = \frac{\bar{X}-\mu}{\sigma/\sqrt{n}} \sim N(0, 1)$$
where $\bar{X}$ is the [[Sample Mean]] and the quantity $\frac{\sigma}{\sqrt n}$ is the [[Standard Error]].

The confidence interval is defined by the critical values $\pm z_{\alpha/2}$, which capture between them the central $(1-\alpha)$ area of the standard normal curve. This is expressed by the inequality:
$$-z_{\alpha/2} \leq \frac{\bar{X}-\mu}{\sigma/\sqrt{n}} \leq z_{\alpha/2}$$

Rearranging the inequality to isolate $\mu$ gives the formula for the confidence interval:
$$CI = \bar{X} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$$

If the sample size is large ($n \geq 30$) but the population variance is unknown, the population standard deviation $\sigma$ is replaced by the [[Sample Variance and Standard Deviation#Unbiased Sample Variance|unbiased sample standard deviation]] $s$:
$$CI = \bar{X} \pm z_{\alpha/2} \frac{s}{\sqrt{n}}$$
---
# T-Interval

This method is used when the population variance $\sigma^2$ is unknown and the sample size is small ($n < 30$). This approach assumes that the underlying population is approximately [[Normal|normally]] distributed.

Instead of the standard normal distribution, the **[[Student-t|Student’s t-distribution]]** is used. The [[Pivotal Quantity]] $T$ is defined as:

$$T = \frac{\bar{X}-\mu}{s/\sqrt{n}} \sim t_{n-1}$$

Where $n-1$ represents the [[Degrees of Freedom]] ($df$). The t-distribution is similar in shape to the normal distribution but has "heavier tails," accounting for the extra uncertainty introduced by estimating the variance.


To find the interval,  the critical values $\pm t_{\alpha/2, n-1}$ are used to capture between them the central $(1-\alpha)$ area of the t-distribution curve:

$$-t_{\alpha/2, n-1} \leq \frac{\bar{X}-\mu}{s/\sqrt{n}} \leq t_{\alpha/2, n-1}$$

Rearranging to solve for $\mu$ gives the formula:

$$CI = \bar{X} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$$

Mathematically, as $n \rightarrow \infty$, the t-distribution converges to the standard normal distribution, and so the Z and T intervals become identical. In practice $n \geq 30$ is a high enough sample size for the two distributions to be near indistinguishable, which is why the Z-interval can be used for sample size $n \geq 30$.

---

> [!example]-
> Suppose $X_1, \dots, X_{16}$ is a sample drawn from a normal distribution $N(\mu, \sigma^2)$, with a sample mean $\bar{X} = 2.5$. Calculate the **95% confidence interval** ($\alpha = 0.05$).
> 
> > [!example]- Case 1: Known Variance
> > **Given:** $\sigma^2 = 25$ (so $\sigma = 5$) and $n = 16$.
> > 
> > Because the population variance is known, use the **Z-Interval**. The critical value for a 95% confidence level is $z_{0.025} \approx 1.96$.
> > 
> > $$CI_Z = \bar{X} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$$
> > $$CI_Z = 2.5 \pm 1.96 \left( \frac{5}{\sqrt{16}} \right)$$
> > $$CI_Z = 2.5 \pm 1.96 (1.25) = 2.5 \pm 2.45$$
> > 
> > **Result:** $[0.05, 4.95]$
> 
> > [!example]- Case 2: Unknown Variance
> > **Given:** $s^2 = 18.5$ (so $s = \sqrt{18.5} \approx 4.30$) and $n = 16$.
> > 
> > Since the variance is unknown and the sample size is small ($n < 30$), the **T-Interval** must be used with $df = n - 1 = 15$. The critical value from the t-distribution table is $t_{0.025, 15} \approx 2.13$.
> > 
> > $$CI_t = \bar{X} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$$
> > $$CI_t = 2.5 \pm 2.13 \left( \frac{\sqrt{18.5}}{\sqrt{16}} \right)$$
> > $$CI_t \approx 2.5 \pm 2.13 (1.075) \approx 2.5 \pm 2.29$$
> > 
> > **Result:** $[0.21, 4.79]$
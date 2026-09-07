The calculation of a $100(1-\alpha)\%$ confidence interval for the difference between two population means $\mu_1 - \mu_2$, based on two independent samples $X_{1,1}, \dots, X_{1,n_1}$ and $X_{2,1}, \dots, X_{2,n_2}$, typically follows one of three methods. The choice depends on whether the population variances $\sigma_1^2$ and $\sigma_2^2$ are known, and if unknown, whether they can be assumed to be equal.

Below is a summary table for when to use which of the methods described below:

| Method | Variances ($\sigma_1^2, \sigma_2^2$) | Assumption | Distribution |
| :--- | :--- | :--- | :--- |
| **Z-Interval** | Known | N/A | Normal ($Z$) |
| **Pooled T-Interval** | Unknown | Equal ($\sigma_1^2 = \sigma_2^2$) | Student's t ($t$) |
| **Welch's T-Interval** | Unknown | Unequal ($\sigma_1^2 \neq \sigma_2^2$) | Student's t ($t$) |

---

# Z-Interval (Difference)
This method is used when the population variances $\sigma_1^2$ and $\sigma_2^2$ are known. It is also applied when sample sizes are large ($n_1, n_2 \geq 30$) even if variances are unknown (where $s_1^2$ and $s_2^2$, the [[Sample Variance and Standard Deviation| sample variances]] are substituted for $\sigma_1^2$ and $\sigma_2^2$).

According to the properties of the [[Normal]] Distribution, the difference in [[Sample Mean|sample means]] follows a normal distribution.
$$\bar{X}_1 - \bar{X}_2 \sim N(\mu_1 - \mu_2, \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2})$$

According to the [[Central Limit Theorem]], the [[Pivotal Quantity]] $Z$ follows a standard normal distribution:

$$Z = \frac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} \sim N(0, 1)$$

The confidence interval is derived by isolating the parameter of interest, $\mu_1 - \mu_2$. The resulting formula is:

$$CI = (\bar{X}_1 - \bar{X}_2) \pm z_{\alpha/2} \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}$$

---

# Pooled T-Interval
This method is used when population variances are unknown but are assumed to be equal ($\sigma_1^2 = \sigma_2^2 = \sigma^2$). This assumption is often validated via a test for equality of variances (e.g. F-test).

Since the variances are assumed identical, the **pooled variance** $S_p^2$ is calculated. This weighted average gives more weight to the sample with the larger size:

$$S_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$$

The [[Pivotal Quantity]] $T$ is constructed using this pooled standard deviation and follows a t-distribution with $n_1 + n_2 - 2$ [[Degrees of Freedom]]:

$$T = \frac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{S_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t_{n_1 + n_2 - 2}$$

The confidence interval formula is given by:

$$CI = (\bar{X}_1 - \bar{X}_2) \pm t_{\alpha/2, n_1+n_2-2} \cdot S_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$$

---

# Welch's T-Interval (Unpooled)
This method is used when population variances are unknown and **cannot** be assumed to be equal ($\sigma_1^2 \neq \sigma_2^2$). This is often referred to as the **Behrens-Fisher problem**.

In this case, the variance of the difference in means is estimated by the sum of the individual sample variances. The test statistic is:

$$T = \frac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}} \overset{\mathrm{approx}}{\sim} t(\nu)$$

However, this statistic does not follow an exact t-distribution. It is approximated by a t-distribution using **Welch's Approximation** for the degrees of freedom ($\nu$). The degrees of freedom are calculated as:

$$\nu \approx \frac{\left( \frac{s_1^2}{n_1} + \frac{s_2^2}{n_2} \right)^2}{\frac{(s_1^2/n_1)^2}{n_1 - 1} + \frac{(s_2^2/n_2)^2}{n_2 - 1}}$$

Usually, $\nu$ is rounded down to the nearest integer. The confidence interval is then given by:

$$CI = (\bar{X}_1 - \bar{X}_2) \pm t_{\alpha/2, \nu} \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}$$

---

> [!example -]
> Suppose two independent samples are drawn
> * **Sample 1:** $\bar{X}_1 = 50$, $n_1 = 12$
> * **Sample 2:** $\bar{X}_2 = 42$, $n_2 = 15$
> 
> A **95% confidence interval** ($\alpha = 0.05$) is required for the difference $\mu_1 - \mu_2$.
> >[!example]- Case 1: Known Variances
> > **Given:** $\sigma_1^2 = 10$, $\sigma_2^2 = 12$.
> > 
> > Since variances are known, the **Z-Interval** is selected. $z_{0.025} \approx 1.96$.
> > 
> > $$SE = \sqrt{\frac{10}{12} + \frac{12}{15}} = \sqrt{0.833 + 0.8} = \sqrt{1.633} \approx 1.278$$
> > $$CI = (50 - 42) \pm 1.96(1.278)$$
> > $$CI = 8 \pm 2.50$$
> > 
> > **Result:** $[5.50, 10.50]$
> 
> >[!example]- Case 2: Unknown, Equal Variances (Pooled)
> > **Given:** $s_1^2 = 10$, $s_2^2 = 12$ (Assumed $\sigma_1^2 = \sigma_2^2$).
> > 
> > The **Pooled T-Interval** is used.
> > First, the pooled variance $S_p^2$ is calculated:
> > $$S_p^2 = \frac{(11)(10) + (14)(12)}{12 + 15 - 2} = \frac{110 + 168}{25} = \frac{278}{25} = 11.12$$
> > $$S_p = \sqrt{11.12} \approx 3.335$$
> > 
> > Degrees of freedom: $df = 25$. Critical value $t_{0.025, 25} \approx 2.06$.
> > 
> > $$SE = 3.335 \sqrt{\frac{1}{12} + \frac{1}{15}} = 3.335 \sqrt{0.15} \approx 1.291$$
> > $$CI = 8 \pm 2.06(1.291) \approx 8 \pm 2.66$$
> > 
> > **Result:** $[5.34, 10.66]$
> 
> >[!example]- Case 3: Unknown, Unequal Variances (Welch)
> > **Given:** $s_1^2 = 10$, $s_2^2 = 12$ (Assumed $\sigma_1^2 \neq \sigma_2^2$).
> > 
> > **Welch's T-Interval** is used. First, the degrees of freedom $\nu$ are approximated:
> > 
> > $$\nu \approx \frac{(0.833 + 0.8)^2}{\frac{(0.833)^2}{11} + \frac{(0.8)^2}{14}} = \frac{2.666}{0.063 + 0.046} = \frac{2.666}{0.109} \approx 24.46 \rightarrow 24$$
> > 
> > Critical value $t_{0.025, 24} \approx 2.064$.
> > 
> > $$SE = \sqrt{\frac{10}{12} + \frac{12}{15}} \approx 1.278$$
> > $$CI = 8 \pm 2.064(1.278) \approx 8 \pm 2.64$$
> > 
> > **Result:** $[5.36, 10.64]$
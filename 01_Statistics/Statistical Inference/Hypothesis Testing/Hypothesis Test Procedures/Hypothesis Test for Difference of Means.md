Given two independent random samples from populations with means $\mu_1, \mu_2$ and variances $\sigma_1^2, \sigma_2^2$, inferences about the difference between the means ($\mu_1 - \mu_2$) are evaluated using a [[Hypothesis Test]] structured as:

$$
\begin{aligned}
H_0: & \quad \mu_1 - \mu_2 = D_0 \\
H_1: & \quad
\begin{cases}
\mu_1 - \mu_2 \neq D_0 & \text{(Two-Tailed)} \\ 
\mu_1 - \mu_2 > D_0 & \text{(Right-Tailed)}\\
\mu_1 - \mu_2 < D_0 & \text{(Left-Tailed)}
\end{cases}
\end{aligned}
$$

*Note: Usually $D_0 = 0$, testing if the means are equal.*

The estimator for the difference $\mu_1 - \mu_2$ is the difference between the [[Sample Mean|Sample Means]]:
$$\bar{X}_1 - \bar{X}_2 = \frac{1}{n_1}\sum x_{1i} - \frac{1}{n_2}\sum x_{2i}$$

---

## Two-Sample Z-Test

**Conditions:**
1. Samples are **independent** and **random**.
2. Population variances $\sigma_1^2$ and $\sigma_2^2$ are **known**.
3. Sample sizes are **large** ($n_1, n_2 > 30$) OR populations are **normal**.

**Test Statistic:**
The test statistic follows a Standard [[Normal]] distribution so this is a [[Z-test]].

$$Z = \frac{(\bar{X}_1 - \bar{X}_2) - D_0}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} \sim N(0, 1)$$

### Decision Rules & Rejection Regions
The rejection region is defined by the critical value(s) $z_{\text{crit}}$ and the significance level $\alpha$.

| Test Type        | Alternative ($H_1$)      | Rejection Rule (Reject $H_0$ if...) | P-Value Calculation                           |
| :--------------- | :----------------------- | :---------------------------------- | :-------------------------------------------- |
| **Two-Tailed**   | $\mu_1 - \mu_2 \neq D_0$ | $\lvert Z \rvert>z_{\alpha/2}$      | $2 \times P(Z >\lvert z_{\text{calc}}\rvert)$ |
| **Left-Tailed**  | $\mu_1 - \mu_2 < D_0$    | $Z < -z_{\alpha}$                   | $P(Z < z_{\text{calc}})$                      |
| **Right-Tailed** | $\mu_1 - \mu_2 > D_0$    | $Z > z_{\alpha}$                    | $P(Z > z_{\text{calc}})$                      |
where $z_{calc}$ is the test statistic in the p-value case.

---

## Two-Sample t-Test

**Conditions:**
1. Population variances $\sigma_1^2, \sigma_2^2$ are **unknown**.
2. Samples are **independent** and **random**.
3. Underlying data is approximately **normal** or sample sizes are large.

**Test Statistic (Unpooled):**
When variances are not assumed to be equal ($\sigma_1^2 \neq \sigma_2^2$), the test statistic follows a Student-t distribution. This is often called **Welch's t-test**.

$$t = \frac{(\bar{X}_1 - \bar{X}_2) - D_0}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}} \sim t_{df}$$

*Where $s_1, s_2$ are the sample standard deviations.*

**Degrees of Freedom ($df$):**
For Welch's t-test, the [[Degrees of Freedom]] are approximated by the Welch-Satterthwaite equation:
$$df \approx \left\lfloor\frac{(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2})^2}{\frac{(\frac{s_1^2}{n_1})^2}{n_1-1} + \frac{(\frac{s_2^2}{n_2})^2}{n_2-1}}\right\rfloor$$
Conservative Estimate: $df = \min(n_1-1, n_2-1)$

> [!NOTE] Pooled t-Test
> If the population variances are assumed equal ($\sigma_1^2 = \sigma_2^2$), a **pooled variance** $s_p^2$ is used for $s_1$ and $s_2$, and $df = n_1 + n_2 - 2$.
> 
> $$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$$

**Decision Rules:**
The inference rules are identical to the Z-test, but the critical values from the t-distribution ($t_{\alpha, df}$) are used rather than the standard normal distribution.

---

> [!example]- Z-test Example
> Two samples of students from different schools take the same test:
>
> * Group 1:
> 	* Number of Students: 57
> 	* Average Score: 77.2
> 	* Variance: 15.3 (known)
> * Group 2:
> 	* Number of Students: 63
> 	* Average Score: 75.3
> 	* Variance: 19.7 (known)
> 
> At $\alpha=0.05$, is there evidence that the true difference is significantly different from zero?
> 
> Hypotheses:
> $$H_0: \mu_1 = \mu_2$$
> $$H_1: \mu_1 \neq \mu_2$$
> 
> This is a **two-tailed test**. Population variances are known and sample sizes are high so a Z-test is appropriate. 
> 
> Test Statistic:
> $$Z = \frac{(\bar{X}_1 - \bar{X}_2) - D_0}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} = \frac{(77.2 - 75.3) - 0}{\sqrt{\frac{15.3}{57} + \frac{19.7}{63}}} = 2.49$$
>  Using a standard normal distribution $N(0,1)$, this leads to a p-value of:
> $$p = 2 \times P(Z >2.49)=0.012$$
> $p<\alpha$ so the null hypothesis is rejected meaning there is evidence to suggest the two sets of test scores are significantly different. 
> ![[mean_difference_test_example_1.svg]]

> [!example]- t-test Example
> A gardener is testing two brands of fertilizer on two different tomato plants. They have been using fertilizer A in the past and want to know if fertilizer B leads to larger tomatoes. After harvest they report the following observations:
> * **Plant A (with Fertilizer A)**:
> 	* **Number of Tomatoes: 10**
> 	* **Average Diameter**: 7 cm
> 	* **Standard Deviation**: 1.5 cm
>  * **Plant B (with Fertilizer B)**:
> 	* **Number of Tomatoes: 22**
> 	* **Average Diameter**: 7.3 cm
> 	* **Standard Deviation**: 2.1 cm
> 
> At significance level $\alpha=0.05$, is the evidence to suggest fertilizer B leads to larger tomatoes?
> 
> Hypotheses:
> $$H_0:\mu_1=\mu_2$$
> $$H_1: \mu_1<\mu_2$$
> This is a **lower-tailed test**. Sample sizes are low and population variances unknown so a t-Test is appropriate. Population variance is not assumed to be equal.
> 
> Test Statistic:
> $$t = \frac{(\bar{X}_1 - \bar{X}_2) - D_0}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}} = \frac{(7 - 7.3) - 0}{\sqrt{\frac{1.5^2}{10} + \frac{2.1^2}{22}}}= -0.45$$
> Degrees of Freedom using the Welch-Satterthwaite equation:
> $$df \approx \left\lfloor\frac{(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2})^2}{\frac{(\frac{s_1^2}{n_1})^2}{n_1-1} + \frac{(\frac{s_2^2}{n_2})^2}{n_2-1}}\right\rfloor = \left\lfloor\frac{(\frac{1.5^2}{10} + \frac{2.1^2}{22})^2}{\frac{(\frac{1.5^2}{10})^2}{9} + \frac{(\frac{2.1^2}{22})^2}{21}}\right\rfloor  = 24$$
> 
> Using a t distribution $t_{24}$, this leads to a p-value of:
> $$p=P(t_{24} < -0.45) = 0.328$$
> $p > \alpha$ so the null hypothesis cannot be rejected and there is not evidence to suggest that fertilizer B produces larger tomatoes.
> ![[mean_difference_test_example_2.svg]]
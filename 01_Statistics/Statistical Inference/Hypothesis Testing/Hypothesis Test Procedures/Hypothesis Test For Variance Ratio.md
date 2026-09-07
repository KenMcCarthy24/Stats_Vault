Given two independent random samples of sizes $n_1$ and $n_2$ from populations with variances $\sigma_1^2$ and $\sigma_2^2$, inferences about the ratio of the variances ($\frac{\sigma_1^2}{\sigma_2^2}$) are evaluated using a [[Hypothesis Test]] structured as:

$$
\begin{aligned}
H_0: & \quad \frac{\sigma_1^2}{\sigma_2^2} = 1 \quad (\sigma_1^2 = \sigma_2^2) \\
H_1: & \quad
\begin{cases}
\frac{\sigma_1^2}{\sigma_2^2} \neq 1 & \text{(Two-Tailed)} \\ 
\frac{\sigma_1^2}{\sigma_2^2} > 1 & \text{(Right-Tailed)} \\
\frac{\sigma_1^2}{\sigma_2^2} < 1 & \text{(Left-Tailed)}
\end{cases}
\end{aligned}
$$

The estimator for the ratio is the ratio of the [[Sample Variance and Standard Deviation|Sample Variances]]:
$$F = \frac{s_1^2}{s_2^2}$$

---

## F-Test For Equality of Variances

**Conditions:**
1. The samples are **independent random samples**.
2. **Normality**: Both populations must be **normally distributed**.

> [!warning]
> the F test for variance is **not robust** to departures from normality. If the population is not normal, this test can give highly misleading results.

**Test Statistic:**
The test statistic follows an [[F-distribution]] with [[Degrees of Freedom]] $d_1 = n_1 - 1$ and $d_2 = n_2 - 1$ so this is an [[F-Test]].

$$F = \frac{s_1^2}{s_2^2} \sim F_{n_1-1, n_2-1}$$

*Where $s_1^2$ is the variance of sample 1 (numerator) and $s_2^2$ is the variance of sample 2 (denominator).*

### Decision Rules & Rejection Regions
The rejection region is defined by the critical value(s) from the F-distribution table ($F_{\alpha, d_1, d_2}$) and the significance level $\alpha$.

**Important:** The F-distribution is **not symmetric**.

| Test Type        | Alternative ($H_1$) | Rejection Rule (Reject $H_0$ if...) |
| :--------------- | :------------------ | :---------------------------------- |
| **Two-Tailed** | $\sigma_1^2 \neq \sigma_2^2$ | $F < F_{1-\alpha/2}$ or $F > F_{\alpha/2}$      |
| **Left-Tailed** | $\sigma_1^2 < \sigma_2^2$   | $F < F_{1-\alpha}$                   |
| **Right-Tailed** | $\sigma_1^2 > \sigma_2^2$   | $F > F_{\alpha}$                    |

*Note: Lower critical values can be found using the reciprocal property: $F_{1-\alpha, d_1, d_2} = \frac{1}{F_{\alpha, d_2, d_1}}$.*

> [!tip] Convention for Two-Tailed Tests
> To avoid dealing with lower-tail critical values, it is common practice in a **two-tailed test** to always place the **larger sample variance** in the numerator. This forces the test statistic to be $> 1$, effectively turning the calculation into a right-tailed test against the critical value $F_{\alpha/2}$.

---

> [!example]- Example
> A quality control manager wants to determine if two machines, A and B, have different variabilities in the weight of the products they produce. A random sample of product weights is taken from each machine.
> 
> * **Machine A:** Sample size $n_1 = 16$, sample standard deviation $s_1 = 0.04$ grams.
> * **Machine B:** Sample size $n_2 = 21$, sample standard deviation $s_2 = 0.06$ grams.
> 
> Using a significance level of $\alpha = 0.05$, is there sufficient evidence to claim that the variance of Machine A differs from the variance of Machine B? Assume the weights are normally distributed.
> 
> Hypotheses:
> $$H_0: \frac{\sigma^2_1}{\sigma^2_2}=1$$
> $$H_1: \frac{\sigma^2_1}{\sigma^2_2} \neq 1$$
> 
> This is a **two-tailed test**
> 
> Test statistic (higher sample variance on top):
> $$F = \frac{s_2^2}{s_1^2}=\frac{0.06^2}{0.04^2}=2.25$$
> Using an F distribution with $n_2-1 = 20$ numerator degrees of freedom and $n_1-1=15$ denominator degrees of freedom $F_{20, 15}$, this leads to a p-value of:
> $$p = 2P(F>2.25) = 0.114$$
> $p>\alpha$ so the null hypothesis cannot be rejected, meaning there is not sufficient evidence to say the variances are significantly different.
> 
![[variance_ratio_test_example.svg]]


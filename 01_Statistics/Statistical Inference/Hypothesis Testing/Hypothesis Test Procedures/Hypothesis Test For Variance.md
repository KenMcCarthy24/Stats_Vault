Given a random sample $X_1, \dots, X_n$ from a population with variance $\sigma^2$, inferences about the variance are evaluated using a [[Hypothesis Test]] structured as:

$$
\begin{aligned}
H_0: & \quad \sigma^2 = \sigma_0^2 \\
H_1: & \quad
\begin{cases}
\sigma^2 \neq \sigma_0^2 & \text{(Two-Tailed)} \\ 
\sigma^2 > \sigma_0^2 & \text{(Right-Tailed)}\\
\sigma^2 < \sigma_0^2 & \text{(Left-Tailed)}
\end{cases}
\end{aligned}
$$

The estimator for $\sigma^2$ used for testing is the [[Sample Variance and Standard Deviation#Unbiased Sample Variance|Unbiased Sample Variance]]:
$$s^2 = \frac{\sum_{i=1}^n (x_i - \bar{X})^2}{n-1}$$

---

## Chi-Square Test For Variance

**Conditions:**
1. The sample is a **random sample**.
2. **Normality**: The population from which the sample is drawn must be **normally distributed**.

> [!warning]
> Unlike tests for the mean, the Chi-Square test for variance is **not robust** to departures from normality. If the population is not normal, this test can give highly misleading results.

**Test Statistic:**
The test statistic follows a Chi-Square distribution with $n-1$ [[Degrees of Freedom]] so this is a [[Chi-Squared Test]].

$$\chi^2 = \frac{(n-1)s^2}{\sigma_0^2} \sim \chi^2_{n-1}$$

*Where $n$ is the sample size and $s^2$ is the sample variance.*

### Decision Rules & Rejection Regions
The rejection region is defined by the critical value(s) from the Chi-Square distribution table ($\chi^2_{\alpha, df}$) and the significance level $\alpha$.

**Important:** The Chi-Square distribution is **not symmetric**.

| Test Type        | Alternative ($H_1$)        | Rejection Rule (Reject $H_0$ if...)                            | P-Value Calculation                                                   |
| :--------------- | :------------------------- | :------------------------------------------------------------- | :-------------------------------------------------------------------- |
| **Two-Tailed**   | $\sigma^2 \neq \sigma_0^2$ | $\chi^2 < \chi^2_{1-\alpha/2}$ or $\chi^2 > \chi^2_{\alpha/2}$ | $2 \times \min(P(\chi^2 > \chi^2_{calc}), P(\chi^2 < \chi^2_{calc}))$ |
| **Left-Tailed**  | $\sigma^2 < \sigma_0^2$    | $\chi^2 < \chi^2_{1-\alpha}$                                   | $P(\chi^2 < \chi^2_{calc})$                                           |
| **Right-Tailed** | $\sigma^2 > \sigma_0^2$    | $\chi^2 > \chi^2_{\alpha}$                                     | $P(\chi^2 > \chi^2_{calc})$                                           |

where $\chi^2_{calc}$ is the test statistic in the p-value case, and critical values $\chi^2_{\alpha}$ refer to the value where the area to the *right* is $\alpha$.

---
> [!example]- Example 1
> A pharmaceutical company manufactures aspirin tablets that are supposed to contain exactly 325 mg of the active ingredient. While slight variations in the mean are controlled, the production manager is specifically concerned that the consistency of the tablet weights has deteriorated, leading to a higher variance than the acceptable population variance of $\sigma^2 = 4$. 
> 
> To test this, a random sample of 20 tablets is selected, and the sample variance is found to be $s^2 = 6.8$. At a significance level of $\alpha = 0.05$, is there sufficient evidence to suggest that the variance in tablet weight has increased?
> 
> Hypotheses:
> $$H_0: \sigma^2 = 4$$
> $$H_1: \sigma^2 > 4$$
> This is an **upper-tailed test**
> 
> Test Statistic:
> $$\chi^2 = \frac{(n-1)s^2}{\sigma_0^2} = \frac{(19)(6.8)}{4}=32.3$$
> Using a Chi-Squared Distribution with $n-1 = 19$ degrees of freedom $\chi^2_{19}$, this leads to a p-value of:
> $$p = P(\chi^2>32.3) = 0.029$$
> $p<\alpha$ so the null hypothesis can be rejected meaning there is evidence that the variance in tablet weight has increased.
> 
![[variance_test_example_1.svg]]

> [!example]- Example 2
> A historical dataset of monthly rainfall in a specific region shows a standard deviation of 1.2 inches. A meteorologist believes that climate patterns may have altered the variability of the rainfall, but is unsure if it has become more erratic or more stable. 
> 
> She collects a random sample of rainfall data from the last 25 months and calculates a sample standard deviation of $s = 0.9$ inches. Using a significance level of $\alpha = 0.10$, test the claim that the variance of monthly rainfall has changed from the historical level.
> 
> Hypotheses:
> $$H_0: \sigma^2=1.2^2$$
> $$H_1:\sigma^2 \neq 1.2^2$$
> This is a **two-tailed test**.
> 
>  Test Statistic:
> $$\chi^2 = \frac{(n-1)s^2}{\sigma_0^2} = \frac{(24)(0.9^2)}{1.2^2}=13.5$$
> Using a Chi-Squared Distribution with $n-1 = 24$ degrees of freedom $\chi^2_{24}$, this leads to a p-value of:
> $$p = 2\min(P(\chi^2 > 13.5), P(\chi^2 < 13.5)) = 2\min(0.957, 0.043) = 0.08$$
> $p < \alpha$ so the null hypothesis can be rejected, so there is  sufficient evidence that the variance has changed from the historical level. 
> 
![[variance_test_example_2.svg]]


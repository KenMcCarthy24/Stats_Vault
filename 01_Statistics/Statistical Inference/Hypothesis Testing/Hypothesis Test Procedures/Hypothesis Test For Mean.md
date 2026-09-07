Given a random sample $X_1, \dots, X_n$ with population mean $\mu$ and population variance $\sigma^2$, inferences about the mean $\mu$ are evaluated using a [[Hypothesis Test]] structured as:

$$
\begin{aligned}
H_0: & \quad \mu = \mu_0 \\
H_1: & \quad
\begin{cases}
\mu \neq \mu_0 & \text{(Two-Tailed)} \\ 
\mu > \mu_0 & \text{(Right-Tailed)}\\
\mu < \mu_0 & \text{(Left-Tailed)}
\end{cases}
\end{aligned}
$$

The estimator for $\mu$ used for testing is the [[Sample Mean]]:
$$\bar{X} = \frac{1}{n}\sum_{i=1}^n x_i$$

---

## Z-Test For Mean

**Conditions:**
1. Population variance $\sigma^2$ is **known** 
2. Sample size is **large** ($n > 30$) OR population is normal.

**Test Statistic:**
The test statistic follows a Standard [[Normal]] distribution so this is a [[Z-test]].

$$Z = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}} \sim N(0, 1)$$

*Note: If $\sigma$ is unknown but $n > 30$, substitute the [[Sample Variance and Standard Deviation#Sample Standard Deviation|sample standard deviation]] $s$ for $\sigma$.*

### Decision Rules & Rejection Regions
The rejection region is defined by the critical value(s) $z_{\text{crit}}$ and the significance level $\alpha$.

| Test Type        | Alternative ($H_1$) | Rejection Rule (Reject $H_0$ if...) | P-Value Calculation                           |
| :--------------- | :------------------ | :---------------------------------- | :-------------------------------------------- |
| **Two-Tailed**   | $\mu \neq \mu_0$    | $\lvert Z \rvert>z_{\alpha/2}$      | $2 \times P(Z >\lvert z_{\text{calc}}\rvert)$ |
| **Left-Tailed**  | $\mu < \mu_0$       | $Z < -z_{\alpha}$                   | $P(Z < z_{\text{calc}})$                      |
| **Right-Tailed** | $\mu > \mu_0$       | $Z > z_{\alpha}$                    | $P(Z > z_{\text{calc}})$                      |
where $z_{calc}$ is the test statistic in the p-value case.

---

## t-Test For Mean

**Conditions:**
1. Population variance $\sigma^2$ is **unknown**.
2. Sample size is **small** ($n < 30$).
3. Underlying data is approximately **normal**.

**Test Statistic:**
The test statistic follows a Student-t distribution with $n-1$ [[Degrees of Freedom]] so this is a [[Student's t-Test]].

$$t = \frac{\bar{X} - \mu_0}{s/\sqrt{n}} \sim t_{n-1}$$

*Where $s$ is the sample standard deviation.*

**Decision Rules:**
The inference rules are identical to the Z-test, but the critical values from the t-distribution ($t_{\alpha, n-1}$) are used rather than the standard normal distribution.

> [!warning]
> The t-test will not be reliable if the underlying data is not approximately normal.

---

> [!example]- Z-Test Example
> A company claims that the average battery life of their phone is 12 hours. A consumer group tests 125 phones and finds the average battery life to be 11.8 hours with a population standard deviation $\sigma = 0.8$. With $\alpha=0.05$, is the evidence to refute the company's claim and show the battery life is lower than they claim.
> 
> Hypotheses:
> $$H_0: \mu=12$$
> $$H_1: \mu<12$$
> This is a **lower-tail test**. Population variance is known and sample size is high so a **Z-test** is appropriate.
> 
> Test Statistic:
> $$Z = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}} = \frac{11.8 - 12}{0.8/\sqrt{125}} = -2.795$$
> Using a standard normal distribution $N(0,1)$, this leads to a p-value of:
> $$p = P(Z<-2.795) = 0.0026$$
> $p < \alpha$ so the null hypothesis is rejected. There is evidence to suggest the true battery life is shorter than claimed.
> ![[z_test_example.svg]]

> [!example]- t-test Example
> For the year of 2024 the average income of residents of an area was reported to be $56,000 with no reported standard deviation. In 2025 an economist ran a survey of 16 residents of the area and learned that their mean income was $58,000 with a sample standard deviation of $6000. Is there evidence that the average income has significantly changed at $\alpha=0.05$?
> 
>  Hypotheses:
> $$H_0: \mu=56000$$
> $$H_1: \mu \neq 56000$$
> This is a **two-tail test**. Population variance is unknown and the sample size is low ($< 30$) so a **t-test** with $n-1 = 15$ degrees of freedom is appropriate.
> 
> Test Statistic:
> $$t = \frac{\bar{X} - \mu_0}{s/\sqrt{n}} = \frac{58000 - 56000}{6000/4} = 1.333$$
> Using a t distribution $t_{15}$, this leads to a p-value of:
> $$2 \times P(t_{15} > 1.33) = 0.203$$
> $p > \alpha$ so the null hypothesis cannot be rejected. There is not enough statistical evidence to show the income has meaningfully changed.
> ![[t_test_example.svg]]

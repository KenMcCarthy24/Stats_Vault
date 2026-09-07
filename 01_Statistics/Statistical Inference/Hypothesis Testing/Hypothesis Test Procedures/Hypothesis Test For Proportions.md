Given a random sample $X$ of size $n$ where each $X_i$ is a [[Bernoulli]] random variable — $X_i \in \{0,1\}$ (0=False, 1=True) — the population proportion $p$ is evaluated using a [[Hypothesis Test]] structured as:

$$
\begin{aligned}
H_0: & \quad p = p_0 \\
H_1: & \quad
\begin{cases}
p \neq p_0 & \text{(Two-Tailed)} \\ 
p > p_0 & \text{(Right-Tailed)}\\
p < p_0 & \text{(Left-Tailed)}
\end{cases}
\end{aligned}
$$

The estimator for $p$ used for testing is the sample proportion, the total number of 1s over the sample size. This is also the [[Sample Mean]]
$$\hat p = \frac{\text{count true}}{\text{sample size}}= \frac{\sum_{i=1}^n x_i}{n} = \bar{X}$$

---

## Z-Test For Proportion

**Conditions:**
1. The sample is a **random sample**.
2. **Independence**: Sample size is less than 10% of the population.
3. **Large Counts** (Normality): The expected number of successes and failures must both be at least 10.
   $$np_0 \ge 10 \quad \text{and} \quad n(1-p_0) \ge 10$$

**Test Statistic:**
The test statistic follows a Standard [[Normal]] distribution so this is a [[Z-test]].

$$Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}} \sim N(0, 1)$$
> [!NOTE]
> The [[Standard Error]] in the denominator uses the *null hypothesis value* $p_0$, not the sample proportion. Opposite of the [[CI For Proportions|confidance interval for proportions]].

### Decision Rules & Rejection Regions
The rejection region is defined by the critical value(s) $z_{\text{crit}}$ and the significance level $\alpha$.

| Test Type        | Alternative ($H_1$) | Rejection Rule (Reject $H_0$ if...) | P-Value Calculation                           |
| :--------------- | :------------------ | :---------------------------------- | :-------------------------------------------- |
| **Two-Tailed**   | $p \neq p_0$        | $\lvert Z \rvert>z_{\alpha/2}$      | $2 \times P(Z >\lvert z_{\text{calc}}\rvert)$ |
| **Left-Tailed**  | $p < p_0$           | $Z < -z_{\alpha}$                   | $P(Z < z_{\text{calc}})$                      |
| **Right-Tailed** | $p > p_0$           | $Z > z_{\alpha}$                    | $P(Z > z_{\text{calc}})$                      |
where $z_{calc}$ is the test statistic in the p-value case.

---

> [!example]- Example 1
> An incumbent politician historically receives 55% of the vote in their district. A recent poll of 1,020 likely voters shows that 520 of them plan to vote for the incumbent. At a significance level of $\alpha=0.05$, is there sufficient evidence to claim that the politician's support has decreased below the historical 55% average?
> 
> Hypotheses:
> $$H_0:p=0.55$$
> $$H_1:p<0.55$$
> 
> This is a **lower tail test**
> 
> Estimator:
> $$\hat p = \frac{520}{1020}=0.5098$$
> 
> Test Statistic:
> $$Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}} = \frac{0.5098 - 0.55}{\sqrt{\frac{0.55(0.45)}{1020}}} = -2.58$$
> 
> Using a standard normal distribution $N(0,1)$, this leads to a p-value of:
> $$\text{p-value} = P(Z < -2.58) = 0.0049$$
> 
> $\text{p-value} < \alpha$ so the null hypothesis is rejected. There is evidence to suggest that the politician's support has decreased.
> ![[proportion_test_example_1.svg]]

> [!example]- Example 2
> A manufacturer of computer chips claims that only 2% of their chips are defective. A quality control engineer selects a random sample of 400 chips from the production line and finds that 14 are defective. Using a significance level of $\alpha=0.01$, is there evidence that the true defect rate differs from the company's claim?
> 
> Hypotheses:
> $$H_0=0.02$$
> $$H_1 \neq 0.02$$
> Because $p_0 = 0.02$ is so small, check large count assumption:
> $$np_0=400*0.02= 8$$
> This is $<10$ so the large count assumption is violated. However, continuing the process anyway.
> 
> Estimator:
> $$\hat p = \frac{14}{400}=0.035$$
> 
> Test Statistic:
> $$Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}} = \frac{0.035 - 0.02}{\sqrt{\frac{0.02(0.98)}{400}}} = 2.14$$
> Using a standard normal distribution $N(0,1)$, this leads to a p-value of:
> $$\text{p-value} = 2 \times P(Z >2.14) = 0.032$$
> 
> $\text{p-value} > \alpha$ so the null hypothesis cannot be rejected, meaning there isn't evidence to show the true rate differs from the company's claim. However, due to the violated assumption the result of this test is questionable. 
> ![[proportion_test_example_2.svg]]
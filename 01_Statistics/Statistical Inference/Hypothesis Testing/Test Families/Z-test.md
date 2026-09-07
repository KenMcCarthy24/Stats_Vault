
The **Z-Test** refers to any [[Hypothesis Test]] where the test statistic $Z$ follows a [[Normal|Standard Normal Distribution]] under the null hypothesis $H_0$:

$$Z \sim N(0,1)$$

It is generally used when parameters are **known** (like population variance $\sigma^2$) or when sample sizes are large enough ($n > 30$) for the [[Central Limit Theorem]] to apply.

> [!INFO] Connection to T-Tests
> The Z-test is the "limit" of the [[Student's t-Test]] as sample size $n$ approaches infinity.
> $$\lim_{n \to \infty} t_n = Z$$

## Assumptions

* **Independence:** Observations in the sample must be independent of each other.
* **Normality:** The sampling distribution of the statistic is normal (either the parent population is normal, or $n$ is large enough that it is approximately normal by the Central Limit Theorem).
* **Known Variance:** The population standard deviation ($\sigma$) is known (or reliably estimated).

## Test Statistic
The calculated $Z$ statistic represents the **distance** between the sample statistic and the hypothesized parameter, measured in units of [[Standard Error]].

$$Z = \frac{\text{Sample Statistic} - \text{Hypothesized Parameter}}{\text{Standard Error}}$$

**Where:**
* **Sample Statistic:** The point estimate of the parameter calculated from sample data.
* **Hypothesized Parameter:** The value of the parameter under the null hypothesis.
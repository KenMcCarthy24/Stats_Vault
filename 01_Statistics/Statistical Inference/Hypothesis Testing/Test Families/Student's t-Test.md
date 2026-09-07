The **Student's t-Test** refers to any [[Hypothesis Test]] where the test statistic $t$ follows a [[Student-t]] distribution under the null hypothesis $H_0$. It is most commonly used when sample sizes are small ($n < 30$) and the population variance is unknown.

$$t \sim t_{\nu}$$
where $\nu$=[[Degrees of Freedom]]

It is designed to handle the additional uncertainty introduced by estimating the population standard deviation ($\sigma$) with the [[Sample Variance and Standard Deviation#Sample Standard Deviation|sample standard deviation]] ($s$).

> [!INFO] Connection to Normal Distribution
> As the degrees of freedom ($\nu$) increase, the t-distribution approaches the [[Normal|Standard Normal Distribution]].
> $$\lim_{\nu \to \infty} t_{\nu} = Z$$

## Assumptions

* **Independence:** Observations in the sample must be independent of each other.
* **Normality:** The underlying population from which samples are drawn should be approximately normally distributed (essential for small samples).
* **Homogeneity of Variance (for two-sample tests):** The variances of the two populations being compared should be equal (unless using Welch's correction).

## Test Statistic
The calculated $t$ statistic represents the difference between the observed sample statistic and the hypothesized population parameter, standardized by the estimated [[Standard Error]].

$$t = \frac{\text{Sample Statistic} - \text{Hypothesized Parameter}}{\text{Estimated Standard Error}}$$

**Where:**
* **Sample Statistic:** The point estimate (e.g., sample mean $\bar{x}$).
* **Hypothesized Parameter:** The value under the null hypothesis (e.g., population mean $\mu_0$).
* **Estimated Standard Error:** The standard error calculated using the sample standard deviation ($s$) rather than $\sigma$.
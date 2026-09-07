A $100(1-\alpha)\%$ [[Confidence Intervals|confidence interval]] for the difference between two population proportions $p_1 - p_2$ is calculated based on two independent random samples of size $n_1$ and $n_2$. This interval estimates the difference in the rate of "success" between two distinct populations.

Let $\hat p_1$ and $\hat p_2$ be the [[Estimators|estimators]] for the true proportions $p_1$ and $p_2$, where:
$$\hat p_1 = \frac{x_1}{n_1} \quad \text{and} \quad \hat p_2 = \frac{x_2}{n_2}$$

Where $x_1$ and $x_2$ represent the count of successes in each sample. Assuming the two samples are independent, the difference $\hat p_1 - \hat p_2$ is an unbiased estimator for $p_1 - p_2$.

* **Mean**: $E[\hat p_1 - \hat p_2] = p_1 - p_2$
* **Variance**: Since samples are independent, variances add:
$$Var[\hat p_1 - \hat p_2] = Var[\hat p_1] + Var[\hat p_2] = \frac{p_1(1-p_1)}{n_1} + \frac{p_2(1-p_2)}{n_2}$$

By the [[Central Limit Theorem]], for large $n_1$ and $n_2$, the sampling distribution of the difference is approximately Normal:
$$(\hat p_1 - \hat p_2) \sim N\left(p_1 - p_2, \sqrt{\frac{p_1(1-p_1)}{n_1} + \frac{p_2(1-p_2)}{n_2}}\right)$$

---
# The Wald Interval for Difference
The confidence interval is constructed similarly to the [[CI For Proportions|single-proportion case]], using critical values $\pm z_{\alpha/2}$ from the standard normal distribution. Because the true population proportions $p_1$ and $p_2$ are unknown, substitute the sample proportions $\hat p_1$ and $\hat p_2$ into the standard error formula.

The formula for the confidence interval is:
$$CI_{Diff} = (\hat p_1 - \hat p_2) \pm z_{\alpha/2}\sqrt{\frac{\hat p_1 (1-\hat p_1)}{n_1} + \frac{\hat p_2 (1-\hat p_2)}{n_2}}$$

### Assumptions (Success/Failure Condition)
To ensure the Normal approximation is valid for *both* sampling distributions, the Success/Failure condition must be met for **both groups** independently. Substitute $\hat p$ for the unknown $p$:

**Group 1:**
$$n_1\hat p_1 \ge 10 \quad \text{and} \quad n_1(1-\hat p_1) \ge 10$$

**Group 2:**
$$n_2\hat p_2 \ge 10 \quad \text{and} \quad n_2(1-\hat p_2) \ge 10$$

If any of these four checks fail, the standard Wald interval may be inaccurate.

---

> [!example]-
> A marketing team wants to compare the click-through rates of two different website designs (A and B).
> * **Design A:** $n_1 = 200$ visitors, $x_1 = 32$ clicks.
> * **Design B:** $n_2 = 200$ visitors, $x_2 = 18$ clicks.
> 
> Construct a 95% confidence interval for the difference in click-through rates ($p_A - p_B$).
> 
> The critical value for a 95% confidence level is $z_{0.025} \approx 1.96$.
> 
> Start by calculating estimators for $p_A$ and $p_B$ and their difference
> $$\hat p_A = \frac{32}{200} = 0.16, \quad \hat p_B = \frac{18}{200} = 0.09$$
> $$\text{Difference} = 0.16 - 0.09 = 0.07$$
> 
> Make sure the assumptions are correct:
> * Group A: $200(0.16)=32 \ge 10$ and $200(0.84)=168 \ge 10$. (Pass)
> * Group B: $200(0.09)=18 \ge 10$ and $200(0.91)=182 \ge 10$. (Pass)
> 
> Now calculate the interval:
> $$
> \begin{align}
> CI_{Diff} &= (\hat p_1 - \hat p_2) \pm z_{\alpha/2}\sqrt{\frac{\hat p_1 (1-\hat p_1)}{n_1} + \frac{\hat p_2 (1-\hat p_2)}{n_2}} \\
> &= 0.07 \pm (1.96)\sqrt{\frac{0.16(0.84)}{200} + \frac{0.09(0.91)}{200}} \\
> &= 0.07 \pm 0.0645
> \end{align}
> $$
> 
> Result: $[0.0055, 0.1345]$
> 
> Since the interval does not contain 0, there is evidence at the 95% confidence level that Design A has a higher click-through rate than Design B.
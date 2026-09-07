A $100(1-\alpha)\%$ [[Confidence Intervals|confidence interval]] for a parameter $p$ — representing a true proportion of the total population for which some boolean choice is True — based on sample data $X_1, \dots, X_n$ where $X_i \in \{0,1\}$ (0=False, 1=True) is calculated using one of two methods. The choice often depends on sample size $n$ and expected population proportion $p$.

Let $\hat p$ be an [[Estimators|estimator]] of the true proportion $p$ with:
$$\hat p = \frac{\text{count true}}{\text{sample size}}= \frac{\sum_{i=1}^n x_i}{n} = \bar{X}$$

The $X_i$ observations are [[Bernoulli]] random variables, and their mean $\hat p$ has a scaled [[Binomial]] distribution ($\hat p \sim Y/n$ where $Y \sim Bin(n, p)$):
* **Mean**: $E[\hat p] = p$
* **Variance**: $Var[\hat p] = \frac{p(1-p)}{n}$

For large $n$, by the [[Central Limit Theorem]]: $\hat p \sim N(p, \frac{p(1-p)}{n})$. So the [[Pivotal Quantity]] Z can be calculated as:
$$Z = \frac{\hat p - p}{\sqrt{\frac{p(1-p)}{n}}}$$
---
# The Wald Interval (Standard)
The confidence interval is defined by the critical values $\pm z_{\alpha/2}$, which capture between them the central $(1-\alpha)$ area of the standard normal curve. This is expressed by the inequality:
$$-z_{\alpha/2} \leq \frac{\hat p - p}{\sqrt{\frac{p(1-p)}{n}}} \leq z_{\alpha/2}$$

Rearranging the inequality to isolate $p$ and plugging in the sample proportion $\hat p$ for the $p$'s in the denominator gives the formula for the confidence interval:
$$CI_{Wald} = \hat p \pm z_{\alpha/2}\sqrt{\frac{\hat p (1-\hat p)}{n}}$$

The most standard rule of thumb to ensure $n$ is "large enough" for the Central Limit Theorem is the **Success/Failure Condition**.

This condition requires that we expect at least 10 successes and 10 failures in our sample to safely use the Normal approximation of the Binomial. Since we don't know the true $p$, we substitute with $\hat p$:

$$n\hat p \ge 10 \quad \text{and} \quad n(1-\hat p) \ge 10$$

---
# The Wilson Interval (Score Interval)
The Wald interval can perform poorly when $n$ is small or $p$ is close to 0 or 1. The Wilson interval solves this by keeping the population proportion $p$ in the standard error term during the derivation, rather than substituting it with $\hat p$.

Starting from the same inequality, now represented as an absolute value:
$$\left| \frac{\hat p - p}{\sqrt{\frac{p(1-p)}{n}}} \right| \leq z_{\alpha/2}$$

Squaring both sides and solving the resulting quadratic equation for $p$ yields the Wilson interval:
$$CI_{Wilson} = \frac{\hat p + \frac{z_{\alpha/2}^2}{2n}}{1 + \frac{z_{\alpha/2}^2}{n}} \pm \frac{z_{\alpha/2}}{1 + \frac{z_{\alpha/2}^2}{n}} \sqrt{\frac{\hat p(1-\hat p)}{n} + \frac{z_{\alpha/2}^2}{4n^2}}$$

This interval is asymmetric (pulls the center towards 0.5) and always stays within $(0, 1)$, making it robust even for small sample sizes or extreme proportions.

---

> [!example]-
> A manufacturing plant produces a new type of battery. To estimate the defect rate, a quality control manager takes a random sample of **n=50** batteries from the production line and tests them. The testing reveals that **x=4** batteries are defective. Calculate both the 95% Wald and 95% Wilson Confidence intervals.
> 
> The critical value for a 95% confidence level is $z_{0.025} \approx 1.96$.
> 
> Start by calculating the estimator $\hat p$
> $$\hat p = \frac{\text{count defective}}{\text{sample size}} = \frac{x}{n} = \frac{4}{50} = 0.08$$
> Now $n \hat p = 4$ which is $<10$, meaning that the normal approximation isn't very accurate and the Wald interval isn't appropriate, but it will be calculated anyway.
> 
> The Wald Interval is given by:
> $$CI_{Wald} = \hat p \pm z_{\alpha/2}\sqrt{\frac{\hat p (1-\hat p)}{n}} = 0.08 \pm (1.96)\sqrt{\frac{(0.08)(0.92)}{50}} = 0.08 \pm 0.075$$
> Result: $[0.005, 0.155]$. Lower bound is almost zero, risks going negative if $x$ were smaller.
> 
> The Wilson Interval is given by:
> $$CI_{Wilson} = \frac{\hat p + \frac{z_{\alpha/2}^2}{2n}}{1 + \frac{z_{\alpha/2}^2}{n}} \pm \frac{z_{\alpha/2}}{1 + \frac{z_{\alpha/2}^2}{n}} \sqrt{\frac{\hat p(1-\hat p)}{n} + \frac{z_{\alpha/2}^2}{4n^2}} = 0.11 \pm 0.078$$
> Result: $[0.032, 0.188]$. Lower bound is more realistic. 
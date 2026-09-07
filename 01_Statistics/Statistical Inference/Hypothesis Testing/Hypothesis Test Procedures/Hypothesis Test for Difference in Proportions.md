Given two independent random samples $X_1, X_2$ of size $n_1$ and $n_2$ where the data consists of [[Bernoulli]] trials — $X_i \in \{0,1\}$ (0=False, 1=True) for each — the difference between population proportions $p_1$ and $p_2$ is evaluated using a [[Hypothesis Test]] structured as:

$$
\begin{aligned}
H_0: & \quad p_1 - p_2 = 0 \quad (p_1 = p_2) \\
H_1: & \quad
\begin{cases}
p_1 - p_2 \neq 0 & \text{(Two-Tailed)} \\ 
p_1 - p_2 > 0 & \text{(Right-Tailed)}\\
p_1 - p_2 < 0 & \text{(Left-Tailed)}
\end{cases}
\end{aligned}
$$

The estimator for the difference $p_1 - p_2$ is the difference between the sample proportions, which is just the difference in [[Sample Mean]]:
$$\hat{p}_1 - \hat{p}_2 = \frac{x_1}{n_1} - \frac{x_2}{n_2}$$
*Where $x_1, x_2$ are the count of successes in each sample.*

---

## Z-Test For Difference of Proportions

**Conditions:**
1. **Random Samples**: Both samples are collected independently and randomly.
2. **Independence**: Both sample sizes are less than 10% of their respective populations.
3. **Large Counts** (Normality): The number of successes and failures in **both** samples must be at least 10.
   $$n_1\hat{p}_1, n_1(1-\hat{p}_1) \ge 10 \quad \text{and} \quad n_2\hat{p}_2, n_2(1-\hat{p}_2) \ge 10$$

**Pooled Proportion:**
Because the null hypothesis assumes the proportions are equal ($p_1 = p_2$), combine the samples to calculate a **pooled sample proportion** ($\hat{p}_c$) to estimate the standard error.

$$\hat{p}_c = \frac{x_1 + x_2}{n_1 + n_2}$$

**Test Statistic:**
The test statistic follows a Standard [[Normal]] distribution so this is a [[Z-test]].

$$Z = \frac{(\hat{p}_1 - \hat{p}_2) - 0}{\sqrt{\hat{p}_c(1-\hat{p}_c)(\frac{1}{n_1} + \frac{1}{n_2})}} \sim N(0, 1)$$

### Decision Rules & Rejection Regions
The rejection region is defined by the critical value(s) $z_{\text{crit}}$ and the significance level $\alpha$.

| Test Type        | Alternative ($H_1$) | Rejection Rule (Reject $H_0$ if...) | P-Value Calculation                           |
| :--------------- | :------------------ | :---------------------------------- | :-------------------------------------------- |
| **Two-Tailed** | $p_1 \neq p_2$      | $\lvert Z \rvert>z_{\alpha/2}$      | $2 \times P(Z >\lvert z_{\text{calc}}\rvert)$ |
| **Left-Tailed** | $p_1 < p_2$         | $Z < -z_{\alpha}$                   | $P(Z < z_{\text{calc}})$                      |
| **Right-Tailed** | $p_1 > p_2$         | $Z > z_{\alpha}$                    | $P(Z > z_{\text{calc}})$                      |
where $z_{calc}$ is the test statistic in the p-value case.

---
>[!example]-
> A marketing firm is testing a new website design to see if it increases the "click-through" rate compared to the old design. The firm displays the old design to a random sample of 800 visitors, and 48 of them click the target link. They display the new design to an independent random sample of 900 visitors, and 72 of them click the target link.
> 
> At a significance level of $\alpha = 0.05$, is there sufficient evidence to claim that the new design has a higher click-through rate than the old design?
> 
> Hypotheses:
> $$H_0: p_1 = p_2$$
> $$H_1: p_1 < p_2$$
> 
> This is a **lower-tail test**. Sample proportions are:
> * $\hat p_1 = \frac{48}{800}=0.06$ (old design)
> * $\hat p_2 = \frac{72}{900}=0.08$ (new design)
> * $\hat p_c = \frac{48+72}{800+900}=0.071$
> 
> Test Statistic:
> $$Z = \frac{(\hat{p}_1 - \hat{p}_2) - 0}{\sqrt{\hat{p}_c(1-\hat{p}_c)(\frac{1}{n_1} + \frac{1}{n_2})}} = \frac{0.06 - 0.08}{\sqrt{0.071(1-0.071)(\frac{1}{800} + \frac{1}{900})}} = -1.603$$
> Using a standard normal distribution $N(0,1)$, this leads to a p-value of:
> $$p = P(Z<-1.603) = 0.0544$$
> $p > \alpha$ (barely) so the null hypothesis cannot be rejected meaning there is not sufficient evidence to claim the new design has a higher click-through rate.
> ![[prop_difference_test_example.svg]]
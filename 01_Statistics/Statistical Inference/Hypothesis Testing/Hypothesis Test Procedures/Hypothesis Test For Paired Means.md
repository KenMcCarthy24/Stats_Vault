Given two samples that are **dependent** (matched pairs, e.g., "Before & After" measurements on the same subjects), inferences are made about the mean of the differences, denoted $\mu_d$.

First, calculate the differences for each pair: $d_i = x_{1i} - x_{2i}$. The test is then treated as a single-sample t-test on these differences.

$$
\begin{aligned}
H_0: & \quad \mu_d = \Delta_0 \quad (\text{Usually } 0) \\
H_1: & \quad
\begin{cases}
\mu_d \neq \Delta_0 & \text{(Two-Tailed)} \\ 
\mu_d > \Delta_0 & \text{(Right-Tailed)}\\
\mu_d < \Delta_0 & \text{(Left-Tailed)}
\end{cases}
\end{aligned}
$$

The estimator is the [[Sample Mean]] of the differences:
$$\bar{d} = \frac{\sum d_i}{n}$$

---

## Paired t-Test

**Conditions:**
1. **Dependent Samples**: Data must be matched pairs.
2. **Random Sample**: The pairs are a random sample.
3. **Normality**: The population of *differences* must be normal (or $n > 30$).

**Test Statistic:**
The test statistic follows a Student-t distribution with $n-1$ [[Degrees of Freedom]] so this is a [[Student's t-Test]].

$$t = \frac{\bar{d} - \Delta_0}{s_d/\sqrt{n}} \sim t_{n-1}$$

*Where $s_d$ is the standard deviation of the differences $d_i$.*

### Decision Rules & Rejection Regions
The rejection region is defined by the critical value(s) $t_{\text{crit}}$ and the significance level $\alpha$.

| Test Type        | Alternative ($H_1$) | Rejection Rule (Reject $H_0$ if...) | P-Value Calculation                           |
| :--------------- | :------------------ | :---------------------------------- | :-------------------------------------------- |
| **Two-Tailed**   | $\mu_d \neq 0$      | $\lvert t \rvert>t_{\alpha/2, n-1}$ | $2 \times P(t >\lvert t_{\text{calc}}\rvert)$ |
| **Left-Tailed**  | $\mu_d < 0$         | $t < -t_{\alpha, n-1}$              | $P(t < t_{\text{calc}})$                      |
| **Right-Tailed** | $\mu_d > 0$         | $t > t_{\alpha, n-1}$               | $P(t > t_{\text{calc}})$                      |

---

> [!example]-
> A group of 10 basketball players test their max vertical jumps before and after a training program. Based on the below data, is the evidence at $\alpha=0.1$ that their jump heights improved by more than 2 inches.
> 
> | Player | Jump Height Before (in) | Jump Height After (in) | Difference |
> | ------ | ----------------------- | ---------------------- | ---------- |
> | 1      | 22                      | 26                     | 4          |
> | 2      | 20                      | 24                     | 4          |
> | 3      | 19                      | 21                     | 2          |
> | 4      | 24                      | 24                     | 0          |
> | 5      | 25                      | 28                     | 3          |
> | 6      | 28                      | 30                     | 2          |
> | 7      | 22                      | 26                     | 4          |
> | 8      | 30                      | 32                     | 2          |
> | 9      | 27                      | 31                     | 4          |
> | 10     | 27                      | 28                     | 1          |
> Sample Difference Stats:
> * $\bar d=2.6$ 
> * $s_d=1.43$
> 
> Hypotheses:
> $$\mu_d \leq2$$$$\mu_d >2$$
> This is an **upper-tailed test**
> 
> Test Statistic:
> $$t = \frac{\bar{d} - \Delta_0}{s_d/\sqrt{n}} = \frac{2.6 - 2}{1.43/\sqrt{10}}=1.327$$
> Using a t Distribution with $n-1=9$ degrees of freedom $t_9$, this leads to a p-value of:
> $$p = P(t>1.327) = 0.109$$
> $p > \alpha$ so the null hypothesis cannot be rejected, meaning there is not sufficient evidence to suggest that the training program increased player's max jump height by more than 2 inches.![[paired_mean_test_example.svg]]
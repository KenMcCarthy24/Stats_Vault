A hypothesis test is a statistical procedure used to decide if a sample of data supports a **hypothesis** about the population. Every hypothesis test consists of two competing claims:

* **Null Hypothesis ($H_0$):** The default or previously assumed hypothesis (often representing "no effect" or "status quo").
* **Alternative Hypothesis ($H_1$):** The claim being tested for (often representing "an effect" or "change").

Let $\Theta$ be the full space of all possible parameter values that define the population. This space is separated into two disjoint subsets, $\Theta_0$ and $\Theta_1$, such that $\Theta_0 \cup \Theta_1 = \Theta$ and $\Theta_0 \cap \Theta_1 = \emptyset$. The hypotheses are defined as:
* $H_0: \theta \in \Theta_0$
* $H_1: \theta \in \Theta_1$

**Example:** Testing if the population mean $\mu$ is significantly different from 0.
* $H_0: \mu = 0$
* $H_1: \mu \neq 0$

### Simple vs. Composite Hypotheses
A hypothesis is called **Simple** if it fully defines the population [[Probability Distribution]], specifying all parameters. If a hypothesis leaves any parameters unspecified or allows for a range of values, it is called **Composite**.

* $\mu = 50$: If the variance is known, this is a simple hypothesis. If the variance is unknown, this is composite (because $\sigma^2$ is unspecified).
* $\mu > 50$: This is a composite hypothesis, as it covers a range that does not fully specify $\mu$.

### Conclusions
There are only two possible conclusions at the end of a hypothesis test:

1.  **Reject the Null Hypothesis ($H_0$):**
    * The data provides sufficient evidence to suggest that the null hypothesis is false.
2.  **Fail to Reject the Null Hypothesis ($H_0$):**
    * The data does *not* provide sufficient evidence to suggest that the null hypothesis is false.
    * **Note:** This is *not* the same as accepting the null hypothesis as true; it simply means it has not been proven false.

A well designed hypothesis test should minimize the chance of a false positive (Type I Error) while the chance of a true positive (Power). See: [[Errors in Hypothesis Testing]] and [[Power of a Test]]

---

## Procedure
Below is the general procedure followed for conducting a hypothesis test.

1.  **Define Hypotheses:** Set up the null hypothesis $H_0$ and the alternate hypothesis $H_1$.
2.  **Set Significance Level ($\alpha$):** Set the probability of rejecting the null hypothesis when, in reality, it was true. This is known as a [[Errors in Hypothesis Testing#Type I Error|Type I Error]].
    $$\alpha = P(\text{Type I Error}) = P(\text{Reject } H_0 \mid H_0 \text{ is true})$$
3.  **Calculate Test Statistic ($t$):** This is a numerical quantity with two important properties:
    * It is a function of the data that quantifies how well the data fits the null hypothesis.
    * It has a known and calculable distribution $T$, such as [[Student-t]], [[Normal]], or [[Chi-Squared]].
    * Note: Many test statistics have assumptions baked in that make the test invalid if they are not met, so they must be checked. (e.g., high sample size, normality, independence)
4.  **Determine Tails:** Identify the direction of the test based on $H_1$:
    * **Right-tailed test:** $H_1: \theta > \theta_0$ (Testing if the parameter is greater than a value).
    * **Left-tailed test:** $H_1: \theta < \theta_0$ (Testing if the parameter is less than a value).
    * **Two-tailed test:** $H_1: \theta \neq \theta_0$ (Testing if the parameter is different in either direction).

From here, there are two equivalent methods for reaching a conclusion.

### 1. Critical Value Method
![[critical_values_plot.svg]]
Based on the level of significance $\alpha$ and the sampling distribution of the test statistic, calculate **critical value(s)**. These values separate the distribution into an **acceptance region** (fail to reject) and a **rejection region**.

* If $t$ lies within the rejection region, **Reject $H_0$**.
* If $t$ lies within the acceptance region, **Fail to Reject $H_0$**.

**Rejection Region Locations:**
* **Right-tailed:** To the right of the critical value.
* **Left-tailed:** To the left of the critical value.
* **Two-tailed:** Split between the high and low tails, bounded by two critical values.

### 2. P-Value Method
![[p_values_plot.svg]]
Calculate the **p-value** ($p$) based on the observed test statistic $t$. This is the probability of obtaining a test statistic at least as extreme as the one observed, assuming the null hypothesis is true.

* If $p \le \alpha$, **Reject $H_0$** (Statistically significant).
* If $p > \alpha$, **Fail to Reject $H_0$** (Not statistically significant).

**Calculating $p$:**
* **Right-tailed:** Area to the right of the statistic.
    $$p = P(T > t)$$
* **Left-tailed:** Area to the left of the statistic.
    $$p = P(T < t)$$
* **Two-tailed:** The sum of the area in the observed tail and the corresponding area in the opposite tail.
    $$p = 2 \cdot \min(P(T \ge t), P(T \le t))$$
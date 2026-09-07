Given a single categorical variable with $k$ categories (or bins) and a set of observed counts $O_1, \dots, O_k$, inferences about whether the data follows a specific theoretical distribution are evaluated using a [[Hypothesis Test]] structured as:

$$
\begin{aligned}
H_0: & \quad \text{The data follows the specified distribution} \\
     & \quad (p_1 = p_{1_0}, p_2 = p_{2_0}, \dots, p_k = p_{k_0}) \\
H_1: & \quad \text{The data does not follow the specified distribution} \\
     & \quad (\text{At least one } p_i \text{ differs from the expected value})
\end{aligned}
$$

The estimator used is the comparison between the **Observed Counts ($O$)** and the **Expected Counts ($E$)**.
$$E_i = n \times p_{i_0}$$
*Where $n$ is the total sample size and $p_{i_0}$ is the hypothesized proportion for category $i$.*

---

## Chi-Square Goodness of Fit Test

**Conditions:**
1. **Random Sample**: The data comes from a random sample.
2. **Counted Data**: The data consists of counts (frequencies) for categorical variables.
3. **Large Counts**: All **expected counts** must be at least 5 ($E_i \ge 5$).

> [!warning]
> If any expected count is less than 5, categories should be combined (binned) to satisfy the condition, or the results may be invalid.

**Test Statistic:**
The test statistic follows a [[Chi-Squared]] distribution so this is a [[Chi-Squared Test]].

$$\chi^2 = \sum_{i=1}^k \frac{(O_i - E_i)^2}{E_i} \sim \chi^2_{df}$$

[[Degrees of Freedom]] ($df$):
$$df = k - 1 - m$$
*Where $k$ is the number of categories and $m$ is the number of parameters estimated from the sample data to calculate the expected counts (often $m=0$, so $df=k-1$).*

### Decision Rules & Rejection Regions
The Goodness of Fit test is **always upper-tailed**. A $\chi^2$ value close to 0 indicates a perfect fit, while a large $\chi^2$ value indicates a large discrepancy between Observed and Expected counts.

The rejection region is defined by the critical value $\chi^2_{\alpha}$.

**Rejection Rule (Reject $H_0$ if...)**
* $\chi^2 > \chi^2_{\alpha, df}$
  
**P-Value Calculation**
* $P(\chi^2 > \chi^2_{\text{calc}})$

where $\chi^2_{calc}$ is the calculated test statistic.

> [!NOTE]
> There is no "two-tailed" or "left-tailed" version of this test. A significantly low $\chi^2$ value (left tail) usually implies data fabrication or error, not a specific alternative hypothesis.

---

> [!example]- Example 1
> A 6 sided die is rolled 60 times and the following frequencies of roll are recorded:
> 
> | **Roll**     | 1   | 2   | 3   | 4   | 5   | 6   |
> | ------------ | --- | --- | --- | --- | --- | --- |
> | **Observed** | 10  | 15  | 6   | 8   | 13  | 8   |
> Perform a goodness of fit test at $\alpha=0.05$ to determine there is evidence that the die is unfair. In other words, does the data follow a [[Discrete Uniform]] distribution $U(1, 6)$
> 
> Hypotheses:
> $$H_0: \text{Data Follows } U(1, 6)$$
> $$H_1: \text{Data Doesn't Follow } U(1, 6)$$
> 
> For $n=60$ roles a fair die would be expected to roll 10 of each number so for each roll $E=10$.
> 
> $O=[10, 15, 6, 8, 13, 8]$
> $E=[10, 10, 10, 10, 10, 10]$
> 
> Test Statistic:
> $$\chi^2 = \sum_{i=1}^k \frac{(O_i - E_i)^2}{E_i} = 5.8$$
> Degrees of Freedom:
> * No parameters were estimated from sample data so $m=0$
> * $df = k-1-m = 6-1-0=5$
> 
> Using a Chi-Squared Distribution with 5 degrees of freedom $\chi^2_{5}$, this leads to a p-value of:
> $$p = P(\chi^2>5.8) = 0.326$$
> $p>\alpha$ so the null hypothesis cannot be rejected. There is not statistical evidence that this die is unfair. 
> ![[goodness_of_fit_test_example1.svg]]

> [!example]- Example 2
> A call center monitors the number of emergency calls received per hour over a 100-hour period. Based on the below observed data, does a goodness of fit test suggest the data doesn't follow a [[Poisson]] distribution at $\alpha=0.05$
> 
> | Number of Calls ($x$) | Observed Frequency ($O_i$) |
> | :-------------------- | :------------------------- |
> | 0                     | 15                         |
> | 1                     | 30                         |
> | 2                     | 25                         |
> | 3                     | 20                         |
> | 4 or more             | 10                         |
> | **Total**             | **$n = 100$**              |
> Hypotheses:
> $$H_0: \text{Data Follows Poisson}(\lambda)$$
> $$H_1: \text{Data Doesn't Follow Poisson}(\lambda)$$
> First need an estimator for the Poisson parameter $\lambda$. Will use the [[Maximum Likelihood Estimation|maximum likelihood estimator]] which is just the sample mean so:
> $$\hat \lambda=\bar X = \frac{1}{n}\sum_i(x_iO_i)=1.8$$
> Estimating this parameter consumed a degree of freedom so $m=1$
> 
> Using Poisson($\lambda=1.8$), the expected frequencies can be added to the table as just $n$ multiplies the probability of each number under that poisson distribution.
> 
> | Number of Calls ($x$) | Observed Frequency ($O_i$) | Expected Frequency ($E_i$) |
> | :-------------------- | :------------------------- | -------------------------- |
> | 0                     | 15                         | 16.53                      |
> | 1                     | 30                         | 29.75                      |
> | 2                     | 25                         | 26.78                      |
> | 3                     | 20                         | 16.07                      |
> | 4 or more             | 10                         | 10.87                      |
> Test Statistic:
> $$\chi^2 = \sum_{i=1}^k \frac{(O_i - E_i)^2}{E_i} = 1.29$$
>  Degrees of Freedom:
> * $m=1$ because of the estimation of $\hat \lambda$
> * $df=k-1-m = 5-1-1 = 3$ 
> 
> Using a Chi-Squared Distribution with 3 degrees of freedom $\chi^2_{3}$, this leads to a p-value of:
> $$p = P(\chi^2>1.29) = 0.73$$
> $p>\alpha$ so the null hypothesis cannot be rejected meaning that there is not sufficient evidence to suggest that this data does not come from a Poisson distribution.
> ![[goodness_of_fit_test_example2.svg]]


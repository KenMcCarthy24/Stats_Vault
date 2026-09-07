The **F-Test** refers to any [[Hypothesis Test]] where the test statistic $F$ follows an [[F-distribution]] under the null hypothesis $H_0$.

$$F \sim F_{\nu_1, \nu_2}$$
*(where $\nu_1$ and $\nu_2$ are degrees of freedom for the numerator and denominator, respectively)*

It is primarily used to compare two variances (ratios of variances). 

## Assumptions

* **Independence:** The samples drawn from the populations must be independent of one another.
* **Normality:** The populations from which the samples are drawn must be normally distributed. This test is highly sensitive to non-normality.

## Test Statistic
The $F$ statistic is a ratio of two variances (or mean squares).

$$F = \frac{\text{Variance 1}}{\text{Variance 2}}$$

**Where:**
* **Numerator:** Represents the variance explained by the model or the larger variance in a comparison.
* **Denominator:** Represents the unexplained or error variance (the smaller variance in a simple comparison).
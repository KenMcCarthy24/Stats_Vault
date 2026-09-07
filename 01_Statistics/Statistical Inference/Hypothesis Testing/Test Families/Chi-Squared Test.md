The **Chi-Squared Test** refers to a class of [[Hypothesis Test]] where the test statistic $\chi^2$ follows a [[Chi-Squared]] distribution under the null hypothesis $H_0$.

$$\chi^2 \sim \chi^2_{k}$$
where $k$=[[Degrees of Freedom]]

These tests are non-parametric and generally used to analyze categorical data or to test hypotheses regarding a single population variance.
## Assumptions

* **Random Sampling:** Data must come from a random selection.
* **Independence:** Observations must be independent.
* **Sample Size (Expected Frequencies):** For categorical tests, the expected frequency in each category or cell should be sufficiently large (usually $\ge 5$).
* **Normality (for Variance tests):** When testing population variance, the parent population must be strictly normal.

## Test Statistic
While the specific formula varies by application, the general principle involves comparing observed values against expected values.

$$\chi^2 = \sum \frac{(\text{Observed} - \text{Expected})^2}{\text{Expected}}$$

**Where:**
* **Observed:** The actual count  measured in the sample.
* **Expected:** The theoretical count predicted by the null hypothesis.
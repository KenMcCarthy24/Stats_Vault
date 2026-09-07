
Standardization is the process of rescaling data to have a mean of 0 and a standard deviation of 1. This allows for the comparison of scores from different distributions. 

### The Z-Score Formula
The **Z-score** (or **standard score**) represents the number of standard deviations a specific data point $x$ is away from the mean.

$$Z = \frac{x - \mu}{\sigma}$$

Where:
* $x$ = The individual data point (raw score).
* $\mu$ = The population mean.
* $\sigma$ = The population standard deviation.

The formula above uses population parameters $\mu,\sigma$ which are rarely used in practice. When working with a data sample, these are replaced by the [[Sample Mean]] $\bar{X}$ and [[Sample Variance and Standard Deviation| Sample Standard Deviation]] $s$
$$Z = \frac{x-\bar{X}}{s}$$
### Key Properties of Standardized Data
* **Centered at Zero:** The mean of a standardized distribution is always 0 ($\mu_z = 0$).
* **Unit Variance:** The standard deviation is always 1 ($\sigma_z = 1$).
* **Shape Retention:** Standardization does **not** change the shape of the distribution. If the original data is skewed, the standardized data will remain skewed. It only shifts and scales the axis.

### Why Standardize?
1.  **Comparability:** It puts different variables on the same scale ("Apples to Apples").
2.  **Outlier Detection:** Z-scores give a quick heuristic for identifying outliers.
    * $|Z| > 2$: Unusual (roughly outside 95% of data in a normal distribution).
    * $|Z| > 3$: Highly unusual outlier (roughly outside 99.7% of data).
3.  **Probability Calculation:** It is a required step to use the Standard Normal Table (Z-table) or software to find probabilities for specific values.
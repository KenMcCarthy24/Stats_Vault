For a sample of observations $\{x_1, x_2, \dots, x_n\}$ with [[Sample Mean|sample mean]] $\bar{X}$, the **sample variance** measures the dispersion or spread of the data points around the mean.

There are two common [[Estimators]] for the population variance $\sigma^2$: the biased estimator and the unbiased estimator.

### Biased Sample Variance
The **biased sample variance**($\hat{\sigma}^2$), is defined as the [[Means and Averages of Data#Arithmetic Mean|arithmetic mean]] of the squared deviations from the sample mean:

$$\hat{\sigma}^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{X})^2$$

It is a **[[Bias#Example Bias of Sample Variance $ hat{ sigma} 2$|biased estimator]]** because it tends to underestimate the true population variance, especially in small samples:

$$\mathbb{E}[\hat{\sigma}^2] < \sigma^2$$

### Unbiased Sample Variance
To correct for the bias, the **unbiased sample variance**, denoted as $s^2$, uses **Bessel's Correction** by dividing by $n-1$ instead of $n$:

$$s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{X})^2$$

This version is the standard definition used in inferential statistics because it is an **[[Estimators|unbiased estimator]]** for the population variance:

$$\mathbb{E}[s^2] = \sigma^2$$

### Why $n-1$?
The intuition for using $n-1$ instead of $n$ comes from **[[Degrees of Freedom]]**.
* In the calculation of variance, we must first calculate the sample mean $\bar{X}$.
* Once $\bar{X}$ is determined, the $n$ observations are no longer independent. If you know $n-1$ of the values and the mean, the final value is determined automatically.
* Therefore, one degree of freedom is "lost" or "used up" to estimate the mean, leaving $n-1$ independent pieces of information to estimate the spread.

#### When to use which?
* **Use Unbiased ($s^2$):** When you are using a sample to estimate the variance of a larger population (inferential statistics).
* **Use Biased ($\hat{\sigma}^2$):** When the dataset *is* the entire population (descriptive statistics).

#### Computational note:
* **Numpy**: `np.var` and `np.std` calculate the biased variance by default. The unbiased variance can be calculated by setting `ddof=1`
* **Pandas**: `df.var` and `df.std` return the unbiased variance by default. 
* **R**: `var` and `sd` calculate the unbiased variance by default

---
# Sample Standard Deviation

The **sample standard deviation** is the square root of the sample variance. It brings the measure of spread back to the original units of the data.

Depending on which variance definition is used, the standard deviation is denoted as either $\hat{\sigma}$ (biased) or $s$ (unbiased):

$$s = \sqrt{s^2} = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{X})^2}$$
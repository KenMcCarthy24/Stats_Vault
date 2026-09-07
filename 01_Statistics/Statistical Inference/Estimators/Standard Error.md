The **Standard Error (SE)** of an [[Estimators|estimator]] is the standard deviation of its sampling distribution. While the standard deviation measures the dispersion of individual data points in a population, the standard error measures the **precision** and **variability** of a statistic (like a mean or proportion) across multiple samples.

It measures how much the estimate is expected to "fluctuate" if you were to repeat the experiment many times.

> [!NOTE]
> The Standard Error assumes that the samples are independent and identically distributed (i.i.d.).

## Standard Deviation vs. Standard Error
These are commonly confused:

| Feature     | [[Expectation and Moments#2nd Central Moment Variance\|Standard Deviation]] ($s$ or $\sigma$) | Standard Error ($SE$)                                |
| :---------- | :-------------------------------------------------------------------------------------------- | :--------------------------------------------------- |
| **Focus**   | Individual observations.                                                                      | The estimator (e.g., the sample mean).               |
| **Purpose** | Describes the spread of data in a population/sample.                                          | Describes the uncertainty of a calculated statistic. |
| **Formula** | $\sigma = \sqrt{\frac{\sum (x_i - \mu)^2}{N}}$                                                | $SE = \frac{\sigma}{\sqrt{n}}$                       |

## The Standard Error of the Mean
The most common application is the Standard Error of the Mean. As the sample size $n$ increases, the standard error decreases, meaning the estimate becomes more precise.

For a population with standard deviation $\sigma$:

$$SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$$

If the population standard deviation is unknown (which is usually the case) use the [[Sample Variance and Standard Deviation#Sample Standard Deviation|sample standard deviation]] ($s$):

$$SE_{\bar{x}} \approx \frac{s}{\sqrt{n}}$$

## Key Properties
* **Inverse Relationship with $n$:** To cut the standard error in half, the sample size must be **quadrupled**
* **Direct Relationship with Variability:** If the underlying population is very "noisy" (high $\sigma$), the standard error will also be higher.
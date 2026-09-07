**Bootstrapping** is a statistical tool for estimating the sampling distribution of an [[Estimators|estimator]] based only on a single sample of data taken from a larger population. It is highly useful when it is impossible or impractical to obtain multiple different samples of data, and is particularly valuable for statistics that lack easy standard error formulas (such as the median, ratios, or correlation coefficients).

A common practical application of the bootstrap sampling distribution is calculating confidence intervals. For example, an approximate 95% confidence interval can be found simply by taking the 2.5th and 97.5th percentiles of the $B$ bootstrap estimates.

There are two primary methods of bootstrapping: **Non-Parametric** and **Parametric**.

---
# Non-Parametric Bootstrapping
This is the standard, most common form of bootstrapping. It makes no assumptions about the underlying probability distribution of the data, and instead relies on resampling directly from the observed data points.

To estimate the sampling distribution of a population parameter $\theta$ based on a sample of data $X$ of size $n$:
1. **Resample With Replacement**: Randomly draw $n$ observations from the original sample to create a new "bootstrap sample" $X^B$. This drawing must be done *with replacement*, meaning a data point from the original sample may appear multiple times in the bootstrap sample.
2. **Calculate Estimator**: Compute the estimator $\hat{\theta}$ based on the bootstrap sample $X^B$.
3. **Repeat**: Repeat steps 1 and 2 $B$ times. $B$ is often a very large number such as 1,000 or 10,000.
4. **Build the Distribution**: The distribution of the $B$ estimates of $\theta$ will form the **bootstrap sampling distribution**, which is an approximation of the true sampling distribution of $\theta$.

**Pros:**
* **No Distribution Assumption**: Conceptually distribution-free, meaning it does not require the data to follow a normal (or any specific) curve.
* **Simplicity**: Straightforward to implement, avoiding complex mathematical derivations for difficult estimators.
* **Sample Efficiency**: Enables rigorous analysis with smaller sample sizes.

**Cons:**
* **Computationally Intensive**: Requires creating thousands of resamples, which can be slow for massive datasets.
* **Dependency on Sample Quality**: If the original sample is not representative of the population, the bootstrap estimates will inherently be biased.
* **Time Series Issues**: Does not work well for time series data or any other data with high dependency and autocorrelation without specialized modifications (like block bootstrapping).

---

# Parametric Bootstrapping
In this approach, instead of resampling directly from the original data points, fit a probability distribution to the data and draw simulated samples from that theoretical model.

To estimate the sampling distribution of a population parameter $\theta$ based on a sample of data $X$ of size $n$:
1. **Fit a Model**: Assume a specific probability distribution for the data (e.g., Normal, Poisson, Exponential) and estimate its parameters using the original sample $X$.
2. **Simulate Data**: Generate a new sample of size $n$, denoted $X^B$, by drawing randomly from the fitted theoretical distribution. 
3. **Calculate Estimator**: Compute the estimator $\hat{\theta}$ based on the simulated sample $X^B$.
4. **Repeat and Build**: Repeat steps 2 and 3 $B$ times to form the bootstrap sampling distribution.

**Pros:**
* **Higher Precision**: If the assumed distribution is correct, parametric bootstrapping is generally more statistically efficient and precise than the non-parametric method.
* **Explores Unseen Values**: Because it draws from a continuous theoretical distribution, it can generate data points that were never actually observed in the original sample.

**Cons:**
* **Risk of Misspecification**: Heavily relies on the assumption that the chosen probability distribution accurately reflects the true population. If the wrong distribution is chosen, the resulting estimates will be highly inaccurate.
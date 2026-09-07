The Central Limit Theorem (CLT) states that the sampling distribution of the [[Sample Mean]] $\bar{X}$ will approach a [[Normal]] distribution as the sample size $n$ increases, regardless of the population's original distribution.

Given a population with mean $\mu$ and standard deviation $\sigma$, for sufficiently high $n$ (rule of thumb $~n \geq 30$):
$$\bar{X} \sim N(\mu, 
\frac{\sigma^2}{n})$$

Implications:
* Even if the source distribution is skewed or uniform, the averages of samples drawn from that data will form a normal distribution.
* As $n$ increases, the resulting variance decreases. This means larger samples provide more precise estimates of the population mean.
* The CLT allows  Normal Distribution properties to be used to make inferences about a population mean, even when the population is not normally distributed.
* Because the sampling distribution of $\bar{X}$ is approximately normal, the CLT implies that the [[Standardization|standardized]] version of the sample mean (the **Z-statistic**), will follow a standard normal as $n$ increases
	* $\displaystyle Z=\frac{\bar{X}-\mu}{\sigma\sqrt{n}} \sim N(0, 1)$

Assumptions:
* **Random Sampling:** Samples must be drawn randomly.
* **Independence:** Each sample should be independent (if sampling without replacement, the population size should be at least 10x the sample size).
* **Sample Size:** Generally, $n \geq 30$ is required for the approximation to be valid, though distributions that are already close to normal may require fewer.
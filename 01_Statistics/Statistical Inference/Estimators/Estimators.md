An estimator is a rule or formula used to calculate an estimate of a given population based on observed data when performing [[Statistical Inference]]

# Definitions
* **Parameter $(\theta)$**: A numerical characteristic of a population to be estimated (e.g., the true population mean $\mu$)
* **Sample Data (X)**: A set of $n$ iid data samples $[x_1, x_2, \dots, x_n]$ collected from the population.
* **Estimator $(\hat{\theta})$**: A function of the sample data used to guess a parameter. It is a [[Random Variable]] that follows a sampling distribution.
* **Estimate**: The specific numerical value obtained by plugging data into an estimator

# Common Estimators
When population parameters are unknown, these estimators are commonly used to create estimates for the true mean $\mu$ and variance $\sigma^2$ of the population.

* Sample Mean ($\bar{X}$)
	* $\displaystyle \hat{\mu} = \bar{X} = \frac{1}{n}\sum_{i=1}^n x_i$
	* Law of Large Numbers states that as $n \rightarrow \infty$, $\bar{X} \rightarrow \mu$
* Sample variance ($s^2$)
	* $\displaystyle S^2=\frac{1}{n-1}\sum_{i=1}^n(x_i - \bar{X})^2$

# Desirable Properties of Estimators
There are several properties that is is good for estimators to have for them to be effective in estimating the true population parameter
* **[[Bias|Unbiasedness]]**: The expected value of the estimator is equal to the parameter ($E[\hat{\theta}] = \theta$)
* **Consistency**: As sample size increases, the estimator gets closer to the parameter
* **[[Estimator Efficiency|Efficiency]]**: Among all unbiased estimators, the one with the lowest variance is the most efficient.
* **Sufficiency**: The estimator uses all the information about the parameter contained in the data.
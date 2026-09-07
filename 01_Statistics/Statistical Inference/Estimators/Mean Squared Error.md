The Mean Squared Error (MSE) of an [[Estimators|estimator]] is a measure of the quality of that estimator. It is defined as the [[Expectation and Moments#1st Raw Moment Expectation Value|expectation value]] of the squared error of the estimator $\hat{\theta}$ against the true parameter $\theta$:
$$MSE(\hat{\theta}) = E[(\hat{\theta}-\theta)^2]$$
which is equivalent the sum of the [[Expectation and Moments#2nd Central Moment Variance|variance]] and the square of the [[Bias|bias]] of the estimator.
$$MSE(\hat{\theta}) = Var(\hat{\theta}) + (\text{Bias}(\hat{\theta}))^2$$
For an unbiased estimator ($\hat{\theta} = \theta$), the MSE is just equal to the variance.

## Bias-Variance Tradeoff
The decomposition of MSE illustrates the [[Bias-Variance Tradeoff]], a central concept in [[Machine Learning]].

> [!Note]
> In machine learning contexts, the estimator is not for a single parameter $\theta$, but for an entire function $f(x)$. So the MSE looks like:
> $$MSE(\hat f) = E[(\hat f(x) - f(x))^2]$$


The MSE is the sum of the variance and the squared bias, minimizing the error requires balancing these two sources of error.

There is often a conflict between these two terms. Modifications that reduce the bias of an estimator $\hat{\theta}$ often increase its variance, and vice versa. 

* **Low Bias / High Variance:** The estimator is accurate on average but sensitive to random noise in the sample.
* **High Bias / Low Variance:** The estimator is stable across different samples but systematically deviates from the true parameter $\theta$.

The optimal estimator is not necessarily one that is unbiased, but one that minimizes the total MSE by finding the optimal balance between variance and bias.
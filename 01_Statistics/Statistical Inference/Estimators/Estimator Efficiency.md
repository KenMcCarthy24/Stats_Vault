Efficiency is a measure of quality of an [[Estimators|estimator]], referring to how much variance an estimator has. 
* A more efficient estimator has a **smaller variance** (it is more precise).
* If an estimator is unbiased, the most efficient estimator is the one with the smallest possible variance.

## Cramér-Rao Lower Bound (CRLB)
The **Cramér-Rao Lower Bound** states that the variance of any unbiased estimator $\hat{\theta}$ of a parameter $\theta$ is bounded, meaning a lower variance cannot be achieved. 

$$Var(\hat{\theta}) \geq \frac{1}{I(\theta)}$$

Where:
* $Var(\hat{\theta})$ is the variance of the estimator.
* $I(\theta)$ is the [[Fisher Information]] number (a measure of how much information the data carries about the unknown parameter).

## Efficiency Equation
The efficiency $e(\hat{\theta})$ of an unbiased estimator $\hat{\theta}$ is defined as the ratio of the Cramér-Rao Lower Bound to the actual variance of the estimator.

$$e(\hat{\theta}) = \frac{\text{CRLB}(\theta)}{Var(\hat{\theta})} = \frac{1}{I(\theta) \cdot Var(\hat{\theta})}$$

* The value of $e(\hat{\theta})$ is always between 0 and 1.
* If $e(\hat{\theta}) = 1$, the estimator is called **Efficient** (or Minimum Variance Unbiased Estimator). It has achieved the theoretical best precision.

## Relative Efficiency
Relative efficiency compares the variances of two different unbiased estimators, $\hat{\theta}_1$ and $\hat{\theta}_2$, for the same parameter.

$$\text{RelEff}(\hat{\theta}_1, \hat{\theta}_2) = \frac{Var(\hat{\theta}_2)}{Var(\hat{\theta}_1)}$$

* If $\text{RelEff} > 1$, then $Var(\hat{\theta}_2) > Var(\hat{\theta}_1)$, meaning $\hat{\theta}_1$ is the more efficient estimator.
* If $\text{RelEff} < 1$, then $\hat{\theta}_2$ is more efficient.

## Asymptotic Efficiency
An estimator is **asymptotically efficient** if it becomes efficient as $n \rightarrow \infty$

Formally, an estimator $\hat{\theta}_n$ is asymptotically efficient if:
1.  It is asymptotically unbiased.
2.  Its efficiency approaches 1 as $n \to \infty$:

$$\lim_{n \to \infty} e(\hat{\theta}_n) = 1$$

Many [[Maximum Likelihood Estimation|Maximum Likelihood Estimators]] possess this property, making them the standard choice for large datasets.
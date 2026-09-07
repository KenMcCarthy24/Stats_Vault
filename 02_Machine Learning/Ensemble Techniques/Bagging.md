**Bagging** or **Bootstrap Aggregation** is an ensemble [[Machine Learning]] technique for reducing [[Bias-Variance Tradeoff|variance]] of models by training many models in parallel on [[Bootstrapping|bootstrap]] samples of the original dataset and aggregating their predictions.

Bagging benefits unstable models where small data perturbations cause large prediction changes such as [[Decision Trees]], but tends not to benefit more stable models. This is largely due to bagging reducing variance but not bias.  

If the true function being estimated by the model is $f(x)$, bagging involves training $B$ different models $(\hat f_1(x), \hat f_2(x),\dots, \hat f_B(x))$, each trained on a bootstrap sample drawn from the original training set. If the original training dataset has $n$ points, each bootstrapped training set is obtained by randomly sampling $n$ points from the original training set with replacement. The model is then trained on the $i$-th training set in order to get $\hat f_i(x)$.

The results of these $B$ models are then aggregated together in order to produce the bagging model's prediction 
* For regression, the $B$ model outputs form a distribution of predictions at each $x$, reflecting the model's sensitivity to different bootstrap samples.
	* The bagging model's output is the mean of this distribution$$\hat f_{bagg}(x) = \frac{1}{B} \sum_{i=1}^B \hat f_i(x)$$
	* The standard deviation of the $B$ predictions can be used as a rough measure of the prediction uncertainty or ensemble disagreement at $x$:
	  $$\hat \sigma(x) = \sqrt{\frac{\sum_{i=1}^B (\hat f_i(x) - \hat f_{bagg}(x))^2}{B-1}}$$
* For classification models, the $B$ models do a majority vote to determine the output.
  $$\hat f_{bagg}(x) = \arg \max_k\left[\sum_{i=1}^B1(\hat f_i(x) = k)\right]$$
  where $1(\cdot)$ is an indicator function that equals 1 when the condition is true and 0 otherwise.
## Out-of-Bag Error

Because each bootstrap sample is drawn with replacement from the original $n$ training points, any given observation has a chance of being left out of a particular bootstrap sample. On average, each bootstrap sample omits roughly **37%** of the original training data. These omitted points are called **out-of-bag (OOB)** samples for that model.

This gives bagging a built-in way to estimate test error without needing a separate [[Data Splitting#The Train-Validation-Test Split|validation set]] or [[Cross Validation]]:

1. For each training point $x_i$, identify the subset of models $\{\hat f_b : x_i \notin \text{bootstrap sample } b\}$ that did *not* see $x_i$ during training. Call this set $B_i$.
2. Aggregate predictions from only those models to produce an OOB prediction for $x_i$:
$$\hat f_{oob}(x_i) = \frac{1}{|B_i|} \sum_{b \in B_i} \hat f_b(x_i)$$
(or a majority vote, for classification).
3. Compare $\hat f_{oob}(x_i)$ to the true $y_i$ across all training points to compute the **OOB error**:
$$\text{OOB Error} = \frac{1}{n}\sum_{i=1}^n L(y_i, \hat f_{oob}(x_i))$$
where $L$ is an appropriate loss function (squared error for regression, 0-1 loss for classification).

Since each $\hat f_{oob}(x_i)$ is produced by models that never saw $x_i$, the OOB error is a nearly unbiased estimate of the test error — effectively free validation, computed as a byproduct of training. For large $B$, it closely approximates [[Cross Validation#Leave-One-Out Cross Validation (LOOCV)|leave-one-out cross-validation]] error but at a fraction of the computational cost.

> [!note]- Why does each bootstrap sample leave out ~37% of the data?
> Consider a single training point $x_i$ and a bootstrap sample of size $n$ drawn with replacement from the original $n$ points.
> 
> On any single draw, the probability that $x_i$ is *not* selected is:
> $$P(\text{not picked on one draw}) = 1 - \frac{1}{n}$$
> 
> Since the $n$ draws are independent, the probability that $x_i$ is not picked in *any* of the $n$ draws is:
> $$P(x_i \notin \text{bootstrap sample}) = \left(1 - \frac{1}{n}\right)^n$$
> 
> Taking the limit as $n \to \infty$:
> $$\lim_{n \to \infty} \left(1 - \frac{1}{n}\right)^n = \frac{1}{e} \approx 0.368$$
> 
> So roughly **36.8%** of the original training points are expected to be missing from any given bootstrap sample, and equivalently, each point is OOB for about 37% of the $B$ models.
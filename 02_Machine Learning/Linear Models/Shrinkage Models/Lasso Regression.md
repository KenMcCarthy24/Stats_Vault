
**Lasso Regression** (or **L1 Regularization**) is a [[Shrinkage Models|shrinkage method]] and regularization technique used to help prevent overfitting in linear models. It works by adding a new penalty term to the loss function to constrain the values of the linear coefficients.

While standard [[Ordinary Least Squares (OLS)]] optimizes coefficients by minimizing just the [[Goodness of Fit#Residual Sum of Squares (RSS)|Residual Sum of Squares]] (RSS), Lasso Regression adds a regularization term to be minimized alongside it. 

> [!WARNING] Standardizing Data
> Lasso Regression performs best when the data is standardized before processing, transforming it to zero mean and unit standard deviation. This ensures that independent variables are on the same scale and prevents larger magnitude coefficients from dominating the regularization.

## The Loss Function
In Lasso Regression, the coefficients $\hat \beta^L$ are obtained by minimizing the RSS plus the scaled L1 Norm of the coefficients, excluding the intercept term $\beta_0$:
$$\hat \beta^L = \min_\beta\left[RSS + \lambda\sum_{j=1}^p |\beta_j|\right]$$
where $\lambda \geq 0$ is a tuning parameter used to control the strength of the regularization. $\lambda = 0$ removes the regularization entirely.

> [!NOTE] $\beta_0$ Exclusion
> $\beta_0$ is not included in the regularization term because it needs to remain a measure of the mean value of the response when all inputs are 0. Which, if the predictor variables are centered at zero, evaluates to $\beta_0 = \bar y$. If the predictor variables are standardized, then $\beta_0 = 0$.

Now there are two competing terms in the loss function:
1. The RSS, minimized by making the coefficients fit the data well.
2. The L1 Norm of the coefficients (or shrinkage penalty), which is minimized _when_ a subset of the coefficients are equal to zero and the rest are close to zero.

Unlike OLS or [[Ridge Regression]], this loss formula does not have a closed form analytical solution, so it must be optimized numerically. This is largely due to the sharp edges introduced by the absolute value making it non-differentiable.

## Feature Selection
Like other shrinkage methods, this regularization has the effect of shrinking the estimates $\hat \beta^L$ toward 0 compared to what they would be without regularization. However, using the L1 norm instead of the L2 norm has the added bonus of tending to set some coefficients to *exactly* 0, acting as a built in **feature selection** method. In other words, Lasso Regression yields a **sparse** model that only involves a subset of the features.

## The Bias-Variance Tradeoff
The reason why Lasso Regression is often better than OLS is rooted in the [[Bias-Variance Tradeoff]]. As $\lambda$ increases, the complexity of the model decreases due to being more constrained:
* At $\lambda = 0$, the model reduces to OLS, meaning the bias is zero (OLS is an unbiased estimator) and the variance is maximized.
* Higher $\lambda$ values will have higher bias and lower variance.
* Somewhere in the middle is a sweet spot where bias and variance are balanced and [[Mean Squared Error]] is minimized.

## Geometric Interpretation
Lasso Regression can alternatively be formulated as a constrained optimization problem. Given a budget $t$, Lasso regression solves:
$$\min_\beta(RSS) \text{ s.t. } \sum_{j=1}^p |\beta_j| \leq t$$

> [!NOTE] The Constraint Budget
> The budget $t$ is inversely related to the tuning parameter $\lambda$. As $\lambda$ increases, the allowable budget $t$ shrinks. While they are not the same value, there is a 1-to-1, data-dependent relationship between them.

This formulation leads to an intuitive geometric perspective. The constraint defines a specific boundary in the optimization space that the coefficients cannot exceed. In 2D, this is a diamond with the vertices on the axes. In 3D, it is an octahedron with the vertices on the axes, and in higher dimensions it is a cross-polytope (the higher dimensional generalization of the octahedron).

Meanwhile, the RSS function forms elliptical contours centered around the unconstrained Ordinary Least Squares (OLS) solution. 

If the OLS solution lies outside the constraint region, the Lasso Regression coefficients ($\hat \beta^L$) will be the exact point where the expanding RSS contours first touch the boundary of the constraint region. This visually demonstrates why Lasso shrinks coefficients, and has the tendency to set one or more coefficients to 0:
* The optimal solution is forced to lie within this budget boundary, physically pulling the coefficients closer to zero (the origin) compared to standard OLS.
* In 2D:
	* If the intersection is a vertex, then one of the coefficients will be 0.
	* If the intersection is an edge, then both will be non-zero.
* In 3D:
	* If the intersection is a vertex, then two of the coefficients will be 0.
	* If the intersection is an edge, then one of the coefficients will be 0.
	* If the intersection is a face, then all three will be non-zero.
* In higher dimensions, there are similar relationships with the intersections at different parts of the hypersurface. 

![[lasso_regression_geometry.svg]]

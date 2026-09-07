**Ridge Regression** (or **L2 regularization**) is a [[Shrinkage Models|shrinkage method]] and regularization technique used to help prevent overfitting in linear models. It works by adding a new penalty term to the loss function to constrain the values of the linear coefficients.

While standard [[Ordinary Least Squares (OLS)]] optimizes coefficients by minimizing just the [[Goodness of Fit#Residual Sum of Squares (RSS)|Residual Sum of Squares]] (RSS), Ridge Regression adds a regularization term to be minimized alongside it. 

> [!WARNING] Standardizing Data
> Ridge Regression performs best when the data is standardized before processing, transforming it to zero mean and unit standard deviation. This ensures that independent variables are on the same scale and prevents larger magnitude coefficients from dominating the regularization.

## The Loss Function
In Ridge Regression, the coefficients $\hat \beta^R$ are obtained by minimizing the RSS plus the scaled L2 Norm of the coefficients, excluding the intercept term $\beta_0$:
$$\hat \beta^R = \min_\beta\left[RSS + \lambda\sum_{j=1}^p \beta_j^2\right]$$
where $\lambda \geq 0$ is a tuning parameter used to control the strength of the regularization. $\lambda = 0$ removes the regularization entirely, leaving just the OLS formula.

> [!NOTE] $\beta_0$ Exclusion
> $\beta_0$ is not included in the regularization term because it needs to remain a measure of the mean value of the response when all inputs are 0. Which, if the predictor variables are centered at zero, evaluates to $\beta_0 = \bar y$. If the predictor variables are standardized, then $\beta_0 = 0$.

Now there are two competing terms in the loss function:
1. The RSS, minimized by making the coefficients fit the data well.
2. The L2 Norm of the coefficients (or shrinkage penalty), which is minimized _when_ the coefficients are close to zero.

## Analytical Solution
Luckily, similar to standard OLS, ridge regression has a closed form analytical solution to calculate the optimal coefficient values:
$$\hat \beta^R = (X^TX + \lambda I)^{-1}X^TY$$

> [!NOTE] Collinearity Solution
> A useful side effect of this closed form equation is that the quantity $X^TX + \lambda I$ is invertible even when there is [[Collinearity|Multicollinearity]] present in the data, unlike just $X^TX$ by itself, which is a weakness of OLS.

## The Bias-Variance Tradeoff
The reason Ridge Regression is often better than OLS is rooted in the [[Bias-Variance Tradeoff]]. As $\lambda$ increases, the complexity of the model decreases due to being more constrained:
* At $\lambda = 0$, the model reduces to OLS, meaning the bias is zero (OLS is an unbiased estimator) and the variance is maximized.
* Higher $\lambda$ values will have higher bias and lower variance.
* Somewhere in the middle is a sweet spot where bias and variance are balanced and [[Mean Squared Error]] is minimized.

## Geometric Interpretation
Ridge Regression can alternatively be formulated as a constrained optimization problem. Given a budget $t$, Ridge regression solves:
$$\min_\beta(RSS) \text{ s.t. } \sum_{j=1}^p \beta_j^2 \leq t$$

> [!NOTE] The Constraint Budget
> The budget $t$ is inversely related to the tuning parameter $\lambda$. As $\lambda$ increases, the allowable budget $t$ shrinks. While they are not the same value, there is a 1-to-1, data-dependent relationship between them.

This formulation leads to an intuitive geometric perspective. The constraint defines a specific boundary in the optimization space that the coefficients cannot exceed. In 2D, this constraint region is a **circle** of radius $\sqrt{t}$. In 3D, it is a sphere, and in higher dimensions, a hypersphere.

Meanwhile, the RSS function forms elliptical contours centered around the unconstrained Ordinary Least Squares (OLS) solution. 

If the OLS solution lies outside the constraint region, the Ridge Regression coefficients ($\hat \beta^R$) will be the exact point where the expanding RSS contours first touch the boundary of the constraint region. This visually demonstrates why Ridge shrinks coefficients: the optimal solution is forced to lie within this budget boundary, physically pulling the coefficients closer to zero (the origin) compared to standard OLS.

![[ridge_regression_geometry.svg]]
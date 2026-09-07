**Elastic Net** is a hybrid [[Shrinkage Models|shrinkage]] method and regularization technique used to prevent overfitting in linear models. It combines the penalties of both [[Ridge Regression]] (L2) and [[Lasso Regression]] (L1). It was designed to overcome some of the limitations of Lasso, particularly its tendency to arbitrarily select only one feature from a group of highly correlated variables while ignoring the rest.

> [!WARNING] Standardizing Data
> Like other shrinkage methods, Elastic Net performs best when the data is standardized before processing, transforming it to zero mean and unit standard deviation. This ensures that independent variables are on the same scale and prevents larger magnitude coefficients from dominating the regularization.

## The Loss Function
In Elastic Net, the coefficients $\hat \beta^{EN}$ are obtained by minimizing the [[Goodness of Fit#Residual Sum of Squares (RSS)|Residual Sum of Squares]] (RSS) plus both the L1 and L2 shrinkage penalties:
$$\hat \beta^{EN} = \min_\beta\left[RSS + \lambda_1\sum_{j=1}^p |\beta_j| + \lambda_2\sum_{j=1}^p \beta_j^2\right]$$

> [!NOTE] The Mixing Parameter $\alpha$
> In software implementations, this is typically parameterized using a single overall penalty strength $\lambda$ and a mixing parameter $\alpha$ (where $0 \leq \alpha \leq 1$) that controls the balance between the L1 and L2 penalties:
> $$\hat \beta^{EN} = \min_\beta\left[RSS + \lambda \left( \alpha\sum_{j=1}^p |\beta_j| + (1 - \alpha)\sum_{j=1}^p \beta_j^2 \right)\right]$$
> Setting $\alpha = 1$ results in pure Lasso, while $\alpha = 0$ results in pure Ridge.

## Benefits of the Hybrid Approach
By combining both terms in the loss function, Elastic Net provides the best of both worlds:
1. **Feature Selection:** Like Lasso, the L1 portion allows it to shrink some coefficients exactly to zero, yielding a sparse model.
2. **Grouping Effect:** Like Ridge, the L2 portion stabilizes the paths of the coefficients, meaning that groups of highly correlated features tend to be selected (or shrunk) together rather than being arbitrarily dropped.

## The Bias-Variance Tradeoff
The reason Elastic Net is often better than OLS is rooted in the [[Bias-Variance Tradeoff]]. As $\lambda$ increases, the complexity of the model decreases due to being more constrained:
* At $\lambda = 0$, the model reduces to OLS, meaning the bias is zero (OLS is an unbiased estimator) and the variance is maximized.
* Higher $\lambda$ values will have higher bias and lower variance.
* Somewhere in the middle is a sweet spot where bias and variance are balanced and [[Mean Squared Error]] is minimized.

## Geometric Interpretation
Elastic Net can alternatively be formulated as a constrained optimization problem. Given a budget $t$, Elastic Net solves:
$$\min_\beta(RSS) \text{ s.t. } \alpha\sum_{j=1}^p |\beta_j| + (1 - \alpha)\sum_{j=1}^p \beta_j^2 \leq t$$

> [!NOTE] The Constraint Budget
> The budget $t$ is inversely related to the overall tuning parameter $\lambda$. As $\lambda$ increases, the allowable budget $t$ shrinks. While they are not the same value, there is a 1-to-1, data-dependent relationship between them.

This formulation provides a geometric perspective that perfectly illustrates how Elastic Net acts as a compromise between Ridge and Lasso. The constraint defines a specific boundary in the optimization space that the coefficients cannot exceed. 

Because Elastic Net is a linear combination of L1 and L2 penalties, its constraint region is a blend of the Lasso diamond and the Ridge circle. In 2D, it looks like a "rounded diamond"—it retains the sharp corners (vertices) on the axes from Lasso, but the edges connecting these vertices are strictly convex (bowed outward) due to the Ridge penalty. 

Meanwhile, the RSS function forms elliptical contours centered around the unconstrained Ordinary Least Squares (OLS) solution. 

If the OLS solution lies outside the constraint region, the Elastic Net coefficients ($\hat \beta^{EN}$) will be the exact point where the expanding RSS contours first touch the boundary of the constraint region. This visually demonstrates the hybrid benefits:
* **Sparsity (Lasso Effect):** Because the constraint region still retains sharp vertices on the axes, the expanding RSS contours can still intersect the boundary exactly at a corner, shrinking one or more coefficients to exactly 0. 
* **Grouping Effect (Ridge Effect):** Because the edges between the vertices are curved (strictly convex) rather than flat straight lines, the optimization is stabilized. If two features are highly correlated, the strict convexity encourages the intersection point to share weight between both coefficients, pulling them together rather than arbitrarily sliding down a flat edge to drop one entirely.

![[elastic_net_geometry.svg]]
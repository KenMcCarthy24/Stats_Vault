In the context of [[Linear Regression]] and [[Ordinary Least Squares (OLS)]], **Leverage** and **Influence** are used to identify and evaluate anomalous observations. Leverage is defined as a measure of how far an observation's predictor variables (the $X$ values) deviate from the mean of the predictor variables for the rest of the dataset. Influence is determined by the extent to which the estimated coefficients ($\hat{\beta}$) are changed when a specific data point is removed from the dataset.

## Distinguishing the Concepts
* **Leverage ($X$-space outlier):** Unusual predictor values are possessed by the data point. The *potential* to impact the regression line is held by these points, but an actual impact might not occur if the overall trend is aligned with.
* **Residual ($Y$-space outlier):** A significant distance is observed between the data point's observed $y$ value and the model's predicted $\hat{y}$ value.
* **Influence:** High influence is not guaranteed by high leverage alone. A high-leverage point is only rendered highly influential if a large residual is also present (meaning the pattern of the rest of the data is not followed).

## Mathematical Definitions

### Measuring Leverage
Leverage is mathematically derived from the **Hat Matrix** ($H$), by which the observed values $y$ are projected onto the predicted values $\hat{y}$:
$$H = X(X^T X)^{-1} X^T$$

The leverage score for the $i$-th observation, denoted as $h_i$ or $h_{ii}$, is represented by the $i$-th diagonal element of the Hat Matrix. It can be expressed as:
$$h_{ii} = x_i^T (X^T X)^{-1} x_i$$
where $x_i$ is the vector of predictor values for the $i$-th observation.

For [[Linear Regression#Special Case Simple Linear Regression|simple linear regression]], this equation can be used:
$$h_i=\frac{1}{n} + \frac{(x_i-\bar x)^2}{\sum_{j=1}^n(x_j-\bar x)^2}$$

Properties:
* **Bounds:** Leverage is always between 0 and 1 (or $1/n$ and $1$ if an intercept is included).
* **Sum of Leverage:** The total number of parameters estimated in the model, including the intercept, is exactly equaled by the sum of all leverage scores. If $p$ predictors are present, $(p+1)$ parameters are modeled.
   $$\sum_{i=1}^{n} h_{ii} = p + 1$$

### Measuring Influence (Cook's Distance)
While the *potential* for influence is captured by leverage, the actual overall influence of an observation is quantified by **Cook's Distance** ($D_i$). Cook's Distance is calculated by combining both the observation's leverage and its residual, providing a single metric to evaluate its overall effect on the regression model. 

It is defined by how much the fitted values are altered if the $i$-th observation is dropped, and can be expressed using the leverage score ($h_{i}$) and the standardized residual ($e_i$):
$$D_i = \frac{e_i^2}{MSE^2 (p+1)} \left[ \frac{h_{i}}{(1-h_{i})^2} \right]$$

A substantial shift in the estimated coefficients is indicated when a large Cook's Distance is calculated for a specific data point.

> [!NOTE] Identifying High-Leverage and Highly Influential Points
> The identification of anomalous points is considered crucial because the regression line can be severely pulled toward them. Standard diagnostic thresholds are commonly applied:
> * **High Leverage:** An observation is conventionally flagged if its leverage score is more than two or three times the average:
>   $$h_{ii} > \frac{2(p+1)}{n} \quad \text{or} \quad h_{ii} > \frac{3(p+1)}{n}$$
> * **High Influence:** An observation is generally flagged for further investigation if its Cook's Distance is greater than $1$, or if a more conservative threshold of $D_i > \frac{4}{n}$ is exceeded.
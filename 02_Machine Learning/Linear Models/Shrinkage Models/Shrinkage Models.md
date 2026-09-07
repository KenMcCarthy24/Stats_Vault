**Shrinkage methods** are regularization techniques used to help prevent overfitting in linear models. Each works by adding a new penalty term to the loss function in order to constrain the values that the linear coefficients can take on, effectively shrinking the coefficient magnitudes toward or to zero.

[[Ordinary Least Squares (OLS)]], the standard used for optimizing [[Linear Regression]] coefficients $\hat \beta$, optimizes the coefficients by minimizing the [[Goodness of Fit#Residual Sum of Squares (RSS)|Residual Sum of Squares]] (RSS) where:
$$RSS = \sum_{i=1}^{n} (y_i - x_i^T\beta)^2$$

Shrinkage models add a new regularization term to be minimized alongside the RSS. 

> [!NOTE]
> These notes will talk about adding this regression term to the RSS function in [[Linear Regression]], but the same technique can be used with other loss functions used for linear models, such as the log loss used for [[Logistic Regression]].

> [!WARNING] Standardizing Data
> All shrinkage models perform best when the data is standardized before processing, transforming it to zero mean and unit standard deviation. This ensures that independent variables are on the same scale and prevents larger magnitude coefficients from dominating the regularization.

## Types of Shrinkage Models
* **[[Ridge Regression]] (L2 Regularization):** Adds a penalty proportional to the square of the coefficient magnitudes. It shrinks coefficients toward zero but rarely exactly to zero.
* **[[Lasso Regression]] (L1 Regularization):** Adds a penalty proportional to the absolute value of the coefficient magnitudes. It can shrink coefficients exactly to zero, acting as a built-in feature selection method.
* **[[Elastic Net]]:** A hybrid technique combining both L1 and L2 penalties, offering both feature selection and a grouping effect for correlated variables.
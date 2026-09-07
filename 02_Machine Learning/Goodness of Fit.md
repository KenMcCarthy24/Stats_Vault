Several different metrics are used to assess the goodness of fit of a regression model, or how well it fits a set of observations.

# Sums of Squares
The three sum of squares metrics quantify how well the regression model explains the variation in the data. They are based on:
* $y$: The observed values
* $\hat y$: The predicted values
* $\bar y$: The sample mean of the observed values

### Residual Sum of Squares (RSS)
RSS quantifies the variability in the data that is unexplained by the model.
$$RSS = \sum_{i=1}^n(y_i-\hat y_i)^2$$
RSS is the objective function optimized by [[Ordinary Least Squares (OLS)]] for [[Linear Regression]]

### Explained Sum of Squares (ESS)
ESS quantifies how much variability is the data is explained by the model.
$$ESS = \sum_{i=1}^n(\hat y_i-\bar y)^2$$
### Total Sum of Squares (TSS)
TSS quantifies the total variability of the data. It is a property of the data sample itself, independent of any model.
$$TSS = \sum_{i=1}^n(y_i-\bar y)^2$$

These three sums of squares are related by:
$$TSS = RSS + ESS$$

# Coefficient of Determination ($R^2$)
The coefficient of determination ($R^2$) is a the proportion of the variation in the data explained by the model, calculated as:
$$R^2 = \frac{ESS}{TSS} = 1-\frac{RSS}{TSS}$$
It indicates how well a statistical model fits the data, with values closer to 1 representing a better fit. $R^2$ can be negative for very poorly fit models that fit worse than a horizontal line.


> [!warning] 
> $R^2$ cannot be used to compare two different models, as it cannot distinguish between a good fit and overfitting. A more complex model with more predictors will always have a higher $R^2$ even if it is not better at predicting new data. 
> 
> $R^2$ should also not be used for non-linear regression 

### Adjusted $R^2$
Adjusted $R^2$ is a variation of $R^2$ that can be used for model comparison, as it accounts for the number of predictors $p$. Defined as:
$$R^2_{adj} = 1 - \left(\frac{RSS}{TSS}\right)\left(\frac{n-1}{n-p-1}\right)$$
$R^2_{adj}$ indicates the proportion of the variation in the data explained by only the independent variables that actually affect the dependent variable, balancing goodness of fit with complexity.
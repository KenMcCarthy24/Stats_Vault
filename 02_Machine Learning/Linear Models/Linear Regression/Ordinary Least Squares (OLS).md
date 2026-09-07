Ordinary Least Squares (OLS) is a method utilized for estimating the unknown parameters in [[Linear Regression]] models. The parameters are estimated by minimizing the sum of the squares of the differences between the observed dependent variable and those predicted by the linear function.

## The Objective Function
The relationship between the dependent variable $y$ and the design matrix $X$ is modeled as:
$$y = X\beta + \varepsilon$$

The goal is to identify an estimator $\hat{\beta}$ that minimizes the **Residual Sum of Squares (RSS)**. The residuals $e$ are defined as the difference between the actual observations and the predictions:
$$e = y - X\hat{\beta}$$

The cost function is the [[Goodness of Fit#Residual Sum of Squares (RSS)|Residual Sum of Squares]] (RSS) is expressed as:
$$RSS(\beta) = \sum_{i=1}^{n} (y_i - x_i^T\beta)^2 = e^T e = (y - X\beta)^T (y - X\beta)$$
Minimizing this cost function yields this equation for the OLS estimator $\hat \beta$. Note: this is also the [[Maximum Likelihood Estimation|Maximum Likelihood Estimator]] for $\hat \beta$ assuming $\varepsilon \sim N(0, \sigma^2I)$.
$$\hat{\beta} = (X^T X)^{-1} X^T y$$

> [!NOTE]- Derivation of the OLS Estimator
> The OLS estimator, $\hat{\beta}$, is derived by finding the parameter vector that minimizes the RSS.
> 
> First, the objective function is expanded:
> $$
> \begin{aligned}
> RSS(\beta) &= (y - X\beta)^T (y - X\beta) \\
> &= y^T y - 2\beta^T X^T y + \beta^T X^T X\beta
> \end{aligned}
> $$
> 
> To locate the minimum, the gradient of the RSS with respect to $\beta$ is calculated and set to zero:
> $$
> \frac{\partial RSS}{\partial \beta} = -2X^T y + 2X^T X\beta
> $$
> 
> The first-order condition for a minimum requires that the gradient equal the zero vector:
> $$-2X^T y + 2X^T X\hat{\beta} = 0$$
> 
> This equation is rearranged to form the **Normal Equations**:
> $$X^T X\hat{\beta} = X^T y$$
> 
> Finally, the equation is solved for $\hat{\beta}$:
> $$\hat{\beta} = (X^T X)^{-1} X^T y$$

> [!warning] Non-Identifiability
> In order to obtain the OLS Estimator $\hat \beta$, the matrix inverse $(X^TX)^{-1}$ must be taken. If this matrix inverse does not exist, that means that the model parameters cannot be uniquely estimated because different parameter combinations produce identical predictions. This is called **Non-identifiability**
> 
> When does this happen?
> * **[[Collinearity]]**: One predictor is just a linear combination of one or more other predictors.
> * **Underdetermined System**: There are more predictors than data points in the sample $(p > n)$, which prevents unique solutions.

# Sampling Distribution
The sampling distribution of the OLS estimator $\hat \beta$ is the probability distribution of $\hat \beta$, treated as a [[Random Variable]] across random samples of size $n$.

> [!NOTE] Gauss-Markov Theorem
The **Gauss-Markov Theorem** states that if the errors have an expectation of zero, are uncorrelated, and have equal variances (standard [[Linear Regression Assumptions]]), the OLS estimator is the **Best Linear Unbiased Estimator**. This indicates that among all linear unbiased estimators, OLS has the minimum variance.

If Gauss Markov Theorem assumptions hold, the OLS estimator is [[Bias|unbiased]]. So.
$$E[\hat \beta] = \beta$$
Under the same assumptions, the variance-covariance matrix of the OLS estimator is defined as:
$$\Sigma = Var(\hat{\beta}) = \sigma^2 (X^T X)^{-1}$$

If population errors are assumed be normally distributed $\varepsilon \sim N(0, \sigma^2)$ then the sampling distribution of $\hat \beta$ is [[Multivariate Normal]].
$$\hat \beta \sim N\left(\beta, \sigma^2(X^TX)^{-1}\right)$$

In real data, errors are rarely perfectly normal. However, according to the [[Central Limit Theorem]], as the sample size $n$ becomes large, the sampling distribution of $\hat \beta$ converges to the above multivariate normal regardless of the distribution of the error term.

If $\sigma^2$ is unknown, an unbiased estimator $\hat \sigma^2$ can be calculated as:
$$\hat\sigma^2 = \frac{RSS}{n-(p+1)}$$
where $n-(p+1)$ is the [[Degrees of Freedom]]. $(p+1)$ parameters (the regression coefficients) must be estimated to calculate RSS, so that loses $(p+1)$ degrees of freedom.
# The Hat Matrix
The predicted values $\hat{y}$ can be expressed as a linear transformation of the observed values $y$ via the **Hat Matrix** ($H$), also known as the projection matrix:
$$\hat{y} = X\hat{\beta} = X((X^T X)^{-1} X^T y) = Hy$$
Where $H = X(X^T X)^{-1} X^T$. This matrix projects the observed $y$ vector onto the column space of $X$.

The diagonal elements of that hat matrix $H_{ii}$, are called the [[Leverage and Influence|Leverage]] values, which measure the influence of each observation on the regression fit.  


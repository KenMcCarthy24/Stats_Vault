A Generalized Linear Model (GLM) is a generalized version of a [[Linear Regression]] model, which relaxes the requirement that the response variable $y$ be normally distributed. Instead, it is assumed that the response follows any of the distributions in the [[Exponential Family of Distributions]]. 

Examples of GLMs: [[Linear Regression]], [[Logistic Regression]], [[Poisson Regression]]

---
# Components
A GLM consists of three components:
1. **A Random Component**: This is the response $y$ which follows a distribution in the exponential family.
2. **A Linear Predictor** ($\eta$): This is a linear combination of the independent variables $X_1, ... X_p$ and the coefficients $\beta_0, \beta_1, ... \beta_p$.
	* $\eta_i = \beta_0 + \beta_1X_{i1} + ... \beta_pX_{ip}$
	* or in matrix form $\eta = X\beta$
3. **A Link Function**: This is a function $g$ that relates the expected value of the response variable $E[y]$ to the linear predictor.
	* $g(E[y|i]) = g(\mu_i) = \eta_i$
	* The function $g$ must be monotone, continuous, and differentiable.

---
# Examples

> [!example]- Linear Regression
> Example: Linear Regression
> 
> In a linear regression, the response is assumed to follow a [[Normal]] distribution so the random component is $y \sim N(\mu, \sigma^2)$. This has a mean $\mu$.
> 
> The linear predictor is $\eta_i = \beta_0 + \beta_1X_{i1} + ... \beta_pX_{ip}$
> 
> The link function is simple in this case, as the expected value is equal to the linear predictor so $g(\mu_i) = \mu_i$
> 
> So the linear regression model equation is:
> $$E[y_i] = \beta_0 + \beta_1X_{i1} + ... \beta_pX_{ip}$$

> [!example]- Logistic Regression
> Example: Logistic Regression
> 
> In a logistic regression, the response represents a binary outcome (e.g., success/failure), so the random component is assumed to follow a [[Binomial]] distribution: $y_i \sim Bin(1, p_i)$. The expected value is the probability of success, so $\mu_i = p_i$.
> 
> The linear predictor is $\eta_i = \beta_0 + \beta_1X_{i1} + ... \beta_pX_{ip}$
> 
> The link function is the logit function, which maps probabilities bounded between $(0, 1)$ to the entire real number line $(-\infty, \infty)$ so $g(\mu_i) = \ln(\frac{p_i}{1-p_i})$
> 
> So the logistic regression model equation is:
> $$\ln(\frac{p_i}{1-p_i}) = \beta_0 + \beta_1X_{i1} + ... \beta_pX_{ip}$$
> 
> Or solved for $p_i$
> 
> $$p_i = \frac{1}{1-e^{-(\beta_0 + \beta_1X_{i1} + ... \beta_pX_{ip})}}$$

> [!example]- Poisson Regression
> Example: Poisson Regression
> 
> In a Poisson regression, the response represents count data (e.g., number of events in a time interval), so the random component is assumed to follow a [[Poisson]] distribution: $y_i \sim Poisson(\lambda_i)$. The expected value is the rate, so $\mu_i = \lambda_i$.
> 
> The linear predictor is $\eta_i = \beta_0 + \beta_1X_{i1} + ... \beta_pX_{ip}$
> 
> The link function is the natural logarithm, which ensures that the predicted rate is always a positive number so $g(\mu_i) = \ln(\mu_i)$
> 
> So the Poisson regression model equation is:
> $$\ln(\lambda_i) = \beta_0 + \beta_1X_{i1} + ... \beta_pX_{ip}$$


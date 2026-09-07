Logistic Regression is a statistical model used to relate one or more independent variables (or predictors) $X_1...X_p$ to a binary dependent variable $y$. The relationship between the predictors and the log-odds of the response ($\eta$) is assumed to be linear. Logistic regression is an example of a [[Generalized Linear Model]] where the response is assumed to follow a [[Binomial]] distribution $y \sim Bin(1, p)$, aka a [[Bernoulli]] distribution.

The general model is defined as:

$$\eta_i = \log\left(\frac{p_i}{1-p_i}\right) = \beta_0 + \beta_1X_{i1}+\beta_2X_{i2} + ... + \beta_pX_{ip}$$
Or solved for $p_i$:

$$p_i = \frac{1}{1+e^{-\eta_i}} = \frac{1}{1+\exp(-(\beta_0 + \beta_1X_{i1} + ... \beta_pX_{ip}))}$$
This is a sigmoid curve.

where $p_i = P(y_i=1)$. The parameters $\beta$ are interpreted as:
* $\beta_0$: The intercept term, representing the log-odds of the response if all predictors are 0
* $\beta_i$: The partial slopes, representing the change in the log-odds of the response variable for a unit change in $X_i$, keeping all other predictors equal

![[logistic_regression.svg]]

Because log-odds can be difficult to interpret intuitively, the parameters are often exponentiated to express the relationship in terms of odds:

$$Odds_i = \frac{p_i}{1-p_i} = \exp(\beta_0 + \beta_1X_{i1} + ... \beta_pX_{ip})=\exp(\beta_0)\exp(\beta_1X_{i1})...\exp(\beta_pX_{ip})$$

The exponentiated parameters are interpreted as:
* $\exp(\beta_0)$: The baseline odds of the response occurring when all predictors are 0
* $\exp(\beta_i)$: The multiplicative factor by which the odds of the response change for a unit increase in $X_i$, keeping all other predictors equal

Given the logistic regression model:
$$\eta_i = \log\left(\frac{p_i}{1-p_i}\right) = 3-0.5X_{1}+1.2X_{2}$$

> [!example]- Example Model 
> The interpretations of the coefficients are:
> * $\beta_0 = 3$: The log-odds of the outcome if all predictors are 0
> * $\beta_1 = -0.5$ The log-odds of the outcome decreases by 0.5 for a unit change in $X_1$
> * $\beta_2 = 1.2$ The log-odds of the outcome increases by 1.2 for a unit change in $X_2$
> 
> Or alternatively:
> * $\exp(\beta_0)=\exp(3) = 20.08$: The odds of the outcome if all predictors are 0
> * $\exp(\beta_1) = \exp(-0.5) = 0.61$: A unit change in $X_1$ will change the outcome odds by a multiplicative factor of $0.61$
> * $\exp(\beta_2) = \exp(1.2) = 3.32$: A unit change in $X_2$ will change the outcome odds by a multiplicative factor of $3.32$

# As a Machine Learning Algorithm
In a machine learning context, logistic regression is often treated as a binary classification Problem|Classification algorithm, with the goal to assign a label of 0 or 1 to each data point. It does this by placing a threshold $T$ on $p_i$ such that:
$$
\hat y = \left\{\begin{matrix}
0 \quad if \quad p_i < T \\
1 \quad if \quad p_i \geq T
\end{matrix}\right.
$$
A standard choice for $T$ is 0.5, meaning an example gets a label of 1 if the model assigns it a probability greater than 50%. However higher $T$ prioritizes [[Confusion Matrix and Metrics#Precision|Precision]], as it is harder to have false positives. On the other hand, lower $T$ prioritizes [[Confusion Matrix and Metrics#Recall|Recall]], as it is harder to have false negatives. 
# Optimization
Logistic regression is most often optimized using [[Maximum Likelihood Estimation]] to find the highest likelihood set of coefficients $\hat \beta$. The loss function to be minimized is the negative of the log likelihood function, which works out to be the [[Cross Entropy#Binary Cross Entropy|Binary Cross Entropy]]:
$$\hat \beta = \min_\beta[-\mathcal{L}(\beta)] = \min_\beta[-\sum_{i=1}^n [y_i\ln(p_i) + (1-y_i)\ln(1-p_i)]]$$
Where $p_i$ contains the hidden $\beta$ coefficients to be optimized as
$$p_i = \frac{\exp(\eta_i)}{1+\exp(\eta_i)} = \frac{\exp(\beta_0 + \beta_1X_{i1}+\beta_2X_{i2} + ... + \beta_pX_{ip})}{1+\exp(\beta_0 + \beta_1X_{i1}+\beta_2X_{i2} + ... + \beta_pX_{ip})}$$
This minimum does not have an analytical solution so it must be optimized numerically.

> [!NOTE]- Log-Likelihood Function Derivation
> Log-Likelihood function derivation:
> 
> The marginal PMF for the [[Binomial]] response variable $y_i \sim Bin(1, p_i)$ is given by:
> $$P(y=y_i) = \binom{1}{y_i}p_i^{y_i}(1-p_i)^{1-y_i}$$
> The likelihood function is then given by:
> $$L(\beta) = \prod_{i=1}^n \binom{1}{y_i}p_i^{y_i}(1-p_i)^{1-y_i}$$
> The Log-likelihood function is then given by:
> $$\mathcal{L}(\beta)= \ln(L(\beta)) = \sum_{i=1}^n\left[\ln (\binom{1}{y_i}) + y_i\ln(p_i) + (1-y_i)\ln(1-p_i)\right]$$
> The first term does not depend on $p_i$ and therefore does not depend on $\beta$ so it is unnecessary for the maximization, making the final log-likeihood function to be maximized:
$$\mathcal{L}(\beta) = \sum_{i=1}^n[y_i\ln(p_i) + (1-y_i)\ln(1-p_i)]$$

# Deviance
Deviance ($D$) is a quantity used to assess the goodness of fit of a logistic regression model, similar to how $R^2$ is used in a linear regression model. It is defined as:
$$D = -2\mathcal{L}(\hat \beta) = -2\sum_{i=1}^n [y_i\ln(p_i) + (1-y_i)\ln(1-p_i)]$$
A lower deviance indicates a better fit. Oftentimes, two different deviances are calculated and reported:
* The **Null Deviance**: The deviance of a model that includes no predictor variables, only the intercept $\beta_0$. This represents how much error there is before adding features.
* The **Residual Deviance**: The deviance for the fully trained model with all its predictor variables included.

How much the features in the model improve the model's fit can be seen by comparing the Null Deviance to the Residual Deviance. A large difference between the two means the predictors are effective. 
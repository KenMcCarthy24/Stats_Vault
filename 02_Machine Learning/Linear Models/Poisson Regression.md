Poisson Regression is a statistical model used to relate one or more independent variables (or predictors) $X_1...X_p$ to a dependent variable $y$ that represents count data. The relationship between the predictors and the natural logarithm of the expected count is assumed to be linear. Poisson regression is an example of a [[Generalized Linear Model]] where the response is assumed to follow a [[Poisson]] distribution $y \sim Poisson(\lambda)$.

Often, count data is observed over varying time periods, spatial areas, or population sizes. This baseline denominator is known as the **exposure** ($t$). To account for this and model the underlying **rate** ($\lambda/t$) rather than just the absolute count, an offset term $\ln(t_i)$ is included in the model.

The general model for the expected count $\lambda_i = E(y_i)$ is defined as:

$$\ln(\lambda_i) = \ln(t_i) + \beta_0 + \beta_1X_{i1} + \beta_2X_{i2} + ... + \beta_pX_{ip}$$

Solved for $\lambda_i$ this is:

$$\lambda_i = t_i\exp(\beta_0 + \beta_1X_{i1} + ... + \beta_pX_{ip})$$

> [!Note] Exposure Exclusion
> If all data samples were collected under the same exposure (e.g. the same amount of time), then the $t_i$ term is often dropped, as it just becomes a constant that can be absorbed into the intercept term $\beta_0$.

The parameters $\beta$ are interpreted as:
* $\beta_0$: The intercept term, representing the log of the expected count *per unit of exposure* when all predictors are 0
* $\beta_i$: The partial slopes, representing the change in the log of the expected count for a unit change in $X_i$, keeping all other predictors and the exposure constant

Because the log of an expected count can be difficult to interpret intuitively, the parameters are often exponentiated to express the relationship in terms of multiplicative changes to the expected count:

$$\lambda_i = t_i \cdot \exp(\beta_0) \cdot \exp(\beta_1X_{i1}) \cdots \exp(\beta_pX_{ip})$$

The exponentiated parameters are interpreted as:
* $\exp(\beta_0)$: The baseline expected count *per unit of exposure* when all predictors are 0 (the baseline rate)
* $\exp(\beta_i)$: The multiplicative factor (or Rate Ratio) by which the expected count changes for a unit increase in $X_i$, keeping all other predictors and the exposure constant

> [!example]- Example Model
> Given the Poisson regression model where counts are observed over $t_i$ days:
> $$\ln(\lambda_i) = \ln(t_i) + 1.5 + 0.8X_{i1} - 0.2X_{i2}$$
> The interpretations of the coefficients are:
> * $\beta_0 = 1.5$: The log of the expected count per day if all predictors are 0
> * $\beta_1 = 0.8$: The log of the expected count increases by 0.8 for a unit change in $X_{i1}$
> * $\beta_2 = -0.2$: The log of the expected count decreases by 0.2 for a unit change in $X_{i2}$
>
> Or alternatively:
> * $\exp(\beta_0) = \exp(1.5) = 4.48$: The baseline expected count per day if all predictors are 0. (For a specific observation over $10$ days, the baseline expected count would be $10 \times 4.48 = 44.8$)
> * $\exp(\beta_1) = \exp(0.8) = 2.23$: A unit increase in $X_{i1}$ multiplies the expected count by a factor of $2.23$ (a 123% increase)
> * $\exp(\beta_2) = \exp(-0.2) = 0.82$: A unit increase in $X_{i2}$ multiplies the expected count by a factor of $0.82$ (an 18% decrease)

# Optimization
Poisson regression is optimized using [[Maximum Likelihood Estimation]] to find the highest likelihood set of coefficients $\hat{\beta}$. The loss function to be minimized is the negative log-likelihood:

$$\hat{\beta} = \min_\beta \left[ -\sum_{i=1}^n \left[ y_i\ln(\lambda_i) - \lambda_i \right] \right]$$

where $\lambda_i$ contains the unknown $\beta$ parameters to be optimized as:

$$\lambda_i = t_i\exp(\beta_0 + \beta_1X_{i1} + \beta_2X_{i2} + ... + \beta_pX_{ip})$$

This minimum does not have a closed-form analytical solution, so it is optimized numerically.

> [!NOTE]- Log-Likelihood Function Derivation
> The probability mass function (PMF) for the [[Poisson]] response variable $y_i \sim Poisson(\lambda_i)$ is given by:
> $$P(y=y_i) = \frac{\lambda_i^{y_i}e^{-\lambda_i}}{y_i!}$$
> The likelihood function is given by taking the product across all $n$ independent observations:
> $$L(\beta) = \prod_{i=1}^n \frac{\lambda_i^{y_i}e^{-\lambda_i}}{y_i!}$$
> Taking the natural logarithm gives the log-likelihood function:
> $$\mathcal{L}(\beta) = \sum_{i=1}^n\left[y_i\ln(\lambda_i) - \lambda_i - \ln(y_i!)\right]$$
> The final term, $\ln(y_i!)$, does not depend on $\lambda_i$ and therefore does not depend on $\beta$. Since it is constant with respect to our parameters, it can be dropped, leaving:
> $$\mathcal{L}(\beta) \propto \sum_{i=1}^n\left[y_i\ln(\lambda_i) - \lambda_i\right]$$

# Overdispersion
A characteristic of the [[Poisson]] distribution that the response is assumed to follow is that the mean is equal to the variance ($E[y] = Var(Y) = \lambda$). **Overdispersion** occurs when the variance is significantly higher than the mean, thus violating this assumption.

Data rarely perfectly fits a Poisson distribution. Overdispersion can happen for several reasons including:
* **Zero Inflation**: The dataset contains a larger number of zero counts than a true Poisson distribution would predict.
* **Violated Independence**: There is dependence between data points, meaning that the count of one data point affects the count of another.
* **Outliers**: Significant outliers in the counts inflating the variance.
* **Missing Explanatory Variables**: Variables are missing from the model that would reduce variance if included.

### Testing For Overdispersion

Overdispersion can be detected by assuming $E[y]=\lambda$ and $Var(y)=\lambda \phi$, where $\phi$ is the **Dispersion Ratio**.
* If $\phi \approx 1$: The variance equals the mean and there is no overdispersion.
* If $\phi > 1$ then there is overdispersion.
* If $\phi < 1$ then there is underdispersion. This is quite rare in practice.

$\phi$ can be estimated using the Pearson goodness-of-fit statistic as:
$$\hat \phi = \frac{\sum_{i=1}^n \frac{(y_i - \hat{\lambda}_i)^2}{\hat{\lambda}_i}}{n-(p+1)}$$
The numerator of this estimator is known to follow a [[Chi-Squared]] distribution with $(n-(p+1))$ [[Degrees of Freedom]]. Thus a [[Hypothesis Test]] can be set up:
$$H_0: \phi = 1$$
$$H_1: \phi > 1$$
with test statistic:
$$\chi^2 = \sum_{i=1}^n \frac{(y_i - \hat{\lambda}_i)^2}{\hat{\lambda}_i}$$
This will be an upper-tailed [[Chi-Squared Test]] at some significance level $\alpha$. If the p-value is $< \alpha$, reject the null hypothesis and conclude that overdispersion is present.
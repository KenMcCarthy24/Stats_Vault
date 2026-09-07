Below are the 4 basic assumptions that go into [[Ordinary Least Squares (OLS)]] and [[Linear Regression]]

## 1. Linearity
The expected value of the response variable is assumed to be a linear combination of the predictor variables: 
$$E[Y|X] = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p$$

**Consequences of Violation:**
* Biased and inconsistent coefficient estimates are produced. 
* The true relationship between variables is not captured by the model
* Predictions are invalid.

**Diagnostics:**
* **Observed vs Fitted:** A plot should be evaluated to ensure points are clustered symmetrically around the $y=x$ line.
* **Residuals vs Fitted:** A random scatter of points around the horizontal zero-line should be observed. The presence of curves or systematic bows indicates a violation.

![[regression_linearity_tests.svg]]

---

## 2. Independence
**Mathematical Description:** The error terms are assumed to be entirely uncorrelated with one another: 
$$Cov(\varepsilon_i, \varepsilon_j) = 0\text{ for all }i\neq j$$

**Consequences of Violation:**
* Means autocorrelation is present
* [[Linear Regression Inference#Standard Error|Standard errors]] are underestimated.
* [[Linear Regression Inference#Confidence Intervals for Coefficients|Confidence intervals]] are artificially narrowed

**Diagnostics:**
* **Residuals vs Index:** A random distribution of residuals across the sequence of observations must be displayed. Tracking, drifting, or cyclical trends should not be seen.
* **Successive Residuals:** When the $i$-th residual ($\varepsilon_i$) is plotted against the preceding residual ($\varepsilon_{i-1}$), a random scatter must be shown rather than a correlated linear trend.

![[regression_independence_tests.svg]]

---

## 3. Homoscedasticity
**Mathematical Description:** The variance of the error terms is assumed to remain constant across all levels of the independent variables: 
$$Var(\varepsilon_i | X) = \sigma^2$$

**Consequences of Violation:**
* Called heteroscedasticity
* Coefficient estimates are still yielded without bias, but they are no longer optimally efficient.
* [[Linear Regression Inference#Standard Error|Standard errors]] are biased, which causes [[Linear Regression Inference#Hypothesis Test Hypothesis Tests|hypothesis tests]] and [[Linear Regression Inference#Confidence Intervals for Coefficients|confidence intervals]] to be invalidated.

**Diagnostics:**
* **Residuals vs Fitted:** The vertical spread or variance of the residuals should be observed as roughly constant across the entire range of fitted values. Funnel, cone, or fan shapes indicate a violation.

![[regression_homoscedasticity_tests.svg]]

---

## 4. Normality
**Mathematical Description:** The error terms are assumed to be normally distributed around a mean of zero: 
$$\varepsilon_i \sim N(0, \sigma^2)$$

**Consequences of Violation:**
* Standard errors, confidence intervals, and p-values are rendered unreliable.
* This is particularly problematic when small sample sizes are utilized, though it is often mitigated in large samples by the [[Central Limit Theorem]].

**Diagnostics:**
* **Shapiro-Wilk Test:** A formal statistical test is performed where the null hypothesis of normality is rejected if the calculated p-value is found to be less than the chosen alpha level (e.g., $p < 0.05$).
* **Residuals vs Fitted:** While primarily used for other assumptions, severe asymmetric skewness or extreme outliers can be detected in this plot, which may indicate departures from normality.
* **QQ-Plot:** The standardized residuals are plotted against theoretical normal quantiles. To confirm normality, a straight diagonal line should be closely followed by the plotted points.

![[regression_normality_tests.svg]]
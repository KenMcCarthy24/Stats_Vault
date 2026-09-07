# Linear Regression Inference

Once the [[Estimators]] for the [[Linear Regression]] coefficients $\beta$ have been calculated using [[Ordinary Least Squares (OLS)]], statistical inference can be performed through confidence intervals and hypothesis testing.

Let the optimized model be given by:
$$\hat{y} = X\hat{\beta}$$

---

## Point Estimates

For a new set of data, predictions using the optimized model can be found as:
$$\hat{y}^* = X^*\hat{\beta}$$
where $X^*$ is a $(k \times (p+1))$ matrix containing $k$ data points and $p$ predictors. The first column is all ones for the bias term $\beta_0$.

If the true $y^*$ is known, the **Mean Squared Prediction Error (MSPE)** can be calculated as:
$$MSPE = \frac{1}{k}\sum_{i=1}^k(y_i^* - \hat{y}_i^*)^2$$

---

## Standard Error

The standard error for a coefficient $\hat{\beta}_j$ is found using the $j$-th diagonal element of the variance-covariance matrix $\Sigma$ for the [[Ordinary Least Squares (OLS)#Sampling Distribution|sampling distribution]] of $\hat{\beta}$:
$$SE_j = \sqrt{\Sigma_{jj}} = \sqrt{(\hat{\sigma}^2(X^TX)^{-1})_{jj}}$$

A smaller standard error indicates higher precision and less variability across samples, while a larger one suggests higher uncertainty in the coefficient's value.

---

## [[Hypothesis Test|Hypothesis Tests]]

### T-Test for Individual Coefficients

Tests whether an individual coefficient $\beta_j$ is significantly different from 0:
$$H_0: \beta_j = 0 \qquad H_1: \beta_j \neq 0$$

If $H_0$ cannot be rejected, there is insufficient evidence of a linear relationship between $X_j$ and $y$, and that predictor may be removable from the model.

Uses a [[Student's t-Test]] with $n-(p+1)$ [[Degrees of Freedom]]. The test statistic is:
$$t = \frac{\hat{\beta}_j}{SE_j}$$

### F-Test for Nested Models

Compares a full model $\Omega$ to a nested model $\omega$ to determine whether the reduced model is sufficient. Define:
$$\Omega: y = \beta_0 + \beta_1X_1 + \cdots + \beta_pX_p + \varepsilon$$
$$\omega: y = \beta_0 + \beta_1X_1 + \cdots + \beta_qX_q + \varepsilon, \quad q < p$$

The hypotheses test whether the extra predictors in $\Omega$ significantly contribute:
$$H_0: \beta_{q+1} = \beta_{q+2} = \cdots = \beta_p = 0$$
$$H_1: \beta_j \neq 0 \text{ for at least one } j \in \{q+1, \ldots, p\}$$

This is an **upper-tailed** [[F-Test]] with $p-q$ numerator and $n-(p+1)$ denominator degrees of freedom:
$$F = \frac{(RSS_\omega - RSS_\Omega)/(p-q)}{RSS_\Omega/(n-(p+1))}$$
where RSS is the [[Goodness of Fit#Residual Sum of Squares (RSS)|Residual Sum of Squares]].

**Full F-Test:** A special case comparing $\Omega$ against $\omega: y = \beta_0 + \varepsilon$, testing whether the model explains any variance at all beyond the mean $\bar{y}$:
$$H_0: \beta_1 = \beta_2 = \cdots = \beta_p = 0$$
$$H_1: \beta_j \neq 0 \text{ for at least one } j \in \{1, \ldots, p\}$$

---

## [[Confidence Intervals]] for Coefficients

The $(1-\alpha)\%$ confidence interval for $\beta_j$ is:
$$\hat{\beta}_j \pm t_{\alpha/2,\, n-(p+1)} \times SE_j$$

This provides a range of plausible values for the true coefficient, capturing uncertainty in the point estimate $\hat{\beta}_j$. If many repeated samples were taken and a confidence interval constructed from each, approximately $(1-\alpha)\%$ of those intervals would contain the true $\beta_j$.

> [!NOTE] Connection to Hypothesis Tests
> If the $(1-\alpha)\%$ confidence interval for $\beta_j$ **does not** contain 0, it is equivalent to rejecting $H_0: \beta_j = 0$ at the $\alpha$ significance level.

---

## Prediction Intervals

A prediction interval provides a range of plausible values for a **new individual observation** $y^*$ given input vector $x^*$, at confidence level $(1-\alpha)$.

Unlike a confidence interval for a coefficient, a prediction interval must account for two sources of uncertainty:
1. **Estimation uncertainty** — uncertainty in $\hat{\beta}$
2. **Irreducible error** — inherent variability $\varepsilon \sim N(0, \sigma^2)$ of any new observation around the true mean

The variance of the prediction error $y^* - \hat{y}^*$ is:
$$\text{Var}(y^* - \hat{y}^*) = \sigma^2\left(1 + x^{*T}(X^TX)^{-1}x^*\right)$$

giving an estimated standard error of:
$$SE_{pred} = \sqrt{\hat{\sigma}^2\left(1 + x^{*T}(X^TX)^{-1}x^*\right)}$$

The $(1-\alpha)\%$ prediction interval is:
$$\hat{y}^* \pm t_{\alpha/2,\, n-(p+1)} \times SE_{pred}$$

> [!NOTE] Prediction Interval vs. Confidence Interval for the Mean
> A **confidence interval for the mean response** at $x^*$ estimates uncertainty in $E[y^*] = x^{*T}\beta$ and uses $SE = \sqrt{\hat{\sigma}^2\, x^{*T}(X^TX)^{-1}x^*}$, omitting the extra $\sigma^2$ term. A prediction interval is always wider because it also accounts for the scatter of individual observations around the mean.
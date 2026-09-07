Assuming there is some true process $f$ that generates data $X$ as $f(X)$, there are many possible models that could approximate it: $g_1(X), g_2(X), \dots, g_n(X)$. 

The **Akaike Information Criterion (AIC)** and **Bayesian Information Criterion (BIC)** are two metrics used to compare and select the best statistical model from a set of candidates. They help prevent overfitting by balancing goodness of fit with model simplicity.

Both metrics involve tradeoffs between three primary components:
* $\hat{L}$: The **maximized value of the likelihood function** for the model.
	* If $\hat \theta$ is the [[Maximum Likelihood Estimation|Maximum Likelihood Estimator]] for the parameters of the model and $L(\theta)$ is the likelihood function, then $\hat L = L(\hat\theta)$
* $k$: The number of estimated parameters in the model.
* $n$: The number of observations (sample size).

---

## Akaike Information Criterion (AIC)
$$AIC = 2k - 2\ln(\hat{L})$$

AIC focuses mainly on **predictive accuracy**, often selecting slightly more complex models that better fit the data.

**Connection to KL Divergence:** AIC is grounded in information theory — it estimates the relative [[KL divergence]] between the true data-generating process $f$ and the candidate model $g$:
$$D_{KL}(f \| g) = \int f(x) \ln\frac{f(x)}{g(x)}\, dx$$
The $-2\ln(\hat{L})$ term estimates the [[Cross Entropy]] between $f$ and $g$. Since the entropy of $f$ is constant across all candidate models, minimizing AIC is equivalent to minimizing the estimated [[KL Divergence]] $D_{KL}(f \| g)$. The $2k$ penalty corrects for the optimistic bias that arises from evaluating the model on the same data used to fit it.

* **Penalty:** The first term, $2k$, acts as a penalty for adding complexity to the model.
* **Reward:** The second term, $-2\ln(\hat{L})$, rewards a tight fit to the data.
* **Decision Rule:** When comparing a set of candidate models, the model with the **lowest** $AIC$ is the best choice.

---

## Bayesian Information Criterion (BIC)
$$BIC = k\ln(n) - 2\ln(\hat{L})$$

BIC focuses on finding the **true model**, placing harsher penalties on unnecessary predictors to favor simplicity.

* **Penalty:** Similar to AIC, the first term, $k\ln(n)$, acts as a penalty for adding complexity. 
	* Because $\ln(n) \geq 2$ for any dataset with at least 8 data points, the BIC penalty is generally harsher than the AIC penalty.
* **Reward:** The second term, $-2\ln(\hat{L})$, is identical to AIC, rewarding a tight fit to the data.
* **Decision Rule:** When comparing a set of candidate models, the model with the **lowest** $BIC$ is the best choice.

---

> [!NOTE] Special Case: Linear Regression
> For [[Linear Regression]], it can be shown mathematically that:
> $$-2 \ln(\hat{L}) = n + n\ln(2\pi) + n\ln\left(\frac{RSS}{n}\right)$$
> 
> Where $RSS$ is the [[Goodness of Fit#Residual Sum of Squares (RSS)|Residual Sum of Squares]]. When comparing models on the same dataset, the first two terms ($n$ and $n\ln(2\pi)$) are constants and can be ignored.
> 
> Based on this, the **AIC** for linear regression simplifies to:
> $$AIC = 2(p+1) + n\ln\left(\frac{RSS}{n}\right)$$
> *(Note: $p$ is the number of predictors, so $k=p+1$ to account for the intercept term $\beta_0$.)*
> 
> Similarly, the **BIC** for linear regression simplifies to:
> $$BIC = (p+1)\ln(n) + n\ln\left(\frac{RSS}{n}\right)$$
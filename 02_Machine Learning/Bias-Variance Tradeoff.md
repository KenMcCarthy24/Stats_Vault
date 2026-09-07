In [[Machine Learning]], the **Bias-Variance Tradeoff** is a phenomenon where as model complexity increases, the tendency of the model to have high bias (**underfitting**) is replaced with the tendency of the model to have high variance (**overfitting**). A well trained model needs to strike a balance between these two extremes.

# Derivation from MSE
The definition of the mean squared error (MSE) can be decomposed to demonstrate the existence of the bias-variance tradeoff.

> [!caution]
> Although the bias-variance tradeoff is shown here as a decomposition of the MSE, the phenomenon is universal to all machine learning and statistical models, not just those that use MSE as a metric.

Assume there is some true relationship between an independent variable $x$ and a dependent variable $y$ given as:
$$y = f(x) + \varepsilon$$
Where $\varepsilon$ represents random, irreducible, and symmetric statistical noise with $E[\varepsilon]=0$.

A machine learning model creates an [[Estimators|Estimator]] of the true function $f(x)$ as $\hat f(x)$, with estimates calculated as:
$$\hat y = \hat f(x)$$
The mean squared error of the model is then defined as:
$$MSE = E[(y-\hat y)^2] = E[(f(x) + \varepsilon -\hat f(x))^2]$$
Through some algebra, this can be rearranged as:
$$MSE= (f(x) - E[\hat f(x)])^2 + Var(\hat f(x)) + Var(\varepsilon)$$
Going term by term:
* $(f(x) - E[\hat f(x)])^2$ is the squared [[Bias]] of the model $\hat f(x)$.
* $Var(\hat f(x))$ is the [[Expectation and Moments#2nd Central Moment Variance|variance]]  of the model $\hat f(x)$.
* $Var(\varepsilon)$ = This is the inherent noise in the system itself. No model can ever reduce the total error beyond this threshold.

So the Bias-Variance decomposition of the mean squared error is:
$$MSE= Bias(\hat f(x))^2 + Var(\hat f(x)) + Var(\varepsilon)$$
> [!note]- Full MSE Decomposition
> To decompose the MSE, we substitute $y = f(x) + \varepsilon$ into the MSE equation and expand the square. The key trick is adding and subtracting the expected model prediction $E[\hat{f}(x)]$ so the cross-terms cancel out.
> 
> Start with the definition of MSE:
> $$MSE = E[(y - \hat{f}(x))^2]$$
> 
> Substitute $y = f(x) + \varepsilon$ and group the terms:
> $$MSE = E[((f(x) - \hat{f}(x)) + \varepsilon)^2]$$
> 
> Expand the squared binomial:
> $$MSE = E[(f(x) - \hat{f}(x))^2 + 2(f(x) - \hat{f}(x))\varepsilon + \varepsilon^2]$$
> 
> Apply the linearity of expectation. Since the noise $\varepsilon$ is independent and $E[\varepsilon] = 0$, the cross-term $2E[f(x) - \hat{f}(x)]E[\varepsilon]$ becomes zero. We also know $E[\varepsilon^2] = Var(\varepsilon)$:
> $$MSE = E[(f(x) - \hat{f}(x))^2] + Var(\varepsilon)$$
> 
> Now, take the remaining expectation and add/subtract the expected model prediction $E[\hat{f}(x)]$ inside the square:
> $$E[(f(x) - \hat{f}(x))^2] = E[((f(x) - E[\hat{f}(x)]) + (E[\hat{f}(x)] - \hat{f}(x)))^2]$$
> 
> Expand this new square:
> $$E[(f(x) - E[\hat{f}(x)])^2 + 2(f(x) - E[\hat{f}(x)])(E[\hat{f}(x)] - \hat{f}(x)) + (E[\hat{f}(x)] - \hat{f}(x))^2]$$
> 
> Apply the expectation to each term:
> 1. **First term:** $f(x)$ and $E[\hat{f}(x)]$ are both deterministic, so $E[(f(x) - E[\hat{f}(x)])^2] = (f(x) - E[\hat{f}(x)])^2$, which is the squared **Bias**.
> 2. **Cross term:** Because $E[E[\hat{f}(x)] - \hat{f}(x)] = E[\hat{f}(x)] - E[\hat{f}(x)] = 0$, the entire middle term drops out.
> 3. **Third term:** $E[(E[\hat{f}(x)] - \hat{f}(x))^2]$ is the exact definition of the **Variance** of $\hat{f}(x)$.
> 
> Bringing it all together:
> $$MSE = (f(x) - E[\hat{f}(x)])^2 + Var(\hat{f}(x)) + Var(\varepsilon)$$
> $$MSE = Bias(\hat{f}(x))^2 + Var(\hat{f}(x)) + Var(\varepsilon)$$

---
# Bias and Variance Interpretation
Below is a more in depth description of the interpretation of the bias and variance terms and their tradeoff as model complexity increases.
### Bias
The bias represents the error introduced by approximating a complex real-world relationship with a simplified model. High bias means that the model is making strong assumptions about the data that are fundamentally incorrect, not modeling nuances very well. In other words, the model is **Underfitting**.

**High bias Example**: A simple [[Linear Regression]] model that tries to predict home price based on only the number of bedrooms, ignoring any other potential features. This model is too simple to capture the underlying pattern.
### Variance
The variance measures how much the predictions of the model would change on average if it was trained on a different dataset drawn from the same population. It reflects the model's sensitivity to small fluctuations or noise in the training set. High variance means the model is **Overfitting** to the training dataset, fitting it very well but not generalizing to new data well.

**High Variance Example**: A 20-th degree polynomial is fit to a dataset that is roughly linear. The polynomial line very closely approximates the training data but is wildly inaccurate on new data. 

### Tradeoff
![[Pasted image 20260330221732.png]]

As the complexity of a model increases, there is a tradeoff between high bias and high variance.

A model with too low of complexity will:
* Fail to capture all the useful nuance of the data and underfitting (High bias)
* Be stable to retraining on a new dataset drawn from the same population (Low Variance)

While a model that is overly complex will:
* Capture all of the useful nuance of the data (Low bias)
* Go too far and also capture a lot of the noise or small fluctuations, overfitting the training data (High variance)

An important goal when designing an effective machine learning model is to find the perfect middle-ground complexity for the problem that balances the bias and variance in order to get the minimum possible total error.
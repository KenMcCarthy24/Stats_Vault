Fisher Information($I(\theta)$) measures how much "information" a [[Random Variable]] $X$ carries about an unknown parameter $\theta$.
* It quantifies the expected curvature of the log-likelihood function.
* It  is inversely proportional to the minimum possible variance of an [[Bias|unbiased estimator]] (The [[Estimator Efficiency#Cramér-Rao Lower Bound (CRLB)|Cramér-Rao Lower Bound]]). 
* Intuitively, if the likelihood function has a **sharp peak**, the data provides a lot of information (high Fisher Information), leading to smaller best case variance.
* If the likelihood function is **flat**, the data provides little information (low Fisher Information), making it hard to estimate $\theta$ precisely.

Often written as $I_n(\theta)$ where $n$ is the size of the sample. $I_1(\theta)$ for example would be the fisher information for a single observation. If the observations  are i.i.d:
$$I_n(\theta) = nI_1(\theta)$$

## The Score Function
To define Fisher Information, first define the **Score Function** ($S(\theta)$), which is the gradient of the log-likelihood with respect to the parameter.

$$S(\theta) = \frac{\partial}{\partial \theta} \log f(X; \theta)$$

* The expected value of the score is always zero: $E[S(\theta)] = 0$.

## Formulas for Fisher Information
Fisher Information is formally defined as the **variance of the score**.

$$I_n(\theta) = Var(S(\theta)) = E\left[ \left( \frac{\partial}{\partial \theta} \log f(X; \theta) \right)^2 \right]$$

If the log-likelihood is twice differentiable, it can be more easily calculated as the negative expectation of the second derivative:

$$I_n(\theta) = -E\left[ \frac{\partial^2}{\partial \theta^2} \log f(X; \theta) \right]$$

## Fisher Information Matrix (FIM)
When $\theta$ is a vector of parameters $\theta = [\theta_1, \theta_2, ..., \theta_k]^T$, the Fisher Information is represented as a symmetric $k \times k$ matrix. 

The elements of the **Fisher Information Matrix** are defined by the covariance between the partial derivatives of the log-likelihood:

$$I(\theta)_{i,j} = E\left[ \left( \frac{\partial}{\partial \theta_i} \log f(X; \theta) \right) \left( \frac{\partial}{\partial \theta_j} \log f(X; \theta) \right) \right]$$

If the log-likelihood is twice differentiable, the components can be calculated as:

$$I(\theta)_{i,j} = -E\left[ \frac{\partial^2}{\partial \theta_i \partial \theta_j} \log f(X; \theta) \right]$$

---

> [!example]- [[Exponential]] Distribution 
> Let $x_i \overset{\mathrm{iid}}{\sim} Exp(\lambda)$. Derive the formula for the fisher information $I_n(\lambda)$
> 
> PDF given by:
> $$f(x_i;\lambda) = \lambda e^{-\lambda x_i}$$
> Likelihood function is then:
> $$L(\lambda) = f(X;\lambda) = \prod_{i=1}^n \lambda e^{-\lambda x_i} = \lambda^ne^{-\lambda\sum x_i} = \lambda^ne^{-\lambda n \bar{X}}$$
> Log Likelihood is:
> $$\mathcal{L}(\lambda) = \ln(L(\lambda)) = \ln(\lambda^ne^{-\lambda n \bar{X}}) = n\ln(\lambda)-\lambda n \bar{X}$$
> Take the second derivative:
> $$\frac{\partial\mathcal{L}(\lambda)}{\partial \lambda} = \frac{n}{\lambda} - n\bar{X}$$
> $$\frac{\partial^2\mathcal{L}(\lambda)}{\partial \lambda^2} = \frac{-n}{\lambda^2}$$
> 
> Finally:
> $$I_n(\lambda) = -E\left[\frac{\partial^2\mathcal{L}(\lambda)}{\partial \lambda^2}\right] = -E\left[\frac{-n}{\lambda^2}\right] = \frac{n}{\lambda^2}$$
> This result also implies that the fisher information for a single observation is:
> $$I_1(\lambda) = \frac{1}{\lambda^2}$$
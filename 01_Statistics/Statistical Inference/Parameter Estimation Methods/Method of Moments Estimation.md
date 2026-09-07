Method of moments estimation is a technique for calculating an [[Estimators|estimator]] from data $[x_1, x_2, \dots]$ by equating the theoretical [[Expectation and Moments|moments]] of a distribution ($\mu_1$, $\mu_2$, $\mu_3$, ...) with the sample moments ($M_1$, $M_2$, $M_3$, ...) where the theoretical moments are given by:
$$\mu_k = E[X^k]$$
and the sample moments are given by:
$$M_k = \frac{1}{n}\sum_{i=1}^n x_i^k$$

Procedure:
* Identify the number of parameters $K$ to be estimated
* Create a system of equations setting the first $K$-th theoretical and sample moments equal to each other.
	* $\mu_k = M_k \,\,\,\forall x \in \{1, 2, \dots, K\}$
* Solve the equations for the parameters
* Put a hat on the final parameters to indicate they are estimators

Notes:
* Method of moments estimators are not necessarily [[Bias|unbiased]] estimators.
* Unlike the [[Maximum Likelihood Estimation|maximum likelihood estimator]] the method of moments estimator is not invariant under reparameterization so $g(\theta) \neq g(\hat\theta)$ in all cases.

> [!example]- Example: [[Exponential]] Distribution
> Let $x_i \overset{\mathrm{iid}}{\sim} Exp(\lambda)$. Calculate the method of moments estimator for the parameter $\lambda$.
> 
> For an exponential distribution $\mu_1 = E[X] = \frac{1}{\lambda}$
> 
> $K=1$ parameter to estimate so set $\mu_1 = M_1$
> $$\frac{1}{\lambda} = \frac{1}{n}\sum_{i=1}^nx_i = \bar{X}$$
> so:
> $$\hat{\lambda} = \frac{1}{\bar{X}}$$
> 
> This turns out to not be an unbiased estimator as: $$E[\hat\lambda] = \frac{n}{n-1}\lambda$$

> [!example]- Example: [[Gamma]] Distribution
> Let $x_i \overset{\mathrm{iid}}{\sim} \Gamma(\alpha, \beta)$. Calculate the method of moments estimator for the parameters $\alpha$ and $\beta$.
> 
> For a gamma distribution $\mu_1 = E[X] = \frac{\alpha}{\beta}$ and $\mu_2 = E[X^2] = \frac{\alpha}{\beta^2} + (\frac{\alpha}{\beta})^2$
> 
> $K=2$ parameters to estimate so set $\mu_1=M_1$ and $\mu_2=M_2$
> $$\frac{\alpha}{\beta} = \bar{X}$$
> $$\frac{\alpha}{\beta^2} + (\frac{\alpha}{\beta})^2 = \frac{1}{n}\sum_{i=1}^nx_i^2$$
> Can substitute $\bar{X}$ into the second equation as $\frac{\alpha}{\beta}$
> $$\frac{\bar{X}}{\beta} + \bar{X}^2 = \frac{1}{n}\sum_{i=1}^nx_i^2$$
> 
> Solving for $\beta$ and making it an estimator gives:
> $$\hat\beta = \frac{\bar{X}}{\frac{1}{n}\sum_{i=1}^nx_i^2 - \bar{X}^2}$$
> and solving for $\alpha$ and making it an estimator gives:
> $$\hat\alpha = \hat\beta\bar{X}$$


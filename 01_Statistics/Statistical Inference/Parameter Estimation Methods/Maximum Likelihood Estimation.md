Maximum Likelihood Estimation is a technique for calculating an [[Estimators|estimator]] from data $[x_1, x_2, \dots]$ by maximizing the likelihood function, under the assumed [[Probability Distribution]], so that the observed data is most probable. The likelihood function is defined as:
$$L(\theta) = \prod_{i=1}^n f(x_i;\theta)$$
where $f(x_i; \theta)$ is the probability mass/density function of the distribution, parameterized by $\theta$. 

And so the Maximum likelihood estimator is defined as:
$$\hat{\theta} = \underset{\theta \in\Theta}{\text{argmax }}L(\theta)$$
Where $\Theta$ is the set of all possible parameter values.

Fore a differentiable likelihood function, this is done by setting the first derivative of the likelihood function equal to zero, solving for the parameter, and putting a hat on the result to indicate that it is an estimator. It is also common to instead maximize the log likelihood function $\mathcal{L}(\theta) = \ln(L(\theta))$. The logarithm does not change the location of the maximum so this will have the same maximum as the likelihood function.

If $\hat\theta$ is the MLE for a parameter $\theta$, then the MLE for a function of that parameter $g(\theta)$ is simply $g(\hat\theta)$.
* This is called the **Invariance Property of MLE**

> [!example]- Example: [[Poisson]] Distribution
> Let $x_i \overset{\mathrm{iid}}{\sim} Poisson(\lambda)$. Calculate the MLE for the parameter $\lambda$. Also, use the result to calculate $P(x_i > 0)$
> 
> The pmf for each $x_i$ is
> $$f(x_i; \lambda) = \frac{\lambda^{x_i}e^{-\lambda}}{x_i!}$$
> 
> The likelihood function is given by:
> $$L(\lambda) = \prod_{i=1}^nf(x_i; \lambda) = \prod_{i=1}^n \frac{\lambda^{x_i}e^{-\lambda}}{x_i!} = \frac{\lambda^{n\bar{X}}e^{-n\lambda}}{\prod_{i=1}^nx_i!}$$
> 
> The log likelihood function is given by:
> $$\mathcal{L}(\lambda) = \ln(L(\lambda)) = \ln\left(\frac{\lambda^{n\bar{X}}e^{-n\lambda}}{\prod_{i=1}^nx_i!}\right) = n\bar{X}\ln(\lambda) - n\lambda - \ln(\prod_{i=1}^nx_i!)$$
> 
> Taking the derivative with respect to lambda of the log likelihood function and setting it equal to zero:
> $$\frac{\partial\mathcal{L}(\lambda)}{\partial\lambda} = \frac{n\bar{X}}{\lambda} - n = 0$$
> 
> Solving for $\lambda$ and making it an estimator gives:
> $$\hat\lambda = \bar{X}$$
> So the MLE for the Poisson distribution is just the [[Sample Mean]].
> 
> Now to find $P(x_i > 0)$, recognize that it is a function of $\lambda$
> $$
> \begin{split}
> g(\lambda) &= P(x_i > 0;\lambda) \\
> &= 1-P(x_i=0;\lambda) \\
> &= 1 -e^{-\lambda}
> \end{split}
> $$
> By the invariance property of MLEs $g(\lambda) = g({\hat\lambda})$ so:
> $$\widehat{P(x_i > 0)} = 1-e^{-\hat\lambda} = 1-e^{-\bar{X}}$$
> 
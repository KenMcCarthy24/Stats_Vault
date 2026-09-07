Given two [[Random Variable|Random Variables]] $X$ and $Y$, the **covariance** is a measure of the joint variability between the two. It is defined as:
$$
\begin{split}
Cov(X, Y) &= E[(X-E[X])(Y-E[Y])] \\
&=E[XY] - E[X]E[Y]
\end{split}
$$

If X and Y are [[Discrete Probability Distributions]], covariance is calculated as:
$$Cov(X, Y) = \sum_x \sum_y (x-\mu_x)(y-\mu_y)P(X=x, Y=y)$$
Where $P(X=x, Y=y)$ is their Joint Probability.

If X and Y are [[Continuous Probability Distributions]], covariance is calculated as:
$$Cov(X, Y) = \int_{-\infty}^\infty \int_{-\infty}^\infty (x-\mu_x)(y-\mu_y)f(x,y)dxdy$$
where $f(x, y)$ is the [[Joint and Multivariate Distributions#Joint Probability Distributions|Joint PDF]].

Some useful identities:
* $Cov(X,X) = Var(X) = \sigma^2$
* $Cov(aX + b, Y) = aCov(X, Y)$
* $Cov(X, Y+Z) = Cov(X, Y) + Cov(X, Z)$

A covariance of 0 indicates that $X$ and $Y$ are **uncorrelated**, meaning there is no linear dependence between them. They may still be statistically dependent in a nonlinear way. A positive or negative sign points towards either a positive or negative linear relationship. However, the magnitude of the covariance is not a good indicator of the strength of the relationship due to unit dependence. Because covariance depends on the units of $X$ and $Y$, it cannot be compared directly across different variable pairs.

# Correlation Coefficient
The correlation coefficient $\rho$ is a normalized version of the covariance between $X$ and $Y$ that is better suited for determining strength of linear dependence.
$$\rho_{X,Y} = \frac{Cov(X, Y)}{\sigma_x\sigma_y}$$
where $\sigma_x, \sigma_y$ are the standard deviations of $X$ and $Y$ respectively. 

The correlation coefficient always lies between -1 and 1 and can be interpreted as:
* More negative correlation coefficients are more strongly negatively related. As one goes up the other goes down.
* Correlation coefficients near 0 indicate there is no strong linear relationship
* More positive correlation coefficients are more strongly positively related. As one goes up the other also increases.

The correlation coefficient between a random variable and itself is always 1
$$\rho_{X, X}= \frac{Cov(X, X)}{\sigma_x^2} = \frac{\sigma_x^2}{\sigma_x^2} = 1$$

Note: there are several different types of correlation coefficient, the one described here is specifically the **Pearson Correlation Coefficient**, which measures linear association only.

# Covariance and Correlation Matrices
It is common to represent the various correlations between many random variables $X = [X_1, X_2, \dots, X_n]$ with means $\mu = [\mu_1, \mu_2, \dots, \mu_n]$ as a covariance matrix $\Sigma$. With each element $(i, j)$ being the pairwise Covariance $Cov(X_i, X_j)$. 
$$
\Sigma
=
E[(X-\mu)(X-\mu)^T]
=
\begin{pmatrix}
\operatorname{Var}(X_1) & \operatorname{Cov}(X_1,X_2) & \cdots & \operatorname{Cov}(X_1,X_n) \\
\operatorname{Cov}(X_2,X_1) & \operatorname{Var}(X_2) & \cdots & \operatorname{Cov}(X_2,X_n) \\
\vdots & \vdots & \ddots & \vdots \\
\operatorname{Cov}(X_n,X_1) & \operatorname{Cov}(X_n,X_2) & \cdots & \operatorname{Var}(X_n)
\end{pmatrix}
$$
Some properties:
* This is a symmetric matrix since $Cov(X_i, X_j) = Cov(X_j, X_i)$ so $\Sigma = \Sigma^T$
* The diagonal elements are the variances of the individual random variables.

A normalized correlation matrix is also often used where each element is the correlation coefficient between $X_i$ and $X_j$
$$
R = Corr(X)
=
\begin{pmatrix}
1 & \rho_{X_1,X_2} & \cdots & \rho_{X_1,X_n} \\
\rho_{X_2,X_1} & 1 & \cdots & \rho_{X_2,X_n} \\
\vdots & \vdots & \ddots & \vdots \\
\rho_{X_n,X_1} & \rho_{X_n,X_2} & \cdots & 1
\end{pmatrix}
$$

> [!example]-
> Given the following joint probability distribution, calculate the covariance and correlation coefficients.
> $$\begin{array}{c|ccc|c}
>  & Y=0 & Y=1 & Y=2 & P_X(x) \\ \hline
> X=0 & 0.10 & 0.20 & 0.10 & 0.40 \\
> X=1 & 0.20 & 0.10 & 0.30 & 0.60 \\ \hline
> P_Y(y) & 0.30 & 0.30 & 0.40 & 1.00
> \end{array}$$
> 
> $\mu_X = 0.6$, $\sigma^2_X = 0.24$
> $\mu_Y = 1.1$, $\sigma^2_Y = 0.69$
> 
> $$E[XY] = (0)(0.1) + (0)(0.2) + (0)(0.1) + (0)(0.2) + (1)(0.1) + (2)(0.3) = 0.7$$
> 
> $$Cov(X, Y) = E[XY]- E[X]E[Y] = 0.7 - (0.6)(1.1) = 0.04$$
> 
> $$\rho_{X,Y} = \frac{Cov(X, Y)}{\sigma_X \sigma_Y} = \frac{0.04}{\sqrt{0.24}\sqrt{0.69}} = 0.098$$
> 
> The variables exhibit a weak positive linear correlation.
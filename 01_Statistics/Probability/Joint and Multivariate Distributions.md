## Joint Probability Distributions

Two random variables $X$ and $Y$ have a continuous joint [[Probability Distribution|distribution]] if they take values on a continuous 2D plane ($\mathbb{R}^2$).

The probability that the pair $(X, Y)$ falls within a specific region $A$ is given by the volume under the **Joint Probability Density Function (Joint PDF)**:

$$P((X,Y) \in A) = \iint_A f(x,y) \,dx\,dy$$

### Requirements
The Joint PDF must satisfy:
* $f(x,y) \geq 0$ for all $x, y$
* $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) \,dx\,dy = 1$

### Cumulative Distribution Function
The **Joint Cumulative Distribution Function (CDF)** gives the probability that $X \le x$ and $Y \le y$:

$$F(x,y) = P(X \leq x, Y \leq y) = \int_{-\infty}^{y} \int_{-\infty}^{x} f(u,v) \,du\,dv$$

### Marginal Expectations
The **means** or **expectations** of the individual variables (Marginal Expectations) are derived from the joint density:

$$
\begin{aligned}
\mu_X &= E[X] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x f(x,y) \,dx\,dy \\
\mu_Y &= E[Y] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} y f(x,y) \,dx\,dy
\end{aligned}
$$

### Variability
The variability is described by the **[[Covariance and Correlation]]**, which measures how $X$ and $Y$ vary together:

$$
\begin{split}
\sigma_{XY} = Cov(X,Y) &= E[(X-\mu_X)(Y-\mu_Y)] \\
&= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} (x-\mu_X)(y-\mu_Y) f(x,y) \,dx\,dy \\
&= E[XY] - E[X]E[Y]
\end{split}
$$

### Independence
If the random variables $X$ and $Y$ are **statistically independent**, the covariance is 0 and the Joint PDF factorizes into the product of the individual Marginal PDFs: 

$$f(x,y) = f_X(x) \cdot f_Y(y)$$

---

## Multivariate Probability Distributions

A random vector $\mathbf{X} = (X_1, X_2, \dots, X_n)^T$ has a multivariate continuous [[Probability Distribution|distribution]] if it takes values in an $n$-dimensional space (e.g., $\mathbb{R}^n$).

The probability that $\mathbf{X}$ falls within a specific region $D$ is given by the multiple integral of the Joint Probability Density Function (Joint PDF), $f(\mathbf{x})$:

$$P(\mathbf{X} \in D) = \int \dots \int_D f(x_1, \dots, x_n) dx_1 \dots dx_n$$

### Requirements
The Joint PDF must satisfy:
* $f(\mathbf{x}) \geq 0$ for all $\mathbf{x} \in \mathbb{R}^n$
* $\int_{-\infty}^{\infty} \dots \int_{-\infty}^{\infty} f(x_1, \dots, x_n) dx_1 \dots dx_n = 1$

### Cumulative Distribution Function
The CDF gives the probability that every component $X_i$ is less than or equal to a specific value $x_i$. To calculate this, you integrate the Joint PDF from $-\infty$ up to the value of interest for each dimension: $$ \begin{split} F(x_1, \dots, x_n) &= P(X_1 \leq x_1, \dots, X_n \leq x_n) \\ &= \underbrace{\int_{-\infty}^{x_n} \dots \int_{-\infty}^{x_1}}_{\text{Integrate up to limit } x_i} f(t_1, \dots, t_n) \, dt_1 \dots dt_n \end{split} $$ ### Mean Vector The **Mean Vector** $\boldsymbol{\mu}$ contains the expected value of each component calculated individually. It is calculated by finding the expectation $E[X_i]$ for every dimension $i$ in the vector: $$ \boldsymbol{\mu} = E[\mathbf{X}] = \begin{bmatrix} E[X_1] \\ E[X_2] \\ \vdots \\ E[X_n] \end{bmatrix} $$ Where each element $E[X_i]$ is calculated by integrating $x_i$ weighted by the joint PDF over the entire $n$-dimensional space: $$ E[X_i] = \int_{-\infty}^{\infty} \dots \int_{-\infty}^{\infty} x_i f(x_1, \dots, x_n) \,dx_1 \dots dx_n $$
### Covariance Matrix
The **variance** is generalized by the **[[Covariance and Correlation]] Matrix** $\boldsymbol{\Sigma}$, which captures the variance of each component and the correlations between them:

$$
\begin{split}
\boldsymbol{\Sigma} = Cov(\mathbf{X}) &= E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T] \\
&= E[\mathbf{X}\mathbf{X}^T] - \boldsymbol{\mu}\boldsymbol{\mu}^T
\end{split}
$$

### Independence
If all components of the random vector $\mathbf{X}$ are mutually independent, the covariance matrix becomes diagonal and the Joint PDF is simply the product of the marginal PDFs of each individual component: 
$$f(x_1, \dots, x_n) = \prod_{i=1}^n f_{X_i}(x_i)$$
Examples: [[Multivariate Normal]], [[Dirichlet]]

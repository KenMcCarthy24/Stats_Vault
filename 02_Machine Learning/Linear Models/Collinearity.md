In regression, **Collinearity** (or **Multicollinearity**) arises when one predictor in an $(n \times p+1)$ data matrix $X$ is a near linear combination of one or more other predictors. If that predictor is an exact linear combination of others, it is called **Perfect Collinearity**.

Collinearity is a problem when performing [[Ordinary Least Squares (OLS)]], as perfect collinearity will mean that $X$ is not full rank, and thus $(X^TX)^{-1}$ is not invertible, as the system of equations has infinitely many solutions. Imperfect collinearity will similarly cause numerical instability. 

# Diagnosing Collinearity
There are two standard methods for diagnosing if the matrix $X$ has a problematic amount of collinearity.

### Condition Number $\kappa$
The condition number $\kappa$ is defined as the ratio of the largest to the smallest of the eigenvalues $\lambda$ of the matrix $X^TX$.
$$\kappa = \sqrt{\frac{\lambda_{max}}{\lambda_{min}}}$$
A common rule of thumb is that $\kappa > 30$ indicates severe, harmful collinearity. If perfect collinearity is present, then $\kappa=\infty$ as at least one of the eigenvalues of $X^TX$ will be 0 due to not being full rank.

### Variance Inflation Factor
The Variance Inflation Factor (VIF) quantifies how much variance of an estimated regression coefficient is increased due to collinearity. It measures how much the variance of an estimated regression coefficient $\hat \beta_j$ is "inflated" compared towhat it would be if the predictor $x_j$ were uncorrelated to other predictors. The VIF is calculated as:
$$VIF_j = \frac{1}{1-R_j^2}$$
Where $R_j^2$ is the [[Goodness of Fit#Coefficient of Determination ($R 2$)|Coefficient of Determination]] ($R^2$) obtained from regressing the predictor $x_j$ on **all other predictors** of the model.

A common rule of thumb is to avoid a VIF value exceeding 5, with $VIF > 10$ indicating severe collinearity.

---

> [!example]-
> Consider this matrix, where $x_3 \approx x_1 + x_2$ with a little bit of noise to avoid perfect collinearity.
> $$X =  \begin{pmatrix}
>  1&  -3&  -2.1\\
>  2&  2&  3.9\\
>  -4&  5&  1.1\\
>  2&  -1&  1.1\\
>  1&  3&  4.2\\
> \end{pmatrix}$$
> Calculate the condition number $\kappa$ and the VIF of $\beta_3$ in order to demonstrate the collinearity present. 
> 
> The Eigenvalues of the matrix $X^TX$ are $\lambda = (0.017664, 36.881999, 76.780338)$, thus:
> $$\kappa = \sqrt{\frac{\lambda_{max}}{\lambda_{min}}} = \sqrt{\frac{76.780338}{0.017664}} =65.93$$
> $\kappa > 30$ so that indicates severe collinearity.
> 
> Now, the $R^2$ value obtained from the model $x_3 = \beta_0 + \beta_1x_1 + \beta_2x_2$ is $R_3^2 = 0.9979$. Thus the VIF is:
> $$VIF_3 = \frac{1}{1-0.9979} = 476.19$$
> This is much greater than 10, once again indicating severe collinearity. 
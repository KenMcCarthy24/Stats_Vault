**Principal Component Analysis (PCA)** is a dimensionality reduction technique used to map high dimensional data down to a lower dimensional space while retaining maximum variance.

Given a dataset with $n$ observations $[X_1, X_2, ... X_n]$ where each $X_i$ is a data vector with $p$ features. This means that the total data matrix $X$ is an $(n \times p)$ dimensional matrix.  

Each data vector lives in $p$-dimensional space, but not every dimension has as much variance as the others. Data may vary widely in some dimensions and barely vary at all in others. PCA seeks a smaller $p'$ number of dimensions to project the data onto such that the new dimensions have the maximum possible amount of variance. 

PCA is often used either as a step in a data processing pipeline to reduce the dimensionality of the data or to reduce high dimensional data to 2 or 3 dimensions for the purpose of visualization.

# Principal Components
![[principal_components.svg]]
Let $\phi_1 = [\phi_{11}, \phi_{21}, \dots, \phi_{p1}]$ be a $(p \times 1)$ unit vector (meaning $\sum_{i=1}^n\phi_{j1}^2 = 1$) representing the **first principal component** of the data X. Its values are such that the projection of $X$ onto $\phi_1$:
$$X\phi_1 = \phi_{11}X_1 + \phi_{21}X_2 + \dots + \phi_{p1}X_p$$
has the largest possible variance.

Geometrically, $\phi_1$ represents the vector in the $p$-dimensional data space where the data varies the most. 

The second principal component $\phi_2$ is then defined similarly as the unit vector in $p$-dimensional space where the data varies the most **AND** that is orthogonal to $\phi_1$ (e.g. $\phi_1 \cdot \phi_2 = 0$). The projection of $X$ onto $\phi_2$ is then given by: 
$$X\phi_2 = \phi_{12}X_1 + \phi_{22}X_2 + \dots + \phi_{p2}X_p$$
In general, $X$ will have $p$ principal components, with the $k$-th principal component $\phi_k$ defined as a unit vector in $p$-dimensional space where the data varies the most **AND** that is orthogonal to all previous principal components $[\phi_{k-1}, \dots, \phi_1]$. The projection of $X$ onto $\phi_k$ is:
$$X\phi_k = \phi_{1k}X_1 + \phi_{2k}X_2 + \dots + \phi_{pk}X_p$$

Assuming that $X$ is a mean centered matrix ($mean(X_i) \approx 0$), the principal components can efficiently be found by using eigen-decomposition of the covariance matrix 
$$Cov(X)=\frac{1}{n-1}X^TX$$
If $X$ is not mean centered, it must be transformed to be mean centered by subtracting the values in each column by the column's mean before performing PCA. It is common to completely standardize the data (subtract mean and divide by standard deviation) so that features measured in larger units don't dominate the principal components. 

The first principal component $\phi_1$ is the eigenvector of the covariance matrix that has the largest corresponding eigenvalue. The second principal component $\phi_2$ is the eigenvector with the second largest eigenvalue, and so on. The $(p \times p)$ PCA transformation matrix used to transform the data to the new principal component basis $\Phi_p = [\phi_1, \phi_2, \dots, \phi_p]$ is therefore the eigenvectors of $X^TX$ sorted by their respective eigenvalues descending. 

The data $X$ can be projected onto only the first $k$ principal components by using the $(p \times k)$ matrix $\Phi_k$, which is  the first $k$ columns of $\Phi_p$ as $X' = X\Phi_k$. For example, to map the data to the first two principal components in order to plot it in 2D, perform the transformation $X' = X\Phi_2$.

> [!NOTE]
> In practice, principal components are usually calculated using [[Singular Value Decomposition]] due to better computational efficiency.

# Explained Variance
The proportion of the variance explained by each principal component can be determined by looking at the eigenvalues associated with each principal component's eigenvector.

Let $[\lambda_1, \lambda_2, \dots, \lambda_p]$ be the descending sorted list of eigenvalues associated with the $p$ principal components. The proportion of variance explained by each $\lambda_i$ is:
$$\%Var_i = \frac{\lambda_i}{\sum_{j=1}^p\lambda_j}$$
This variance explained can be used for deciding how many principal component dimensions to keep in the transformation matrix to reduce the number of dimensions as much as possible without discarding too much of the variance in the data.

> [!Example]-
> Imagine a set of eigenvalues associated with the 10 principal components of a 10-dimensional data set
> $$[25, 10, 6, 1.2, 0.5, 0.4,0.2, 0.05, 0.001, 0.0005]$$
> The respective percentage variance explained by these would be:
> $$[0.577,0.231, 0.138, 0.028, 0.011, 0.0092, 0.0046, 0.0012, 0.000023, 0.000015]$$
> 94.6% of the variance can be explained by just the first three principal components, with subsequent components only explaining small amounts of variance. So a logical dimensionality reduction choice might be to project $X$ onto just the first three principal components as $X' = X\Phi_3$.


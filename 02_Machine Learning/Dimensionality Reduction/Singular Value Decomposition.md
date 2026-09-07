**Singular Value Decomposition (SVD)** is a linear algebra technique used to factorize a matrix into three distinct component matrices. It is related to [[Principal Component Analysis]] (PCA) and is generally the standard algorithm used under the hood by machine learning libraries to perform dimensionality reduction.

Given a dataset represented by an $(n \times p)$ dimensional matrix $X$, where $n$ is the number of observations and $p$ is the number of features. SVD states that this matrix can be perfectly decomposed into the product of three distinct matrices:
$$X = U\Sigma V^T$$

# The Component Matrices
The three matrices derived from SVD provide a geometric breakdown of the transformations applied to the data space:

* **$U$ (Left Singular Vectors):** An $(n \times n)$ orthogonal matrix. Its columns form an orthonormal basis for the column space of $X$. In the context of a dataset, these vectors capture the relationships and patterns between the $n$ observations.
* **$\Sigma$ (Singular Values):** An $(n \times p)$ diagonal matrix. The non-negative values on its diagonal, denoted as $[\sigma_1, \sigma_2, \dots, \sigma_p]$, are called **singular values**. These values are always sorted in descending order ($\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_p \ge 0$). They represent the magnitude or "strength" of the variance along each respective singular vector.
* **$V^T$ (Right Singular Vectors transposed):** A $(p \times p)$ orthogonal matrix. The columns of $V$ (or rows of $V^T$) form an orthonormal basis for the row space of $X$. These vectors represent the principal directions of the feature space.

# Connection to PCA
Calculating the principal components in PCA involves finding the eigenvectors of the data's covariance matrix, which is proportional to $X^TX$ (assuming the matrix $X$ is mean-centered).

If we substitute the SVD factorization of $X$ into $X^TX$, we get:
$$X^TX = (U\Sigma V^T)^T(U\Sigma V^T)$$
$$X^TX = V\Sigma^T U^T U\Sigma V^T$$
Because $U$ is an orthogonal matrix, multiplying it by its transpose results in the identity matrix ($U^TU = I$). Therefore, the equation simplifies to:
$$X^TX = V\Sigma^2 V^T$$
This result is exactly the eigen-decomposition of $X^TX$. This proves two relationships:
1.  The right singular vectors $V$ from SVD are exactly the same as the principal components (eigenvectors) $\Phi$ found in PCA.
2.  The singular values $\sigma_i$ are directly related to the PCA eigenvalues $\lambda_i$ by the equation $\lambda_i = \frac{\sigma_i^2}{n-1}$.

In practice, explicitly calculating the covariance matrix $X^TX$ can be computationally expensive and prone to numerical instability (floating-point precision errors) for very large, high-dimensional datasets. Because of this, applying SVD directly to the mean-centered matrix $X$ is the preferred computational method for solving PCA.

# Dimensionality Reduction
Just as PCA projects data onto the first $k$ principal components, SVD reduces dimensionality by keeping only the top $k$ components. 

By retaining only the largest $k$ singular values in $\Sigma$ and the corresponding $k$ columns of $U$ and $V$, we create $X'$, a compressed approximation of the original matrix:
$$X' \approx U_k\Sigma_k V_k^T$$
This technique is called **Truncated SVD**. According to the Eckart-Young-Mirsky theorem, this specific truncation guarantees the best possible lower-rank approximation of the original data.

To project the original data into this new, lower-dimensional space (e.g., transforming a 100-feature dataset down to 3 dimensions), you simply multiply the original data by the truncated right singular vectors:
$$X_{reduced} = XV_k$$

# Explained Variance
Because the eigenvalues from PCA are proportional to the squared singular values from SVD, the proportion of variance explained by each singular vector can be calculated directly from the $\Sigma$ matrix. 

The percentage of the total variance explained by the $i$-th singular value is:
$$\%Var_i = \frac{\sigma_i^2}{\sum_{j=1}^p\sigma_j^2}$$

> [!Example]-
> Imagine a dataset with 5 features where the SVD yields the following singular values on the diagonal of $\Sigma$:
> $$[10, 5, 2, 1, 0.5]$$
> First, square the singular values to relate them to variance:
> $$[100, 25, 4, 1, 0.25]$$
> The sum of these squared values is $130.25$. The percentage of total variance explained by each component is:
> $$[0.768, 0.192, 0.031, 0.008, 0.002]$$
> The first two singular values alone account for 96% ($76.8\% + 19.2\%$) of the data's variance. Therefore, using Truncated SVD with $k=2$ would be a highly efficient way to reduce this dataset to 2 dimensions with minimal information loss.
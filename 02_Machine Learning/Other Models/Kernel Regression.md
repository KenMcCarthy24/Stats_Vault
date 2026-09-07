**Nadaraya-Watson Kernel Regression** or **Kernel Smoothing** is a non-parametric regression technique that estimates a function based on data by using a rolling **kernel** window to compute a weighted moving average. Given the true model $y_i = f(x_i) + \varepsilon_i$, the kernel regression estimate of $f$ is given by:
$$\hat y = \hat f(x) = \frac{\sum_{i=1}^nK(\frac{x-x_i}{\lambda})y_i}{\sum_{i=1}^nK(\frac{x-x_i}{\lambda})}$$
where:
* $K(.)$ is the **kernel function**
	* Must be a non-negative real function such that $K(x) = K(-x)$ for all values of x.
	* Must be true that $\int K(x)dx = 1$
* $\lambda$ is the **bandwidth**
	* This acts as a smoothing factor
	* Larger bandwidth results in a smoother curve (risk underfitting)
	* Smaller bandwidth results in a less smooth curve (risk overfitting)

This is just a weighted average over all data points:
$$\hat f(x) = \frac{\sum_{i=1}^n w_iy_i}{\sum_{i=1}^n w_i}$$with weights $w_i = K(\frac{x-x_i}{\lambda})$

Common Kernels:
* Uniform: $K(z) = 0.5$ for $|z| \leq 1$
* Gaussian: $K(z) = \frac{1}{\sqrt{2\pi}} exp\left(-\frac{z^2}{2}\right)$
* Epanechnikov: $\frac{3}{4}(1-z^2)$ for $|z| \leq 1$
![[kernels_example.svg]]

---
# Example
The below plot show an example of these three kernels applied to regress some noisy sinusoidal data. For each kernel $\lambda=1$ for this plot. 
![[kernels_smoothing_example.svg]]
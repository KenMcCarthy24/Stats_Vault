For two sets of observations $\{x_1, \dots, x_n\}$ and $\{y_1, \dots, y_n\}$ with sample means $\bar{x}$ and $\bar{y}$, the **sample covariance** measures the degree to which the two variables change together.

Similar to [[Sample Variance and Standard Deviation|Sample Variance]], the unbiased estimator for the population covariance uses $n-1$:

$$s_{xy} = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})$$

* **Positive $s_{xy}$:** Indicates that when $x$ increases, $y$ tends to increase.
* **Negative $s_{xy}$:** Indicates that when $x$ increases, $y$ tends to decrease.
* **Zero $s_{xy}$:** Indicates no linear relationship.

---
# Sample Covariance Matrix

When dealing with multivariate data represented by an $n \times p$ data matrix $\mathbf{X}$ (where columns represent variables), the **sample covariance matrix** $\mathbf{S}$ is a $p \times p$ symmetric matrix that summarizes the covariances between all pairs of variables.

An element $s_{jk}$ in the matrix represents the covariance between the $j$-th and $k$-th variables:

$$\mathbf{S} = \begin{bmatrix} 
s_{11} & s_{12} & \cdots & s_{1p} \\
s_{21} & s_{22} & \cdots & s_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
s_{p1} & s_{p2} & \cdots & s_{pp} 
\end{bmatrix}$$

Where:
* The **diagonal elements** ($s_{jj}$) are the **[[Sample Variance and Standard Deviation|sample variances]]** of each variable ($s_j^2$).
* The **off-diagonal elements** ($s_{jk}$ where $j \neq k$) are the sample covariances between variables $j$ and $k$.

In matrix notation, if $\mathbf{X}_c$ is the **centered data matrix** (where the column means have been subtracted from each observation), $\mathbf{S}$ can be calculated as:

$$\mathbf{S} = \frac{1}{n-1} \mathbf{X}_c^\top \mathbf{X}_c$$

---
# Sample Correlation Matrix

Because covariance depends on the scale (units) of the variables, it is often normalized to produce the **sample correlation matrix** $\mathbf{R}$.

The correlation coefficient $r_{jk}$ between variables $j$ and $k$ is obtained by dividing the covariance by the product of their [[Sample Variance and Standard Deviation|standard deviations]]:

$$r_{jk} = \frac{s_{jk}}{s_j s_k} = \frac{s_{jk}}{\sqrt{s_{jj} s_{kk}}}$$

This results in the $p \times p$ matrix $\mathbf{R}$:

$$\mathbf{R} = \begin{bmatrix} 
1 & r_{12} & \cdots & r_{1p} \\
r_{21} & 1 & \cdots & r_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
r_{p1} & r_{p2} & \cdots & 1 
\end{bmatrix}$$

* **Diagonal elements:** Always equal to 1 (a variable's correlation with itself).
* **Range:** All values are bounded between $-1$ and $1$.

### Interpretation of Correlation Values

The correlation coefficient $r_{jk}$ provides a standardized measure of the linear relationship between variables.

* **Magnitude (Strength):**
    * **$|r_{jk}| \approx 1$:** Indicates a strong linear relationship. The points lie close to a straight line.
    * **$|r_{jk}| \approx 0$:** Indicates a weak or no linear relationship. The points appear as a random cloud with no discernible direction.

* **Direction:**
    * **Positive ($r_{jk} > 0$):** Variables move in the same direction (as one increases, the other increases).
    * **Negative ($r_{jk} < 0$):** Variables move in opposite directions (as one increases, the other decreases).
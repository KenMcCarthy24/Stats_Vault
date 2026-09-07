**K-Nearest Neighbors** (KNN) is a simple non-parametric [[Classification Problem|Classification]] algorithm that determines the class of a data point $x^*$ based on the majority class of its $k$ nearest neighbors from a pre-existing set of data points $X=[x_1, x_2, ...,x_n]$ with known classifications  $y = [y_1, y_2, ..., y_n]$. Each $x$ in this case is a vector with $p$ features.

# Steps
K-Nearest Neighbors is performed by performing the following steps.
1. Calculate the distance $d_i$ between $x^*$ and each $x_i \in X$ according to some distance metric $D(x^*, x_i)$
2. Determine the $k$ smallest distances, these are the $k$ nearest neighbors to $x^*$
3. Look up the class of each of the $k$ nearest neighbors
4. The majority class among the $k$ nearest neighbors is assigned to $x^*$ as $\hat y$

This process has two hyperparameters that can be adjusted to achieve the best fit:
* **$k$**: The number of nearest neighbors to base the classification on
* **Distance Metric $D$**: The chosen method of measuring distance between points

### Implementation Notes
* **Feature Scaling**: KNN relies entirely on distance, so features with larger numerical ranges can dominate the calculation. Because of this it is important to standardize the data a a pre-processing step
* **Tie Breaking**: If there is a tie between classes than KNN is inconclusive. This can be fixed by decreasing $k$ by 1 in the case of a tie and re-running or by only considering odd numbered choices of $k$ in the first place
* **Regression**: KNN can also be used as a regression algorithm with a slight modification. Instead of taking the majority class vote of the $k$ nearest neighbors, instead set $\hat y=mean(y_k)$ where $y_k$ are the target values for the $k$ nearest neighbors

# Bias Variance Tradeoff
As $k$ increases, the complexity of the model decreases, leading to lower variance and higher bias due to the [[Bias-Variance Tradeoff]]:
* At $k=1$ the model is at its most complex and is highly dependent on the specific set of training data, always only taking one point into account. This has maximum variance and low bias.
* As $k$ increases the model is forced to look at more points. The decision boundaries smooth out and become simpler. This leads to better lower variance as it is less depending on single training points and higher bias as it starts potentially ignoring underlying patterns in the data
* At the most extreme $k=n$, the model will always predict the majority class in the training data. This has maximum bias and zero variance.
* Somewhere in the middle is a value of $k$ where bias and variance are balanced

# Distance Metrics
There are several possible choices for distance metrics to use with KNN including:
* Euclidean Distance ($L_2$ Norm)$$D(x^*, x_i) = ||x^*-x_i||_2 = \sqrt{\sum_{j=1}^p (x^*_j-x_{i,j})^2}$$
* Manhattan Distance ($L_1$ Norm)$$D(x^*, x_i) = ||x^*-x_i||_1 = \sum_{j=1}^p |x^*_j-x_{i,j}|$$
* Minkowski Distance ($L_p$ Norm)$$D(x^*, x_i) = ||x^*-x_i||_p = (\sum_{j=1}^p |x^*_j-x_{i,j}|^p)^{1/p}$$

Quantiles are a series of statistical cut-off points that divide the range of a [[Probability Distribution]] or sorted dataset in to $q$ equal sized subsets. 

The $k$-th $q$-quantile is the value below which a $\frac{k}{q}$ fraction of the data falls. Formally, $x$ is a $k$-th $q$-quantile for a [[Random Variable]] $X$ if:

$$P(X < x) \leq \frac{k}{q}$$
and 
$$
P(X \leq x) \geq \frac{k}{q}
$$

For sample data or for [[Discrete Probability Distributions]], quantiles are not necessarily unique, however for [[Continuous Probability Distributions]], quantiles are unique so long as the CDF is strictly increasing. 

# Common Quantiles:
Any number of divisions can be used, but specific $q$-quantiles have standardized names:

* **Median**: q=2. Divides the data into 2 parts.
* **Quartiles**: q=4. Divides the data into 4 parts.
	* The **Interquartile Range (IQR)** is defined as the distance between the first and the third quartiles ($Q_3 - Q_1$), representing the middle 50% of the data. Often used as a measure of variability that ignores outliers.
* **Quintiles**: q=5. Divides the data into 5 parts.
* **Deciles**: q=10. Divides the data into 10 parts.
* **Percentiles**: q=100. Divides the data into 100 parts. 

# Sample Quantiles

For a finite dataset (sample) of size $n$, quantiles are defined in terms of the **ordered sample values**, called *order statistics*. Let
$$
x_1 \le x_2 \le \cdots \le x_n
$$
denote the sample sorted in nondecreasing order.

Sample quantiles are estimates of the corresponding population quantiles. Unlike population quantiles, **sample quantiles are not uniquely defined** in general, because the desired probability level may fall between two observed data points.

As a result, multiple conventions exist for defining sample quantiles, including:
- **Nearest-rank methods**, which select an order statistic directly
- **Linear interpolation methods**, which interpolate between adjacent order statistics
# Quantile Function

The quantile function $Q(p)$ of a [[Probability Distribution]] is defined as a function that takes in a probability $p \in (0, 1)$ and returns the value from the distribution below which that proportion of the data falls.

If the Cumulative Distribution Function (CDF) $F(x)$ of the distribution is strictly increasing then $Q(p)$ is the inverse of the CDF so:
$$F(x) = p $$
and 
$$F^{-1}(p)=Q(p) = x$$

The $q$-quantiles for the distribution can be found by plugging in the values $\{1/q, 2/q, \dots, (q-1)/q\}$ into $Q(p)$


> [!example]-
> Derive the Quantile function for the [[Exponential]] with parameter $\lambda$ and use it to find the quantiles and the Interquartile Range
> 
> The CDF $F(x)$ for the exponential distribution is:
> $$F(x) = 1-e^{-\lambda x} \text{ , } x\geq 0$$
> The Quantile function $Q(p)$ is the inverse of this function:
> $$Q(p) = \frac{-\ln(1-p)}{\lambda}$$
> The quartiles are given by:
> * $\displaystyle Q_1 = Q(1/4) = \frac{-\ln(3/4)}{\lambda}$
> * $\displaystyle Q_2 = Q(2/4) = \frac{-\ln(1/2)}{\lambda}$
> * $\displaystyle Q_3 = Q(3/4) = \frac{-\ln(1/4)}{\lambda}$
> 
> And the IQR is:
> $$IQR = Q_3 - Q_1 = \frac{-\ln(1/4)}{\lambda} - \frac{-\ln(3/4)}{\lambda} = \frac{\ln(3)}{\lambda}$$


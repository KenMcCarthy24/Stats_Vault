Given a vector of logits $X=(x_1, x_2, ..., x_n)$, where $X \in \mathbb{R}^n$, the SoftMax function is a method for turning that vector into a properly normalized probability distribution. It is commonly used as an activation function for neural networks when performing classification tasks, the output representing the probability that the input falls into the various categories.

It is defined as:
$$SoftMax(X,T)=\frac{e^{x_i/T}}{\displaystyle \sum_{j=1}^n e^{x_j/T}}\text{ for each }x_i \in X$$
where $T$ is the **Temperature**, controlling the smoothness of the resulting probability distribution. $T$ is between 0 and $\infty$.
* $T=1$ is considered the standard, neutral option.
*  Lower $T$ makes the distribution more conservative and peaked at the higher input logits.
* Higher $T$ reduces the influence of high input logits, increasing diversity and randomness.

The output of the SoftMax function is a valid probability distribution as:
* The results will always sum to 1
* The results will all be non-zero.

> [!example]-
> Let $X = (2.1, -0.1, 3.1, 2.2, 0.5, -1.1)$
> 
> If $T=1$ then:
> $$SoftMax(X,1) = (0.19, 0.02, 0.53, 0.21, 0.04, 0.01)$$
> This has a strong peak at $x_3$, some probability at $x_1$ and $x_4$, and low probability for $x_2$, $x_5$, and $x_6$.
> 
> While if $T=3$ then:
> $$SoftMax(X,3) = (0.21, 0.1, 0.29, 0.21, 0.12, 0.07)$$
> The maximum probability is still at $x_3$, but the probabilities have been smoothed so that they now all have a reasonable magnitude.
> 
> Taking to an extreme, when $T=1000$:
> $$SoftMax(X,1000) \approx (1/6,1/6,1/6, 1/6, 1/6,1/6)$$
> The distribution has become essentially uniform.


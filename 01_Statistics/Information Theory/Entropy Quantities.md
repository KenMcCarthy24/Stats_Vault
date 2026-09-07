![[info_theory_venn.png]]

# Entropy
In information theory, **Entropy** (or **Shannon Entropy**) is a measure of the average uncertainty or surprise associated with the outcomes of a [[Random Variable]].
* High entropy means that the outcome is unpredictable and uncertain, being spread out mostly evenly among many possible outcomes.
* Low entropy means that the outcome is highly predictable, with one or few outcomes being very likely.

Given a random variable $X$ which takes values in the set $\mathcal X$, entropy $H$ is defined as the expectation value of the [[Information|Information Content]] $I(x)$ across all $x \in \mathcal X$.

For a [[Discrete Probability Distributions|Discrete Random Variable]], this is:
$$H(X) = E[I(x)] = E[-\log_b(P(x))] = -\sum_{x \in \mathcal X} P(x)\log_bP(x)$$
with the convention that $0 \log_b 0 = 0$. Entropy cannot be negative. 

For a [[Continuous Probability Distributions|Continuous Random Variable]], entropy is known as **differential entropy** and is:
$$H(X) = -\int f(x)\log_bf(x)dx$$
unlike regular entropy, differential entropy can be negative. 

If the logarithm base $b=2$, the units of entropy are "bits" and if the base $b=e$ the units of entropy are "nats". The same units as Information Content. 

The maximum possible entropy for a discrete variable with $|\mathcal X|=n$ outcomes is $\log_b(n)$, which occurs when the distribution is uniform. This is due to uncertainty being maximized when no outcome is favored. 

> [!example]- Fair 6-Sided Die
> What is the entropy associated with rolling a fair 6-sided die. (follows [[Discrete Uniform]] distribution)
> 
> Since all outcomes are equally likely with $P(x) = 1/6$:
> $$H(X) = -\sum_{i=1}^{6} \frac{1}{6} \log_2 \frac{1}{6} = \log_2 6 \approx 2.585 \text{ bits}$$
>

> [!example]- Skewed distribution
> What is the entropy associated with a heavily skewed [[Categorical]] distribution where:
> * $P(X=1)=0.95$
> * $P(X=2) = 0.04$
> * $P(X=3) = 0.01$
> 
> $$H(X) = -[0.95\log_2(0.95)+0.04\log_2(0.04)+0.01\log_2(0.01)] = 0.322 \text{ bits}$$
> Low entropy due to high certainty that $X$ probably equals 1. 

---
# Joint Entropy
**Joint Entropy** measures the total uncertainty associated with a set of random variables (e.g. $X$ and $Y$). It is defined as the average uncertainty over their joint probability distribution. 
$$H(X, Y) = -\sum_{x \in \mathcal X, y \in \mathcal Y} P(x, y)\log_bP(x, y)$$
where $P(x, y)$ is the joint probability. 

In the continuous case:
$$H(X, Y) = -\int\int f(x, y)\log_bf(x, y)dydx$$
Properties of Joint Entropy:
* **Relationship to Individual Entropy**: $H(X, Y) \leq H(X) + H(Y)$
	* The total uncertainty is at most the sum of individual uncertainties; any shared information reduces the joint entropy below this bound.
* **Independence**: If $X$ and $Y$ are independent then $H(X, Y) = H(X) + H(Y)$
* **Perfect Dependence**: If $X$ and $Y$ are perfectly dependent (e.g. $Y=X^2$) then $H(X, Y)=H(X)=H(Y)$

> [!example]- Independent Events
> Let $X$ and $Y$ be the result of two independent fair coin flips. What is $H(X, Y)$. 
> 
> $H(X) = H(Y) = 1$ bit due to being a single fair 50/50 flip.
> 
> The joint probability for any combination of heads and tails is $P(X=x, Y=y)=0.25$ so:
> $$H(X, Y) = -(4)(0.25)\log_2(0.25) = 2 \text{ bits}$$
> This demonstrates that for two independent events $H(X, Y) = H(X) + H(Y)$

> [!example]- Non-Independent Events
> Consider a join distribution over $X, Y \in \{0, 1\}$
> 
> |     | X=0  | X=1  |
> | --- | ---- | ---- |
> | Y=0 | 0.45 | 0.05 |
> | Y=1 | 0.05 | 0.45 |
> Calculate the Joint entropy $H(X, Y)$. How does it compare to $H(X) + H(Y)$
> 
> The Marginal probability of all outcomes is 0.5 so $H(X) + H(Y) = 1 + 1 = 2$
> 
> The Joint probability is:
> $$H(X, Y) = -[0.45\log_2(0.45) + 0.05\log_2(0.05) + 0.45\log_2(0.45) + 0.05\log_2(0.05)] = 1.47 \text{ bits}$$
> In this case $X$ and $Y$ are not independent of each other so $H(X, Y) < H(X) + H(Y)$


---
# Conditional Entropy

**Conditional Entropy** measures the average uncertainty associated with outcomes of a random variable $Y$ *given* that the value of another random variable $X$ is already measured/known. It is defined as:
$$H(Y|X) = \sum_{x\in \mathcal X}P(x)H(Y|X=x)$$
where $H(Y|X=x)$ is the entropy calculated using the conditional probability $P(y|x)$. This is essentially a weighted average of conditional entropies for different values of $X$. It can be expanded as:
$$H(Y|X) = -\sum_{x \in \mathcal X, y \in \mathcal Y} P(x, y)\log_bP(y|x)$$
where $P(x, y)$ is the joint probability. 

In the continuous case:
$$H(Y|X) = \int\int f(x, y)\log_bf(y|x)dydx$$

Properties of Conditional Entropy:
* **Completely Dependent Case**: If $Y$ is completely determined by $X$ (e.g. $Y=X^2$) then knowing $X$ leads to zero uncertainty in $Y$, so $H(Y|X)=0$
* **Independence Case**: If $Y$ is completely independent of $X$ then knowing $X$ doesn't give any information about $Y$ so $H(Y|X) = H(Y)$
* **Bounds**: The above two cases create bounds so $0 \leq H(Y|X) \leq H(Y)$
	* Knowing more can never increase the entropy, but it can add nothing. 
* **Chain Rule**: $H(X, Y) = H(X) + H(Y|X)$
	* Total uncertainty (Joint Entropy) of a pair of random variables is the uncertainty in $X$ plus the remaining uncertainty in $Y$ once $X$ is known.
	* Also works other way around so $H(X, Y) = H(Y) + H(X|Y)$
* **Asymmetry**: In general $H(Y|X) \neq H(X|Y)$

> [!example]- Simple Joint Distribution 
> Consider a joint distribution over $X, Y \in \{0, 1\}$ with joint probabilities given by the following table. Compute $H(Y|X)$ in bits.
> 
> |     | X=0 | X=1 |
> | --- | --- | --- |
> | Y=0 | 0.4 | 0.2 |
> | Y=1 | 0.1 | 0.3 |
> The marginals are $P(X=0)=0.5$ and $P(Y=0)=0.5$
> 
> The conditionals are:
> * $P(Y=0|X=0)=0.8$
> * $P(Y=1|X=0)=0.2$
> * $P(Y=0|X=1)=0.4$
> * $P(Y=1|X=1)=0.6$
> 
> so:
> * $H(Y|X=0)=-0.8\log_2(0.8)-0.2\log_2(0.2) = 0.722$
> * $H(Y|X=1) = -0.4\log_2(0.4) - 0.6\log_2(0.6) = 0.971$
> 
> Taking the weighted average of these by the marginals
> $$H(Y|X) = (0.5)(0.722) + (0.5)(0.971) = 0.847 \text{ bits}$$

> [!example]- Asymmetry
> Let $X$ be the results of rolling a fair six sided die and define:
> $$Y =  \left\{\begin{matrix}
> 0 \text { if X is even}\\
> 1 \text { if X is odd}
> \end{matrix}\right.$$
> Compute both $H(Y|X)$ and $H(X|Y)$
> 
> Since $Y$ is fully determined when $X$ is known, it is immediately apparent that $H(Y|X)=0$
> 
> For $H(X|Y)$
> * Given $Y=0$ (even), $X$ is uniform over $\{2, 4, 6\}$, giving entropy $\log_2(3)$
> * Given $Y=1$ (odd), $X$ is uniform over $\{1, 3, 5\}$, giving entropy $\log_2(3)$
> * $P(Y=0)=P(Y=1)=0.5$
> 
> So the weighted sum is:
> $$H(X|Y) = 0.5\log_2(3) + 0.5\log_2(3) = \log_2(3) = 1.585 \text{ bits}$$
> This demonstrates that $H(Y|X) \neq H(X|Y)$ in this example, demonstrating asymmetry.

# Mutual Information

**Mutual Information** between two random variables $X$ and $Y$ measures how much knowing one variable reduces the uncertainty about the other. Alternatively, it can be thought of as the amount of shared information between $X$ and $Y$. It can be equivalently defined using either joint entropy or conditional entropy as:
$$I(X; Y) = H(X) - H(X|Y)$$
or
$$I(X;Y)= H(X) + H(Y) - H(X,Y)$$

Mutual information is the [[KL Divergence]] between the joint probability distribution $P(x, y)$ and the product of the marginal distributions $P(x)P(y)$. This makes it a measurement of how far the joint probability is from being independent ($P(x, y) = P(x)P(y)$). It can such be calculated in the discrete case as:
$$I(X;Y) = D_{KL}(P(x, y)||P(X)P(y)) = \sum_{x, y}P(x, y)\log_b\left(\frac{P(x, y)}{P(x)P(y)}\right)$$
Or in the continuous case:
$$I(X;Y) = \int\int f(x, y)\log_b\left(\frac{f(x, y)}{f(x)f(y)}\right)dydx$$

Properties of Mutual Information:
* **Non-negative**: $I(X; Y) \geq 0$, with equality if $X$ and $Y$ are independent.
	* Knowing one variable cannot increase uncertainty about the other on average.
* **Symmetric**: $I(X; Y) = I(Y; X)$
	* Knowing $Y$ reduces uncertainty in $X$ by the same amount that knowing $X$ reduces uncertainty in $Y$.
* **Self-information**: $I(X; X) = H(X)$
	* Knowing $X$ eliminates all uncertainty about itself.
* **Bounded**: $I(X; Y) \leq \min(H(X), H(Y))$
	* Mutual information cannot exceed the entropy of either variable.

Mutual information captures statistical dependence more broadly than [[Covariance and Correlation]], which only detect linear relationships. Mutual information captures **any** statistical dependence, including nonlinear ones. 

> [!example]- Symmetric Joint Distribution
> Consider two random variables $X, Y \in \{0, 1, 2\}$ with the following joint distribution:
> 
> |     | X=0  | X=1  | X=2  |
> | --- | ---- | ---- | ---- |
> | Y=0 | 0.10 | 0.05 | 0.05 |
> | Y=1 | 0.05 | 0.30 | 0.05 |
> | Y=2 | 0.05 | 0.05 | 0.30 |
> 
> Compute the mutual information $I(X;Y)$ using both formulas.
> 
> First, compute the marginals. Both work out to $P(X) = P(Y) = (0.2, 0.4, 0.4)$, giving:
> $$H(X) = H(Y) = -0.2\log_2(0.2) - 2(0.4)\log_2(0.4) = 1.522 \text{ bits}$$
> 
> The joint entropy is:
> $$H(X, Y) = -[0.1\log_2(0.1) + 2(0.3)\log_2(0.3) + 6(0.05)\log_2(0.05)] = 2.671 \text{ bits}$$
> 
> Using the chain rule: $H(X|Y) = H(X, Y) - H(Y) = 2.671 - 1.522 = 1.149$ bits
> 
> Computing $I(X;Y)$ using both formulas:
> $$I(X;Y) = H(X) - H(X|Y) = 1.522 - 1.149 = 0.373 \text{ bits}$$
> $$I(X;Y) = H(X) + H(Y) - H(X, Y) = 1.522 + 1.522 - 2.671 = 0.373 \text{ bits}$$
> 
> Both formulas yield the same answer, as expected.

> [!example]- Deterministic Function
> Let $X$ be the result of rolling a fair six-sided die, and define $W$ as a coarser grouping:
> $$W = \left\{\begin{matrix}
> \text{"low"} & \text{if } X \in \{1, 2\}\\
> \text{"mid"} & \text{if } X \in \{3, 4\}\\
> \text{"high"} & \text{if } X \in \{5, 6\}
> \end{matrix}\right.$$
> Compute $H(X)$, $H(W)$, $H(X|W)$, $H(W|X)$, and $I(X;W)$.
> 
> Since $X$ is uniform over 6 outcomes: $H(X) = \log_2(6) = 2.585$ bits
> 
> Since $W$ is uniform over 3 equally-likely groups: $H(W) = \log_2(3) = 1.585$ bits
> 
> Because $W$ is completely determined by $X$, knowing $X$ leaves no uncertainty in $W$:
> $$H(W|X) = 0$$
> 
> Given any value of $W$, $X$ is uniform over its 2 corresponding die faces, so $H(X|W=w) = \log_2(2) = 1$ for each $w$. Taking the weighted average:
> $$H(X|W) = 1 \text{ bit}$$
> 
> Mutual Information:
> $$I(X;W) = H(X) - H(X|W) = 2.585 - 1 = 1.585 \text{ bits}$$
> 
> Note that $I(X;W) = H(W)$, which follows from $H(W|X) = 0$:
> $$I(X;W) = H(W) - H(W|X) = 1.585 - 0 = 1.585 \text{ bits}$$
> 
> This illustrates a general principle: when one variable is a deterministic function of another, the mutual information equals the entropy of the determined variable. All of $W$'s uncertainty is shared with $X$, but $X$ retains 1 bit of "extra" uncertainty (which face within the group) that $W$ does not capture.


# Relationships Between Quantities
![[info_theory_venn.png]]
The relationships between all of the quantities discussed above — Entropy, Joint Entropy, Conditional Entropy, and Mutual Information — can be cleanly summarized using the venn diagram shown. Each circle represents the total uncertainty (entropy) of a single random variable $X$ or $Y$, and the way they overlap encodes the relationships between them.

Mapping each quantity to a region:
* $H(X)$: the entire left circle — total uncertainty in $X$
* $H(Y)$: the entire right circle — total uncertainty in $Y$
* $H(X, Y)$: the union of both circles — total uncertainty of the pair, including everything they share and everything unique to each
* $H(X|Y)$: The left crescent — uncertainty remaining in $X$ after $Y$ is known
* $H(Y|X)$: The left crescent — uncertainty remaining in $Y$ after $X$ is known
* $I(X;Y)$: The intersection of both circles — information shared between $X$ and $Y$

Key identities visible from the diagram:
* If $X$ and $Y$ are completely independent, the circles do not overlap at all. Therefore:
	* $H(X, Y) = H(X) + H(Y)$
	* $H(X|Y) = H(X)$
	* $H(Y|X) = H(Y)$
	* $I(X;Y)=0$
* If $X$ and $Y$ are perfectly dependent in both directions (e.g. $Y=f(X)$ and $X=f^{-1}(Y)$), the circles are perfectly overlapping. Therefore:
	* $H(X, Y) = I(X;Y) = H(X) = H(Y)$
	* $H(X|Y) = H(Y|X) = 0$
* If one is dependent on the other but not the other way around (e.g. $Y=f(X)$ but $f$ isn't an invertible function), then one circle is smaller and is completely surrounded by the other.
* When there is some shared information, the circles partially overlap (like in the diagram). Therefore:
	* $H(X, Y) = H(X) + H(Y) - I(X;Y)$
	* $H(X, Y) = H(X) + H(Y|X) = H(Y) + H(X|Y)$ (chain rule)
	* $H(Y|X) \neq H(X|Y)$
	* $I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)$
	* $I(X;Y)=I(Y;X)$


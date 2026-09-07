In information theory, **Kullback-Leibler (KL) divergence** (also called **relative [[Entropy Quantities|entropy]]**) measures the *gap* between a true distribution $P$ and an approximating distribution $Q$. It answers the question "How much worse is $Q$ than $P$ as a description of the data?" — or equivalently, "How much [[Information]] is lost when $P$ is approximated by $Q$?"

Unlike [[Cross Entropy]], KL divergence isolates *only* the approximation error. It strips out the irreducible uncertainty inherent to $P$ itself and reports just the penalty incurred by using $Q$ in place of $P$. The relationship between the two quantities makes this explicit:
$$D_{KL}(P||Q) = H(P, Q) - H(P)$$
This makes KL divergence the natural quantity when the question is about distributional fit rather than total predictive cost — for example, when comparing approximation quality across different true distributions, or when KL appears explicitly as a regularization term.

For probability distributions $P$ and $Q$ defined over the same space, the KL divergence from $Q$ to $P$ is:
* Discrete case: $$D_{KL}(P||Q)=\sum_x P(x)\log_b\frac{P(x)}{Q(x)}$$
* Continuous case: $$D_{KL}(p||q) = \int p(x)\log_b\frac{p(x)}{q(x)}dx$$
If the logarithm base $b=2$, the units of KL divergence are "bits" and if the base $b=e$ the units are "nats".

Properties of KL divergence:
* **Non-negative**: $D_{KL}(P||Q) \geq 0$, with equality only when $P=Q$ everywhere.
	* This is **Gibbs' Inequality**
* **Non-symmetry**: $D_{KL}(P||Q) \neq D_{KL}(Q||P)$ in general.
* **Undefined when $Q(x) = 0$ but $P(x) > 0$**
	* Can't approximate something with zero probability when truth has a positive probability.

> [!example]- Biased Coin Flip
> Suppose a coin's true distribution is $P=(0.9, 0.1)$ for heads/tails. However it is modeled with a uniform distribution $Q=(0.5, 0.5)$. What is the KL Divergence between $P$ and $Q$.
> 
> $D_{KL}(P||Q)=0.9\log_2\frac{0.9}{0.5} + 0.1\log_2\frac{0.1}{0.5} = 0.531$ bits

> [!example]- Student-t and Standard Normal
> The [[Student-t]] distribution ($t_\nu$) is said to asymtotically approach the [[Normal|Standard Normal]] distribution ($N(0, 1)$) as the degrees of freedom parameter $\nu \rightarrow \infty$, and is considered a sufficiently good approximation in many cases when $\nu \geq 30$. Calculate the KL divergence between the student_t and the standard normal distribution for three values of $\nu$ — 1, 5, 30, and 100. Give answers in nats. 
> 
> Let $p(x)$ be the pdf of the standard normal distribution
> $$p(x) = \frac{1}{\sqrt{2\pi}}\exp(\frac{-x^2}{2})$$
> and let $q(x;\nu)$ be the pdf of the t distribution, parametrized with $\nu$ degrees of freedom.
> $$q(x;\nu)= \frac{\Gamma\!\left(\frac{\nu+1}{2}\right)}
>  {\sqrt{\nu\pi}\,\Gamma\!\left(\frac{\nu}{2}\right)}
>  \left(1 + \frac{x^2}{\nu}\right)^{-\frac{\nu+1}{2}},
>  \quad x \in \mathbb{R}$$
> 
> The KL divergence as a function of $\nu$ is then given by:
> $$D_{KL}(\nu)= D_{KL}(p(x), q(x;\nu))=\int_{-\infty}^\infty p(x)\ln\frac{p(x)}{q(x;\nu)}dx$$
> Evaluating this numerically for different values of $\nu$ gives:
> * $D_{KL}(1) = 0.259$ nats
> * $D_{KL}(5) = 0.033$ nats
> * $D_{KL}(30) = 0.0016$ nats
> * $D_{KL}(100) = 0.00016$ nats
> 
> This demonstrates that as $\nu$ increases, $D_{KL}(\nu) \rightarrow 0$, as the t-distribution is converging to the standard normal.


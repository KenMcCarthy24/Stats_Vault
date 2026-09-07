In information theory, **Information** is defined as a measure of the reduction in uncertainty about the state of a system caused by observing an event $E$. Alternatively, it can be thought of as the "surprise" of observing the event $E$. Rare events carry more uncertainty and thus are more surprising to see, and common events have less uncertainty and are less surprising.

**Information content** (also called **self-information** or **surprisal**) is mathematically defined for an event $E$ as:
$$I(E) = \log_b\left(\frac{1}{P(E)}\right) = -\log_b(P(E))$$
where $P(E)$ is the probability of observing $E$. This formulation has a few useful properties:
* **Non-negativity**: Since $P(E) \in [0, 1]$, $I(E) \geq 0$ always. Information content is always a non-negative quantity.
* **Impossible events**: If $P(E)=0$, then $I(E)=\infty$. It would be infinitely surprising to observe an impossible event.
* **Certain events**: If $P(E) = 1$, then $I(E) = 0$. There is no surprise in observing a certain event.
* **Additivity**: For independent events ($P(E_1 \cap E_2) = P(E_1)P(E_2)$), information content is additive:
	* $I(E_1 \cap E_2) = I(E_1) + I(E_2)$
	* The Additivity property is why $I(E)$ is defined using the logarithm rather than just the inverse probability. 

The choice of base $b$ for the logarithm gives the units of information content:
* $b=2$ gives units of **bits**. A bit is the amount of information needed to distinguish between two equally likely outcomes.
* $b=e$ (natural log) gives units of **nats**. Less clean to interpret, but more convenient for calculus (common in ML).
* Conversion: $1 \text{ nat} = \log_2(e) \approx 1.443 \text{ bits}$.

The *expected* value of information content over a distribution is the [[Entropy Quantities#Entropy|Entropy]] of that distribution:
$$H(X) = \mathbb{E}[I(X)] = -\sum_i P(x_i) \log_b P(x_i)$$
---

> [!Example]-
> Given the following [[Categorical]] probability distribution, calculate the information content of observing each event in bits.
> * $P(A) = 0.02$
> * $P(B) = 0.95$
> * $P(C) = 0.02$
> * $P(D) = 0.01$
>
> $I(A) = -\log_2(0.02) = 5.64$
> $I(B) = -\log_2(0.95) = 0.074$ (least surprising)
> $I(C) = -\log_2(0.02) = 5.64$
> $I(D) = -\log_2(0.01) = 6.64$ (most surprising)

> [!Example]-
> Consider a fair six-sided die and a biased coin with $P(\text{heads}) = 0.9$.
>
> **Rolling the die** — each outcome has $P = 1/6$:
> $$I(\text{any face}) = -\log_2(1/6) = \log_2(6) \approx 2.585 \text{ bits}$$
> Every roll is equally surprising because the distribution is uniform.
>
> **Flipping the biased coin**:
> $$I(\text{heads}) = -\log_2(0.9) \approx 0.152 \text{ bits}$$
> $$I(\text{tails}) = -\log_2(0.1) \approx 3.322 \text{ bits}$$
> Seeing tails is roughly 22× more surprising than seeing heads.
>
> **Joint event** — rolling a 3 *and* flipping tails (independent):
> $$I(3 \cap \text{tails}) = I(3) + I(\text{tails}) \approx 2.585 + 3.322 = 5.907 \text{ bits}$$


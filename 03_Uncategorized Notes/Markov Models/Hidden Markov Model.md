A **Hidden Markov Model** (HMM) is a mathematical model that is based on a  [[Markov Chain]], but where the $n$ various states $S$ are not directly observable or measurable. Instead, there is a set of $k$ possible observations $O$ that can be observed that all have a particular probability of coming from each state.

As in a standard Markov Chain, the transition probabilities between states are represented in a $(n \times n)$ **transition matrix** $P$, where $p_{ij} = P(s_i \rightarrow s_j)$, or the probability when going to the next step in the sequence of transitioning from $s_i$ to $s_j$.

An HMM has an additional $(n \times k)$ **emission matrix** $B$, where $b_{ij}=P(o_j|s_i)$, or the probability of observing $o_j$ when in state $s_i$.
* If $o_j$ cannot be observed when in state $s_i$, then $b_{ij} = 0$
* The sum of the probabilities in each row of $B$ must equal 1, as there is a 100% chance that something is observed.
	* $\displaystyle \sum_j b_{ij} = 1$
* Values are non-negative (they are probabilities)

Finally, like a standard Markov Chain, an HMM needs a $(1 \times n)$ **Initial State Vector** $\pi_0$, representing the probability distribution of each state being the first state in the sequence.

A common notation for defining a full HMM is as the triplet:
$$\lambda = (P, B, \pi_0)$$
# Algorithms
Several algorithms are commonly used with Hidden Markov Models to answer various questions:
* [[Forward Algorithm]]: Given a model $\lambda$, computes the probability of a sequence of observations occurring.
* [[Viterbi Algorithm]]: Given a model $\lambda$ and a sequence of observations, computes the most likely sequence of hidden states that produced those observations.

---

> [!example]
> A casino dealer has a set of three dice hidden behind the table, swapping between them every roll. The dice cannot be seen but the results of of the rolls can be seen.
> 
> The hidden states $S$ represent the 3 possible dice:
> * $s_1$: A fair die
> * $s_2$: A weighted die (in favor of rolling a 6)
> 	* Has a 50% chance of rolling a 6 and 10% chance of all others
> * $s_3$: A weighted die (in favor of rolling a 1)
> 	* Has a 50% chance of rolling a 1 and a 10% change of all others
> 
> The observations $O$ are just the six numbers of the dice:
> $$O = \{1,2,3,4,5,6\}$$
> It is initially assumed that the dealer plays with the fair dice 80% of the time and equally uses the loaded dice the remaining 20% of the time (10% each) so:
> $$\pi_0 = (0.8, 0.1, 0.1)$$
> Usually, the dealer keeps using the same die for a while before switching, leading to this transition matrix (would need to be learned from data in practice):
> $$
> P= \begin{pmatrix}
> 0.8 &  0.1 &  0.1\\
> 0.2 &  0.7 &  0.1\\
> 0.2 &  0.1 &  0.7\\ 
> \end{pmatrix}
> $$
> ![[hidden_markov_example_graph.png]]
> Finally, the emission matrix can be derived from the probability distribution of rolls for each die.
> $$
> B= \begin{pmatrix}
> 1/6 &  1/6 &  1/6 & 1/6 & 1/6 & 1/6\\
> 0.1 &  0.1 &  0.1 & 0.1 & 0.1 & 0.5\\
> 0.5 &  0.1 &  0.1 & 0.1 & 0.1 & 0.1\\ 
> \end{pmatrix}
> $$
> So the final Hidden Markov Model for this scenario is represented as the triplet of these:
> $$\lambda = (P, B, \pi_0)$$



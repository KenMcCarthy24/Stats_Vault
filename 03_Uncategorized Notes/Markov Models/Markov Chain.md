A **Markov Chain** or **Markov Process** is a mathematical structure consisting of a set of $n$ states $S$, along with the probabilities of transitioning between them. These states follow the **Markov Property**: the probability of moving from one state to another depends only on the current state, regardless of the sequence of states that came before it.

Markov chains are often constructed and visualized as a directed graph where:
* **Nodes**: Each node represents one of the states $s_i \in S$.
* **Edges**: Each edge represents a possible transition between two states $(s_i, s_j) \in S^2$.
	* The weight of the edge represents the probability of transitioning from $s_i$ to $s_j$: $P(s_i \rightarrow s_j)$.
	* If $i=j$, the edge connects the node to itself, representing the probability of staying in the same state.

---
## Transition Matrix

The various transition probabilities are represented as elements of the **Transition Matrix** $P$.
* Rows in this matrix represent the current state in the sequence.
* Columns represent the next state in the sequence.
* Each element $p_{ij}$ represents the probability of transitioning from $s_i$ to $s_j$:
	* $p_{ij} = P(s_i \rightarrow s_j)$
* If there is no edge in the graph between $s_i$ and $s_j$, then the transition is impossible and $p_{ij} = 0$.
* The transition matrix is a right-stochastic matrix because:
	* The sum of probabilities in any given row must equal 1, as there is a 100% chance that some transition (or non-transition) occurs when moving to the next step in the sequence:
		* $\displaystyle \sum_j p_{ij} = 1$
	* The transition matrix is square with dimensions $(n \times n)$.
	* Values are non-negative (they are probabilities)
* Diagonal elements $p_{ii}$ represent the probabilities of staying in the same state.

---
## Modeling Transitions

Let $\pi_0$ be the $(1 \times n)$ **Initial State Vector** representing the starting [[Probability Distribution]] of each state being the first state in the sequence. Then, the probability distribution of states for the next step in the sequence, $\pi_1$, is given by:
$$\pi_1 = \pi_0P$$

In general, the probability distribution of the next step in the sequence given the previous state is:
$$\pi_{i+1} = \pi_iP$$

Therefore, the probability distribution $\pi_k$ of states for the $k$-th element in the sequence is:
$$\pi_k = \pi_0P^k$$
---
# Steady States
A **steady-state** of a Markov chain is a probability distribution over all of the states $\pi^*$ such that:
$$\pi^* = \pi^*P$$
Once a system is in this state, the probability of being in any given state in the next step in the sequence is exactly the same as the current step.

Because $P$ is a right-stochastic matrix, it is guaranteed to have one of its eigenvalues be equal to 1. The **left eigenvectors** associated with these eigenvalues are the steady states.

While a steady state is mathematically guaranteed to exist, a Markov chain will only converge to a **unique** steady state if the chain is **regular**. A regular Markov chain is defined by two properties:
* **Irreducible**: Any state can eventually be reached from any other state (there are no completely isolated nodes or absorbing states that trap the system forever).
* **Aperiodic**: The system's transitions do not get trapped in strict, deterministic cycles.

If a Markov chain is regular, as the number of transitions $k$ approaches infinity, the probability distribution $\pi_k$ converges to the unique steady state $\pi^*$. This convergence happens entirely independent of the initial state vector $\pi_0$:
$$\lim_{k \to \infty} \pi_0 P^k = \pi^*$$
---

> [!example]- Example: Transitions and Steady State
> Consider the following Markov chain:
> ![[markov_example.png]]
> 
> The transition matrix $P$ is given by:
> $$
> P= \begin{pmatrix}
>  0 &  0.6 &  0.2 &  0.2 \\
>  0 &  0.5 &  0 &  0.5 \\
>  0.7 &  0 &  0.3 &  0 \\
>  0 &  0 &  0.6 &  0.4 
> \end{pmatrix}
> $$
> 
> **1. Calculate $\pi_1$ and $\pi_2 $** given a uniform initial state.
> Given a uniform initial state vector $\pi_0 = (0.25, 0.25, 0.25, 0.25)$, the probability distributions for the next two steps in the sequence are:
> 
> $$
> \pi_1 = \pi_0P = (0.25, 0.25, 0.25, 0.25)
> \begin{pmatrix}
>  0 &  0.6 &  0.2 &  0.2 \\
>  0 &  0.5 &  0 &  0.5 \\
>  0.7 &  0 &  0.3 &  0 \\
>  0 &  0 &  0.6 &  0.4 
> \end{pmatrix} 
> = (0.175, 0.275, 0.275, 0.275)
> $$
> 
> 
> $$
> \pi_2 = \pi_1P = (0.175, 0.275, 0.275, 0.275)
> \begin{pmatrix}
>  0 &  0.6 &  0.2 &  0.2 \\
>  0 &  0.5 &  0 &  0.5 \\
>  0.7 &  0 &  0.3 &  0 \\
>  0 &  0 &  0.6 &  0.4 
> \end{pmatrix} 
> = (0.1925, 0.2425, 0.2825, 0.2825)
> $$
> 
> 
> **2. Find the steady state vector $\pi^*$**
> Because $P$ is a regular, right-stochastic matrix, its dominant eigenvalue is $\lambda_1 = 1$. The remaining eigenvalues are approximately $\lambda_2 \approx -0.349$ and $\lambda_{3,4} \approx 0.275 \pm 0.495i$.
> 
> To find the unique steady state, solve for the normalized left eigenvector associated with $\lambda = 1$ (where $\pi^* = \pi^*P$). This results in the following steady state probability distribution:
> 
> $$\pi^* \approx (0.2015, 0.2418, 0.2879, 0.2687)$$

Given a [[Hidden Markov Model]] defined as $\lambda = (P, B, \pi_0)$ and a sequence of $T$ events $O=(o_1, o_2, \dots,o_T)$ that came from unknown hidden states $H= (h_1, h_2, \dots h_T)$, the **forward algorithm** calculates the probability of that sequence being observed $P(O|\lambda)$.

Naively, this can be calculated by brute force considering every possible sequence of hidden states, independently calculating the joint probability of the observations and each possible hidden state sequence, and adding up the probabilities. Let $\mathcal{H}$ be the set of all possible sequences of hidden states $H$. Then:
$$P(O|\lambda) = \sum_{H \in \mathcal{H}}P(O, H|\lambda)$$

However if the model has $n$ distinct hidden states and a sequence length of $T$, there are $n^T$ possible state sequences. Evaluating the probability of each path would take $O(Tn^T)$ operations, or exponential complexity.

Instead a recursive dynamic programming algorithm is used that recognizes that many state sequences share overlapping sub-paths, which ends up bringing the complexity down to $O(Tn^2)$.

---
# The Algorithm
First, let the **forward variable** $\alpha_t(i)$ be defined as the probability of seeing the partial sub-sequence of $O$: $(o_1, o_2, \dots, o_t)$, and landing in the $i$-th hidden state, as indexed on the transition matrix $P$.

The forward algorithm runs in 3 steps:
### 1. Initialization
First, the forward variables are calculated for the very first element in the sequence. To end up in state $i$ at $t=1$, the model must have started in state $i$ and then emitted observation $o_1$.
$$\alpha_1(i) = \pi_0(i)B_i(o_1)$$
where:
* $\pi_0(i)$ is the initial probability of starting in state $i$
* $B_i(o_1)$ is the probability of observing $o_1$ when in state $i$

### 2. Recursion
Next, probabilities are recursively calculated for the remaining elements in the sequence.

To find the probability of being in state $j$ at element $t+1$ having observations up to $o_{t+1}$, consider all the possible states $i$ the model could have been in at element $t$.

For $t = 1, 2, \dots, T-1$ and for every $j$:
$$\alpha_{t+1}(j) = \left(\sum_{i=1}^n \alpha_t(i)P_{ij} \right)B_j(o_{t+1})$$
where:
* $\alpha_t(i)$ is the probability of having reached state $i$ at element $t$ while emitting the correct sequence up to that point.
* $P_{ij}$ is the transition probability between states $i$ and $j$
* $B_j(o_{t+1})$ is the probability of state $j$ actually emitting the next observation $o_{t+1}$

The product $\alpha_t(i)P_{ij}$ represents the probability that the model was in state $i$ at element $t$ and transitioned to state $j$. This is summed over all possible states to get the total probability of transitioning from any state $i$ to state $j$. Finally this is multiplied by $B_j(o_{t+1})$ to get the final probability of observing the subsequence at that point.

### 3. Termination
Once all the forward variables have been calculated, the final probability of the observations $P(O|\lambda)$ can be calculated as sum of the final set of forward variables for element $T$ in the sequence, which individually give the probabilities of generating the complete observation sequence $O$ and ending on each possible state $i$
$$P(O|\lambda) = \sum_{i=1}^n\alpha_T(i)$$
---

> [!example]- 
> Consider a Hidden Markov Model $\lambda = (P, B, \pi_0)$ with $n=2$ hidden states (State 1 and State 2) and 3 possible observations ($A, B,$ and $C$). 
> * **Initial Probabilities**:
>    $\pi_0 = (0.6, 0.4)$
> * **Transition Matrix:**
>   $P = \begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}$
> * **Emission Matrix**:
>   $B = \begin{bmatrix} 0.1 & 0.4 & 0.5 \\ 0.7 & 0.2 & 0.1 \end{bmatrix}$
> * **Observed Sequence (T=3)**
>   $O = (A, C, B)$
> 
> **Goal:** Use the forward algorithm to calculate the probability of this observation sequence occurring, $P(O|\lambda)$.
> 
> ### Initialization
> Start by calculating the forward variables $\alpha_1(1)$ and $\alpha_1(2)$ for first observation $o_1 = A$:
> $\alpha_1(1) = \pi_0(1)B_1(A) = (0.6)(0.1) = 0.06$
> $\alpha_1(2) = \pi_0(2)B_2(A) = (0.4)(0.7) = 0.28$
> 
> ### Recursion
> Now the remaining can be calculated, moving through the observed sequence
> $\alpha_2(1) = (\alpha_1(1)P_{11} + \alpha_1(2)P_{21})B_1(C) = ((0.06)(0.7) + (0.28)(0.4))(0.5) = 0.077$
> $\alpha_2(2) = (\alpha_1(1)P_{12} + \alpha_1(2)P_{22})B_2(C) = ((0.06)(0.3) + (0.28)(0.6))(0.1) = 0.0186$
> 
> $\alpha_3(1) = (\alpha_2(1)P_{11} + \alpha_2(2)P_{21})B_1(B) = ((0.077)(0.7) + (0.0186)(0.4))(0.4) = 0.0245$
> $\alpha_3(2) = (\alpha_2(1)P_{12} + \alpha_2(2)P_{22})B_2(B) = ((0.077)(0.3) + (0.0186)(0.6))(0.2) = 0.0069$
> 
> ### Termination
> Now the final result is just the sum of the final forward variables for the final element in the sequence:
> $$P(O|\lambda) = \alpha_3(1) + \alpha_3(2) = 0.0245 + 0.0069 = 0.0314$$
> 



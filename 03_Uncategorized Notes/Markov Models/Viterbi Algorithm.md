Given a [[Hidden Markov Model]] defined as $\lambda = (P, B, \pi_0)$ and a sequence of $T$ events $O=(o_1, o_2, \dots,o_T)$, the **Viterbi Algorithm** computes the most likely sequence of hidden states that produced those observations, called the **Viterbi Path**.

The Viterbi Algorithm is a dynamic programming algorithm that solves for the Viterbi Path by populating and then interpreting two matrices. With $N$ possible states in the HMM, these matrices are:
1. The Probability Matrix ($C$): An $(N \times T)$ matrix where each entry $(i, t)$ stores the maximum probability of being in state $i$ at element $t$, considering all paths from the start.
2. The Back-pointer Matrix ($D$): An $(N \times T)$ matrix where each entry $(i, t)$ stores the index of the previous state at step $t-1$ that led to the maximum probability for the current state $i$ at step $t$.

> [!note] 
> Practically, log-probabilities are often used rather than raw probabilities. For long sequences, multiplying many small probabilities together risks floating-point numerical underflow.

The Viterbi algorithm is done in three steps:
### 1. Initialization
First, the first column of the probability matrix $C$ is calculated as simply the probability of observing the first element in the sequence given different initial states $i$. 
$$C_{i, 1} = \pi_0(i)B_i(o_1)$$
Or in log space:
$$C_{i, 1} = \ln(\pi_0(i)) + \ln(B_i(o_1))$$

Where:
* $\pi_0(i)$ is the initial probability of starting in state $i$
* $B_i(o_1)$ is the probability of observing $o_1$ when in state $i$
*(Note: If a probability is $0$, its log is mathematically $-\infty$, which is handled programmatically as a very small negative number).*

The first column of the back-pointer matrix $D$ is initialized to all zeros, since there is no previous state to point back to.
$$D_{i, 1} = 0$$

### 2. Forward Pass
Next, the rest of the $C$ and $D$ matrices are filled out by moving forward through the elements of the sequence.

To find the maximum probability of being in state $i$ at element $t$ having observations up to $o_t$, consider all the possible states $k$ the model could have been in at element $t-1$ and calculate the maximum probability of transitioning from one of those states to state $i$, then observing $o_t$.
$$C_{i, t} = \max_{k=1}^N(C_{k, t-1}P_{k,i})B_i(o_t)$$
Or in log space:
$$C_{i, t} = \max_{k=1}^N(C_{k, t-1} + \ln(P_{k,i})) + \ln(B_i(o_t))$$

Where:
* $C_{k, t-1}$ is the maximum probability of being in state $k$ at element $t-1$
* $P_{k, i}$ is the probability of transitioning from state $k$ to state $i$
* $B_i(o_t)$ is the probability of state $i$ actually emitting the observation $o_t$

> [!note] 
> This is conceptually very similar to how the probabilities are calculated in the recursive step of the [[Forward Algorithm]], only here the maximum is taken instead of summing all the probabilities together to consider all states.

The back-pointers are simply the indexes of these maximums, or the argmax.
$$D_{i, t} = \arg\max_{k=1}^N(C_{k, t-1}P_{k,i})$$
Or in log space:
$$D_{i, t} = \arg\max_{k=1}^N(C_{k, t-1} + \ln(P_{k,i}))$$

### 3. Backtracking
Finally, the most likely sequence of hidden states, $H = (h_1, h_2, \dots, h_T)$, is reconstructed by working backward from the final time step $T$ to the beginning.

First, the final state $h_T$ is determined by finding the state $i$ that maximizes the probability at the final element $T$ in the probability matrix $C$.
$$h_T = \arg\max_{i=1}^N(C_{i, T})$$

Where:
* $C_{i, T}$ is the maximum probability of being in state $i$ at the final element $T$

Then, the rest of the sequence is built by tracing backward through the back-pointer matrix $D$. Starting from $t = T$ and stepping backward down to $t = 2$, the previous state $h_{t-1}$ is found by looking up the entry in $D$ for the current state $h_t$ at step $t$.
$$h_{t-1} = D_{h_t, t}$$
Where:
* $h_t$ is the most likely state at element $t$
* $D_{h_t, t}$ is the index of the state at element $t-1$ that resulted in the maximum probability for state $h_t$

Once the process reaches the first element, the full sequence of states $H$ is complete, representing the Viterbi Path.

---
> [!example]- 
> Consider a Hidden Markov Model $\lambda = (P, B, \pi_0)$ with $N=2$ hidden states (State 1 and State 2) and 3 possible observations ($A, B,$ and $C$). 
> * **Initial Probabilities**:
>    $\pi_0 = (0.6, 0.4)$
> * **Transition Matrix:**
>   $P = \begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}$
> * **Emission Matrix**:
>   $B = \begin{bmatrix} 0.1 & 0.4 & 0.5 \\ 0.7 & 0.2 & 0.1 \end{bmatrix}$
> * **Observed Sequence (T=3)**
>   $O = (A, C, B)$
> 
> **Goal:** Use the Viterbi Algorithm to compute the most likely sequence of hidden states that produced those observations, known as the Viterbi Path.
> 
> ### 1. Initialization
> First, calculate the first column of the probability matrix $C$ using the first observation $o_1 = A$:
> $C_{1, 1} = \pi_0(1)B_1(A) = (0.6)(0.1) = 0.06$
> $C_{2, 1} = \pi_0(2)B_2(A) = (0.4)(0.7) = 0.28$
> 
> The first column of the back-pointer matrix $D$ is initialized to 0:
> $D_{1, 1} = 0$
> $D_{2, 1} = 0$
> 
> ### 2. Forward Pass
> Next, fill out the rest of the $C$ and $D$ matrices moving forward through the sequence. 
> 
> **For $t=2$ and observation $o_2 = C$:**
> $C_{1, 2} = \max(C_{1, 1}P_{11}, C_{2, 1}P_{21})B_1(C) = \max((0.06)(0.7), (0.28)(0.4))(0.5) = \max(0.042, 0.112)(0.5) = 0.056$
> $D_{1, 2} = \arg\max(0.042, 0.112) = 2$ (Since the maximum came from state $k=2$)
> 
> $C_{2, 2} = \max(C_{1, 1}P_{12}, C_{2, 1}P_{22})B_2(C) = \max((0.06)(0.3), (0.28)(0.6))(0.1) = \max(0.018, 0.168)(0.1) = 0.0168$
> $D_{2, 2} = \arg\max(0.018, 0.168) = 2$
> 
> **For $t=3$ and observation $o_3 = B$:**
> $C_{1, 3} = \max(C_{1, 2}P_{11}, C_{2, 2}P_{21})B_1(B) = \max((0.056)(0.7), (0.0168)(0.4))(0.4) = \max(0.0392, 0.00672)(0.4) = 0.01568$
> $D_{1, 3} = \arg\max(0.0392, 0.00672) = 1$
> 
> $C_{2, 3} = \max(C_{1, 2}P_{12}, C_{2, 2}P_{22})B_2(B) = \max((0.056)(0.3), (0.0168)(0.6))(0.2) = \max(0.0168, 0.01008)(0.2) = 0.00336$
> $D_{2, 3} = \arg\max(0.0168, 0.01008) = 1$
> 
> **At the end of the forward pass, the fully populated matrices are:**
> $C = \begin{bmatrix} 0.06 & 0.056 & 0.01568 \\ 0.28 & 0.0168 & 0.00336 \end{bmatrix}$
> $D = \begin{bmatrix} 0 & 2 & 1 \\ 0 & 2 & 1 \end{bmatrix}$
> 
> ### 3. Backtracking
> Finally, reconstruct the most likely sequence by working backward.
> 
> First, find the final state $h_3$ by maximizing the probabilities at the final element $T=3$:
> $h_3 = \arg\max(C_{1, 3}, C_{2, 3}) = \arg\max(0.01568, 0.00336) = 1$
> 
> Then, step backward using the back-pointer matrix $D$:
> $h_2 = D_{h_3, 3} = D_{1, 3} = 1$
> $h_1 = D_{h_2, 2} = D_{1, 2} = 2$
> 
> The most likely sequence of hidden states, or the Viterbi Path, is $H = (2, 1, 1)$, meaning the model likely transitioned through State 2, then State 1, then State 1.
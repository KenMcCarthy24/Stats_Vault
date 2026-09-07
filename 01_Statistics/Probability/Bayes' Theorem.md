Given two events $A$ and $B$, **Bayes' Theorem** describes the relationship between the conditional probabilities $P(A|B)$ and $P(B|A)$ as:
$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$
Where:
* $P(A)$ is the **prior probability**, representing the initial probability of event $A$ before taking $B$ into account.
* $P(B|A)$ is the **likelihood**, representing the probability of observing evidence $B$ given that event $A$ is true.
* $P(B)$ is the **marginal probability** (or **evidence**), representing the total probability of observing $B$ without taking $A$ into account.
	* This is often calculated using the **Law of Total Probability**, which expands $P(B)$ into the sum of all mutually exclusive ways $B$ can occur. For a binary event, this is: $P(B) = P(B|A)P(A) + P(B|\neg A)P(\neg A)$.
* $P(A|B)$ is the **posterior probability**, representing the updated probability of $A$ compared to the prior, after taking the evidence $B$ into account.

> [!example]- Bayes' Theorem Derivation
> For events $A$ and $B$, the conditional probability of $A|B$ is given by:
> $$P(A|B) = \frac{P(A \cap B)}{P(B)}$$
> Similarly, the conditional probability of $B|A$ is:
> $$P(B|A) = \frac{P(B \cap A)}{P(A)}$$
> Since $P(A \cap B) = P(B \cap A)$, those two terms can be set equal to each other:
> $$P(A|B)P(B) = P(B|A)P(A)$$
> Solving for $P(A|B)$ yields:
> $$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$
> which is Bayes' Theorem.

> [!Example]- Disease Testing (Base Rate Fallacy)
> A man is told that he has tested positive for a disease. This disease is known to affect 0.1% of the population, and the test is known to have a 90% true positive rate and a 5% false positive rate. What is the probability that the man actually has the disease given that he tested positive?
> 
> Define the two events:
> * $D$: The man has the disease
> * $T$: The man tested positive for the disease
> 
> The prior probability of having the disease is $P(D) = 0.001$.
> 
> The likelihood of testing positive given that he has the disease is $P(T|D) = 0.90$.
> 
> To find the marginal probability of testing positive $P(T)$, we apply the **Law of Total Probability** defined above. It is the sum of the probabilities of two scenarios:
> 1. You tested positive AND you have the disease: $P(T|D)P(D)$
> 2. You tested positive AND you don't have the disease: $P(T|\neg D)P(\neg D)$
> 
> So, $P(T) = P(T|D)P(D) + P(T|\neg D)P(\neg D) = (0.90)(0.001) + (0.05)(0.999) = 0.05085$.
> 
> By Bayes' Theorem, the posterior probability of having the disease given a positive test is:
> $$P(D|T) = \frac{P(T|D)P(D)}{P(T)} = \frac{(0.90)(0.001)}{0.05085} \approx 0.0177$$
> Despite the positive test result, there is only about a 1.77% chance that the man actually has the disease.


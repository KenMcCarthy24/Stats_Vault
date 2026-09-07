
There are two types of errors when conducting a [[Hypothesis Test]], representing the two ways a test can fail to reflect reality.

| | **Fail to Reject $H_0$** | **Reject $H_0$** |
| :--- | :---: | :---: |
| **$H_0$ is True** | $\checkmark$ Correct Decision $(1-\alpha)$ | **Type I Error** ($\alpha$) |
| **$H_0$ is False** | **Type II Error** ($\beta$) | $\checkmark$ Correct Decision $(1-\beta)$ |

---
![[power_visualization.svg]]
This image visualizes the concepts of Type I Error ($\alpha$), Type II Error ($\beta$), and Power for a right-tailed test.
## Type I Error ($\alpha$): False Positive
A Type I error occurs when the null hypothesis $H_0$ is actually true, but the hypothesis test incorrectly rejects it in favor of the alternative hypothesis $H_1$.

The probability of committing a Type I error is denoted by $\alpha$ and is called the **Level of Significance** of the test.
    $$\alpha = P(\text{Reject } H_0 \mid H_0 \text{ is True})$$

## Type II Error ($\beta$): False Negative
A Type II error occurs when the null hypothesis $H_0$ is actually false (and should be rejected), but the hypothesis test fails to reject it.

The probability of committing a Type II error is denoted by $\beta$.
    $$\beta = P(\text{Fail to Reject } H_0 \mid H_0 \text{ is False})$$
The quantity $1-\beta$ is the [[Power of a Test]]. 

# Power of a Test
The [[Power of a Test|Power]] of a test is the probability of correctly rejecting the null hypothesis when it is false. It is the complement of the Type II error rate.
$$\text{Power} = P(\text{Reject } H_0|H_0 \text{ is False}) =1 - \beta$$

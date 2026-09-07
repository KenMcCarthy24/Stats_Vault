The **Power** of a [[Hypothesis Test]] is the probability of correctly rejecting the null hypothesis when it is false. It is the complement of the [[Errors in Hypothesis Testing#Type II Error ($ beta$) False Negative|Type II Error Rate]].

$$\text{Power} = P(\text{Reject } H_0|H_0 \text{ is False}) =1 - \beta$$

---
The below plot visualizes the intuition behind the power of a right tailed test:
$$H_0: \theta = \theta_0$$
$$H_1: \theta > \theta_0$$
![[power_visualization.svg]]
* The top plot visualizes the sampling distribution of an [[Estimators|estimator]] $\hat \theta$ of $\theta$ under the Null hypothesis $H_0$. Centered at the null parameter $\theta_0$
	* The critical value $c$ is labeled and to the right of $c$ is the **rejection region**. The area under this rejection region is $\alpha$: the probability of a [[Errors in Hypothesis Testing#Type I Error ($ alpha$) False Positive|Type I Error]] (False Positive)
* The bottom plot visualizes the sampling distribution $\hat \theta$ under the Alternate Hypothesis $H_1$. Centered at the true parameter $\theta$.
	* This distribution is not directly observable without knowing the true parameter $\theta$. But it is still useful to consider as a theoretical.
	* Again the critical value $c$ is labeled
	* The area to the left of c is $\beta$: the probability of a [[Errors in Hypothesis Testing#Type II Error ($ beta$) False Negative|Type II Error]] (False Negative)
	* The area to the right of $c$ is the Power.

A well designed hypothesis test should minimize $\alpha$ while maximizing Power. However, for a fixed sample size $n$, decreasing $\alpha$ generally decreases power, so test design involves balancing the two.
* Common rule of thumb to shoot for is $\text{Power} \geq 0.8$ and $\alpha \leq 0.05$.
* This gives an 80% chance of a significant result if the effect is real and a 5% chance of mistakenly concluding the effect is real when it is not.

# Ways to increase Power
 There are several ways to increase the power of a test that a researcher can use:

* Aim for a larger effect size, which is the difference between the true parameter $\theta$ and the null parameter $\theta_0$.
	* This leads to a larger separation between the two distributions.
* Reduce the [[Standard Error]] of the sampling distributions $\frac{\sigma}{\sqrt n}$. Either by:
	* Decreasing the standard deviation $\sigma$. Make more precise measurements (often hard)
	* Increase the sample size $n$. (most common method)
	* In both cases this leads to narrower distributions

Tests are often designed with a particular $\alpha$ and Power in mind and the sample size needed for that Power is calculated before the data is collected.

---

> [!example]- Example: Calculating Power
> A botanist is testing a new organic fertilizer to see if it increases the 
> mean height of sunflower plants compared to the current standard, which 
> results in a mean height of 150 cm. The population standard deviation is known to be 12 cm.
> 
> A sample of 36 plants is taken and the following hypothesis test is performed at level of significance $\alpha=0.05$:
> $$H_0: \mu=150$$
> $$H_1:\mu > 150$$
> Calculate the power of the test if the true population mean height with the new fertilizer is actually 156 cm.
> 
> This is an upper tailed [[Hypothesis Test For Mean]] (a [[Z-test]]). The non-standardized sampling distribution for the mean under the null and alternate hypotheses are:
> $$\bar X_{H_0} \sim N(\mu_0, \frac{\sigma^2}{n}) = N(150, \frac{12^2}{36}) = N(150, 4)$$
> $$\bar X_{H_1} \sim N(\mu, \frac{\sigma^2}{n}) = N(156, \frac{12^2}{36}) = N(156, 4)$$
> The critical value $c$ is the value such that $P(\bar X_{H_0} > c)=\alpha=0.05$. In this case that works out to $c=153.29$.
> 
> Now the power of the test is:
> $$\text{Power} = P(\bar X_{H_1} > c) = P(\bar X_{H_1} > 153.29) = 0.912$$


> [!example]- Example: Calculating Sample Size for Power
> An engineer is testing a new manufacturing process for steel cables to see if it increases the 
> mean breaking strength compared to the old process, which has a mean strength of 2000 kg. 
> The population standard deviation is known to be 50 kg.
> 
> The engineer wants to ensure the test has a power of 0.80 if the new process actually improves 
> the mean strength to 2025 kg. The test will be performed at a level of significance $\alpha = 0.05$.
> 
> The hypotheses are:
> $$H_0: \mu = 2000$$
> $$H_1: \mu > 2000$$
> 
> Calculate the minimum sample size $n$ required to achieve this power.
> 
> This is an upper tailed [[Hypothesis Test For Mean]]. The non-standardized sampling distributions 
> for the mean under the null and alternate hypotheses are:
> $$\bar X_{H_0} \sim N\left(2000, \frac{50^2}{n}\right)$$
> $$\bar X_{H_1} \sim N\left(2025, \frac{50^2}{n}\right)$$
> 
> 
> **1. From the perspective of $H_0$ ($\alpha = 0.05$):**
> The critical value $c$ is the value such that $P(\bar X_{H_0} > c) = 0.05$. 
> $$c = \mu_0 + z_\alpha \frac{\sigma}{\sqrt{n}} = 2000 + 1.645 \frac{50}{\sqrt{n}}$$
> 
> **2. From the perspective of $H_1$ (Power $= 0.80$):**
> The power of the test is
> $$\text{Power}= P(\bar X_{H_1} > c) = 0.80$$
> This implies that the area to the *left* of $c$ on the $H_1$ curve is $0.20$ ($\beta$).
> $$c = \mu_1 + z_\beta \frac{\sigma}{\sqrt{n}} = 2025 + (-0.842) \frac{50}{\sqrt{n}}$$
> 
> **3. Solving for $n$:**
> Since both equations equal $c$, set them equal to each other:
> $$2000 + 1.645 \frac{50}{\sqrt{n}} = 2025 - 0.842 \frac{50}{\sqrt{n}}$$
> 
> Rearranging to isolate terms with $n$:
> $$(1.645 + 0.842) \frac{50}{\sqrt{n}} = 2025 - 2000$$
> $$2.487 \frac{50}{\sqrt{n}} = 25$$
> $$\frac{124.35}{\sqrt{n}} = 25$$
> $$\sqrt{n} = \frac{124.35}{25} \approx 4.974$$
> $$n \approx 24.74$$
> 
> Since fractional samples are not allowed, round up:
> **Required Sample Size $n = 25$**
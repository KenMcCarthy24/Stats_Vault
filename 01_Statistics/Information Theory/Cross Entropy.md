In information theory, **Cross Entropy** measures the *total expected cost* of representing a true distribution $P$ using an approximating distribution $Q$. It answers the question "What is the total expected cost when scoring outcomes drawn from $P$ using the model $Q$?"

This total cost decomposes into two parts: the inherent unpredictability of $P$ itself, plus a penalty for using $Q$ instead of $P$. Formally:
$$H(P, Q) = H(P) + D_{KL}(P||Q)$$
where $H(P)$ is the [[Entropy Quantities#Entropy|entropy]] of $P$ and $D_{KL}(P||Q)$ is the [[KL Divergence]] from $P$ to $Q$. Note that $H(P)$ depends only on $P$ and is irreducible — no choice of $Q$ can shrink it. The only piece controlled by the approximation is $D_{KL}(P||Q)$.

For probability distributions $P$ and $Q$ defined over the same space, the cross entropy $H(P, Q)$ is:
* Discrete case: $$H(P, Q) = -\sum_x P(x)\log_b Q(x)$$
* Continuous case: $$H(p, q) = -\int p(x)\log_b q(x)\,dx$$
If the logarithm base $b=2$, the units are "bits"; if $b=e$, the units are "nats".

Cross entropy is minimized when $P=Q$ everywhere, at which point $D_{KL}(P||Q)=0$ and $H(P, Q) = H(P)$.

Properties of Cross Entropy:
* **Lower Bound**: $H(P, Q) \geq H(P)$, with equality when $P=Q$.
	* This is when $D_{KL}(P||Q)=0$
* **Asymmetry**: $H(P, Q) \neq H(Q, P)$ in general

> [!example]- Weather Forecast Model
> A meteorologist records the true long-run distribution of daily weather as $P = (0.6, 0.3, 0.1)$ for sunny, cloudy, and rainy. A forecast model assigns probabilities $Q = (0.5, 0.4, 0.1)$. Compute $H(P, Q)$ in bits and verify the decomposition $H(P, Q) = H(P) + D_{KL}(P \| Q)$.
> 
> **Cross entropy:**
> $$H(P, Q) = -(0.6\log_2 0.5 + 0.3\log_2 0.4 + 0.1\log_2 0.1)$$
> $$= -(0.6(-1) + 0.3(-1.322) + 0.1(-3.322)) = 1.329 \text{ bits}$$
> 
> **Entropy of $P$:**
> $$H(P) = -(0.6\log_2 0.6 + 0.3\log_2 0.3 + 0.1\log_2 0.1)$$
> $$= -(0.6(-0.737) + 0.3(-1.737) + 0.1(-3.322)) = 1.295 \text{ bits}$$
> 
> **KL divergence:**
> $$D_{KL}(P\|Q) = 0.6\log_2\frac{0.6}{0.5} + 0.3\log_2\frac{0.3}{0.4} + 0.1\log_2\frac{0.1}{0.1}$$
> $$= 0.6(0.263) + 0.3(-0.415) + 0 = 0.034 \text{ bits}$$
> 
> **Verification:** $H(P) + D_{KL}(P\|Q) = 1.295 + 0.034 = 1.329$ bits $= H(P, Q)$ ✓
> 
> The small KL divergence indicates the model is a good approximation of the true distribution; most of the cross entropy comes from the irreducible uncertainty $H(P)$.

# Binary Cross Entropy
**Binary Cross Entropy** (BCE) is the special case of cross entropy when $P$ and $Q$ are [[Bernoulli]] distributions over two outcomes labeled $1$ and $0$. Given the true label $y \in \{0, 1\}$ and the model's predicted probability $\hat{y} = Q(Y=1)$. It is calculated as is:

$$H(y, \hat{y}) = -\left[y\log_b \hat{y} + (1-y)\log_b(1-\hat{y})\right]$$

When $y=1$, only the first term survives and the loss penalizes $\hat{y}$ for being far from $1$. When $y=0$, only the second term survives and the loss penalizes $\hat{y}$ for being far from $0$.

BCE is the standard loss function for **binary classification** in [[Machine Learning]]. In this case it is also called the **log-loss**. The model outputs a single probability $\hat{y} \in (0,1)$ — typically from a sigmoid activation — and BCE measures how well that probability matches the true label. Minimizing the average BCE over a training set is equivalent to maximizing the log-likelihood of the data under a Bernoulli model, and by the cross entropy / KL decomposition it simultaneously drives the predicted distribution toward the true label distribution.

> [!example]- Spam Classifier
> A spam classifier produces predicted probabilities for three emails, each with a known true label. Compute the BCE loss for each prediction and the average loss over the batch.
> 
> | Email | True label $y$ | Predicted $\hat{y}$ |
> | ----- | -------------- | -------------------- |
> | 1     | 1 (spam)       | 0.85                 |
> | 2     | 0 (not spam)   | 0.15                 |
> | 3     | 1 (spam)       | 0.40                 |
> 
> **Email 1** ($y=1$, only the first term survives):
> $$H = -\log_2(0.85) = 0.234 \text{ bits}$$
> **Email 2** ($y=0$, only the second term survives):
> $$H = -\log_2(1 - 0.15) = -\log_2(0.85) = 0.234 \text{ bits}$$
> **Email 3** ($y=1$, model is uncertain):
> $$H = -\log_2(0.40) = 1.322 \text{ bits}$$
> 
> **Average BCE:**
> $$\bar{H} = \frac{0.234 + 0.234 + 1.322}{3} = 0.597 \text{ bits}$$
> 
> Email 3 dominates the average loss. Even though emails 1 and 2 are well-predicted, the model's uncertainty on a spam email pulls the batch loss up substantially — illustrating how BCE heavily penalizes confident wrong predictions and uncertain correct ones.

# Categorical Cross Entropy
**Categorical Cross Entropy** (CCE) generalizes BCE to $K > 2$ classes. Let $\mathbf{y} = (y_1, \ldots, y_K)$ be a one-hot true label vector and $\hat{\mathbf{y}} = (\hat{y}_1, \ldots, \hat{y}_K)$ be the model's predicted probability vector over all $K$ classes. Then:

$$H(\mathbf{y}, \hat{\mathbf{y}}) = -\sum_{k=1}^{K} y_k \log_b \hat{y}_k$$

Because $\mathbf{y}$ is one-hot, all terms vanish except the one for the true class $c$, reducing the expression to $-\log_b \hat{y}_c$. The loss is therefore simply the negative log-probability assigned to the correct class — it is large when the model is uncertain or wrong, and approaches zero as $\hat{y}_c \to 1$.

CCE is the standard loss function for **multiclass classification** in [[Machine Learning]]. The model typically outputs a raw score (logit) per class, passed through a [[Softmax]] to produce a valid probability vector $\hat{\mathbf{y}}$. BCE is a special case of CCE with $K=2$.

> [!example]- Image Classifier (Cat, Dog, Bird)
> A 3-class image classifier is shown a picture of a cat. The true label is therefore $\mathbf{y} = [1, 0, 0]$. Compute the CCE loss for two different model outputs and compare them.
> 
> **Model A** (confident and correct): $\hat{\mathbf{y}} = [0.70,\ 0.20,\ 0.10]$
> 
> Since $\mathbf{y}$ is one-hot, only the cat term survives:
> $$H(\mathbf{y}, \hat{\mathbf{y}}) = -\log_2(0.70) = 0.515 \text{ bits}$$
> 
> **Model B** (confused): $\hat{\mathbf{y}} = [0.10,\ 0.60,\ 0.30]$
> 
> $$H(\mathbf{y}, \hat{\mathbf{y}}) = -\log_2(0.10) = 3.322 \text{ bits}$$
> 
> Model B assigns only 10% probability to the correct class, producing a loss more than 6× higher than Model A. The CCE loss is entirely determined by the probability the model assigns to the true class — the distribution over wrong classes is irrelevant.

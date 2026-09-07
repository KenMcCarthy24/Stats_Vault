**Naïve Bayes** is a probabilistic classification algorithm based on [[Bayes' Theorem]]. Given training data $X$ with categorical labels $y$, it estimates the posterior probability that a new point $x$ belongs to each class, and assigns the class with the highest posterior probability as the prediction $\hat{y}$.

Bayes' Theorem states:
$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$
In order to apply Bayes' Theorem to solve a multi-class classification problem, let $C_k$ be event that an example belongs to class $k$, then Bayes' Theorem states:
$$P(C_k|x) = \frac{P(x|C_k)P(C_k)}{P(x)}$$
Where:
* $P(C_k|x)$ is the **posterior** probability that $x$ belongs to class $k$
* $P(C_k)$ is the **prior** probability that $x$ belongs to class $k$
* $P(x|C_k)$ is the **likelihood** of observing $x$ given class $k$
* $P(x)$ is the total probability of observing $x$ across all classes.

Because the denominator term $P(x)$ is not class dependent, it is a constant across all classes and is often disregarded, leaving Bayes' Theorem as:
$$P(C_k|x) \propto P(x|C_k)P(C_k)$$

The "naïve" part of Naïve Bayes is the assumption that all features in $x$ are conditionally independent given the class, meaning:
$$P(x|C_k) = \prod_{i=1}^p P(x_i|C_k)$$
So:
$$P(C_k|x) \propto P(C_k)\prod_{i=1}^pP(x_i|C_k)$$

The final estimate of the class of $x$ is given by the Maximum A Posteriori (MAP) estimator, which is the class with the maximum posterior probability.
$$\hat{y} = \arg\max_k \; P(C_k)\prod_{i=1}^p P(x_i|C_k)$$
In practice it is common to work in log space when doing this calculation to avoid numerical underflow caused by multiplying small probabilities together, so:
$$\hat{y} = \arg\max_k \left[\ln P(C_k) + \sum_{i=1}^p \ln P(x_i|C_k)\right]$$

Different variations of Naïve Bayes have different ways of calculating these prior and likelihood terms from the training data.

# Gaussian Naïve Bayes
Gaussian Naïve Bayes assumes that the likelihood of each feature $P(x_i|C_k)$ follows a [[Normal]] distribution with parameters $\hat \mu_k$ and $\hat \sigma_k^2$ for class $k$. These parameters are estimated from the data through [[Maximum Likelihood Estimation]]. The estimate for the likelihood of $x_i$ given class $k$ is given by the normal pdf value at $x_i$.
$$P(x_i|C_k) = f(x_i|\mu_k, \sigma_k^2) = \frac{1}{\sqrt{2\pi\sigma_k^2}}\exp\left(\frac{-(x_i-\mu_k)^2}{2\sigma_k^2}\right)$$

> [!example]-
> A wildlife researcher wants to classify animals as either **Fox** or **Wolf** based on two features: **weight (kg)** and **Ear Length (cm)**. From training data, the following class statistics were calculated. A new animal is observed with **weight=10 kg** and **ear length = 9 cm**. What class does it belong to according to Gaussian Naïve Bayes?
> 
> Let $k=1$ represent the "Fox" class and $k=2$ represent the "Wolf" class
> 
> Let the new data point be represented by the vector $x=(10, 9)$
> 
> |      | P(class) | $\hat \mu$ (weight) | $\hat \sigma$ (weight) | $\hat \mu$ (ear length) | $\hat \sigma$ (ear length) |
> | ---- | -------- | ------------------- | ---------------------- | ----------------------- | -------------------------- |
> | Fox  | 0.4      | 5.0                 | 1.0                    | 8.0                     | 1.5                        |
> | Wolf | 0.6      | 30.0                | 5.0                    | 11.0                    | 2.0                        |
> Assuming a Gaussian distribution for both features, the likelihoods for the new data point are calculated as:
> $$P(x_1=10|k=1)=\frac{1}{\sqrt{2\pi(1.0)^2}}\exp\left(\frac{-(10-5.0)^2}{2(1.0)^2}\right) = 1.49\times10^{-6}$$
> $$P(x_2=9|k=1)=\frac{1}{\sqrt{2\pi(1.5)^2}}\exp\left(\frac{-(9-8.0)^2}{2(1.5)^2}\right) = 0.213$$
> $$P(x_1=10|k=2)=\frac{1}{\sqrt{2\pi(5.0)^2}}\exp\left(\frac{-(10-30.0)^2}{2(5.0)^2}\right) = 2.68\times10^{-5}$$
> $$P(x_2=9|k=2)=\frac{1}{\sqrt{2\pi(2.0)^2}}\exp\left(\frac{-(9-11.0)^2}{2(2.0)^2}\right) = 0.121$$
> Now the posterior probabilities of each class can be calculated. Because there are only two features and two classes, working in log space isn't necessary here.
> $$P(k=1|x) \propto P(k=1)P(x_1=10|k=1)P(x_2=9|k=1) = (0.4)(1.49\times10^{-6})(0.213) = 1.27\times10^{-7}$$
> $$P(k=2|x) \propto P(k=2)P(x_1=10|k=2)P(x_2=9|k=2) = (0.6)(2.68\times10^{-5})(0.121) = 1.95\times10^{-6}$$
> The posterior probability for $k=2$ is larger, so the classifier predicts $\hat{y} = 2$ (**Wolf**).

# Multinomial Naïve Bayes
Multinomial Naïve Bayes is suited for features that represent counts. Each feature $x_i$ is a non-negative integer representing the number of times event $i$ occurs in the example.

The likelihood of observing feature vector $x$ given class $k$ is modeled as proportional to a [[Multinomial]] distribution:
$$P(x|C_k) \propto \prod_{i=1}^p \theta_{ki}^{x_i}$$
where $\theta_{ki}$ is the probability that a single token in a class-$k$ example is feature $i$. These are estimated from training data with Laplace smoothing parameter $\alpha$:
$$\hat{\theta}_{ki} = \frac{N_{ki} + \alpha}{N_k + \alpha p}$$
where $N_{ki}$ is the total count of feature $i$ across all class-$k$ training examples, $N_k = \sum_i N_{ki}$ is the total feature count in class $k$, and $p$ is the number of features. Setting $\alpha = 1$ prevents zero probabilities for features absent from a class in training.

The MAP decision rule in log space is:
$$\hat{y} = \arg\max_k \left[\ln P(C_k) + \sum_{i=1}^p x_i \ln \hat{\theta}_{ki}\right]$$

> [!example]-
> An email spam classifier uses a three-word vocabulary: **"buy"**, **"free"**, and **"meeting"**. From a training corpus, the following word counts were recorded. A new email with word counts $x = (2, 1, 0)$ is observed. Is it spam?
> 
> |      | P(class) | $N_{k,\text{buy}}$ | $N_{k,\text{free}}$ | $N_{k,\text{meeting}}$ | $N_k$ |
> | ---- | -------- | ------------------ | ------------------- | ---------------------- | ----- |
> | Spam | 0.7      | 30                 | 20                  | 5                      | 55    |
> | Ham  | 0.3      | 2                  | 1                   | 25                     | 28    |
> 
> With Laplace smoothing ($\alpha = 1$, $p = 3$), the estimated feature probabilities are:
> $$\hat{\theta}_{\text{spam,buy}} = \frac{31}{58} \approx 0.534, \quad \hat{\theta}_{\text{spam,free}} = \frac{21}{58} \approx 0.362, \quad \hat{\theta}_{\text{spam,meeting}} = \frac{6}{58} \approx 0.103$$
> $$\hat{\theta}_{\text{ham,buy}} = \frac{3}{31} \approx 0.097, \quad \hat{\theta}_{\text{ham,free}} = \frac{2}{31} \approx 0.065, \quad \hat{\theta}_{\text{ham,meeting}} = \frac{26}{31} \approx 0.839$$
> The log posteriors are:
> $$\ln P(\text{spam}|x) \propto \ln(0.7) + 2\ln(0.534) + 1\ln(0.362) + 0\ln(0.103) = -0.357 - 1.252 - 1.015 = -2.624$$
> $$\ln P(\text{ham}|x) \propto \ln(0.3) + 2\ln(0.097) + 1\ln(0.065) + 0\ln(0.839) = -1.204 - 4.671 - 2.741 = -8.616$$
> Since $-2.624 > -8.616$, the classifier predicts **Spam**.

# Bernoulli Naïve Bayes
Bernoulli Naïve Bayes is used when each feature is binary, indicating the **presence** ($x_i = 1$) or **absence** ($x_i = 0$) of a feature.

The likelihood for each feature given class $k$ follows a [[Bernoulli]] distribution:
$$P(x_i|C_k) = \theta_{ki}^{x_i}(1 - \theta_{ki})^{1 - x_i}$$
where $\theta_{ki}$ is the probability that feature $i$ is present in a class-$k$ example. With Laplace smoothing:
$$\hat{\theta}_{ki} = \frac{N_{ki} + \alpha}{N_k + 2\alpha}$$
where $N_{ki}$ is the number of class-$k$ training examples where feature $i$ is present, $N_k$ is the total number of class-$k$ training examples, and the denominator uses $2\alpha$ to account for both possible outcomes (present and absent).

A key distinction from Multinomial Naïve Bayes is that Bernoulli explicitly models feature absence: when $x_i = 0$, the term $(1 - \theta_{ki})$ penalizes classes where feature $i$ is commonly present. Multinomial Naïve Bayes ignores features with zero count entirely.

> [!example]-
> A sentiment classifier identifies reviews as **Positive** or **Negative** using four binary features indicating the presence or absence of the words **"excellent"**, **"terrible"**, **"recommend"**, and **"avoid"**. A new review contains "excellent" and "recommend" but not "terrible" or "avoid", so $x = (1, 0, 1, 0)$. What is the predicted sentiment?
> 
> |          | P(class) | $N_k$ | $N_{k,\text{excellent}}$ | $N_{k,\text{terrible}}$ | $N_{k,\text{recommend}}$ | $N_{k,\text{avoid}}$ |
> | -------- | -------- | ----- | ------------------------ | ----------------------- | ------------------------ | -------------------- |
> | Positive | 0.6      | 40    | 32                       | 3                       | 28                       | 4                    |
> | Negative | 0.4      | 30    | 4                        | 22                      | 5                        | 24                   |
> 
> With Laplace smoothing ($\alpha = 1$):
> $$\hat{\theta}_{\text{pos,excellent}} = \frac{33}{42} \approx 0.786, \quad \hat{\theta}_{\text{pos,terrible}} = \frac{4}{42} \approx 0.095, \quad \hat{\theta}_{\text{pos,recommend}} = \frac{29}{42} \approx 0.690, \quad \hat{\theta}_{\text{pos,avoid}} = \frac{5}{42} \approx 0.119$$
> $$\hat{\theta}_{\text{neg,excellent}} = \frac{5}{32} \approx 0.156, \quad \hat{\theta}_{\text{neg,terrible}} = \frac{23}{32} \approx 0.719, \quad \hat{\theta}_{\text{neg,recommend}} = \frac{6}{32} \approx 0.188, \quad \hat{\theta}_{\text{neg,avoid}} = \frac{25}{32} \approx 0.781$$
> The posterior proportionals are:
> $$P(\text{pos}|x) \propto (0.6)(0.786)(1-0.095)(0.690)(1-0.119) = (0.6)(0.786)(0.905)(0.690)(0.881) \approx 0.259$$
> $$P(\text{neg}|x) \propto (0.4)(0.156)(1-0.719)(0.188)(1-0.781) = (0.4)(0.156)(0.281)(0.188)(0.219) \approx 7.22\times10^{-4}$$
> Since $0.259 > 7.22\times10^{-4}$, the classifier predicts **Positive**.

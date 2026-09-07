Let $X$ and $Y$ be two [[Random Variable|random variables]] and define the sum as $Z = X+Y$.

If $X$ and $Y$ are **independent**, the distribution of their sum is determined by the **convolution** of their individual distributions.

## Probability Distributions

### Discrete Case (PMF)
If $X$ and $Y$ are [[Discrete Probability Distributions|discrete]] random variables with probability mass functions $P(X)$ and $P(Y)$:

$$P(Z=z) = \sum_{k} P(X=k) P(Y=z-k)$$

### Continuous Case (PDF)
If $X$ and $Y$ are [[Continuous Probability Distributions|continuous]] random variables with probability density functions $f_X$ and $f_Y$:

$$f_Z(z) = (f_X * f_Y)(z) = \int_{-\infty}^{\infty} f_X(x) f_Y(z-x) \, dx$$

---
## Moments

### Expectation (Mean)
The [[Expectation and Moments#1st Raw Moment Expectation Value|expectation value]] is linear. This property holds **whether or not** $X$ and $Y$ are independent:

$$E[Z] = E[X] + E[Y]$$

### Variance
The [[Expectation and Moments#2nd Central Moment Variance|variance]] depends on independence.

**If $X$ and $Y$ are independent:**
$$Var[Z] = Var[X] + Var[Y]$$

**General Case (Dependent Variables):**
If they are not independent, the [[Covariance and Correlation|Covariance]] must be accounted for:
$$Var[Z] = Var[X] + Var[Y] + 2Cov(X, Y)$$

---

## Other Properties

* If $X$ and $Y$ are **independent**, the [[Moment Generating Functions|Moment Generating Function]] of the sum is the product of the individual MGFs:
$$M_{Z}(t) = M_X(t) \cdot M_Y(t)$$
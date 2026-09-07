For a sample of observations $\{x_1, x_2, \dots, x_n\}$, the **sample mean** is defined as the [[Means and Averages of Data#Arithmetic Mean|arithmetic mean]] of the observations:

$$\bar{X} = \frac{1}{n} \sum_{i=1}^{n} x_i$$

The sample mean serves as both a descriptive statistic and an **[[Bias#Example Bias of Sample Mean $ bar{X}$|unbiased]] [[Estimators|estimator]]** for the population mean $\mu$. As an estimator, it satisfies:

$$\mathbb{E}[\bar{X}] = \mu$$
---
# Sample Mean Vector

When dealing with multivariate data, let $\mathbf{X}$ be an $n \times p$ data matrix where $n$ is the number of observations and $p$ is the number of variables. An element $x_{ij}$ represents the $j$-th variable of the $i$-th observation.

If we let $\mathbf{x}_i^\top$ denote the $i$-th row (the $i$-th observation vector), the **sample mean vector** $\bar{\mathbf{x}}$ is the average of these $n$ row vectors:

$$\bar{\mathbf{x}} = \frac{1}{n} \sum_{i=1}^{n} \mathbf{x}_i = \begin{bmatrix} \bar{x}_1 \\ \bar{x}_2 \\ \vdots \\ \bar{x}_p \end{bmatrix}$$

Where each component $\bar{x}_j$ is the sample mean of the $j$-th variable:

$$\bar{x}_j = \frac{1}{n} \sum_{i=1}^{n} x_{ij}$$
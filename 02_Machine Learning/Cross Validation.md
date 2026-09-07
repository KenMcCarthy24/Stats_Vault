**Cross Validation** is a data resampling technique used in [[Machine Learning]] to estimate a model's test error. It works by training the model on multiple subsets of the dataset and testing it on unseen portions. This maximizes data usage—ensuring every data point is used for both training and validation—and helps prevent overfitting while ensuring the model generalizes well.

To guarantee an unbiased final evaluation, a [[Data Splitting#The Train-Test Split|train-test split]] must be performed first, with cross validation applied *only* to the resulting training set. This distinguishes cross validation from a standard [[Data Splitting#The Train-Validation-Test Split|train-test-validation]] split, which relies on a single, static validation set.

Ultimately, cross validation results are used for model comparison, whether evaluating completely different algorithms on the same dataset or tuning hyperparameters for a single model.

## Leave-One-Out Cross Validation (LOOCV)

Leave-One-Out Cross Validation involves excluding a single data point from the dataset, training the model on the remaining data, and evaluating the error on that excluded point. This process is repeated for every point in the dataset, and the individual errors are averaged to calculate the final cross validation error.

More formally, let the training dataset $(X, y)$ contain $n$ examples. For each data point $(X_i, y_i)$:
* Exclude $(X_i, y_i)$ from the training dataset.
* Train the model using the remaining $n-1$ examples.
* Evaluate the model on the held-out point $(X_i, y_i)$ to obtain a validation error $e_i$.

The final cross validation error is the average of these individual validation errors:
$$CV_n = \frac{1}{n}\sum_{i=1}^n e_i$$
LOOCV can be expensive to implement, requiring the training of $n$ different models in order to produce the final cross validation error.

> [!note] Special Case
> If the model is a linear model fit with [[Ordinary Least Squares (OLS)]], there is a shortcut that only requires a single model fit using all the training data. In that case:
> $$CV_n = \frac{1}{n}\sum_{i=1}^n\left(\frac{y_i-\hat y_i}{1-h_i}\right)^2$$
> where $h_i$ is the [[Leverage and Influence|leverage]] of the $i$-th training point, reflecting the amount that observation $X_i$ influences its own fit. $h_i$ can be found as the $i$-th diagonal element of the [[Ordinary Least Squares (OLS)#The Hat Matrix|hat matrix]].

To visualize how LOOCV splits data, let each line below represent how the training data is split for the training of a single model. Points represented by O are used for training and points represented by X are used for validation. In this case $n=10$:

XOOOOOOOOO
OXOOOOOOOO
OOXOOOOOOO
OOOXOOOOOO
OOOOXOOOOO
OOOOOXOOOO
OOOOOOXOOO
OOOOOOOXOO
OOOOOOOOXO
OOOOOOOOOX

## K-Fold Cross Validation

K-Fold Cross Validation randomly splits the training data into $k$ groups (or folds) of approximately equal size. The model is then trained $k$ times, each time holding out a different one of the $k$ folds and training on the remaining folds.

More formally, let the training dataset $(X, y)$ contain $n$ examples that have been equally split into $k$ folds $F_1, ..., F_k$. For each fold $F_i$:
* Exclude $F_i$ from the training dataset.
* Train the model using the remaining $k-1$ folds.
* Evaluate the model on the held-out fold $F_i$ to obtain a validation error $e_i$.

The final cross validation error is the average of these individual validation errors:
$$CV_k = \frac{1}{k}\sum_{i=1}^k e_i$$

> [!NOTE]
> If $k=n$, then each data point has its own fold. This is equivalent to LOOCV.

To visualize how K-Fold Cross Validation splits data, let each line below represent how the training data is split for the training of a single model. Points represented by O are used for training and points represented by X are used for validation. In this case $n=10$ and $k=3$:

XXXOOOOOOO
OOOXXXOOOO
OOOOOOXXXX

## Bias-Variance Tradeoff in Cross Validation

The choice of $k$ in K-Fold Cross Validation involves a [[Bias-Variance Tradeoff]] in the *estimate of the test error itself*.

**Bias**:
* A model trained on fewer data points tends to have higher error than one trained on more data, meaning it will overestimate the true test error.
* Since LOOCV trains on $n-1$ points its error estimate has very low bias.
* K-Fold with smaller $k$ (e.g., $k=5$) trains on a smaller fraction of the data per fold, introducing slightly more bias into the estimate.

**Variance**:
* In LOOCV, the $n$ training sets overlap almost entirely (each shares $n-2$ points with every other), so the $n$ resulting error estimates are highly correlated. Averaging highly correlated quantities yields a result with higher variance.
* In K-Fold with smaller $k$, the training sets overlap less, producing less correlated error estimates and a lower-variance average.

In practice, $k=5$ or $k=10$ tends to strike the best balance, yielding error estimates that are neither excessively biased nor excessively variable. This—combined with the computational advantage of training far fewer models than LOOCV—is why K-Fold Cross Validation is generally preferred.
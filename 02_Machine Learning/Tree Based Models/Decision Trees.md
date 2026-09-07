![[Tree Region Diagram 1.png]]

**Decision Trees** are a class of [[Machine Learning]] model that, based on the training data $(X, y)$, algorithmically segment the $p$-dimensional predictor space into distinct and non-overlapping regions. Depending on how they are optimized and used, they can be used for both Regression and Classification.

Decisions trees are considered highly interpretable/explainable and can handle categorical predictors natively. However they tend not to be as accurate as other model types and cannot extrapolate, as predictions are bounded to bounds of training data.
# Structure

The splitting rules used to segment the predictor space can be summarized as a tree with the following properties:
* Each node represents a subspace of the predictor space $R_k$
* The root node is $R_0$, representing the entire predictor space
* Each leaf node represents the final regions that segment the space
* Each non-leaf node has exactly two child nodes, representing its region $R_k$ being divided into two new regions.
	* These splits occur on one data dimension $X_j$ at a cut-point $s_j$, splitting $R_k$ into the subset where $X_j \geq s_j$ and the subset where $X_j < s_j$
	* If $X_j$ is categorical, the split is instead defined by a subset of categories $\mathcal{S}_j$, partitioning $R_k$ into the subset where $X_j \in \mathcal{S}_j$ and the subset where $X_j \notin \mathcal{S}_j$

> [!example]- 2D Example Tree (all continuous)
> ![[Tree Region Diagram 1.png]]
> In this simple 2D example (same as page image):
> * $R_0$ is the root node representing the entire 2D region
> * $R_0$ is split on $X_1$, making regions $R_1$ and $R_2$.
> * $R_1$ is split on $X_2$, making regions $R_3$ and $R_4$.
> * $R_2$ is split on $X_2$, making regions $R_5$ and $R_6$.
> * $R_3$ is split on $X_1$, making regions $R_7$ and $R_8$.
> * Final leaf nodes are $(R_4, R_5, R_6, R_7, R_8)$ representing the final segmentation of the space represented by the decision tree.

> [!example]- 2D Example Tree (categorical and continuous)
> ![[Tree Region Diagram 2.png]]
> In this example $X_1$ is categorical with categories $(A, B, C, D)$ and $X_2$ is continuous:
> * $R_0$ is the root node representing the entire predictor space
> * $R_0$ is split on $X_1$ with $\mathcal{S}_1 = \{A, B\}$, making $R_1$ (where $X_1 \in \{A, B\}$) and $R_2$ (where $X_1 \in \{C, D\}$)
> * $R_1$ is split on $X_2$, making regions $R_3$ and $R_4$.
> * $R_2$ is split on $X_2$, making regions $R_5$ and $R_6$.
> * Final leaf nodes are $(R_3, R_4, R_5, R_6)$ representing the final segmentation of the space.
# Building Decision Trees
## Recursive Binary Splitting
Decision Trees are most often optimized through **Recursive Binary Splitting**, a top-down, greedy algorithm used to build a decision tree from data. Going through each node $R_k$ recursively as they appear, at each step:
1. For each data dimension $X_j$, find the optimal split that minimizes some splitting criteria (dependent on task). For continuous $X_j$ this is a cutpoint $s_j$; for categorical $X_j$ this is a subset of categories $\mathcal{S}_j$.
2. Keep the split $(j^*, s_{j^*})$ that minimizes the splitting criterion across all dimensions, and apply it to divide $R_k$ into two child regions.

This process repeats on each resulting child node until a stopping condition is met. Stopping conditions include (these are often hyperparameters):
* Maximum Number of Leaf Nodes
* Maximum tree depth
* Node Purity (All data points in region have same $y$ value)
## Pruning
Recursive Binary Splitting by itself tends to fit very well to the training data, always fitting it perfectly if allowed to to continue until each data point has its own child node, but this leads to poor test performance (High [[Bias-Variance Tradeoff#Variance|Variance]]/overfitting). On the other hand too shallow of a tree won't effectively capture the patterns in the data (High [[Bias-Variance Tradeoff#Bias|Bias]]/underfitting).

To combat this [[Bias-Variance Tradeoff]], building decision trees usually involves an extra **pruning** step called **Cost Complexity Pruning**. Define a new cost function that is a function of a tree $T$ and a tuning parameter $\alpha$:
$$f(T, \alpha) = Error(T) + \alpha|T|$$
where:
* $Error(T)$ is an error function depending on task (e.g. RSS for regression or misclassification rate for classification)
* $|T|$ is the number of leaf nodes of the tree

This penalizes trees that grow too large without significant improvements in error. The role of $\alpha$ is to control the Bias-Variance Tradeoff directly:
* When $\alpha=0$, there is no penalty on size, yielding the largest tree possible.
* As $\alpha$ increases, the penalty on leaf count grows, so trees with fewer leaves are preferred. Branches whose error reduction does not justify the added leaves get collapsed into a leaf node.
* As $\alpha \rightarrow \infty$, the penalty dominates and the tree collapses to just the root node $R_0$.


> [!NOTE] 
> Pruning is often not applied when decision trees are part of an ensemble such as in [[Bagging]] or [[Random Forest]]. This is due to the ensemble approach reducing variance, replacing the need for pruning


## Full Training Procedure
Below is the full training procedure that uses Recursive Binary Splitting followed by Cost Complexity Pruning.
1. Grow a large tree $T_0$ using Recursive Binary Splitting, stopping based on defined stopping criteria.
2. For a given $\alpha$, find a subtree $T_\alpha$ that minimizes $f(T, \alpha)$. As $\alpha$ sweeps from 0 to $\infty$, this produces a finite, nested sequence of subtrees. Each one is obtained from the previous by collapsing the internal node whose removal yields the smallest per-leaf increase in error. 
3. Select $\alpha$ via [[Cross Validation#K-Fold Cross Validation|K-Fold Cross Validation]]: For each fold, grow $T_0$ on the training portion, generate the sequence of subtrees, and evaluate each on the held-out fold. Pick the $\alpha^*$ that minimizes validation error
4. Refit on the full training set and return $T_{\alpha^*}$ as the final tree.

# Decision Tree Regression

## Prediction

For a test point $x^*$ that falls into leaf region $R_k$, the prediction is the mean response of all training points in that region:

$$\hat{y}(x^*) = \bar{y}_k = \frac{1}{|R_k|}\sum_{i \in R_k} y_i$$

The mean is a natural choice here because it is the value that minimizes the sum of squared deviations within the region — consistent with the RSS splitting criterion below.

Since $\hat y$ is always a training-set mean, predictions are bounded by $[\min(y), \max(y)]$, and therefore cannot extrapolate.
## Splitting Criterion

The splitting criterion for regression is the [[Goodness of Fit#Residual Sum of Squares (RSS)|Residual Sum of Squares]]. At each node with region $R_k$, for each predictor $X_j$ and candidate cutpoint $s$, define the two proposed child regions:

$$R_L = \{x \in R_k : x_j < s\}, \qquad R_R = \{x \in R_k : x_j \geq s\}$$

The optimal split $(j^*, s_{j^*})$ minimizes the **combined RSS** across both child regions:

$$\text{RSS}(j, s) = \sum_{i \in R_L}(y_i - \bar{y}_L)^2 + \sum_{i \in R_R}(y_i - \bar{y}_R)^2$$

where $\bar{y}_L$ and $\bar{y}_R$ are the means of the response in each child region. This is equivalent to maximizing the reduction in variance explained by the split.

At the end of training, the total training RSS is the sum of the within-region RSS across all leaf nodes $L$:

$$\text{RSS}_{total} = \sum_{R_k \in L} \sum_{i \in R_k} (y_i - \bar{y}_k)^2$$
# Decision Tree Classification

## Prediction

For a test point $x^*$ that falls into leaf region $R_k$, let $\hat{p}_c$ denote the proportion of training points in $R_k$ belonging to class $c$. The predicted class is the majority class in the region:

$$\hat{y}(x^*) = \underset{c}{\arg\max}\; \hat{p}_c$$

## Splitting Criterion

The goal of each split is to produce child nodes that are as **pure** as possible — dominated by a single class. Two standard impurity measures are used.

### Gini Index

$$G = \sum_{c=1}^{C} \hat{p}_c(1 - \hat{p}_c) = 1 - \sum_{c=1}^{C} \hat{p}_c^2$$

$G = 0$ for a perfectly pure node (all one class) and reaches its maximum of $1 - 1/C$ when all $C$ classes are equally represented. Intuitively, $G$ is the probability that a randomly drawn point would be mislabeled if assigned a class drawn from the region's class distribution.

### [[Entropy Quantities#Entropy|Entropy]]

$$H = -\sum_{c=1}^{C} \hat{p}_c \log_2 \hat{p}_c$$

(with the convention $0 \log_2 0 = 0$). $H = 0$ for a pure node and is maximized at $\log_2 C$ when all classes are equally represented.

### Choosing a Split

For both criteria, the optimal split $(j^*, s_{j^*})$ is found by minimizing the **weighted combined impurity** $Q$ across both child regions, where $Q$ is either $G$ or $H$:

$$Q(j, s) = \frac{n_L}{n}\,Q_L + \frac{n_R}{n}\,Q_R$$

where $n = |R_k|$, $n_L = |R_L|$, $n_R = |R_R|$.

In practice, Gini and entropy produce similar trees. Gini is cheaper to compute (no logarithm), while entropy can produce slightly more balanced splits.

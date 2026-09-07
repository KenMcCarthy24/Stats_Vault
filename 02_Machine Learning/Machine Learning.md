**Machine Learning** refers to a broad class of statistical algorithms with the shared goal of learning information from data and making decisions or predictions without being explicitly programmed. By using these algorithms to identify patterns in data, models can generalize to new, unseen information.

Machine Learning Algorithms in general fall into one of two categories:
# Supervised Learning
Supervised learning algorithms are trained on labeled data (input-output pairs) with the goal of having a model that can predict outputs for new, unseen, and unlabeled data.

Supervised learning algorithms usually fall into one of two categories, with some models/algorithms falling under both categories depending on how they are used:
### Regression
The goal of a regression algorithm is to model and predict **continuous numerical values** based on input features, essentially learning a mathematical function that approximates the output as well as possible.

Examples:
[[Linear Regression]], [[K-Nearest Neighbors]], [[Decision Tree Regression]], [[Random Forest Regression]]

### Classification
The goal of a classification algorithm is to model a discrete or categorical variable based on input features, usually outputting either one of several pre-determined categories as the result or a probability distribution over the categories.

A distinction is usually made between 

Examples:
[[Logistic Regression]], [[K-Nearest Neighbors]], [[Naïve Bayes]], [[Decision Tree Classification]], [[Support Vector Machines]], [[Random Forest Classification]]

# Unsupervised Learning
Unsupervised learning algorithms are designed to be used on un-labeled data, and seek to discover hidden patterns, structures, or relationships between the input variables.

Types of unsupervised learning tasks include:
### Clustering
The goal of a clustering algorithm is to group similar data points together into clusters based on distance or density metrics.

Examples:
[[K-Means Clustering]], [[Hierarchical Clustering]], [[DBSCAN]] 
### Dimensionality Reduction
The goal of a dimensionality reduction algorithm is to take high dimensional data and intelligently map it down to some lower dimensional space, while also preserving as much of the useful information within the data as possible. 

Examples:
[[Principal Component Analysis]], [[t-SNE]], [[UMAP]], [[Singular Value Decomposition]]
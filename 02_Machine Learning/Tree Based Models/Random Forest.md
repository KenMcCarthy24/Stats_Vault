A **Random Forest** is an ensemble [[Machine Learning]] model that trains a collection of [[Decision Trees]] on different subsets of the training data, similar to [[Bagging]] decision trees. The key difference is that in a random forest, each tree is trained on a bootstrap sample from the training set (bagging) and at each split, only a random subset of size $m$ of the $p$ predictors are considered. Typically $m \approx \sqrt{p}$ for classification tasks and $m \approx p/3$ for regression tasks is a good rule of thumb.

This has the effect of *decorrelating* the trees. If there are a few very strong predictors in the dataset, all trees would likely make their initial splits based on those predictors, making all trees very similar and making their predictions highly correlated. By forcing trees to ignore a majority of predictors, it creates more diversity in the decisions the trees are making, which often leads to a decrease in error when their results are aggregated (averaging for regression, majority vote for classification).

Random forests can also give an [[Bagging#Out-of-Bag Error|Out-of-Bag Error]] (details in linked page), providing an estimation for test error without the need for a validation set or cross validation. 



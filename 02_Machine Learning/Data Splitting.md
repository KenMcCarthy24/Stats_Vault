In [[Machine Learning]], splitting the dataset into a training set, a testing set, and often a validation set is a fundamental practice to ensure the model generalizes well to new, unseen data.

When performing is splitting, it is necessary for the distributions of the different sets to be as similar as possible to make sure they are representing the same set of conditions. To ensure this the data is often randomized/shuffled before splitting.

---
## The Train-Test Split
The simplest way to evaluate a machine learning model is to divide the dataset into two distinct subsets.

* **Training Set (Usually 70% - 80%):** The portion of the data used to actually train the algorithm. The model learns the underlying patterns, weights, and relationships from this data.
* **Testing Set (Usually 20% - 30%):** The portion of the data kept completely hidden from the model during training. Used to evaluate how well the model performs on new, unseen data.

If the model is trained and evaluated on the *exact same* data, the model might just memorize the training data (a problem called **overfitting**). Testing on unseen data gives a realistic estimate of real-world performance.

---
## The Train-Validation-Test Split
When tuning hyperparameters or comparing different algorithms, a three-way split is often used.

* **Training Set (Usually 60% - 80%):** Used to train the initial models.
* **Validation Set (Usually 10% - 20%):** Used to "tune" the model. Evaluating the trained models on this set to tweak hyperparameters and select the best-performing algorithm. 
* **Testing Set (Usually 10% - 20%):** The final, untouched "holdout" set. Used *only once* at the very end of the project to evaluate the absolute final model.

If the model is repeatedly tweaked to get a higher score on the *Testing Set*, information is leaked about the test data into the model. It becomes biased toward the test set and loses generality. The validation set acts as a dataset that is not used for optimization but is used for adjustments, keeping the test set completely pristine for the final evaluation. 
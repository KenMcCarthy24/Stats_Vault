Many metrics used to evaluate the performance of a classification algorithm revolve around a **Confusion Matrix** $C$, which compares the true observed labels $y$ to the predicted labels $\hat{y}$. It is constructed so that:
* Each row of the matrix represents an actual class.
* Each column represents a predicted class.
* Each cell $C_{ij}$ counts how many instances were predicted as being $\hat{y}_j$ while actually being $y_i$.
* The diagonal elements represent correct predictions where the predicted class matches the actual class.
* The off-diagonal elements represent errors.

Confusion Matrices can either be binary (two classes) or multi-class (more than two classes).

**Binary Confusion Matrix:**

|                     | Predicted Positive  | Predicted Negative  |
| :------------------ | :-----------------: | :-----------------: |
| **Actual Positive** | True Positive (TP)  | False Negative (FN) |
| **Actual Negative** | False Positive (FP) | True Negative (TN)  |

**Multi-Class Confusion Matrix (3-Class Example):**

| | Predicted Class A | Predicted Class B | Predicted Class C |
| :--- | :---: | :---: | :---: |
| **Actual Class A** | True A <br> *(Correct)* | Misclassified as B | Misclassified as C |
| **Actual Class B** | Misclassified as A | True B <br> *(Correct)* | Misclassified as C |
| **Actual Class C** | Misclassified as A | Misclassified as B | True C <br> *(Correct)* |

---

# Metrics

Various metrics can be calculated using the confusion matrix for a classifier. For multi-class scenarios, metrics like Precision, Recall, and F-1 Score are typically calculated on a *per-class* basis (e.g., evaluating Class $i$ against all other classes) before being aggregated.

### Accuracy
Accuracy is the proportion of the total examples that were correctly classified. It is calculated as the sum of the diagonals of $C$ divided by the sum of all cells.
$$Accuracy = \frac{\sum_{i=1}^k C_{ii}}{\sum_{i=1}^k\sum_{j=1}^k C_{ij}}$$

Or more simply in the binary case:
$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$

**Examples of when to use Accuracy:**
1. **Balanced Datasets:** When evaluating a model predicting whether an animal is a cat or a dog, and your dataset contains roughly 50% cats and 50% dogs. 
2. **Uniform Cost of Errors:** When the "cost" or penalty of a False Positive is exactly the same as a False Negative (e.g., guessing user demographics for basic analytics where no critical decisions are made based on the outcome).

### Precision
Precision is the proportion of the examples predicted as being a specific class that *actually* belonged to that class. It punishes **False Positives**. Precision is between 0 and 1 with higher precision being ideal. 

For a specific class $i$ in a multi-class problem, it is the true predictions for class $i$ divided by the sum of the entire column $i$ (everything predicted as $i$):
$$Precision_i = \frac{C_{ii}}{\sum_{j=1}^k C_{ji}}$$

In the binary case:
$$Precision = \frac{TP}{TP + FP}$$

**Examples of when to use Precision:**
1. **Email Spam Detection:** You want to be absolutely sure that if you flag an email as "Spam" (Positive), it actually is. A False Positive here means a legitimate, potentially important email is hidden from the user.
2. **Video Recommendations:** If you recommend a video to a user, you want a high probability they will like it. Recommending a bad video (False Positive) hurts user retention more than failing to recommend every single good video (False Negative).

### Recall
Recall is the proportion of actual examples of a specific class that were correctly identified by the model. It punishes **False Negatives**. Recall is between 0 and 1 with higher recall being ideal. 

For a specific class $i$ in a multi-class problem, it is the true predictions for class $i$ divided by the sum of the entire row $i$ (all actual instances of class $i$):
$$Recall_i = \frac{C_{ii}}{\sum_{j=1}^k C_{ij}}$$

In the binary case:
$$Recall = \frac{TP}{TP + FN}$$

**Examples of when to use Recall:**
1. **Medical Diagnoses (e.g., Cancer Detection):** The cost of missing a cancerous tumor (False Negative) is catastrophic, whereas a False Positive only leads to a secondary screening. 
2. **Bank Fraud Detection:** Banks want to flag as many fraudulent transactions as possible. If a few normal transactions get flagged and paused (False Positives), it's a minor inconvenience compared to letting a thief drain a customer's account (False Negative).

### $F_1$ Score
The $F_1$ Score is the [[Means and Averages of Data#Harmonic Mean|Harmonic Mean]] of Precision and Recall. It provides a single metric that balances both concerns, particularly useful when you cannot afford to optimize for just one at the expense of the other. $F_1$ Score is between 0 and 1 with higher $F_1$ score being ideal. 

For a specific class $i$ in a multi-class problem:
$$F_{1,i} = 2 \times \frac{Precision_i \times Recall_i}{Precision_i + Recall_i}$$

In the binary case:
$$F_1 = 2 \times \frac{Precision \times Recall}{Precision + Recall} = \frac{2TP}{2TP + FP + FN}$$

**Examples of when to use $F_1$ Score:**
1. **Imbalanced Datasets (e.g., Rare Disease Detection):** If only 1% of patients have a disease, a model that guesses "No Disease" every time will have 99% Accuracy, but a 0% $F_1$ Score. $F_1$ properly exposes the model's inability to identify the minority class.
2. **Search Engine Queries / Information Retrieval:** When a user searches for a document, the engine must return highly relevant results (Precision) while ensuring it doesn't miss the most critical documents (Recall). The $F_1$ score measures this delicate balance.

# $F_\beta$ Score
An extension of the $F_1$ Score, the $F_\beta$ score also takes into account the precision and the recall, but weights the recall as $\beta$ times more important as the precision. The $F_1$ score is the case where they are equally weighted. $\beta$ can be chosen to be $< 1$ to weight precision higher than recall. For example:
* **$F_2$ Score**: $\beta=2$. Weights recall twice as high as precision.
* **$F_{0.5}$ Score**: $\beta=0.5$. Weights precision twice as high as recall.

For a specific class $i$ in a multi-class problem:
$$F_{\beta, i} = \frac{(1+\beta^2)*(Precision_i)(Recall_i)}{\beta^2(Precision_i)+Recall_i}$$
In the binary case:
$$F_\beta = \frac{(1+\beta^2)TP}{\beta^2(TP+FN)+(TP+FP)}$$

---


> [!example]-
> Given the following confusion matrix, calculate the accuracy, precision, recall, and $F_1$ Score
> 
> |                     | Predicted Positive | Predicted Negative |
> | :------------------ | :----------------: | :----------------: |
> | **Actual Positive** |         50         |         15         |
> | **Actual Negative** |         5          |         30         |
> So:
> * TP = 50
> * TN = 30
> * FP = 5
> * FN = 15
> $$Accuracy = \frac{TP + TN}{TP + TN + FP + FN} = \frac{50+30}{50+30+5+15} = 0.8$$
> $$Precision = \frac{TP}{TP + FP} = \frac{50}{50+5}=0.91$$
> $$Recall = \frac{TP}{TP + FN}=\frac{50}{50+15} = 0.77$$
> $$F_1 = 2 \times \frac{Precision \times Recall}{Precision + Recall} = 2\times\frac{(0.91)(0.77)}{0.91+0.77} = 0.83$$
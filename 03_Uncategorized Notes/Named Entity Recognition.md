**Named Entity Recognition** is a Natural Language Processing task that aims to label words/phrases within a document as belonging to one of several categories.

For example the sentence:

"Ally Mulligan is coming to New York City on December 18th for the Global Marketing Conference"

might get labeled as:
"(Ally Mulligan)<sub>Person</sub> is coming to (New York City)<sub>Place</sub> on (December 18th)<sub>Date</sub> for the (Global Marketing Conference)<sub>Event</sub>"
# Classification Problem
Under the hood, Named Entity Recognition is usually framed as a [[Classification Problem]], with each word/token in a document being classified as having one of several annotations. The most common classification format is **Inside-Outside-Beginning (IOB)** which has tags like:
* B-x (Beginning): The first token of a named entity of type x
* I-x (Inside): Any tokens within a named entity x that aren't the first token
* O (Outside): Tokens that are not part of any entity

x is replaced with whatever tags are being considered such as PER (Person), PL (Place), DATE, or EVT (Event).

So if there are $k$ different classes of tag, there are $2k+1$ different categories for the classification.

Using the same example above, each word would ideally be given the following labels:

| **Word**   | Label  |
| ---------- | ------ |
| Ally       | B-PER  |
| Mulligan   | I-PER  |
| is         | O      |
| coming     | O      |
| to         | O      |
| New        | B-PL   |
| York       | I-PL   |
| City       | I-PL   |
| on         | O      |
| December   | B-DATE |
| 18th       | I-DATE |
| for        | O      |
| the        | O      |
| Global     | B-EVT  |
| Marketing  | I-EVT  |
| Conference | I-EVT  |
# Evaluation Metrics
The vast majority of tokens in any given document are "Outside" (`O`) any entity, simply measuring overall accuracy is heavily skewed and misleading. 

Instead, NER models are evaluated using metrics that focus specifically on the entities themselves:
* **[[Confusion Matrix and Metrics#Precision|Precision]]:** The percentage of entities found by the model that are actually correct. 
* **[[Confusion Matrix and Metrics#Recall|Recall]]:** The percentage of actual entities in the text that the model successfully found. 
* **[[Confusion Matrix and Metrics#F-1 Score|F-1 Score]]:** The harmonic mean of Precision and Recall, providing a balanced measure of a model's performance. 

These metrics can be calculated at either the Token-Level (each word individually) or at the Entity-Level (entire entity at once).
# Methodology
In modern NLP, the most common methodology for this classification task is to:
1. Encode each token in the document as a multi-dimensional vector
2. Use a pre-trained transformer to transform the token vectors and infuse them with the meaning and context from the rest of the document
3. Train a new classification head on top of the transformer, taking the [[Softmax]] of each transformed word vector to determine the probability that each word is in each category.
4. Choose the maximum probability category for each word.
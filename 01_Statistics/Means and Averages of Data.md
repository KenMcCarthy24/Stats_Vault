# Averages vs. Means

There is a technical distinction between an **average** and a **mean**:

- **Average**: A general term for a "measure of central tendency." It represents a single value that attempts to describe a set of data by identifying the central position within that set.
- **Mean**: A specific type of average calculated using a mathematical formula. There are several types of means, each suited for different types of data and applications.

Given a set of data $X=[x_1, x_2, \dots, x_n]$ there are several ways to define the mean $\bar{X}$ of the data:
# Arithmetic Mean

The arithmetic mean is the most common mean and is the quantity that is most often referred to as just the "mean" or "average" of the data.

It is the sum of all the numbers divided by their count.

$$\bar{X}_A = \frac{1}{n}\sum_{i=1}^nx_i$$

The arithmetic mean is best used when quantities combine by addition and there are no extreme outliers. Examples:

- Mean Test Score
- Mean Temperature
- Mean Height

# Geometric Mean

The Geometric Mean is the $n$-th root of the product of all of the data

$$\bar{X}_G = \left(\prod_{i=1}^nx_i\right)^{1/n}$$

The Geometric Mean is best used when quantities multiply together and the data is all positive such as growth and ratios. Examples:

- Investment returns
    - +50% and −50% have an arithmetic mean of 0%, but a geometric mean of −13.4%, which correctly reflects the fact that the investment loses value overall.
- Population Growth
# Harmonic Mean
The Harmonic Mean is the reciprocal of the sum of the reciprocals of all of the data

$$\bar{X}_H = n\left(\sum_{i=1}^n\frac{1}{x_i}\right)^{-1}$$

The Harmonic Mean is best used when when averaging rates where the numerator is fixed and the denominator varies. Examples:
- Average speed (equal distances at different speeds)
- Average cost per unit

The Arithmetic, Geometric, and Harmonic means are collectively referred to as the **Pythagorean means**.

# Generalized Mean

The three Pythagorean means, along with other useful quantities, can be represented by a single Generalized mean, which is parametrized by a number $p$.

$$\bar{X}_{Gen}(p) = \left(\frac{1}{n}\sum_{i=1}x_i^p\right)^{1/p}$$

For certain values of $p$, the generalized mean corresponds to well known quantities:

- $p=-\infty$ : Minimum of the data
- $p=-1$ : Harmonic Mean
- $\displaystyle \lim_{p \to 0}$ : Geometric Mean
- $p=1$: Arithmetic Mean
- $p=2$ : Root Mean Square
- $p=+\infty$ : Maximum of the data

# Other Measures of Central Tendency

Beyond means, there are other ways to calculate the "average" of a dataset that are more robust to outliers or better suited for categorical data.

### Median

The median is the middle value in a dataset when the values are arranged in ascending or descending order. If there is an even number of observations, the median is the arithmetic mean of the two middle values. Best used for skewed data or data with extreme outliers.

### Mode

The mode is the value that appears most frequently in a dataset. A dataset can have one mode, more than one mode (bimodal or multimodal), or no mode at all. Often used for categorical data where numerical calculations don't apply

### Midrange

The midrange is the arithmetic mean of the maximum and minimum values in a dataset. Used for quick estimates when only the range is known. 

$$\text{Midrange} = \frac{\min(X) + \max(X)}{2}$$
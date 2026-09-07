Given two categorical variables $A$ and $B$ observed in a sample of size $n$, organized into a contingency table with $r$ rows and $c$ columns, inferences about the relationship between the variables are evaluated using a [[Hypothesis Test]] structured as:

$$
\begin{aligned}
H_0: & \quad \text{The two variables are independent} \\
     & \quad (\text{There is no association between the variables}) \\
H_1: & \quad \text{The two variables are dependent} \\
     & \quad (\text{There is an association between the variables})
\end{aligned}
$$
A contingency table is a table where each set of rows represents the levels of variable $A$ and each column represents the levels variable $B$. The value of the cell $O_{ij}$ is the total count of observed samples where both variables are true:

|                          | Variable B (Level 1) | Variable B (Level 2) |    Row Totals     |
| :----------------------- | :------------------: | :------------------: | :---------------: |
| **Variable A (Level 1)** |       $O_{11}$       |       $O_{12}$       |       $R_1$       |
| **Variable A (Level 2)** |       $O_{21}$       |       $O_{22}$       |       $R_2$       |
| **Column Totals**        |        $C_1$         |        $C_2$         | $N$ (Grand Total) |


The estimator used is the comparison between the **Observed Counts ($O_{ij}$)** and the **Expected Counts ($E_{ij}$)** derived under the assumption of independence.

$$E_{ij} = \frac{R_iC_j}{N}$$
This is based on the fact that if two random variables $A$ and $B$ are independent:
$$P(A \cap B) = P(A)P(B)$$

---

## Chi-Square Test for Independence

**Conditions:**
1. **Random Sample**: The data comes from a random sample or randomized experiment.
2. **Counted Data**: The data consists of counts (frequencies) for categorical variables.
3. **Large Counts**: All **expected counts** must be at least 5 ($E_{ij} \ge 5$).

> [!warning]
> If expected counts are too low, the Chi-Square approximation fails. Categories may need to be merged (collapsed) to satisfy this condition.

**Test Statistic:**
The test statistic follows a [[Chi-Squared]] distribution so this is a [[Chi-Squared Test]].

$$\chi^2 = \sum_{\text{all cells}} \frac{(O_{ij} - E_{ij})^2}{E_{ij}} \sim \chi^2_{df}$$

**Degrees of Freedom ($df$):**
The [[Degrees of Freedom]] depend on the dimensions of the contingency table:
$$df = (r - 1)(c - 1)$$
*Where $r$ is the number of rows and $c$ is the number of columns.*

### Decision Rules & Rejection Regions
The Test for Independence is **always right-tailed**. A large $\chi^2$ statistic indicates a large discrepancy between the observed data and what we would expect if the variables were truly independent.

The rejection region is defined by the critical value $\chi^2_{\alpha}$.

**Rejection Rule (Reject $H_0$ if...)**
* $\chi^2 > \chi^2_{\alpha, df}$

**P-Value Calculation**
* $P(\chi^2 > \chi^2_{\text{calc}})$

where $\chi^2_{calc}$ is the calculated test statistic.

---

> [!example]- Example
> For a random sample of 240 students that are enrolled at a university it is recorded if they:
> 1. Are an undergraduate or graduate student
> 2. If they take classes in person, remote or hybrid
> 
> Below is a table of the observations:
> 
> | Student Level     | In Person | Remote | Hybrid | Row Totals |
> | ----------------- | --------- | ------ | ------ | ---------- |
> | Undergrad         | 80        | 40     | 60     | 180        |
> | Graduate          | 29        | 7      | 24     | 60         |
> | **Column Totals** | 109       | 47     | 84     | 240        |
> 
> At $\alpha=0.05$, is there evidence to suggest that these two variables are independent?
> 
> Hypotheses:
> * $H_0$: Student Level and Student Type are Independent
> * $H_1$: They are not independent
> 
> Calculating the expected counts under the null hypothesis where the two are independent $E_{ij}$ gives: 
> 
> | Student Level | In Person | Remote | Hybrid |
> | ------------- | --------- | ------ | ------ |
> | Undergrad     | 81.75     | 35.25  | 63     |
> | Graduate      | 27.25     | 11.75  | 21     |
> 
> Test Statistic:
> $$\chi^2 = \sum_{i=1}^k \frac{(O_i - E_i)^2}{E_i} = 3.282$$
> 
> Degrees of Freedom:
> * $df = (r - 1)(c - 1)=(1)(2)=2$
> 
> Using a Chi-Squared Distribution with 2 degrees of freedom $\chi^2_{2}$, this leads to a p-value of:
>  $$p = P(\chi^2>3.282) = 0.1937$$
>  $p > \alpha$ so the null hypothesis cannot be rejected. There is insufficient evidence to claim an association exists between Student Level and Class Type.
>  ![[independence_test_example.svg]]
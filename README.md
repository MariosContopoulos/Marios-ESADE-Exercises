# Exercise 7

## Overview

In this exercise, we will practice advanced data manipulation techniques using the Iris dataset. The dataset can be downloaded from:  
[https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)

---

## Exercises

### **Series Manipulation**
1. **Create a lambda function to classify flowers based on their petal length**:
    - Classify petal lengths as "short" if they are less than 3 cm, and "long" otherwise.
    - Apply this function to the `PetalLengthCm` column using the `apply` method.
   
2. **Map the `Species` column into numeric values**:
    - Map species names to numeric values:
      - *Iris-setosa*: 0
      - *Iris-versicolor*: 1
      - *Iris-virginica*: 2

### **DataFrame Manipulation**
1. **Use `value_counts` on the `Species` column**:
    - Count how many entries belong to each species.

2. **Remove duplicate rows**:
    - Use `drop_duplicates` to remove duplicates based on the `SepalLengthCm` and `PetalLengthCm` columns.

3. **Convert column types**:
    - Convert the `SepalLengthCm` column to a string type using `astype`.
    - Convert it back to a float type. If there are any conversion errors, handle them gracefully.

4. **Save the modified DataFrame to a CSV file**:
    - Use `to_csv` to save the modified DataFrame.
    - Ensure that the index is included in the saved file.

---

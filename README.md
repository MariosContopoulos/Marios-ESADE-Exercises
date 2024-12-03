They are seperated by group based on the slides provided in the lecture.

# Python-Assignments

# Session 1

# Syntax and variables
    Exercise 1: Print Basic Greeting
    Exercise 2: Basic Arithmetic
    Exercise 3: String Manipulation

# Lists and Dictionaries
    Exercise 4: Lists
    Exercise 5: Dictionaries

# Tuples and Sets
    Exercise 6: Tuples
    Exercise 7: Sets

# Control flow
    Exercise 8: Conditional Statements
    Exercise 9: For Loop
    Exercise 10: While Loop
    Exercise 11: Match Statement 
    
# Function
    Exercise 12: Define a Function
    Exercise 13: Function with Return Value
    Exercise 14: Function with Default Parameters

# Combining all we learned
    Exercise 15: List Comprehension
    Exercise 16: Nested Data Structures
    Exercise 17: Simple Calculator


# Session 2

# Python - Syntax and variables
    Exercise 1: FizzBuzz
    Exercise 2: Basic Data Filtering
    Exercise 3: Simple To-Do List
    Exercise 4: Temperature Converter


# Assignment 3: Course Registration System

### Object-Oriented Programming Project

## Overview

This project is a **Course Registration System** built using Object-Oriented Programming (OOP) in Python. The system includes classes to manage courses, students, and enrollment, as well as to calculate students' grades and GPA.

---

## Classes and Key Functions

### 1. `Course` Class

Represents a course with details and methods to manage students.

- **Attributes**:
  - `name`, `description`, `students` (list of enrolled students)
  
- **Methods**:
  - `add_student()`, `remove_student()`, `show_students()`

### 2. `Student` Class

Represents a student with personal info, enrolled courses, and grades.

- **Attributes**:
  - `name`, `student_id`, `address`, `courses` (enrolled courses), `grades` (course-grade mapping)
  
- **Methods**:
  - `enroll_in_course()`, `drop_course()`, `show_courses()`, `add_grade()`

### 3. `Registration` Class

Manages all students and courses, and handles enrollments.

- **Attributes**:
  - `students`, `courses` (lists of all students and courses)
  
- **Methods**:
  - `enroll_student_in_course()`, `drop_student_from_course()`, `add_course()`, `add_student()`, `show_all_courses()`, `show_all_students()`

### 4. `Grade` Class

Handles grade assignment and GPA calculation.

- **Attributes**:
  - `student`, `course`, `grade_value`
  
- **Methods**:
  - `add_grade()`, `calculate_gpa()`

---

## Workflow

1. **Set Up Courses and Students**: Create course and student profiles.
2. **Enroll and Drop Students**: Enroll students in courses and manage enrollments.
3. **Assign Grades**: Add grades to students in specific courses.
4. **Calculate GPA**: Generate a GPA for each student.



# Session 4: Annotation File Analysis

## Overview

This session involves analyzing a collection of satellite annotation files. Each file follows a specific naming convention and contains metadata in the filename. The goal is to gather insights about these files, including counts, date distributions, and satellite usage.

---

## Annotation File Naming Convention

Each file in the dataset is named according to the format:

{DATE}_{TIME}SN{SATELLITE_NUMBER}QUICKVIEW_VISUAL{VERSION}{UNIQUE_REGION}.txt

- **DATE**: `YYYYMMDD` format (e.g., 20241201, 20230321)
- **TIME**: `HHMMSS` format (e.g., 213430)
- **SATELLITE_NUMBER**: Integer representing the satellite number.
- **VERSION**: Pipeline version (e.g., "0_1_2", "1_3_1").
- **UNIQUE_REGION**: String describing the location (e.g., "SATL-2KM-10N_552_4164").

---

## Workflow

1. **Count Files**: Determine the total number of files in the annotations folder.
2. **Check Naming Convention**: Identify how many files follow the specified naming convention.
3. **Monthly and Yearly Distribution**: 
   - Count the number of annotations per month and year.
   - Identify the month with the highest number of annotations.
4. **Organize by Month**: Create a new folder structure within `annotations`, grouping files by month.
5. **Sort by Date**: Print all annotations from the most recent to the oldest.
6. **Satellite Usage**:
   - Count the number of unique satellites.
   - Determine how many annotations each satellite has.
   - Identify the satellite used in the most recent annotation.
7. **Unique Regions**: Count the number of unique regions in the dataset.

# Session 5: Annotations

# Annotation Data Processing

This project processes annotation data files and categorizes them based on their month and year. The annotations are then analyzed, sorted, and stored in different formats (JSON and Pickle) for easy access and further analysis. The script provides functionality to filter and display annotations that fall within the second half of 2024 (July–December).

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Data Formats](#data-formats)
- [Saving and Loading Data](#saving-and-loading-data)
- [Filter and Sort Annotations](#filter-and-sort-annotations)
- [Troubleshooting](#troubleshooting)

## Overview

This project is designed to handle annotation files in a structured way. The main objective is to:

- Count the number of annotations per month and identify the month with the highest number of annotations.
- Organize annotations into a dictionary where each key represents a month, and the value is a list of annotation dictionaries with their respective name and date.
- Store the data in **JSON** and **Pickle** formats for easy access and serialization.
- Filter and sort annotations that occurred during the second half of 2024 (July–December), displaying them in chronological order.

## Features

- **Monthly Annotation Count**: Count the number of annotation files for each month and year.
- **JSON and Pickle Export**: Save the annotations data in both JSON and Pickle formats.
- **Second Half 2024 Filter**: Filter annotations that fall between July and December 2024 and sort them in chronological order.
- **Debugging Information**: Print out the data for debugging and verification of the month-wise annotation categorization.

# Exercise 6

## **Pandas Exercises: A Hands-On Approach to Data Manipulation**

Datasets:
1. **Netflix Dataset**: Contains information about TV shows and movies available on Netflix.
2. **Titanic Dataset**: Contains data on Titanic passengers, including demographics and survival information.

---

## **Exercises**

### **Pandas I**
This section introduces common data wrangling tasks using the Netflix dataset.

1. **Count Missing Values in Each Column**  
   Identify columns with missing values and count how many are missing.

2. **Fill Missing 'country' Values with "Unknown"**  
   Replace missing values in the `country` column with "Unknown".

3. **Filter for TV Shows Only**  
   Extract and display rows where the content type is "TV Show".

4. **Count the Number of Entries per Rating**  
   Determine the number of titles associated with each `rating` value.

5. **Add a Column Showing Content Age**  
   Calculate how many years have passed since each title's release. Add a new column `ContentAge` with the calculated value.

---

### **Home Exercises for Netflix**

1. **Check for Missing Ratings**  
   Determine if there are any missing values in the `rating` column.

2. **Count Films from Your Country in 2021**  
   Filter the dataset to find the number of films released in 2021 corresponding to your country.

3. **Movies in 2020 with Full Information**  
   Count the number of movies from 2020 that have no missing values in any column.

4. **Year with the Most Titles**  
   Find the year with the highest number of titles in the dataset.

5. **Average Number of Releases from 2010**  
   Calculate the average number of titles released per year from 2010 onwards.

---

### **Titanic Exercises**

1. **Calculate Gender-Based Survival Percentage**  
   Compute the percentage of survivors for each gender.

2. **Survival Percentage by Gender and Class**  
   Group the data by gender and passenger class, then calculate survival percentages.

---

### **Additional Titanic Exercises**

1. **Count Missing Values in Each Column**  
   Identify and count missing values in each column.

2. **Fill Missing 'Age' Values with the Mean Age**  
   Replace missing values in the `Age` column with the column’s mean value.

3. **Fill Missing 'Embarked' Values with the Mode**  
   Replace missing values in the `Embarked` column with its mode (most common value).

4. **Filter Passengers Who Paid Above the Average Fare**  
   Extract rows where passengers paid a fare above the dataset’s average fare.

5. **Add a Family Size Column**  
   Create a new column `FamilySize`, which is the sum of the `SibSp` (siblings/spouses) and `Parch` (parents/children) columns.

---
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
# Exercise 8

# Plotting with Seaborn

This repository contains exercises related to data visualization using Seaborn. You will need to use Pandas to perform data manipulation and Seaborn for plotting. 

## Exercises

### 1. Create a *lineplot* showing how **Study Time** varies by **Student Name**. Which student has the highest study time?
- **Goal**: Use Seaborn's `lineplot` to visualize the variation in study time for each student.
- **Insight**: Identify the student with the highest study time.

### 2. Plot a histogram (*histplot*) of **Grade** and determine which grade range has the highest frequency of students.
- **Goal**: Create a histogram using Seaborn's `histplot` to understand the distribution of student grades.
- **Insight**: Find out which grade range has the highest frequency of students. You may need to check if there are multiple grade ranges with the same highest frequency.

### 3. Create an ECDF plot (*ecdfplot*) for **Grade**. What is the percentage of students scoring less than 85?
- **Goal**: Use Seaborn's `ecdfplot` to plot the empirical cumulative distribution function (ECDF) of grades.
- **Insight**: Calculate the percentage of students whose grade is below 85.

### 4. Create a *stripplot* showing **Grade** distribution for each **Course**. Which course has the most spread in grades?
- **Goal**: Use Seaborn's `stripplot` to show the distribution of grades for each course.
- **Insight**: Identify which course has the widest distribution of grades.

### 5. Create a *swarmplot* to show the relationship between Gender and **Study Time**. Which gender has a higher average study time?
- **Goal**: Use Seaborn's `swarmplot` to visualize the relationship between gender and study time.
- **Insight**: Compare the average study time between genders.

### 6. Plot a *pointplot* to show the average **Grade** for each Course. Which course has the highest average grade?
- **Goal**: Use Seaborn's `pointplot` to plot the average grade for each course.
- **Insight**: Determine which course has the highest average grade.

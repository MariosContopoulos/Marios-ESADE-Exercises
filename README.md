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

## Setup

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- `glob` (usually comes with Python)
- `re` (regular expression library, included in Python)
- `os` (used for file system manipulation)
- `datetime` (to handle date and time)
- `json` (for JSON handling)
- `pickle` (for Pickle serialization)

You can install any missing libraries using pip, if necessary.

### Directory Structure

Ensure that you have the following directory structure for your annotations data:



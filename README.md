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



# Session 4

# Python - Session 4
  
    Given a zip file with a subfolder with multiple annotations, where the name convention for each one of them is: 
    
    {DATE}_{TIME}_SN{SATELLITE_NUMBER}_QUICKVIEW_VISUAL_{VERSION}_{UNIQUE_REGION}.txt
    
    where:
    
    - DATE expressed as YYYYMMDD (year, month and day), e.g. 20241201, 20230321 ...
    - TIME expressed as HHMMSS (hour, minutes and seconds), e.g. 2134307
    - SATELLITE_NUMBER an integer that represents the satellite number.
    - VERSION provides the version of the pipeline, e.g. "0_1_2", "1_3_1" ...
    - UNIQUE_REGION provides a unique location in the form of a string, e.g SATL-2KM-10N_552_4164
    
    Find out the following thing about your data:
    
    1. How many files the annotations folder has.
    2. How many of them follow the name convention expressed above.
    3. How many of annotations you have per month and year. Which month has more annotation files.
    4. Create a new annotations folder with multiple folders corresponding to a month.
    5. Print all the annotations from the most recent to the oldest one. 
    6. How many different satellites there are, how many annotations we have per satellite number, and which one was used in the most recent annotation file. 
    7. How many unique regions there are.
    
    some tips:
    - str class has a method called split, you can use it to get each field per annotation.
    - you can use sort from numpy on strings.



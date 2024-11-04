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


# Session 3

# Python - Object Oriented Programming
    Exercise 1: Course Class
    Exercise 2: Student Class
    Exercise 3: Registration Class
    Exercise 4: GPA

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



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


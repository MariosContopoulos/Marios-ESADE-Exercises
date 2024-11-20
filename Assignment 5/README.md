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


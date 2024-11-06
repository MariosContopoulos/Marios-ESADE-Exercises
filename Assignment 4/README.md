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


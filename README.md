# SmallerDBScript

## Overview
`SmallerDBScript.py` is a Python script for migrating a subset of data from a large SQLite database to a smaller one. It's particularly useful for extracting and transferring specific records based on defined criteria.

## Features
- Connects to an existing large SQLite database.
- Creates a new smaller SQLite database or connects to an existing one.
- Defines a new table structure in the smaller database.
- Transfers a limited number of records (100 in this case) from the large database to the smaller one.

## Requirements
- Python 3.x
- sqlite3 module for Python

## Setup
1. Ensure Python 3.x is installed on your system.
2. The `sqlite3` module is a part of the Python standard library, so no additional installation is required.

## Usage
1. Place the `SmallerDBScript.py` in your desired directory.
2. Open your terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using Python:
   ```bash
   python SmallerDBScript.py

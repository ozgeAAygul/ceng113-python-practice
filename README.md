# CENG113 Python Practice Tasks

This repository contains practice tasks prepared for the  
**CENG113 – Introduction to Computer Programming** course.

The tasks are organized by chapters and difficulty levels to reinforce
fundamental Python concepts such as input/output, decision structures,
loops, functions, files, lists, strings, dictionaries, and sets.

---

## 🟢 LEVEL 1 — Basic Warm-Up (Chapter 1–2)

### Task 1: Student Info Program
- Takes student name, department, midterm and final grades
- Calculates average (`40% midterm + 60% final`)
- Prints student information and average

**Concepts:** input, type casting, print

---

### Task 2: Simple Calculator
- Takes two numbers and an operator (`+ - * /`)
- Performs the selected operation
- Checks division by zero

---

## 🟡 LEVEL 2 — Decision Structures (Chapter 3)

### Task 3: Letter Grade Calculator
- Calculates average grade
- Assigns letter grade based on score ranges:
  - 90–100 → A
  - 80–89 → B
  - 70–79 → C
  - 60–69 → D
  - else → F

---

### Task 4: Login Simulation
- Uses predefined username and password
- Compares user input with stored values
- Prints login result

---

## 🟠 LEVEL 3 — Loops (Chapter 4)

### Task 5: Number Analyzer
- Takes a positive number
- Counts how many even and odd numbers exist from 1 to that number

---

### Task 6: Guess the Number
- Program generates a random number between 1 and 50
- User tries to guess it
- Displays number of attempts

---

## 🔵 LEVEL 4 — Functions (Chapter 5)

### Task 7: Utility Functions
- Implements:
  - `is_even(n)`
  - `factorial(n)`
  - `average(numbers)`
- Tests functions in the main program

---

### Task 8: Menu-Based Program
- Displays a menu:
  1. Calculate factorial  
  2. Check even/odd  
  3. Exit  
- Calls appropriate functions based on user choice

---

## 🟣 LEVEL 5 — Files & Exceptions (Chapter 6)

### Task 9: Student Grades File
- Reads grades from `grades.txt`
- Calculates average grade
- Handles file errors using try-except

---

### Task 10: Log Writer
- Takes a message from the user
- Appends the message to `log.txt`
- Log file grows with each execution

---

## 🟤 LEVEL 6 — Lists & Tuples (Chapter 7)

### Task 11: Shopping List
- Creates a shopping list using a list
- Allows the user to:
  - Add items
  - Remove items
  - Display the list

---

### Task 12: Exam Statistics
- Uses a list of exam grades
- Finds:
  - Highest grade
  - Lowest grade
  - Average grade

---

## ⚫ LEVEL 7 — Strings (Chapter 8)

### Task 13: Password Validator
- Checks if a password:
  - Has at least 8 characters
  - Contains at least one digit
  - Contains at least one uppercase letter
- Displays clear validation messages

---

### Task 14: Word Counter
- Takes a sentence from the user
- Counts number of words
- Finds the longest word

---

## 🔴 LEVEL 8 — Dictionaries & Sets (Chapter 9)

### Task 15: Phone Book
- Uses a dictionary to store names and phone numbers
- Allows:
  - Adding contacts
  - Removing contacts
  - Searching contacts

---

### Task 16: Unique Words
- Takes a sentence from the user
- Removes repeated words
- Displays unique words using a set

---

## 🧠 Purpose
The purpose of this repository is to practice Python programming
step by step and reinforce core programming concepts taught in CENG113.

Each task is written clearly and uses functions where appropriate
to improve readability and reusability.

---

## ▶ How to Run
Navigate to the desired task folder and run:

```bash
python task_name.py


# BMI Calculator 🧮

A simple Python-based **Body Mass Index (BMI) Calculator** that calculates a user's BMI based on their height and weight. It also determines the corresponding BMI category and validates user input to prevent errors.

---

## 📌 About the Project

This project is a beginner-friendly Python application designed to practice fundamental programming concepts, including:

- Variables and data types
- User input using `input()`
- Type conversion using `float()`
- Conditional statements (`if`, `elif`, `else`)
- Looping using `while True`
- Input validation
- Exception handling using `try` and `except`
- `break` and `continue` statements
- Formatted output using f-strings

The program ensures that users enter valid numerical values before calculating their BMI. If an invalid input is detected, the program automatically restarts and asks the user to enter their information again.

---

## ✨ Features

- **BMI Calculation** – Calculates Body Mass Index using the user's height and weight.
- **BMI Classification** – Identifies whether the user is Underweight, Normal, Overweight, or Obese.
- **Input Validation** – Prevents zero and negative height or weight values.
- **Error Handling** – Handles non-numeric inputs using `try-except`.
- **Automatic Restart** – Repeats the program when invalid information is entered.
- **Formatted Results** – Displays BMI results rounded to one decimal place.

---

## 📐 BMI Formula

The program uses the standard BMI formula:

\[
BMI = \frac{Weight\ (kg)}{Height\ (m)^2}
\]

Where:
- **Weight** is measured in kilograms (kg).
- **Height** is measured in meters (m).

---

## 📊 BMI Categories

The program classifies BMI results using the following ranges:

| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal |
| 25.0 – 29.9 | Overweight |
| 30.0 and above | Obese |

---

## 🛠️ Technologies Used

- **Programming Language:** Python
- **IDE:** Any Python-supported IDE (e.g., PyCharm, VS Code)
- **Version Control:** Git and GitHub

---

## 🚀 How to Run the Program

### Prerequisites

Make sure you have Python installed on your computer.

You can download it here:

[Download Python](https://www.python.org/downloads/)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/NyelPagalan/BMI-Calculator.git
```

**2. Navigate to the project folder**

```bash
cd BMI-Calculator
```

**3. Run the Python file**

```bash
python bmi_calculator.py
```

---

## 💻 Sample Output

```text
===================================
  Welcome to the BMI Calculator
===================================
Enter your height in meters (e.g., 1.54): 1.54
Enter your weight in kilograms (e.g., 45): 45

Your BMI is 19.0
Your category is Normal
```

### Example: Invalid Input

```text
===================================
  Welcome to the BMI Calculator
===================================
Enter your height in meters (e.g., 1.54): -1.54
Enter your weight in kilograms (e.g., 45): 45

Please enter a valid number

===================================
  Welcome to the BMI Calculator
===================================
```

The program automatically restarts when an invalid value is entered.

---

## 📂 Project Structure

```text
BMI-Calculator/
│
├── bmi_calculator.py
└── README.md
```

---

## 🎯 Learning Objectives

Through this project, I practiced implementing Python programming concepts in a simple real-world application. It helped me understand how loops, conditional statements, input validation, and exception handling work together to create a more reliable program.

---


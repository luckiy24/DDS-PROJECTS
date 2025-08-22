# 🧮 Expression Calculator

---
## 📌 Overview
**The Expression Calculator** is a project that evaluates mathematical expressions entered by the user. It supports operators like addition, subtraction, multiplication, division, and parentheses. The system uses stack-based evaluation to handle operator precedence and associativity, making it a practical example of applying Data Structures to real-world problems.

---

## 🛠 Features
- Accepts arithmetic expressions from the user
- Supports operators: +, -, *, /, and parentheses ()
- Converts infix expressions to postfix form (using stack)
- Evaluates postfix expressions efficiently
- Detects invalid expressions (like unmatched parentheses)
- Easy to extend for more operators and functions

- --
## 📂 Data Structures Used
- Stack → To handle operators, operands, and parentheses during infix-to-postfix conversion and postfix evaluation
- Array / List → To store expression tokens
- String Handling → To parse user input expression

- ---
## 🚀 How to Run
```bach
# Clone the repository
git clone https://github.com/your-username/expression-calculator.git
cd expression-calculator/src

# Run the program
python calculator.py

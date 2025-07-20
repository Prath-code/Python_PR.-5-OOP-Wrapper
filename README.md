# OOP Wrapper: Employee Management System

## Overview
This project is an Employee Management System built using Object-Oriented Programming (OOP) principles in Python. It demonstrates the use of classes, inheritance, encapsulation, method overloading, method overriding, dunder methods, and operator overloading. The system allows for the creation and management of employees, managers, and developers, as well as comparison of their salaries and displaying their details.

## Features
- **Employee Class (Base):**
  - Attributes: name, age, employee ID, salary
  - Getter and setter methods for salary
  - Encapsulation of sensitive data
  - Custom string representation
- **Manager Class (Derived):**
  - Inherits from Employee
  - Additional attribute: department
  - Overridden details display
- **Developer Class (Derived):**
  - Inherits from Employee
  - Additional attribute: programming language
  - Overridden details display
- **Method Overloading:**
  - Multiple ways to create employee objects
- **Encapsulation:**
  - Private attributes with getter/setter methods
- **Inheritance & Method Overriding:**
  - Specialized classes for Manager and Developer
- **Use of `super()` and `issubclass()`:**
  - Call parent methods and check class relationships
- **Dunder Methods:**
  - Custom `__str__` for string representation
  - Overloaded comparison operators for salary
- **Operator Overloading:**
  - Compare employees by salary
- **Menu-Driven Console UI:**
  - Create and manage employees, managers, and developers
  - Show details and compare salaries
  - Exit and free resources

## Requirements
- Python 3.x

## How to Run
1. Clone or download this repository.
2. Run the main script:
   ```bash
   python project-5.py
   ```
3. Follow the on-screen menu to interact with the system.

## Example Console Interaction
```
--- Python OOP Project: Employee Management System ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Compare Salaries
0. Exit

Enter your choice: 2
Enter Name: Jane Smith
Enter Age: 28
Enter Employee ID: E123
Enter Salary: 50000
Employee created with name: Jane Smith, age: 28, ID: E123, salary: $50000.00

--- Choose another operation ---

Enter your choice: 3
Enter Name: Alice Johnson
Enter Age: 40
Enter Employee ID: M456
Enter Salary: 80000
Enter Department: Sales
Manager created with name: Alice Johnson, age: 40, ID: M456, salary: $80000.00, department: Sales.

--- Choose another operation ---

Enter your choice: 5
1. Name: Jane Smith, Age: 28, ID: E123, Salary: $50000.00
2. Name: Alice Johnson, Age: 40, ID: M456, Salary: $80000.00, Department: Sales

--- Choose another operation ---

Enter your choice: 6
Enter the first employee's index (1-based, e.g., 1): 1
Enter the second employee's index (1-based, e.g., 2): 2
Comparing salaries:
Jane Smith (E123) has a lower salary than Alice Johnson (M456)

--- Choose another operation ---

Enter your choice: 0
Exiting the system. All resources have been freed.
```

## Notes
- Ensure you have Python 3 installed.
- All data is stored in memory for the session; exiting the program will clear all data.
- The code demonstrates OOP concepts for educational purposes.

## License
This project is for educational use only.

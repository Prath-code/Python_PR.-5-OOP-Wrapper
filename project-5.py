class Employee:
    def __init__(self, name, age, emp_id, salary):
        self._name = name
        self._age = age
        self._emp_id = emp_id
        self._salary = salary

    def get_details(self):
        return f"Name: {self._name}, Age: {self._age}, ID: {self._emp_id}, Salary: ${self._salary:.2f}"

    def set_salary(self, salary):
        self._salary = salary

class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self._department = department

    def get_details(self):
        return f"{super().get_details()}, Department: {self._department}"

class Developer(Employee):
    def __init__(self, name, age, emp_id, salary, programming_language):
        super().__init__(name, age, emp_id, salary)
        self._programming_language = programming_language

    def get_details(self):
        return f"{super().get_details()}, Language: {self._programming_language}"

def compare_salaries(emp1, emp2):
    if emp1._salary < emp2._salary:
        return f"{emp1._name} ({emp1._emp_id}) has a lower salary than {emp2._name} ({emp2._emp_id})"
    elif emp1._salary > emp2._salary:
        return f"{emp2._name} ({emp2._emp_id}) has a lower salary than {emp1._name} ({emp1._emp_id})"
    else:
        return f"{emp1._name} ({emp1._emp_id}) and {emp2._name} ({emp2._emp_id}) have the same salary"

def main():
    employees = []
    while True:
        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Create a Developer")
        print("5. Show Details")
        print("6. Compare Salaries")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            employees.append({"type": "Person", "name": name, "age": age})
            print(f"Person created with name: {name} and age: {age}")
        
        elif choice == '2':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            employees.append(Employee(name, age, emp_id, salary))
            print(f"Employee created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary:.2f}")
        
        elif choice == '3':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            employees.append(Manager(name, age, emp_id, salary, dept))
            print(f"Manager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary:.2f}, department: {dept}")
        
        elif choice == '4':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            lang = input("Enter Programming Language: ")
            employees.append(Developer(name, age, emp_id, salary, lang))
            print(f"Developer created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary:.2f}, language: {lang}")
        
        elif choice == '5':
            if not employees:
                print("No employees to show!")
            else:
                for i, emp in enumerate(employees):
                    if hasattr(emp, 'get_details'):
                        print(f"{i+1}. {emp.get_details()}")
                    else:
                        print(f"{i+1}. Person - Name: {emp['name']}, Age: {emp['age']}")
        
        elif choice == '6':
            if len(employees) < 2:
                print("Need at least two employees to compare!")
            else:
                print("Enter the first employee's index (1-based, e.g., 1): ")
                idx1 = int(input()) - 1
                print("Enter the second employee's index (1-based, e.g., 2): ")
                idx2 = int(input()) - 1
                if hasattr(employees[idx1], 'get_details') and hasattr(employees[idx2], 'get_details'):
                    print("Comparing salaries:")
                    print(compare_salaries(employees[idx1], employees[idx2]))
                else:
                    print("Both must be employees with salaries to compare!")
        
        elif choice == '0':
            print("Exiting the system. All resources have been freed.")
            break

if __name__ == "__main__":
    main()
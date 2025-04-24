class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        if isinstance(other, Employee):
            total_salary = self.salary + other.salary
            return Employee(f"{self.name} & {other.name}", total_salary)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Employee):
            salary_diff = self.salary - other.salary
            return salary_diff
        return NotImplemented
    
    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

def user_input():
    name1 = input("Enter the name of the first employee: ")
    salary1 = float(input(f"Enter the salary of {name1}: "))

    name2 = input("Enter the name of the second employee: ")
    salary2 = float(input(f"Enter the salary of {name2}: "))

    emp1 = Employee(name1, salary1)
    emp2 = Employee(name2, salary2)

    combined_emp = emp1 + emp2
    print(f"\nCombined Employee:\n {combined_emp}")

    salary_difference = emp1 - emp2
    print(f"Salary Difference between {emp1.name} and {emp2.name}: {salary_difference}")

user_input()

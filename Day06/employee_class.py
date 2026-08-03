from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def show_info(self):
        print(f"name:{self.name}\nemployee_id:{self.employee_id}")

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        #super().calculate_salary()
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours, hourly_rate):
        super().__init__(name,employee_id)
        self.hours = hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        #super().calculate_salary()
        return self.hours * self.hourly_rate

employees = [
    FullTimeEmployee("Tom", "001", 5000),
    PartTimeEmployee("Jerry", "002", 80, 25)
]

for employee in employees:
    employee.show_info()
    print(employee.calculate_salary())
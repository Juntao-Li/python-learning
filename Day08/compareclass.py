class Employee:
    def __init__(self, eid, name, salary):
        self.eid = eid
        self.name = name
        self.salary = salary

    def __eq__(self, other):
        return self.eid == other.eid

    def __lt__(self, other):
        return self.salary < other.salary 

a = Employee("001", "Tom", 10000)
b = Employee("001", "Jerry", 30000)
c = Employee("002", "Jack", 8000)
d = Employee("003", "Rose", 15000)

print(a == b)

employees = [a, c, d]

employees.sort()

for employee in employees:
    print(employee.name)


    





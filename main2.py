class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
    def get_info(self):
        return f"Name: {self.name}, Department: {self.department}, Salary: ₹{self.salary}"
    def __str__(self):
        return f"Employee({self.name}, {self.department}, ₹{self.salary})"
emp = Employee("Fidha", "IT", 500000)
print(emp.get_info())
print(emp)

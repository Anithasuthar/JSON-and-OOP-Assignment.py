import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state
    
    def __str__(self):
        return f"{self.name} ({self.dob}) from {self.city}, {self.state}. Height: {self.height} cm"

with open("employee.json", "r") as f:
    employee_data = json.load(f)

employees = []
for data in employee_data:
    employee = Employee(data["Name"], data["DOB"], data["Height"], data["City"], data["State"])
    employees.append(employee)

for employee in employees:
    print(employee)

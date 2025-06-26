#Employee-Management-System
class Employee:
    def __init__(self,company,name,age,id,salary):
        self.company=company
        self.name=name
        self.id=id
        self.age=age
        self.salary=salary
    def get_salary(self):
        return self.salary
    def display(self):
        return self.age
    def found(self):
        '''c=int(Input("Enter employ id:"))'''
        if c==self.id:
            return "Employye is found in our company"
        else:
            return "Employee is not found in our company"
c=int(input("Enter employ id:"))
emp=Employee("IT","shasi",45,676,54000)

print("Company_Name",emp.company)
if emp.id ==c:
    print(emp.get_salary())
    print(emp.display())
    print(emp.found())        
else:
    print("Employee not found in our company")

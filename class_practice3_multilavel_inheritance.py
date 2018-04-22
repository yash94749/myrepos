class company:

    def __init__(self,Name,location,types):
        self.CompanyName = Name
        self.CompanyLocation = location
        self.CompanyDomain = types
        self.CompanyWebsite = 'www' + '.' +  Name +  '.com'
class Employee(company):
    amount = 1.04
    def __init__(self,Name,location,types,emp_first_Name,emp_last_Name,emp_salary):
        company.__init__(self,Name,location,types)
        self.Emp_FirstName = emp_first_Name
        self.Emp_LastName = emp_last_Name
        self.Emp_pay = emp_salary
        self.emp_email =self.Emp_FirstName + '.' +  self.Emp_LastName + '@' + self.CompanyName + '.com'
    def emp_raise_salary(self):
        return (self.Emp_pay * self.amount)
class emp_company_details(Employee):
    def __init__(self,Name,location,types,emp_first_Name,emp_last_Name,emp_salary):
        
       Employee.__init__(self,Name,location,types,emp_first_Name,emp_last_Name,emp_salary)
    
    def employee_company_details(self):
        return(self.Emp_FirstName + ' ' + self.Emp_LastName + ' ' + 'belongs to' + ' ' + self.CompanyName + ' ' + 'slotions')
        

emp1=emp_company_details('amazon','pune','IT','Yashwant','Singh',60000)
emp2=company('Netmagic','Mumbai','Datacenter')
emp3=Employee('Netmagic','Mumbai','Datacenter','Reema','Singh',70000)
print (emp1.CompanyWebsite)
print (emp1.Emp_pay)
print (emp1.employee_company_details())
print (emp_company_details.__mro__)
print(issubclass(emp_company_details,Employee))
print(issubclass(emp_company_details,company))
print(issubclass(Employee,company))
print(issubclass(Employee,emp_company_details))
print(issubclass(company,emp_company_details))
print(isinstance(emp1,emp_company_details))
print(isinstance(emp3,Employee))
print(isinstance(emp2,company))
print(isinstance(emp2,emp_company_details))
print(isinstance(emp1,Employee))
print(isinstance(emp3,company))
print(isinstance(emp1,company))


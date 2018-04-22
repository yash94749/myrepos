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
        
##cmp1 = company.emp_details('amazon','pune',60000)
###print(cmp1.emp_details('Yashwant','Singh',60000).emp_email)
##print (cmp1.emp_email)
emp1=Employee('amazon','pune','IT','Yashwant','Singh',60000)
print (emp1.CompanyWebsite)
print (emp1.Emp_pay)
print (emp1.emp_raise_salary())
emp1.amount = 10
print (emp1.emp_raise_salary())

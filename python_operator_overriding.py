class Employee:
    def __init__(self,name,lname,pay):
        self.Fname = name
        self.lname = lname
        self.pay = pay

    def variable_pay(self,varpay):
        self.varpay = varpay
        return(self.pay + self.varpay)
class Developer(Employee):
    def __init__(self,name,lname,pay,prog_lang):
        self.prog_lang = prog_lang
        super().__init__(name,lname,pay)
    def variable_pay(self,varpay):
        self.varpay = varpay
        return(self.pay + self.varpay + 1000)
    

emp1 = Employee('yash','singh',60000)
emp2 = Developer('Rima','singh',60000,'python')
#emp1.varpay=14000
print(emp1.variable_pay(14000))
print(emp2.variable_pay(18000))


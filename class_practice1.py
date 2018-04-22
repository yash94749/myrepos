class company:
    def __init__(self, name, location, service):
        self.Name = name
        self.Location = location
        self.Service = service
        self.email = name + '@comapany.com'
    def fulldetails(self):
        return self.Name + ' ' + self.Location + ' ' + self.Service
cmp1 = company('infosys', 'pune', 'support')
cmp2 = company('Netmagic', 'mumbai', 'datacenter')
##print (cmp1.Name)
##print (cmp1.Location)
##print (cmp1.Service)
##print (cmp1.email)
##print (cmp2.Name)
##print (cmp2.Location)
##print (cmp2.Service)
##print (cmp2.email)
print (cmp1.fulldetails())
print (cmp2.fulldetails())

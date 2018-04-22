class point:
    def __init__(self,x,y,z):
        self.first_point = x
        self.second_point = y
        self.last_point = z

    def display(self):
        return(self.first_point,self.second_point,self.last_point)
    def __add__(self,other):
        self.first_point = self.first_point + other.first_point
        self.second_point = self.second_point + other.second_point
        self.last_point = self.last_point + other.last_point
        return(self.first_point,self.second_point,self.last_point)
    def __lt__(self,other):
        return (self.first_point > other.second_point)
p1 = point(1,1,1)
p2 = point(2,3,4)
print (p1.display())
print (p2.display())
print(p1 + p2)
print(p1<p2)
        

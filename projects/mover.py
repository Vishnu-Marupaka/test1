#Method overloading
from multipledispatch import dispatch
class example:
    @dispatch(int, int)
    def add(self, a, b):
        x = a+b
        return x
    @dispatch(int, int, int)
    def add(self, a, b, c):
        x = a+b+c
        return x
ex=example()  
print(ex.add(10,20))
print(ex.add(10,20,30))  
#Operator overloading
class example:
    def __init__(self,X):
        self.X=X
    def __add__(self,U):
        return self.X+U.X
o1=example(5)
o2=example(8)
o3=o1+o2
print(o3)        

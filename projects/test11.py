#calculator using class
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b 
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
while True:
    a=int(input("Enter 1st no:")) 
    b=int(input("Enter 1st no:"))         
    x=input("Choose the operation that yu want to perform:")
    cal=calculator(a,b)
    if x=="+":
      print(cal.add())
    elif x=="-":
        print(cal.sub())
    elif x=="*":
        print(cal.mul())
    elif x=="/":
        print(cal.div())     
    else:
        break         

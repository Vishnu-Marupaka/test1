#Stacks using lists
a=[]
for i in range(5):
    b=input("Enter the values of list:")
    a.append(b)
print(a)
c=input("Enter the value that you want to append:")
d=input("enter that yu wnat to perform append or delete or peak:")
if d =="1":
    a.append(c)
    print(a)
elif d=="2":
    a.pop()
    print(a)
    
elif d=="3":
    print("peak",a[len(a)-1])
else:
    print("error in op")

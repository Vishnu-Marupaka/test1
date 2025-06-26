#tuple to check user is present in datbase or not
a=(1,2,3,4,5)
b=("abhi","ajay","karthi","surya","dany")        


user=input("Enter the username:")

if user not in b:
    print("user not found")
else:
    l=b.index(user)
    p=b[l]
    if p== user:
        print("User found")
    else:
        print("user not found")    

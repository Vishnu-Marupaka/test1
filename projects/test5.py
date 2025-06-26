#Dictionary
d={"ashwa":14253927,"arjun":42431352,"bhima":53631211,"dharma":62626941,"krishan":8171731}
e=input("enter the name in yur contacts:")

g=d.keys()
if e in g:

    print("Value found in contact",d.get(e))
   
else:
    print("contact not found")    
#dictionary
a={"brand":"BMW","colour":"red","price":5000000} 
print(a) 
print(type(a)) 
print(a.get("brand")) 
print(a.keys()) 
print(a.values()) 
print(a.update({"model":"SF5"})) 
a["colour"]="blue" 
print(a) 
print(a.pop("colour")) 
print(len(a)) 
print(a["price"]) 
a.clear() 
print(a) 
b=a.copy() 
print(b)

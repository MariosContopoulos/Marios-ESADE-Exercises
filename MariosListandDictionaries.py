#4
#Create list
universities=['UCL','IE','ESADE','LSE','IMPERIAL'] #list

#Print the entire list
print(universities)

#Print first and last entries
print(universities[0])
print(universities[-1])

---
#5
#Create dictionaries
random={'name':"Marios",'age':5,'grade':"A***"}

#Print all key-value pairs
for key, value in random.items():
  print(f"{key}:{value}")

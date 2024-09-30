#15
#Define a list

list=[i for i in range(1,11)]

#Square the list unsing list comprehension
square_list=[i**2 for i in range(1,11)]
print(square_list)

---
#16
#Create a dictionary
dict={'Marios':[11,23,45,4],'Anna':[3,53,14,66],'Jeremy':[23,43,45,65],'Suzie':[45,54,34,23]}

#Function that gives the average grade of student
def Average(dict):
    for name, grades in dict.items():
        average=sum(grades)/len(grades)
        print(f"{name}: Average Grade = {average:.2f}")
    else:
        print(" That is all the average grades we have for now.")

Average(dict)

---
#17
#Define function
from typing import Union

def calculate(a: float,b: float,c: str)->Union[float, int, str]:
    """
    a: The first number -float
    b: The second number -float
    c: The operator (+,-,*,/) -str

    Returns:
    A number (float,int) or an error message (str)
    """
    if type(a)=str:
        print("First argument needs to be a number.")
    if type(b)=str:
        print("Second argument needs to be a number.")
    if c=='+':
        return a+b
    elif c=='-':
        return a-b
    elif c=='/':
        if b==0:
            #We cannot divide by 0
            print('Second argument must not be zero')
        else:
            return a/b
    elif c=='*':
        return a*b
    else print('Operator is invalid, try again with (+,-,*,./).')

#Ask user for input
a = float(input("Enter the first number: ")) #We need to make sure the first argument is a number
b = float(input("Enter the second number: ")) #We need to make sure the second argument is a number
c = input("Enter the operator (+, -, *, /): ") #We will check in the funciton whether this operator is valid or not

#Call the calculate function
result = calculate(a,b,c)

#Print the result
print(f"The result is:{result}")





    





#12
#Define a function that prints Hello, {name}!

def greet(name):
    print(f"Hello, {name}!")

greet("Marios") #Calling the function by my own name

---
#13
#Define a function that returns the square number

def square(number):
    return number**2 #Return the square of the number

print(square(5)) #Returns 25
print(square(-3)) #Returns 9

---
#14
#Define a function that multiplies two variables

def multiply(a,b=1):
    return a*b

print(multiply(5)) #Returns 5, so it uses the default value for the second argument
print(multiply(5,5)) #Returns 25, so second argument overridesthe default value

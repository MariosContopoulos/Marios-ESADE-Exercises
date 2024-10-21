def fizzbuzz(n):
    """
    The function returns:
    "FizzBuzz" if n is a multiple of 3 and 5
    "Buzz" if n is a multiple of 5
    "Fizz" if n is a multiple of 3
    n if otherwise
    """
    if (n%3==0 and n%5==0):
        return "FizzBuzz" #If n is multiple of 3 and 5
    elif n%5==0:
        return "Buzz" #If n is multiple of 5
    elif n%3==0:
        return "Fizz" #If n is multiple of 3
    else:
        return n

for i in range(1,20):
    check=fizzbuzz(i)
    print(check)

#1
#2
#Fizz
#4
#Buzz
#Fizz
#7
#8
#Fizz
#Buzz
#11
#Fizz
#13
#14
#FizzBuzz
#16
#17
#Fizz
#19
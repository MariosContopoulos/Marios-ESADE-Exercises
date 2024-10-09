def fizzbuzz(n):
    """
    The function returns
    FizzBuzz if n is a multiple of 3 and 5
    Buzz if n is a multiple of 5
    Fizz if n is a multiple of 3
    n if none of the above
    """
    if (n%3==0 and n%5==0):
        return "FizzBuzz"
    elif n%5==0:
        return "Buzz"
    elif n%3==0:
        return "Fizz"
    else:
        return n

for i in range(1,20):
    check=fizzbuzz(i)
    print(f"The number {i} is {check}")

#Creating a list with integers, floats and strings
mix=[3,3.4,"wow"]
#Using the comprehension list method to generate a new list with only the integers from the previous list
integer_list=[i for i in mix if isinstance(i, int)]
#Print the new list of integers
print(integer_list)

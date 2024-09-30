#8
#Check if the input is positive,zero or negative and display that to the user
number=int(input("Give a number:")) #The function "input" returns a string, so we have to use "int" to turn that to an integer

if number>0:
    print("This is positive.")

elif number=0:
    print("This is zero.")

else:
    print("This is negative.")

---
#9
#Create a list of number from 1-5.
Marios=[1,2,3,4,5]

for number in Marios:
    print(number) #By iteration print all numbers from the lis

else:
    print("All numbers have been printed")

---
#10
#Create a list
Marios=1

while Marios<=5:
    print(Marios)
    Marios+=1 #Add 1 to Marios for every iteration of the loop

else:
    print("Loop finished.")

---
#11
#Prompt the user for a grade
Grade=input("Write a grade:")

match Grade:
  case "A":
    print("Excellent!")

  case "B":
    print("Good Job!")

  case "C":
    print("Fair.")

  case "D":
    print("Needs Improvement.")

  case "F":
    print("Failing.")

  case _:
    print("Unkown command.") #For any input other than A,B,C,D,F

---
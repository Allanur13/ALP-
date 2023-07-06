def add(num1, num2):
  print(str(num1) + " added by " + str(num2) + " is equal to " + str(num1+num2))
def subtract(num1, num2):
  print(str(num1) + " subtracted by " + str(num2) + " is equal to " + str(num1-num2))
def multiply(num1, num2):
  print(str(num1) + " multiplied by " + str(num2) + " is equal to " + str(num1*num2))
def divide(num1, num2):
  print(str(num1) + " divided by " + str(num2) + " is equal to " + str(num1/num2))

num1 = int(input("please enter number1: "))
num2 = int(input("please enter number2: "))

choice = int(input("enter 1 to add, 2 to subtract, 3 to multiply and 4 for divide: "))

if choice == 1:
 add(num1, num2) 
elif choice == 2:
 subtract(num1, num2) 
elif choice == 3:
 multiply(num1, num2) 
elif choice == 4:
 divide(num1, num2) 
else:
  print("enter a valid number!!")
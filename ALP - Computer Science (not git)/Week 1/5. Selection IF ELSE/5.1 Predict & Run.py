'''
Task - Predict and Run
This task contains three code examples.

Look at each example , study it carefully. Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms selection, condition and branch in your prediction.
'''

# Example code 1

age = 18 
 
if age > 18: 
 print("You are old enough to drive") 
#it won't print anything, because 18 is not bigger than 18
#we can use >=, then it will print 18

# Example code 2

num1 = 1337 
 
if num1 == 10: 
  print("This text is output because the condition was true") 
else:
  print("This text is output because the condition was false") 
#This text is output because the condition was false
#num1 is not equal to 10. "==" checks if the given two numbers are equal

# Example code 3

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))
#it gets any number as an input from the user and converts it to the integer
if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")
#if the entered number from the user is equal to 5, it prints Correct, if the guessed number is smaller than number, it prints too low!. If the number is bigger than the numbet it prints too high
#for ex: 5
#Output: Correct!
#3 output: Too Low!
#8 output: Too high!
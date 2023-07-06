# Example code 1

number = 7
# variable number assigned
print("I have thought of a number between 1 and 10")
# displays the prompt
guess = int(input("Can you guess what it is?"))
# variable guess is assigned from the input of the user

if guess == number:
# condition: checks if the user input, which is a guess variable is equal to the number 
  print("Correct!")
  # if the above if statement is true, it prints "Correct!"
elif guess < number:
# if the above if statement was false, it check this condition: if the guessed variable is smaller than the number
# if the above if statement was true, it doesn't go through elif
  print("Too Low!")
  # if the elif statement satisfied, it execudes, "Too Low!"
else:
# if both above conditions were false, then it execudes whatever inside else
  print("Too High!")
  # displays the prompt "Too high!"

# Example code 2

number1 = int(input("Please enter a number"))
# variable number1 assigned from user input, in the form of integer
number2 = int(input("Please enter another number"))
# variable number2 assigned from user input, in the from of integer

if number1 > number2:
# condition: checks if the number1 variable is bigger than the number2 variable
  print("Number 1 is bigger than number 2")
  # if the condition was correct, it displays the prompt
elif number2 > number1: 
# if the above if condition wasn't satisfied, it checks second if
  print("Number 2 is bigger than number 1")
  # if elif condition is true, it execudes the prompt
else:
# if the both ifs conditions were false, then it runs through else
  print("Both numbers are the same")
  # displays the prompt


# Starter Code

number = 5
# assigns variable named number to an integer with value 5
print("I have thought of a number between 1 and 10")
# displays the prompt
guess = int(input("Can you guess what it is?"))
# assigns another variable named guess to an input from the user converted into an integer with a prompt


if guess < number:
# checks if the guessed number smaller than the variable number, which is 5
# if the condition is true, it displays too low prompt
  print("Too Low!")
if guess > number:
# checks if the guessed number  bigger than 5
# if it is bigger, it displays too high prompt
  print("Too High!")


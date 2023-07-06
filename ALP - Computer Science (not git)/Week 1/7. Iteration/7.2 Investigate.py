number = 7
print("I'm thinking of a number, can you guess it?")
guess = int(input())
while guess != number:
  print("Wrong! Guess again!")
  guess = int(input())
print("You guessed it!")

# Give the line number where iteration starts.
  # Answer: 4

# What does '!=' mean?
  # Answer: is not equal to

# How many variables are there in the code?
  # Answer: 2

# How can you tell which lines of code are inside the loop?
  # Answer: looking at the indentation

# How many times will the loop repeat?
  # Answer: until your input is equal to 7

# What has to happen to make the program run the last line of code?
  # Answer: guess variable must be equal to number variable, or the condition inside while is false

# Task 3

secret = 13
print("Guess the secret number: ")
guess = int(input())
while secret != guess:
  print("Wrong! Guess again!")
  guess = int(input())
print("You guessed it!")
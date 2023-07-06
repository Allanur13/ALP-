'''
Task - Investigate
Use comments to answer the investigate questions on the example code.

'''
# Example Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")

# What happens if you input the guess '2'?
  # Answer: Too Low! (2 is smaller than 5)

# What happens if you input the guess '6'?
  # Answer: Too High! (6 is bigger than 5)

# What happens if you input the guess '5'?
  # Answer: Correct! (5 is equal to 5)

# What happens if you input the guess '-5'?
  # Answer: Too Low!

# What happens if you input the guess '0'?
  # Answer: Too Low!

# What do the symbols '<' and '>' mean on lines 9 and 11?
  # Answer: it checks if the input guessed number is bigger or smaller than the given number, which is assigned to 5

# What happens if you change line 5 to if guess = number: ?
  # Answer: it will give an error. "=" is used in the assignment of numbers, but here we want to check the conditions

# What do you notice about each line that FOLLOWS each IF statement?
  # Answer: At the end you have to put the comma and the new line starts with the indentation



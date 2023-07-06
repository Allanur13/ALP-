# Example code 1

# Add comments to each line to say whehter it is inside or outside the loop and what it does.

# Explain the circumstances in which the loop will run.

print("What is the capital of France?")
#outside the loop
#display the prompt
answer = input() 
#outside the loop
#variable assigned from user

while answer != "Paris":
#where loop starts, starting point
#checks if the variable from user is not equal to "Paris"
  print("Incorrect! Try again.")
  #inside the loop
  #if the condition inside while is met, then it displays this prompt
  answer = input("What is the capital of France?")
  #inside the loop
  #variable answer is assigned to a new value from the input inside the loop

print("Correct!")
#outside the loop
#when the user got correct answer, it display this.

# Example code 2

counter = 1
# variable assigned
# outside loop

while counter < 5:
# starting point of loop
# checks if the variable counter is smaller than 5
  print("This code is inside the loop")
  # if the condition is true inside while, it prints the prompt
  # inside loop
  counter += 1
  # counter = counter + 1
  # inside loop
#output: 
#1
#2
#3
#4

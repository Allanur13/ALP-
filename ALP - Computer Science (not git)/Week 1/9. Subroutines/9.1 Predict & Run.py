# Example Code 1

def say_hi():
# subroutine is defined
  print("Why hello there!")
  # when subroutine is called it displays the prompt

def offer_drink():
# subroutine is defined
  print("Would you care for a spot of tea?")
  # displays the prompt

def offer_food():
# subroutine is defined
  print("Biscuit?")
  # displays the prompt

def say_bye():
# subroutine is defined  
  print("Cheerio then.")
  # displays the prompt


offer_drink()
#subroutine offer_drink is called
say_hi()
#subroutine say_hi is called
offer_food()
#subroutine offer_food is called

# Example code 2
def maths1():
# subroutine maths1 is defined
  num1 = 50
  #variable assigned
  num2 = 5
  #variable assigned
  return num1 + num2
  # returns the value of num1 + num2 when the subroutine is callled

def maths2():
# subroutine maths2 is defined
  num1 = 50
  # variable assigned
  num2 = 5
  # variable assigned
  return num1 - num2
  # returns the subtraction of two values when the function is called

def maths3():
# subroutine maths3 is called
  num1 = 50
  # variable assigned
  num2 = 5
  # variable assigned
  return num1 * num2
  # return the multiplication of num1 and num2 when the subroutine is called

outputNum = maths2()
# assigns variable outputNum to the return value of subroutine maths2
print(outputNum)
# displays outputNum

# Example Code 3
def location(country):
# subroutine is defined,inside there is a parameter named country
  print("I am from " + country)
  # displays the prompt concatenated with the subroutine argument

location("Brazil")
# subroutine is called with argument "Brazil"

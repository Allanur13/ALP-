'''
In the modify tasks, you are given some starter code.
Use the instructions below to make changes to the code.
Comment your changes to explain what you have done.

Adapt the code to:
- Rename the function so that it has a sensible name. Don't forget to rename it when it is called.
- Call the function with the argument 'Sweden'.
- Get the user to input a country. Store it in a variable. Call the function again with the variable as the parameter.
'''
def my_country(country):
# I renamed the function name to my_country
  print("I am from " + country)


my_country("Brazil")
my_country("Sweden")
# I called the function with an argument "Sweden"
country = input("Please input a country: ")
# variable is assigned from the user
my_country(country)
# previous assigned variable used as a parameter with my_country function





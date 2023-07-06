'''
Answer the questions

'''

# Example code:

names = ["Alex","Anita","Patrick","Atif","Sue"]

print("Enter a number for your choice.")
print("1. Show all")
print("2. Add name")
print("3. Show name")
print("4. Exit")
choice = int(input())

if choice == 1:
  print(names)
elif choice == 2:
  name = input("Enter the name")
  names.append(name)
elif choice == 3:
  print("Enter the index of the name")
  index = int(input())
  print(names[index])
else:
  print("Goodbye")


# What is the identifier for the list in this program?
  # Answer: name

# What would happen if you choose option “3” and entered index “0”? 
  # Answer: it will print "Alex"

# What would happen if you choose option “3” and entered index “7”?
  # Answer: it will give an error. list index is out of range

# What would happen if you choose option “2” and entered the name “Stuart”?
  # Answer: It will add one item to the end of names list

# What is the purpose of int(input()) on line 10 ?
  #gets an input and converts that input into an integer


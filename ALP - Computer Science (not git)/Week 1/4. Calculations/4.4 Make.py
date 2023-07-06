# Program to calculate the area of a rectangle

# Get input for height & width. Convert to integers and store in variables

# Calculate the area & store the result in the area variable

# Output the area variable (converted to string)
height = int(input("Enter the height of the rectangle: "))
width = int(input("Enter the width of the rectange:"))
area = height * width
print("The area of rectangle is: " + str(area))






# Perimeter of rectangle
perimeter = (height + width) * 2
print("The perimeter of rectangle is: "+ str(perimeter))

#Restaurant Tip Calculator
price = int(input("Please enter the price of your meal:"))
tip = price / 5
total = price + tip
print("The tip is; " + str(tip))
print("The total price: " + str(total))

#Volume and Surface Calculations
height = int(input("Please enter the height of the cuboid: "))
width = int(input("Please enter the width of the cuboid: "))
length = int(input("Please enter the length of the cuboid"))
volume = height * width * length
area = 2*(height + width + length)
print("The volume of the cuboid is: " + str(volume) + ". The total surface area of the cuboid is: " + str(area))

'''
Extra Challenges
Perimeter Calc
Create a program that allows the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the perimeter of the rectangle. 
Restaurant Tip Calculator 
Create a program that allows the user to enter the price of a meal at a restaurant. The program calculates the amount of the tip to be paid at 20%. The tip and total price are then displayed separately.
Volume and Surface Calc 
Create a program that allows the user to enter 3 numbers representing the height, width and length of a cuboid. The program calculates and displays the volume and total surface area of the cuboid. 
'''
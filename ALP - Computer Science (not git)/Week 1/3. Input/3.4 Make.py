'''
Chat-Bot Challenge

Lots of websites use chat bots to interact with their customers.  These chat bots are often very sophisticated and use AI to learn and adapt to the user.  Our chat bot is going to be a bit simpler.

The chat bot should work like this:

1.Ask the user their name and store it in a variable.
2. Greet the user by name.
3. Ask the user three(or four) questions about themselves and store their responses in three(or four) different suitably named variables.
4. Respond to each of the questions one by one, using the 5. user’s name in the response.
5. Output a summary of all of the user’s answers in a single sentence.

'''

name = input("What's your name??")
print("Hello " + name + "! Nice to meet you!")
country = input("What country did you come from?")
print("Wow! " + name +". I have never heard of that country")
food = input("What food do you like the most?")
print("Lovely! I also love it, " + name)
age = input("How old are you?")
print("Oh, you are not old enough to drink an alcohol. Sorry " + name)
job = input("What do you do for living")
print("That's the job that I dreamt about! I also want to be " + job + " like you, " + name)
print(name + " is from " + country + "! He/She/They love/loves " + food + "! " + age + " years old! and he/she/they is a/an " + job)
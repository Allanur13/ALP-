'''
Task - Which Room?
----------------------

Write a program that asks the user for their name and which subject they are studying.
The program should output a message telling the student by name which room to go to for that class (make up the room numbers if you need to).  You should include at least 3 subjects and have a message such as 'I don't know which room that class is in' for any you don't include.
 Example - an input of 'Ben' and 'Computing' might get an output of 'Hi Ben, go to room 401 for Computing'


You may use any method taught in class that is appropriate for this task. There is room for interpretation.

'''
#Start coding below
name = input("Please enter your name: ")
subject = input("What subject are you studying: ")
subjectNames = ['Computing', 'Math', 'Biology', 'Physics', 'Chemistry']
if subject == subjectNames[0]:
  print("hi " + name + ", go to room 401 for " + subjectNames[0])
elif subject == subjectNames[1]:
  print("hi " + name + ", go to room 402 for " + subjectNames[1])
elif subject == subjectNames[2]:
  print("hi " + name + ", go to room 403 for " + subjectNames[2])
elif subject == subjectNames[3]:
  print("hi " + name + ", go to room 404 for " + subjectNames[3])
elif subject == subjectNames[4]:
  print("hi " + name + ", go to room 405 for " + subjectNames[4])
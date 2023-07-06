testMark = int(input("Please enter the your test mark: (It should be between 1 and 100)\n"))
if testMark < 1:
  print("Too Low! Enter a valid test mark")
  exit()
elif testMark > 100:
  print("Too High! Enter a valid test mark")
  exit()
# I used the exit() function to terminate the program, so if the test score value is too high or too low, it will exit the running code immediately
# I didn't use AND operator, because if the value is too high or too low it already will terminate the program
if testMark < 40:
  fail = 'Y'
else:
  fail = 'N'

if fail != 'N':
  print("Retake required")
else:
  print("Passed")

if testMark < 40:
  print('"U" grade')
elif testMark < 69:
  print('"C" grade')
elif testMark < 80:
  print('"B" grade')
else:
  print('"A" grade')
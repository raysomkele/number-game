import random
number = random.randint(0,100)
question = input(A number was picked between 0 and 100)
if question > 50:
   print("low")
   print(question)
if question < 50:
   print("high")
   print(question)

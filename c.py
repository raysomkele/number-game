import random
playing = True
highscore = 0
attemps = 1
number = str(random.randint(0,20))
print("You have to guess a number between 0 and 20 ")
while playing :
    guess = input("What is your guess? ")
    if number == guess:
        print("You win? ")
        print("the number was " + number)
        print("You took " , attemps ," attemps")
        if highscore < attemps:
            print("New highscore" , highscore)
        break
    else:
        print("Try again")
        attemps = attemps + 1
    if attemps > 10:
        print("10 attempts")
        pass
    

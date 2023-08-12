import random

max=100
min=1
randomnum=random.randint(min,max)
attempts=0
guessedcorrectly= False
while not guessedcorrectly:
    userguess=int(input("Enter your number:"))
    attempts+=1
    if userguess<randomnum:
        print("Low! try a higher number")
    elif userguess>randomnum:
        print("High! try a low number")
    else:
        guessedcorrectly= True
        print("Congratulations! you got it right")
        print("You guessed the number ",randomnum," in ",attempts," attempts")
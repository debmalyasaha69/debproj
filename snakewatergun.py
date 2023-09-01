import random
main=("Snake","Water","Gun")
name=input("Enter your name:")
print(f"Welcome {name}")
user=(input(f"Would you like to play our game(yes/no)?")).lower()
points=0
if user=="yes":
  print("RULES:-")
  print("• If the computer and user both throw the same thing it's a draw")
  print("• If the computer throws water and you throw snake you will win and vice-versa")
  print("• If the computer throws water and you throw gun computer will win and vice-versa")
  print("• If the computer throws gun and you throw snake computer will win and vice-versa")
  n = int(input("How many times you wanna play??"))
  for i in range(n):
      computer=random.choice(main)
      user_choice=(input("What do you wanna take: ")).lower()
      if(user_choice=="water" and computer=="Water"):
          print(f"Computer choose: {computer}")
          print("It's a draw")
      elif(user_choice=="snake" and computer=="Water"):
          print(f"Computer choose: {computer}")
          print("You won")
          points+=1
      elif(user_choice=="gun" and computer=="Water"):
          print(f"Computer choose: {computer}")
          print("You lost")
      elif(user_choice=="gun" and computer=="Snake"):
          print(f"Computer choose: {computer}")
          print("You won")
          points+=1
      elif(user_choice=="gun" and computer=="Gun"):
          print(f"Computer choose: {computer}")
          print("It's a draw")
      elif(user_choice=="snake" and computer=="Snake"):
          print(f"Computer choose: {computer}")
          print("It's a draw")
      elif(user_choice=="snake" and computer=="Gun"):
          print(f"Computer choose: {computer}")
          print("You lost")
      elif(user_choice=="water" and computer=="Snake"):
          print(f"Computer choose: {computer}")
          print("You lost")
      elif(user_choice=="water" and computer=="Gun"):
          print(f"Computer choose: {computer}")
          print("You won")
          points+=1
      else:
          print("Undefined")
  print("Your points= ",points)
elif(user=="no"):
    print(f"OK {name} come again THANK YOU")
else:
    print("Please enter yes or no")
print(f"Thank You!!! {name} for playing with us")



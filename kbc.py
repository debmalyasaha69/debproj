

questions=[["What is the capital of india?","1. New Delhi","2. Assam","3. Manipur","4. Nagaland"],["Who is the prime minister of india?","1. Barack Obama","2. Donald Duck","3. Vlamadir Putin","4. Narendra Modi"],["How many months do we have in a year?","1. 12","2. 15","3. 19","4. 20"],["How many days do we have in a week?""1. 10","2. 6","3. 7","4. 8"],["How many days are there in a year?","1. 400","2. 325","3. 360","4. 365"],["How many alphabates are there?","1. 30","2. 26","3. 40","4. 69"]]
answers=["New Delhi","Narendra Modi","12","7","365","26","1","4","1","3","4","2"]
money=[0,1000,20000,300000,4000000,5000000,10000000]
name=input("Enter your name: ")
print("Hello ",name)
print("Welcome to KBC")
ready=input("Are you ready: ")
count=0
num=0
if (ready=="yes"):
    for i in questions:
        print(questions[count])
        guess=input("Enter your answer: ")
        if(guess==answers[count] or guess==answers[6+num] ):
            print("Congartulations! Your answer is correct")
            print("You won: ",money[count+1])
        else:
            print("Sorry your answer is incorrect")
            print("You won: ",money[count])
            break
        count=count+1
        num=num+1
    print("Thank you very much for playing this game")
    print("You cannot withdraw the money Sorry!")
else:
    print("Ok after being ready u can continue")

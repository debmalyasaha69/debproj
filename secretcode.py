import random
def code(message):
    if len(message)>=3:
        first_char=message[0]
        new_word=''.join(random.choices("abcdefghijklmnopqrstuvwxyz",k=3))+message[1:]+first_char+''.join(random.choices("abcdefghijklmnopqrstuvwxyz",k=3))
        return new_word
    else:
        return message[::-1]
def decode(message):
    if len(message)<3:
        return message[::-1]
    else:
        if(len(message)<=6):
            print("Invalid Input")
        else:
            new_word=message[3:-3]
            new_word2=new_word[-1]+new_word[0:-1]
            return new_word2
user_input=(input("Enter what do you want to do code or decode(c/d): ").lower())
if(user_input=="c"):
    message=(input("Enter the message you want to code: ").lower())
    coded_message=code(message)
    print("Coded message: ",coded_message)
elif(user_input=="d"):
    message=(input("Enter the message you want to decode: ").lower())
    if (len(message)>6):
      decoded_message=decode(message)
      print("Decoded message: ",decoded_message)
    else:
        decoded_message=decode(message)
else:
    print("Invalid Input")
    print("Please enter \'c\' for coding and \'d\' for decoding")
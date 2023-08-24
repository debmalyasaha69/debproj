import time
timestamp=time.strftime("%H:%M:%S")
print("The time is: ",timestamp)
hour=time.strftime("%H")
minutes=time.strftime("%M")
seconds=time.strftime("%S")
if ((hour>="6" and minutes>="00" and seconds>="00") and (hour<="11" and minutes<="59" and seconds<="59")):
    print("Good morning Sir")
elif ((hour>="12" and minutes>="00" and seconds>="00") and (hour<="18" and minutes<="59" and seconds<="59")):
    print("Good afternoon Sir")
elif ((hour>="18" and minutes>="00" and seconds>="00") and (hour<="24" and minutes<="59" and seconds<="59")):
    print("Good evening Sir")
else:
    print("Good night Sir")

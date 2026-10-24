#پروژه ششم
#بازی حدس اعداد
import random

computer=random.randint(1,100)
count=0
while True:
    x=int(input("guess the number >>>"))
    count +=1
    if x> computer:
        print("too high")
    elif x< computer:
     print("too low")
    else:
        print("correct")
        break
print("you guessed",count, "times ")
import random #to generate random numbers in our case 1-6

i =0

while i in range(10):   
    text = input("Please press enter for rolling dice" if i ==0  else "Press enter again")  
    if text == "":
        print("You got :", random.choice([1,2,3,4,5,6]))
        i = i+1
        continue
    else:
        print("you typed some text before pressing enter so program execution completed")
        break
    
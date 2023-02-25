import random #to generate random numbers in our case 1-6

userOne = str(input("Enter first user name :"))
userTwo = str((input("Enter second user name :")))
i =0

while i in range(10):    
    try :
        text = input("Please press enter to start game" if i ==0  else "\nPress enter to play again")  
        if text == "":
            userOneScore = random.choice([1,2,3,4,5,6])
            userTwoScore = random.choice([1,2,3,4,5,6])

            print(f"{userOne} 'You got :'{userOneScore}")
            print(f"{userTwo} 'You got :'{userTwoScore}")

            if userOneScore > userTwoScore :
                print(f"\nResult : {userOne} won the game ")
            elif userTwoScore > userOneScore : 
                print(f"\nResult : {userTwo} won the game ")
            elif userOneScore == userTwoScore :
                print("\nResult : Dro")
            else :
                print("\nSome exception occurred")
            i = i+1
            continue
    except :
        print("\nYou typed some text before pressing enter so program execution completed")
        break
        


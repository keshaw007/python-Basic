print("Total number of guesses=9")
orinum=26
i=1
while(i<=10):
    if(i==10):
        print("\n BETTER LUCK NEXT TIME! Your Attempt  is over")
        break

    print("\nattempt left =", end=" ")
    print(9-i)
    print("\nEnter your Number")
    innum=int(input())
    if(innum==orinum):
        print("Congrats! You Guess Correct Number")
        break
    if(innum>orinum):
        print("Entered Number is greater than original number")
        continue
    i=i+1
    if(innum<orinum):
        print("Entered Number is lesser than original number")
        continue
    i=i+1

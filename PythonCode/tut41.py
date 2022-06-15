print("WELCOME TO SNAKE WATER GUN GAME \n")
import time
time.sleep(2)
print("YOU HAVE GIVEN 10 CHANCES AND WINNER WILL BE DECIDED AFTER 10 ROUNDS \n")
time.sleep(2)
print("YOUR CHOICE MUST BE SNAKE or WATER or GUN in case sensitive manner i.e all alphabet must be in lowercase\n")
time.sleep(2)
print("BONUS POINT IS GIVEN WHEN INVALID CHOICE IS ENTERED\n")
i=0
user_point=0
tie_point=0
AI_point=0
bonus_point=0
while(i<10):
    time.sleep(2)
    print(f"This is your {i} chance")
    print("Enter your choice in small case")
    user_choice=input()

    #For valid choice
    if(user_choice=="snake" or user_choice=="water" or user_choice=="gun"):
        import random
        list_of_choice=["snake", "water", "gun"]
        AI_choice=random.choice(list_of_choice)
        print("Computer choice is ",AI_choice)

        #case 1 snake for AI
        if(AI_choice=="snake" and user_choice=="snake"):
            print("No one win\n")
            tie_point=tie_point+1
        elif(AI_choice=="snake" and user_choice=="water"):
            print("Computern win\n")
            AI_point=AI_point+1
        elif(AI_choice=="snake" and user_choice=="gun"):
            print("You win\n")
            user_point=user_point+1

        #case 2 water for AI
        elif(AI_choice=="water" and user_choice=="snake"):
            print("You win\n")
            user_point=user_point+1
        elif(AI_choice=="water" and user_choice=="water"):
            print("No one win\n")
            tie_point=tie_point+1
        elif(AI_choice=="water" and user_choice=="gun"):
            print("Computer win\n")
            AI_point=AI_point+1

        #case 3 gun for AI
        if(AI_choice=="gun" and user_choice=="snake"):
            print("Computer win\n")
            AI_point=AI_point+1
        if(AI_choice=="gun" and user_choice=="water"):
            print("You win\n")
            user_point=user_point+1
        if(AI_choice=="gun" and user_choice=="gun"):
            print("No one win\n")
            tie_point=tie_point+1

    #For invalid choice
    else:
        print("YOU ENTERED INVALID CHOICE\n")
        time.sleep(1)
        print("A bonus point is given to computer for this round\n")
        bonus_point=bonus_point+1
    i=i+1

#final RESULT
if(user_point>AI_point+bonus_point):
    print("Congrats! YOU WIN GAME")
elif(user_point<AI_point+bonus_point):
    print("OOPS! BETTER LUCK NEXT TIME")
elif(user_point==AI_point+bonus_point):
    print("Match Tied")

#FINAL SCORE
print("Enter Y or y to see final score or any other key to exit")
ans=input()
if(ans=="Y" or "y"):
    print("Computer score is ", AI_point)
    print("Your Score is ", user_point)
    print("Tied attempt score is ",tie_point)
    print("Conputer bonus score is ",bonus_point)
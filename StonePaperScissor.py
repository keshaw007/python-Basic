import time
print("\nWELCOME TO STONE PAPER SCISSOR GAME \n")
time.sleep(2)
print("YOU HAVE GIVEN 5 CHANCES AND WINNER WILL BE DECLARED AFTER 5 ROUNDS \n")
time.sleep(3)
print("YOUR CHOICE MUST BE STONE or PAPER or SCISSOR in case sensitive manner i.e all alphabet must be in lowercase\n")
time.sleep(5)
print("BONUS POINT IS GIVEN WHEN INVALID CHOICE IS ENTERED\n")
i = 1
user_point = 0
tie_point = 0
AI_point = 0
bonus_point = 0
while(i < 6):
    print(f"---------This is your {i} chance----------")
    time.sleep(2)
    print("Enter your choice in small case")
    user_choice = input()

    # For valid choice
    if(user_choice == "stone" or user_choice == "paper" or user_choice == "scissor"):
        import random
        list_of_choice = ["stone", "paper", "scissor"]
        AI_choice = random.choice(list_of_choice)
        print("Computer choice is ", AI_choice)

        # case 1 stone for AI
        if(AI_choice == "stone" and user_choice == "stone"):
            print("Round Tied\n")
            tie_point = tie_point+1
        elif(AI_choice == "stone" and user_choice == "scissor"):
            print("Computern win\n")
            AI_point = AI_point+1
        elif(AI_choice == "stone" and user_choice == "paper"):
            print("You win\n")
            user_point = user_point+1

        # case 2 paper for AI
        elif(AI_choice == "paper" and user_choice == "scissor"):
            print("You win\n")
            user_point = user_point+1
        elif(AI_choice == "paper" and user_choice == "paper"):
            print("Round Tied\n")
            tie_point = tie_point+1
        elif(AI_choice == "paper" and user_choice == "stone"):
            print("Computer win\n")
            AI_point = AI_point+1

        # case 3 scissor for AI
        if(AI_choice == "scissor" and user_choice == "paper"):
            print("Computer win\n")
            AI_point = AI_point+1
        if(AI_choice == "scissor" and user_choice == "stone"):
            print("You win\n")
            user_point = user_point+1
        if(AI_choice == "scissor" and user_choice == "scissor"):
            print("Round Tied\n")
            tie_point = tie_point+1

    # For invalid choice
    else:
        print("YOU ENTERED INVALID CHOICE\n")
        time.sleep(1)
        print("A bonus point is given to computer for this round\n")
        bonus_point = bonus_point+1
    i = i+1

# final RESULT
time.sleep(2)
print("----------FINAL RESULT----------")
if(user_point > AI_point+bonus_point):
    print("\nCongrats! YOU WIN GAME\n")
elif(user_point < AI_point+bonus_point):
    print("\nOOPS! BETTER LUCK NEXT TIME\n")
elif(user_point == AI_point+bonus_point):
    print("\nMATCH  TIED\n")

# FINAL SCORE
print("Enter Y or y to see final score or any other key to exit")
ans = input()
if(ans == "Y" or ans=="y"):
    print("Computer score is ", AI_point)
    print("Your Score is ", user_point)
    print("Tied attempt is ", tie_point)
    print("Computer bonus score is ", bonus_point)
    print("Computer total score is ", bonus_point+AI_point)
    print("\n----------THANKS FOR USING MY GAME----------")
else:
    print("\n----------THANKS FOR USING MY GAME----------\n")
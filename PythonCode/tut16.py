while(True):
    print("Enter 1st number")
    num1=int(input())
    print("Enter operand")
    opd=(input())
    print("Enter 2nd number")
    num2=int(input())
    #for Addition
    if(opd=='+'):
        if(num1==56 and num2==9):
            print("77")
        else:
        
                sum=num1+num2
                print(sum)

    # For Substraction
    if(opd=='-'):
        diff=num1-num2
        print(diff)

    #For Multiplication
    if(opd=='*'):
        if(num1==45 and num2==3):
            print("555")
        else:
        
                product=num1*num2
                print(product)

    #For Division
    if(opd=='/'):
        if(num1==56 and num2==6):
            print("4")
        else:
        
                divisor=num1/num2
                print(divisor)
    print("Do you want to calculate again? Y or N")
    ans=input()
    if(ans=='Y'):
        continue
    if (ans=='N') :
        print("thanks for using calculater")
        break
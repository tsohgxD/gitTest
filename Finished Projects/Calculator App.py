
#This is my Calculator app 100% free of AI, using only cheatsheets. I realise there are better ways to make a calculator but i believe 
#i need to get way more confortable with dictionaries, i will focus heavily on the and the next project upload will be a dictionary based program.

try:
    userInputNumbers1 = int(input("Please write any number: "))
    userInputOperator = input("Choose a operator: ")
    userInputNumbers2 = int(input("Please write any number: "))

    if userInputOperator == "+":
        print(userInputNumbers1 + userInputNumbers2)

    elif userInputOperator == "-":
        print(userInputNumbers1 - userInputNumbers2)

    elif userInputOperator == "*":
        print(userInputNumbers1 * userInputNumbers2)

    elif userInputOperator == "/":
        print(userInputNumbers1 / userInputNumbers2)
    
    else:
        print("Your Operator must contain '+', '-', '/' or '*' ")
    
except:
    print("Only Numbers Are acceptable, This is a Calculator") 
def age_verification_system():
    try:
        user_input = int(input("Please tell me your Age: "))
        if user_input >= 18:
            print("You are of the legal age")
        else:
            print("You are too young")
    
    except ValueError:
        print("You need to write a number!")


age_verification_system()
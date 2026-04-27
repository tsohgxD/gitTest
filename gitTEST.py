print("Welcome to Linux Challenger")
user_input = input("give me ur name: ")
choose_mode = input(f"Hello {user_input}! Choose a mode\n1 = Start Game\n2 = Exit\nEnter: ")

if choose_mode == "1":
    print(f"Starting Linux Challenge for {user_input}")
elif choose_mode == "2":
    print(f"Goodbye {user_input}")
else:
    print("Invalid choice")


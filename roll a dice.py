import random

while True:
    user_input = input("Press Enter to roll a dice or type 'exit' to quit: ")
    if user_input == "":
        print(random.randint(1,6))
    elif user_input == "exit":
        print("Exiting...")
        break
    else:
        print("Invalid input. Try again.")





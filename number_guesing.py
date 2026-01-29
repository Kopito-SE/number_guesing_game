import random

play_options=("r","p","s")
emoji_set = {'r':'🪨','p':'📃','s':'✂️'}

while True:
    user_choice = input("Enter your play (r,p,s): ").lower()
    if user_choice not in play_options:
        print("Please enter a valid play option!")
        continue

    computer_choice = random.choice(play_options)

    print(f"You chose {emoji_set[user_choice]}")
    print(f"Computer chose {emoji_set[computer_choice]}")


    if computer_choice == user_choice :
        print("Tie")
    elif user_choice == "r" and computer_choice == "s"\
        or user_choice == "s" and computer_choice == "p"\
        or user_choice == "p" and computer_choice == "r" :
        print("You Win")
    else:
        print("You Lose")

    continue_play = input("Play again?(y/n) : ").lower()
    if continue_play != "y" and continue_play != "n" :
        print("Enter a Valid Option.")
    elif continue_play == "n" :
        print("Thanks for playing😊.")
        break


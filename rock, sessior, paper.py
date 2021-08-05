import random
while True :
    my_list = ["rock", "sessior", "paper"]
    computer = random.choice(my_list)
    player = None
    while player not in my_list:
        player = input("Enter a value (rock, sessior, paper):")
        if player == computer:
            print("Computer :" +computer)
            print("Player :" + player)
            print("Tie !")
        if player == "rock":
            if computer == "sessior":
                print("Computer :" +computer)
                print("Player :" + player)
                print("You lose !")
            elif computer == "paper":
                print("Computer :" +computer)
                print("Player :" + player)
                print("You win!")
        if player == "sessior":
            if computer == "paper":
                print("Computer :" +computer)
                print("Player :" + player)
                print("You lose !")
            elif computer == "rock":
                print("Computer :" +computer)
                print("Player :" + player)
                print("You win!")
        if player == "paper":
            if computer == "rock":
                print("Computer :" +computer)
                print("Player :" + player)
                print("You lose !")
            elif computer == "sesior":
                print("Computer :" +computer)
                print("Player :" + player)
                print("You win!")
    play_again = input("Do you want to play again(yes, no): ")
    if play_again != "yes":
        print("Bye !!!!!")
        break
    elif play_again != "yea":
        print("Bye !!!!!")
        break
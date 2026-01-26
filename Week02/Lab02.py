import random

choices = ["Scissors", "Rock", "Paper"]

playerChoice = input("Enter your choice - (1-Scissors, 2-Rock, 3-Paper): ")
playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice Should Between 1 and 3!")
else:
    computerChoice = random.randint(1,3)
    
    # use if/elif/else to determine the winner logic
    if playerChoice == computerChoice:
        print("It's a Tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Scissors beats Paper - You Win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Rock beats Scissors - You Win!")
    elif playerChoice == 3 and computerChoice == 2:
        print("Paper beats Rock - You Win!")
    else:
        print("YOU LOST!")
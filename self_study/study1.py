import random
def get_choices():
    print("please pick rock, paper, scissors")
    player_choice = input("what is your choice? \n")
    computer = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"you choose {player} , computer choose {computer}")
    if player == computer:
        return "it's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "YOU WIN! rock absolutely killed scissors"
        else:
            return "YOU LOSE! rock killed by paper"
    elif player == "paper":
        if computer == "scissors":
            return "YOU LOSE! paper killed by scissors"
        else:
            return "YOU WIN! paper absolutely killed rock"
    elif player == "scissors":
        if computer == "paper":
            return "YOU WIN! scissors absolutely killed paper"
        else:
            return "YOU LOSE! rock killed scissors"
#
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)



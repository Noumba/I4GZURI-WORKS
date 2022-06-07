import random


play_outcome = "tie"
mapping_choice = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}

while play_outcome == "tie":
    choices = ["R", "P", "S"]

    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("R, P, or S? (Rock, Paper, Scissors): ").upper()

    if player == computer:
        print("Player: ", mapping_choice[player],
              " : ", "CPU: ", mapping_choice[computer])
        play_outcome = "tie"
        print("Its a tie")
    elif player == "R":
        if computer == "P":
            print("Player: ", mapping_choice[player],
                  " : ", "CPU: ", mapping_choice[computer])
            print("You lose")
            play_outcome = "end"
        if computer == "S":
            print("Player: ", mapping_choice[player],
                  " : ", "CPU: ", mapping_choice[computer])
            print("You win")
            play_outcome = "end"
    elif player == "S":
        if computer == "R":
            print("Player: ", mapping_choice[player],
                  " : ", "CPU: ", mapping_choice[computer])
            print("You lose")
            play_outcome = "end"
        if computer == "P":
            print("Player: ", mapping_choice[player],
                  " : ", "CPU: ", mapping_choice[computer])
            print("You win")
            play_outcome = "end"
    elif player == "P":
        if computer == "S":
            print("Player: ", mapping_choice[player],
                  " : ", "CPU: ", mapping_choice[computer])
            print("You lose")
            play_outcome = "end"
        if computer == "R":
            print("Player: ", mapping_choice[player],
                  " : ", "CPU: ", mapping_choice[computer])
            print("You win")
            play_outcome = "end"

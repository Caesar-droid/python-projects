import random
game_list = ['Rock','Paper','Scissors']
computer = c = 0
Player = p = 0
print(f"Score: Computer {c} Player {p}")
#the loop

while True:
    computer_choice = random.choice(game_list)
    command = input("Rock, Paper, Scissors or Quit: ")
    if command == computer_choice:
        print("Its a tie.")
    elif command == 'Rock':
        if computer_choice == 'Scissors':
            print("Player won!")
            p +=1
        else:
            print("Computer won!")
            c +=1
    elif command == 'Paper':
        if computer_choice == 'Rock':
            print("Player won!")
            p +=1
        else:
            print("computer won!")
            c += 1
    elif command == 'Scissors':
        if computer_choice == 'Paper':
            print("Player won!")
            p +=1
        else:
            print("Computer won!")
            c +=1
    elif command == 'Quit':
        break
    else:
        print("Invalid command!")
print(f"Player: {command}")
print(f"Computer: {computer_choice}")
print("")
print(f"Score: Computer {c}\nPlayer {p}")
print("")
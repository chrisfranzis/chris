#Schere Stein Papier

#Dictionary
# numconversion = {
#     0: "Rock",
#     1: "Paper",
#     2: "Scissors",
#     "q": "Quit"
#
# }
#
# choice = input("Choice: ")
#
# def tool(choice):
#     print("--- Make a choice\n --- Rock: 0\n --- Paper: 1 \n ---Scissors: 2 \n --- Quit: q")
#
#     if choice == 0:
#             print(numconversion.get(choice))
#     elif choice == 1:
#             print(numconversion.get(choice))
#     elif choice == 2:
#             print(numconversion.get(choice))
#     elif choice == "q":
#             print(numconversion.get(choice))
#     else:
#             print("Enter a valid choice")
#     return(tool(choice))


import random

tools = (0, 1, 2)
player = ""
print("Welcome to Rock Paper Scissors!")

def single_player(player):
    player = input("Player Name: ")
    
    if user == 3 and computer < 3:
        print(player + "has won the game!")
    elif computer == 3 and user < 3:
        print("Computer has won the game!")

#1. Menu
def menu():
    print(" --- MAKE A CHOICE:\n --- Rock: 0\n --- Paper: 1 \n --- Scissors: 2 \n --- Quit: q")
    #input("Choice: ")

    # if Computer > Player choice:
    #     print("SCISSORS wins against PAPER Computer scored 1 Point")
    #     print("SCORE")
    # elif Computer = Player choice
    #     print("DRAW")
    #     print("SCORE")
    # elif Computer < Player
    #     print("Player wins")
    #     print("SCORE")
    return

#2. Choice
# choice_list = ["ROCK", "PAPER", "SCISSORS", "Quit"]
# choice = input("Your Choice: ")
# choice_list.index[0] = str("ROCK")
#     choice[1] = str("PAPER")
#     choice[2] = str("SCISSORS")
def tool(choice):
    while choice not in range(0, 3):
        print("ERROR: Please enter a valid option!")
        choice = input("Choice: ")
    if choice == 0:
        print("ROCK")
    elif choice == 1:
        print("PAPER")
    elif choice == 2:
        print("SCISSORS")
    # elif choice == "q":
    #     print("You quit the game!")
    return

#3. Who_wins
def who_wins(user, computer, choice_a, choice_b):
    choice_a = choice
    choice_b = random.choice(tools)
    user = 0
    computer = 0

    if choice_a == choice_b:
        print("It's a draw!")
#Player chooses ROCK=0
    elif choice_a == 0 and choice_b == 1
        print("PAPER wins against ROCK/n Computer scored 1 Point!")
        computer += 1
#Reverse Funktion wäre gut, damit ich mir die doppelte Arbeit spare???
    elif choice_a == 0 and choice_b == 2
        print("ROCK wins against PAPER/n" + player + "scored 1 Point!")
        user += 1
#Player chooses PAPER=1
    elif choice_a == 1 and choice_b == 0:
        print("PAPER wins against ROCK/n" + player + "scored 1 Point!")
        user += 1
    elif choice_a == 1 and choice_b == 2:
        print("SCISSORS wins against PAPER/n Computer scored 1 Point!")
        computer += 1
#Player chooses SCISSORS=2
    elif choice_a == 2 and choice_b == 0:
        print("ROCK wins against SCISSORS/n Computer scored 1 Point!")
        computer += 1
    elif choice_a == 2 and choice_b == 1:
        print("SCISSORS wins against PAPER/n" + player + "scored 1 Point!")
        user += 1
        
    return print(user + " --- | --- " + computer))


#Ich bleibe in der while loop hängen!
    print(menu())
    choice = input("Choice: ")
    print(tool(choice))


















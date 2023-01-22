print("Welcome to two-player TicTacToe. \nIn this game, the board is set up like this:\n1 2 3\n"
      "4 5 6\n"
      "7 8 9")
print("Every turn each player will be asked to pick the location of their \nmove one after another, "
      "first player to get three in a row wins.")

spaces = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

already_picked = []

game_status = True

player = 1


def make_grid(list_item):
    print(list_item[0], list_item[1], list_item[2], "\n")
    print(list_item[3], list_item[4], list_item[5], "\n")
    print(list_item[6], list_item[7], list_item[8])


def player_one_turn():
    global player, spaces, already_picked, game_status
    guess = input("\nPlayer 1, choose a location for your next move: ")
    if guess in already_picked:
        print("You chose an unavailable square, try again")
        guess = input(f"\nPlayer {player}, choose a location for your next move: ")
        already_picked.append(guess)
        guess = int(guess)
        spaces[guess - 1] = "x"
        make_grid(spaces)
        player = 2
    else:
        already_picked.append(guess)
        guess = int(guess)
        spaces[guess-1] = "x"
        make_grid(spaces)
        player = 2

    if spaces[0] == "x" and spaces[1] == "x" and spaces[2] == "x" or spaces[3] == "x" and spaces[4] == "x" and spaces[5] == "x" or spaces[6] == "x" and spaces[7] == "x" and spaces[8] == "x":
        game_status = False
        print("\nPlayer 1 has won the game!")

    if spaces[0] == "x" and spaces[3] == "x" and spaces[6] == "x" or spaces[1] == "x" and spaces[4] == "x" and spaces[7] == "x" or spaces[2] == "x" and spaces[5] == "x" and spaces[8] == "x":
        game_status = False
        print("\nPlayer 1 has won the game!")

    if spaces[0] == "x" and spaces[4] == "x" and spaces[8] == "x" or spaces[2] == "x" and spaces[4] == "x" and spaces[6] == "x":
        game_status = False
        print("\nPlayer 1 has won the game!")

    if "_" not in spaces:
        game_status = False
        print("\nTie")


def player_two_turn():
    global player, spaces, already_picked, game_status

    guess_two = input("\nPlayer 2, choose a location for your next move: ")
    if guess_two in already_picked:
        print("You chose an unavailable square, try again")
        guess_two = input(f"\nPlayer {player}, choose a location for your next move: ")
        already_picked.append(guess_two)
        guess_two = int(guess_two)
        spaces[guess_two - 1] = "o"
        make_grid(spaces)
        player = 1
    else:
        already_picked.append(guess_two)
        guess_two = int(guess_two)
        spaces[guess_two-1] = "o"
        make_grid(spaces)
        player = 1

    if spaces[0] == "o" and spaces[1] == "o" and spaces[2] == "o" or spaces[3] == "o" and spaces[4] == "o" and spaces[5] == "o" or spaces[6] == "o" and spaces[7] == "o" and spaces[8] == "o":
        game_status = False
        print("\nPlayer 2 has won the game!")

    if spaces[0] == "o" and spaces[3] == "o" and spaces[6] == "o" or spaces[1] == "o" and spaces[4] == "o" and spaces[7] == "o" or spaces[2] == "o" and spaces[5] == "o" and spaces[8] == "o":
        game_status = False
        print("\nPlayer 2 has won the game!")

    if spaces[0] == "o" and spaces[4] == "o" and spaces[8] == "o" or spaces[2] == "o" and spaces[4] == "o" and spaces[6] == "o":
        game_status = False
        print("\nPlayer 2 has won the game!")

    if "_" not in spaces:
        game_status = False
        print("\nTie")


while game_status:
    player_one_turn()
    if not game_status:
        break
    else:
        player_two_turn()

import random

board = {
    # each square gets a number, 1 = top left, 2 = top center, etc.
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " "
}


def printboard(board):
    print(board[1], "|", board[2], "|", board[3])
    print("---------")
    print(board[4], "|", board[5], "|", board[6])
    print("---------")
    print(board[7], "|", board[8], "|", board[9])


def main():
    loop = True
    while loop:
        start = input("enter 1 to play, and 2 for help: ")
        if (start == "1") or (start == "2"):
            if start == "1":
                loop = False
                game()
            elif start == "2":
                print(
                    "\nuse the num pad as if it is the tic-tac-toe grid\n (example below)\n"
                )
                print("7", "|", "8", "|", "9")
                print("---------")
                print("4", "|", "5", "|", "6")
                print("---------")
                print("1", "|", "2", "|", "3\n")
        else:
            print("\nInvalid response\n")


def game():
    pass


# more like a function handler than a game tbh


def playerchoice():
    pass


# input ez


def cpuchoice(board):

    for x in board:
        fakeboard = board.copy()
        if board[x] == " ":
            fakeboard[x] = "x"
            result = checkwin(fakeboard)
            if result == "x":
                return x

    available_squares = []

    for z in board:
        if board[z] == " ":
            available_squares.append(z)
    return random.choice(available_squares)


def checkwin(board):

    #checking if x won
    if (board[1] == "x") and (board[2] == "x") and (board[3] == "x"):
        return "x"
    elif (board[4] == "x") and (board[5] == "x") and (board[6] == "x"):
        return "x"
    elif (board[7] == "x") and (board[8] == "x") and (board[9] == "x"):
        return "x"
    elif (board[1] == "x") and (board[5] == "x") and (board[9] == "x"):
        return "x"
    elif (board[3] == "x") and (board[5] == "x") and (board[7] == "x"):
        return "x"
    elif (board[1] == "x") and (board[4] == "x") and (board[7] == "x"):
        return "x"
    elif (board[2] == "x") and (board[5] == "x") and (board[8] == "x"):
        return "x"
    elif (board[3] == "x") and (board[6] == "x") and (board[9] == "x"):
        return "x"

#checking if o won
    elif (board[1] == "o") and (board[2] == "o") and (board[3] == "o"):
        return "o"
    elif (board[4] == "o") and (board[5] == "o") and (board[6] == "o"):
        return "o"
    elif (board[7] == "o") and (board[8] == "o") and (board[9] == "o"):
        return "o"
    elif (board[1] == "o") and (board[5] == "o") and (board[9] == "o"):
        return "o"
    elif (board[3] == "o") and (board[5] == "o") and (board[7] == "o"):
        return "o"
    elif (board[1] == "o") and (board[4] == "o") and (board[7] == "o"):
        return "o"
    elif (board[2] == "o") and (board[5] == "o") and (board[8] == "o"):
        return "o"
    elif (board[3] == "o") and (board[6] == "o") and (board[9] == "o"):
        return "o"


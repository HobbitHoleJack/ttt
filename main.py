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


def printboard(testboard):
    print(testboard[1], "|", testboard[2], "|", testboard[3])
    print("---------")
    print(testboard[4], "|", testboard[5], "|", testboard[6])
    print("---------")
    print(testboard[7], "|", testboard[8], "|", testboard[9])


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


def cpuchoice(testboard):
    for x in testboard:
        fakeboard = testboard.copy()
        if testboard[x] == " ":
            fakeboard[x] = "x"
            result = checkwin(fakeboard)
            if result == "x":
                return x

    available_squares = []

    for z in testboard:
        if testboard[z] == " ":
            available_squares.append(z)
    return random.choice(available_squares)


def checkwin(testboard):
    if (testboard[1] == "x") and (testboard[2] == "x") and (testboard[3] == "x"):
        return "x"
    elif (testboard[4] == "x") and (testboard[5] == "x") and (testboard[6] == "x"):
        return "x"
    elif (testboard[7] == "x") and (testboard[8] == "x") and (testboard[9] == "x"):
        return "x"
    elif (testboard[1] == "x") and (testboard[5] == "x") and (testboard[9] == "x"):
        return "x"
    elif (testboard[3] == "x") and (testboard[5] == "x") and (testboard[7] == "x"):
        return "x"
    elif (testboard[1] == "x") and (testboard[4] == "x") and (testboard[7] == "x"):
        return "x"
    elif (testboard[2] == "x") and (testboard[5] == "x") and (testboard[8] == "x"):
        return "x"
    elif (testboard[3] == "x") and (testboard[6] == "x") and (testboard[9] == "x"):
        return "x"

    # checking if o won
    elif (testboard[1] == "o") and (testboard[2] == "o") and (testboard[3] == "o"):
        return "o"
    elif (testboard[4] == "o") and (testboard[5] == "o") and (testboard[6] == "o"):
        return "o"
    elif (testboard[7] == "o") and (testboard[8] == "o") and (testboard[9] == "o"):
        return "o"
    elif (testboard[1] == "o") and (testboard[5] == "o") and (testboard[9] == "o"):
        return "o"
    elif (testboard[3] == "o") and (testboard[5] == "o") and (testboard[7] == "o"):
        return "o"
    elif (testboard[1] == "o") and (testboard[4] == "o") and (testboard[7] == "o"):
        return "o"
    elif (testboard[2] == "o") and (testboard[5] == "o") and (testboard[8] == "o"):
        return "o"
    elif (testboard[3] == "o") and (testboard[6] == "o") and (testboard[9] == "o"):
        return "o"

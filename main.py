import random
import time
from time import sleep
start_time = time.time()

def printboard(resetboard):
    print(resetboard[1], "|", resetboard[2], "|", resetboard[3])
    print("---------")
    print(resetboard[4], "|", resetboard[5], "|", resetboard[6])
    print("---------")
    print(resetboard[7], "|", resetboard[8], "|", resetboard[9], "\n")


def main():
    loop = True
    while loop:
        start = input("\nenter 1 to play, 2 for help, and 3 to exit: ")
        if (start == "1") or (start == "2") or (start == "3"):
            if start == "1":
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
            elif start == "3":
              print("\nstopping program")
              loop = False
        else:
            print("\nInvalid response\n")


def game():
    menu_time = time.time()
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
    playing = True
    first = goesfirst(time.time() - start_time)
    if first == 1:

      while playing:
          pc = playerchoice(board)
          board[pc] = "o"
          printboard(board)
          if checkwin(board) != False:
              print(checkwin(board), "won")
              sleep(1)
              return
          sleep(.5)
          cc = cpuchoice(board)
          board[cc] = "x"
          printboard(board)
          if checkwin(board) != False:
              print(checkwin(board), "won")
              sleep(1)
              return
    else:

      while playing:
          sleep(.5)
          cc = cpuchoice(board)
          board[cc] = "x"
          printboard(board)
          if checkwin(board) != False:
              print(checkwin(board), "won")
              sleep(1)
              return
          pc = playerchoice(board)
          board[pc] = "o"
          printboard(board)
          if checkwin(board) != False:
              print(checkwin(board), "won")
              sleep(1)
              return

def playerchoice(testboard):

    available_squares = []
    # find empty squares
    for x in testboard:
        if testboard[x] == " ":
            available_squares.append(x)
    loop = True
    while loop:
      # convert user input to square number
        cipher = {
            1: 7,
            2: 8,
            3: 9,
            4: 4,
            5: 5,
            6: 6,
            7: 1,
            8: 2,
            9: 3,
        }
        choice = input("\nenter a square using your num pad: ")
        try:
            # if the input is convertable to an integer, and the square is empty, the function returns the square number back to the game function
            if cipher[int(choice)] in available_squares:
                loop = False

                return cipher[int(choice)]
            else:
                print("\ninvalid response")
        except:
          # runs if user input is not convertable to an integer
            print("\ninvalid response")


def cpuchoice(testboard):

    for x in testboard:

        fakeboard = testboard.copy()
        # fakeboard is a temporary copy of the main board that is used to check future
        # moves without editing the main board

        # this loop looks for one move wins by checkng every possible move and seeing if the move will win the game

        if testboard[x] == " ":
            fakeboard[x] = "x"
            result = checkwin(fakeboard)
            if result == "x":
                return x

    # if no easy wins were found, this code below will choose one at random

    available_squares = []

    for z in testboard:
        if testboard[z] == " ":
            available_squares.append(z)
    return random.choice(available_squares)


def goesfirst(p1):
  s = 1
  p1 = p1 * 1000
  p1 = int(p1)
  p2 = 5

  for i in range(p1):
    s += 1

  num = ((p1 * p2) * s)

  if num == 0:
    return 1
  else:
    return 2  


def checkwin(testboard):
  #checking if x won
    if (testboard[1] == "x") and (testboard[2] == "x") and (testboard[3]
                                                            == "x"):
        return "x"
    elif (testboard[4] == "x") and (testboard[5] == "x") and (testboard[6]
                                                              == "x"):
        return "x"
    elif (testboard[7] == "x") and (testboard[8] == "x") and (testboard[9]
                                                              == "x"):
        return "x"
    elif (testboard[1] == "x") and (testboard[5] == "x") and (testboard[9]
                                                              == "x"):
        return "x"
    elif (testboard[3] == "x") and (testboard[5] == "x") and (testboard[7]
                                                              == "x"):
        return "x"
    elif (testboard[1] == "x") and (testboard[4] == "x") and (testboard[7]
                                                              == "x"):
        return "x"
    elif (testboard[2] == "x") and (testboard[5] == "x") and (testboard[8]
                                                              == "x"):
        return "x"
    elif (testboard[3] == "x") and (testboard[6] == "x") and (testboard[9]
                                                              == "x"):
        return "x"

    # checking if o won
    elif (testboard[1] == "o") and (testboard[2] == "o") and (testboard[3]
                                                              == "o"):
        return "o"
    elif (testboard[4] == "o") and (testboard[5] == "o") and (testboard[6]
                                                              == "o"):
        return "o"
    elif (testboard[7] == "o") and (testboard[8] == "o") and (testboard[9]
                                                              == "o"):
        return "o"
    elif (testboard[1] == "o") and (testboard[5] == "o") and (testboard[9]
                                                              == "o"):
        return "o"
    elif (testboard[3] == "o") and (testboard[5] == "o") and (testboard[7]
                                                              == "o"):
        return "o"
    elif (testboard[1] == "o") and (testboard[4] == "o") and (testboard[7]
                                                              == "o"):
        return "o"
    elif (testboard[2] == "o") and (testboard[5] == "o") and (testboard[8]
                                                              == "o"):
        return "o"
    elif (testboard[3] == "o") and (testboard[6] == "o") and (testboard[9]
                                                              == "o"):
        return "o"
      
    else:
      #draw condition
      # if there's no more open squares, and the game isn't a win, it's a draw
      sum = 0
      for x in testboard:
        if testboard[x] != " ":
          sum += 1
      if sum == 9:
        return "Draw, nobody"
      else:
        return False


main()

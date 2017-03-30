#! /usr/bin/python3

# game of tic tac toe for the command line

gameboard = {"top-l": " ", "top-m": " ", "top-r": " ",
         "mid-l": " ", "mid-m": " ", "mid-r": " ", 
         "bot-l": " ", "bot-m": " ", "bot-r": " "}

def printToScreen(board):
    print(board["top-l"] + "|" + board["top-m"] + "|" + board["top-r"])
    print("-+-+-")
    print(board["mid-l"] + "|" + board["mid-m"] + "|" + board["mid-r"])
    print("-+-+-")
    print(board["bot-l"] + "|" + board["bot-m"] + "|" + board["bot-r"])

turn = "X"

for i in range(9):
    printToScreen(gameboard)
    print("Turn for " + turn + ". Pick your move")
    move = input()
    gameboard[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

printToScreen(gameboard)

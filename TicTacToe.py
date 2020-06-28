# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:22:36 2020

TIC-TAC-TOE!

@author: Etheking
"""

import random

theBoard = {
        "TOPL":" ",
        "TOPM":" ",
        "TOPR":" ",
        "MIDL":" ",
        "MIDM":" ",
        "MIDR":" ",
        "BOTL":" ",
        "BOTM":" ",
        "BOTR":" "
        }

playerLetter = "X"
AIletter = "O"
options = True

def playGame():
    print("********************************************************************")
    print()
    print("WELCOME TO ELI'S TIC-TAC-TOE, FRICKER!")
    print()
    showBoard()
    while options:
        makeMove()
        aiMove()
    if options is False:
        print("You ran out of options! The AI wins ties, sorry!")
        winCond("AI")
    

def showBoard():
    #used to print current version of playing board
    printLine = []
    for key in theBoard:
        printLine.append(theBoard[key])
        if "R" in key:
            print(" ".join(printLine))
            printLine = []
            if key != "BOTR":
                print("----------")
        else:
            printLine.append("|")
        
def aiMove():
    print()
    print("AI turn to move!")
    legalMoves = []
    for ele in theBoard:
        if theBoard[ele] == " ":
            legalMoves.append(ele)
    decision = random.choice(legalMoves)
    theBoard[decision] = "O"
    checkBoard()
    showBoard()
            
def makeMove():
    #used to take user input to make a player's move
    mistakeCounter = 0
    while True:
        move = input("Type an open location to move!: ").upper()
        if move in theBoard:
            if theBoard[move] == " ":
                theBoard[move] = playerLetter
                checkBoard()
                showBoard()
                break
        print("Invalid entry, try again!")
        mistakeCounter += 1
        if mistakeCounter >= 3:
            print("Legal moves are:")
            for ele in theBoard:
                if theBoard[ele] == " ":
                    print(ele)
                    
def winCond(player):
    showBoard()
    if player == "human":
        print("Congratulations, you win!")
    else:
        print("Sorry, the computer won!")
    for ele in theBoard:
        theBoard[ele] = " "
    print("")
    while True:
        restart = input("Play again? Y/N ").upper()
        if restart == "Y":
            playGame()
        elif restart == "N":
            break
        print("Incorrect input, try again.")
        print("")
        
                    
def checkBoard():
    global options
    XcheckList, OcheckList = [], []
    checkLists = [XcheckList, OcheckList]
    for key in theBoard:
        if theBoard[key] == "X":
            XcheckList.append(key)
        elif theBoard[key] == "O":
            OcheckList.append(key)
            
    def checkForWin(aList):
        possibleLines = ["TOP", "MID", "BOT", "L", "M", "R"]
       # print(possibleLines)
        diags = [["TOPL", "MIDM", "BOTR"],["TOPR", "MIDM", "BOTL"]]
        for line in possibleLines:
            rowCounter = 0
            #print("Checking through {} lines.".format(line))
            for ele in aList:
                if line in ele:
                    rowCounter += 1
                else:
                    rowCounter = 0
                if rowCounter >= 3:
               #     print("Match found at line {}".format (line))
                    return True
        for diLine in diags:
           # print("Checking diag line {}".format(diLine))
            if all(elem in aList for elem in diLine):
                return True
        return False
    
    for check in checkLists:
#        for ele in check:
#            print(ele)
        if checkForWin(check) is True:
            if check == XcheckList:
                winCond("human")
                break
            else:
                winCond("AI")
                break
        else:
#            print("Reseting checklist")
            check = []
    for ele in theBoard:
        if ele == " ":
            break
    options == False
                

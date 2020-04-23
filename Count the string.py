# tic tac toe game

import sys

# Global Variables
# Stores the game board
theBoard = {'topL': ' ', 'topM': ' ', 'topR': ' ', 'midL': ' ',
            'midM': ' ', 'midR': ' ', 'lowL': ' ', 'lowM': ' ', 'lowR': ' '}
ComputerGoesFirst = False  # Set to true if computer is to go first
UserChar = ''

#Determine Moves
UserInput = ''


welcome = " Hello, let's play tic tac toe! \n \
Would you like to be X's or O's?"

# generates the board


def printBoard(theBoard):
    print(theBoard['topL'] + '|' + theBoard['topM'] + '|' + theBoard['topR'])
    print('-----')
    print(theBoard['midL'] + '|' + theBoard['midM'] + '|' + theBoard['midR'])
    print('-----')
    print(theBoard['lowL'] + '|' + theBoard['lowM'] + '|' + theBoard['lowR'])

# Verify First Userinput


def UserVerification(UserSelectFirst):
    global UserVerificationCounter
    global ComputerGoesFirst
    global UserChar
    print("Userinputted " + UserSelectFirst)  # debug users input
    if (UserSelectFirst is 'X'):
        print("You've select X's, O's go first you noob.")
        ComputerGoesFirst = True
        UserChar = 'X'
    elif (UserSelectFirst is "O"):
        print("You've selected O's, all you do is win muthafucka! \nLet's gooooo, where you putting that sweet thang")
        UserChar = 'O'
    else:
        print("Did I stutter? Pick either X's or O's you spack.")
        UserSelectFirst = input()
        UserVerification(UserSelectFirst)

##
# Start
##
# Code to execute program
print(welcome)
UserSelectFirst = input()
UserVerification(UserSelectFirst)
# debug if True the computer goes first
print("Debug: Computer goes first? " + str(ComputerGoesFirst))


# Verify userinput and makes the first user move
def ValidInput(UserFirstMove):
    if (UserFirstMove in theBoard):
        global UserChar
        print("Debug: Input is Valid")
        theBoard[str(UserFirstMove)] = UserChar
        printBoard(theBoard)
    else:
        print("Come on now Peralta, that's not the game. You'll need to choose an option above...")
        ValidInput(input())

##
# First Move
##
# Makes the first pc move
if (ComputerGoesFirst == True):
    theBoard['topR'] = 'O'
    printBoard(theBoard)    
else:
    print("Your options are: topL, topM, topR, midL, midM, midR, lowL, lowM, lowR, fullR")
    UserFirstMove = input()
    if (UserFirstMove == 'fullR'):  # The fullretard test
        print("Never go full retard.")
        sys.exit()
    else:
        ValidInput(UserFirstMove)



#UserMove
def UserMove():
    global UserInput
    print("Your Move, what's it gonna be punk?")
    print("topL, topM, topR, midL, midM, midR, lowL, lowM, lowR")
    UserInput = input()
    validator(UserInput)
    
    #Now we need to check if there's already a move in that space!!!!!!
    
    print("this needs to go to descision tree")

#Validates all user moves   
def validator(i):
    if i in theBoard:
        print("Debug: Input is Valid")
               
    else:
        print("Please enter a valid position")
        Return = input()
        validator(Return)
            

    #if (i == "test"):
    #    print("validator working")


#ComputerMove
def ComputerMove():
    print("The computer will go next")

#Second move descision tree
if (ComputerGoesFirst == True):
    UserMove()
else:
    ComputerMove()






print("End of Program")

#
# 
# # Displays the game board
# printBoard(theBoard)
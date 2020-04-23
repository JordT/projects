# tic tac toe game

import sys

# Global Variables
# Stores the game board
theBoard = {'topL': ' ', 'topM': ' ', 'topR': ' ', 'midL': ' ',
            'midM': ' ', 'midR': ' ', 'lowL': ' ', 'lowM': ' ', 'lowR': ' '}
ComputerGoesFirst = False  # Set to true if computer is to go first
UserChar = ''

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
# Makes the first move
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


# Function needs to loop through best options, so it's gone top right, so bottom left first
#def ComputerMoveTwo():
#    if (ComputerGoesFirst == True) and (theBoard['topR'] == 'O'):
#        print("second move successful")

##
#Verify all user put - needs written
##


if (ComputerGoesFirst == True):
    print("Alright chump, you're up. Your options are: topL, topM, topR, midL, midM, midR, lowL, lowM, or lowR.")
    Move2 = Userinput

def FirstUserMove():
    



# defines first move if PC is to select
# def FirstMove(UserSelectFirst):
#    if (UserSelectFirst is 'X'):
#        #theBoard['topR'] = 'O'
#        print(theBoard)
#    else:
#        print('Debug')


# Displays the game board
# printBoard(theBoard)

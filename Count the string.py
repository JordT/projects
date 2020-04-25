# tic tac toe game

import sys

# Global Variables
# Stores the game board
theBoard = {'topL': ' ', 'topM': ' ', 'topR': ' ', 'midL': ' ',
            'midM': ' ', 'midR': ' ', 'lowL': ' ', 'lowM': ' ', 'lowR': ' '}
ComputerGoesFirst = False  # Set to true if computer is to go first
UserChar = ''
UserMoveHistory = []


#Determine Moves
FirstUserMove = ''
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
        global UserMoveHistory
        print("Debug: Input is Valid")
        UserMoveHistory.append(UserFirstMove)
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



#UserMove - Verifies a user can make a move, then executes it
def UserMove():
    global UserInput
    global UserChar
    print("Your move, what's it gonna be punk?")
    print("(topL, topM, topR, midL, midM, midR, lowL, lowM, lowR)")
    UserInput = input()
    validator(UserInput)
    if (theBoard[UserInput] == ' '):
        print("that's a valid move!")
        theBoard[UserInput] = UserChar
        printBoard(theBoard)
    else:
        print("Hmm, there's already a move in that space!")
        UserInput = input()
        validator(UserInput)
        theBoard[UserInput] = UserChar
        printBoard(theBoard)
        
    #Now we need to check if there's already a move in that space!!!!!!!!


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
    global UserInput
    global UserChar
    print("The computer will go next")
    print("The users move was " + UserFirstMove)
    #Check Horizontal Win Conditions
    






#Second move descision tree
if (ComputerGoesFirst == True):
    UserMove()
else:
    ComputerMove()


print(UserMoveHistory)
print("End of Program")

#
# 
# # Displays the game board
# printBoard(theBoard)
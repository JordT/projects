#tic Tac Toe Game

import sys

##
#Global Variables
##

UserChar = ''
CompChar = ''
UserIsNext = False
UserMoveHistory = []
PossibleMoves =['X', 'x', 'O', 'o']
WinCondition = False

##
# Stores the game board
##

theBoard = {'topL': ' ', 'topM': ' ', 'topR': ' ', 'midL': ' ',
            'midM': ' ', 'midR': ' ', 'lowL': ' ', 'lowM': ' ', 'lowR': ' '}

##
# Prints the current board state
##

def printBoard(theBoard):
    print(theBoard['topL'] + '|' + theBoard['topM'] + '|' + theBoard['topR'])
    print('-----')
    print(theBoard['midL'] + '|' + theBoard['midM'] + '|' + theBoard['midR'])
    print('-----')
    print(theBoard['lowL'] + '|' + theBoard['lowM'] + '|' + theBoard['lowR'])
    print()


##
#Verifies first user input
##

def FirstInputVer(FirstInput):
    if (FirstInput in PossibleMoves):
        global UserChar
        global CompChar
        global UserIsNext
        UserChar = FirstInput
        UserChar = UserChar.upper()
        print(UserChar)
        if (UserChar == 'X'):
            UserIsNext = False
            CompChar = 'O'
            print("O's go first:") 
        else: 
            UserIsNext = True
            CompChar = 'X'
            print("Alright alright alright, you're up first")
            pass
    else:       
        print("That's not a valid choice, you can either be X or O's.")
        FirstInput = input()
        FirstInputVer(FirstInput)


def computerLoseCheck():
    global UserIsNext
    global UserMoveHistory
    global CompChar
    if ('topL' in UserMoveHistory) or ('topM' in UserMoveHistory) or ('topR' in UserMoveHistory): #checks top Horizontal Win condition
        if ('topL' in UserMoveHistory) and ('topR' in UserMoveHistory):
            theBoard['topM'] = CompChar
            printBoard(theBoard)
        elif ('topM' in UserMoveHistory) and ('topR' in UserMoveHistory):
            theBoard['topL'] = CompChar
            printBoard(theBoard)
        elif ('topL' in UserMoveHistory) and ('topM' in UserMoveHistory):
            theBoard['topR'] = CompChar
            printBoard(theBoard)
    elif ('midL' in UserMoveHistory) or ('midM' in UserMoveHistory) or ('midR' in UserMoveHistory): #checks for mid horizontal win condition
        if ('midL' in UserMoveHistory) and ('midR' in UserMoveHistory): 
            theBoard['midM'] = CompChar
            printBoard(theBoard)
        elif ('midM' in UserMoveHistory) and ('midR' in UserMoveHistory):
            theBoard['midL'] = CompChar
            printBoard(theBoard)
        elif ('midL' in UserMoveHistory) and ('midM' in UserMoveHistory):
            theBoard['midR'] = CompChar
            printBoard(theBoard)
    elif ('lowL' in UserMoveHistory) or ('lowM' in UserMoveHistory) or ('lowR' in UserMoveHistory): #checks for bottom horizontal win condition
        if ('lowL' in UserMoveHistory) and ('lowR' in UserMoveHistory):    
            theBoard['midM'] = CompChar
            printBoard(theBoard)
        elif ('midM' in UserMoveHistory) and ('lowR' in UserMoveHistory):
            theBoard['lowL'] = CompChar
            printBoard(theBoard)
        elif ('lowL' in UserMoveHistory) and ('lowM' in UserMoveHistory):
            theBoard['lowR'] = CompChar
            printBoard(theBoard)
    elif ('topL' in UserMoveHistory) or ('midL' in UserMoveHistory) or ('lowL' in UserMoveHistory): #checks for left vertical win condition
        if ('topL' in UserMoveHistory) and ('midL' in UserMoveHistory):    
            theBoard['lowL'] = CompChar
            printBoard(theBoard)
        elif ('topL' in UserMoveHistory) and ('lowL' in UserMoveHistory):
            theBoard['midL'] = CompChar
            printBoard(theBoard)
        elif ('midL' in UserMoveHistory) and ('lowL' in UserMoveHistory):
            theBoard['topL'] = CompChar
            printBoard(theBoard)
    elif ('topM' in UserMoveHistory) or ('midM' in UserMoveHistory) or ('lowM' in UserMoveHistory): #checks for mid vertical win condition
        if ('topM' in UserMoveHistory) and ('midM' in UserMoveHistory):    
            theBoard['lowM'] = CompChar
            printBoard(theBoard)
        elif ('topM' in UserMoveHistory) and ('lowM' in UserMoveHistory):
            theBoard['midM'] = CompChar
            printBoard(theBoard)
        elif ('midM' in UserMoveHistory) and ('lowL' in UserMoveHistory):
            theBoard['topM'] = CompChar
            printBoard(theBoard)
    elif ('topR' in UserMoveHistory) or ('midR' in UserMoveHistory) or ('lowR' in UserMoveHistory): #checks for right vertical win condition
        if ('topR' in UserMoveHistory) and ('midR' in UserMoveHistory):    
            theBoard['lowR'] = CompChar
            printBoard(theBoard)
        elif ('topR' in UserMoveHistory) and ('lowR' in UserMoveHistory):
            theBoard['midR'] = CompChar
            printBoard(theBoard)
        elif ('midR' in UserMoveHistory) and ('lowR' in UserMoveHistory):
            theBoard['topR'] = CompChar
            printBoard(theBoard)
    elif ('topR' in UserMoveHistory) or ('topL' in UserMoveHistory) or ('lowR' in UserMoveHistory) or ('lowL' in UserMoveHistory): #checks for diag win condition
        if ('topR' in UserMoveHistory) and ('lowL' in UserMoveHistory):    
            theBoard['midM'] = CompChar
            printBoard(theBoard)
        elif ('topL' in UserMoveHistory) and ('lowR' in UserMoveHistory):
            theBoard['midM'] = CompChar
            printBoard(theBoard)   
    

    


                                      

def UserMove():
    global UserChar
    global UserIsNext
    global UserMoveHistory
    print("It's your turn, what's your move?")
    print("Potential Moves are: topL, topM, topR, midL, midM, midR, lowL, lowM, LowR")
    UserInput = input()
    if UserInput in theBoard:             ### Checks the Userinput is a valid move ###
        print("UserMove is valid")
        if (theBoard[UserInput] == ' '):
            theBoard[UserInput] = UserChar
            UserIsNext = False
            printBoard(theBoard)
            UserMoveHistory.append(UserInput)
        else:
            print("Whoops, there's already a move there. Enter anther position")
            UserMove()
    else:
        print("You'll need to enter a Valid move")
        UserMove()





##
# Code Running Order
##

print("Welcome to Tic Tac Toe, will you play as 'X's or 'O's?")
FirstInput = input()
FirstInputVer(FirstInput) #Verifies input and assigns user/comp char

##
# Determines who plays next
##

while (WinCondition == False):
    if (UserIsNext == True):
        print("Calls UserMove")
        UserMove()
    else:
        computerLoseCheck()
        theBoard['topR'] = CompChar
        print("We're not checking win condition")    ### No blocking move required ###          
        printBoard(theBoard)
        UserIsNext = True



"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numX = 0
    numO = 0
    for row in board:
        numX += row.count("X")
        numO += row.count("O")
    if numX == numO:  # Since X starts first, if number of Xs and Os are equal, it is X's turn
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionSet = set()
    for i, row in enumerate(board):  # enumerate is used to track item and index
        for j, item in enumerate(row):
            if item is None:
                actionSet.add((i, j))
    return actionSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    validActions = actions(board)
    if action not in validActions:  # check if action is valid
        raise ValueError
    play = player(board)  # returns either "X" or "O"
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = play  # Rewrite action into newBoard
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    "X" or "O" if X or O wins, None if no winners(yet)
    """
    for row in board:
        mySet = set(row)
        if len(mySet) == 1:
            if "X" in mySet:  # if any row contains only X, X wins
                return "X"
            elif "O" in mySet:  # if any row contains only O, O wins
                return "O"

    for column in range(3):
        mySet = set()
        for row in board:
            mySet.add(row[column])
        if len(mySet) == 1:
            if "X" in mySet:  # if any column contains only X, X wins
                return "X"
            elif "O" in mySet:  # if any column contains only O, O wins
                return "O"
            
        if board[0][0] == board[1][1] == board[2][2] == "X" or board[0][2] == board[1][1] == board[2][0] == "X":  # if diagonal line contains only X, X wins
            return "X"
        if board[0][0] == board[1][1] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O":  # if diagonal line contains only X, X wins
            return "O"
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:  # if there is a winner, the game ends
        return True
    elif winner(board) is None:  # if there is no winner, check if there are still empty cells
        for row in board:
            if EMPTY in row:  # if there are empty cells, the game is still in progress
                return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):  # if the board is a terminal state, return the score
        return None
    
    Maxplayer = player(board)
    if Maxplayer == "O":
        Value, move = MinValue(board)
    else:
        Value, move = MaxValue(board)
    print(f'The AI ({Maxplayer}) made move {move}')
    return move
        

def MaxValue(board):
    if terminal(board):
        return utility(board), None
    
    v = -math.inf  # start with -infinity so that any value would be bigger than this
    for action in actions(board):
        returnedVal, move = MinValue(result(board, action))
        if returnedVal > v:
            v = returnedVal
            best_move = action
    return v, best_move


def MinValue(board):
    if terminal(board):
        return utility(board), None
    
    v = math.inf  # start with +infinity so that any value would be smaller than this
    for action in actions(board):
        returnedVal, move = MaxValue(result(board, action))
        if returnedVal < v:
            v = returnedVal
            best_move = action
    return v, best_move
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
    x = 0
    o = 0
    for i in board:
        for j in i:
            if j == X:
                x+=1
            elif j ==O:
                o+=1
    if x < o :
        return X
    elif o < x :
        return O
    else:
        return X     
    raise NotImplementedError


def actions(board):
    set1 = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                set1.add((i,j))
    
    return set1        
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_move = player(board)
    newboard = copy.deepcopy(board)
    
    i = action[0]
    j = action[1]
    if board[i][j] != EMPTY:
        raise ValueError("Invalid move")
    newboard[i][j] = player_move
    return newboard
    raise NotImplementedError


def winner(board):
    
    #Returns the winner of the game, if there is one. 
    for i in board:
        if i[0] == i[1] == i[2] != EMPTY:
            return i[0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None    
    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        if winner(board) == O:
            return -1
        if winner(board) == None:
            return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        optimal_move = ()
        if terminal(board) == True:
            return utility(board) , optimal_move
        else:
            v = -math.inf
            for action in actions(board):
                x = min_value(result(board, action))[0]
                if x > v:
                    v = x
                    optimal_move = action
                 
            return v , optimal_move
    def min_value(board):
        optimal_move = ()
        if terminal(board) == True:
            return utility(board) , optimal_move
        else:
            v = math.inf
        
            for action in actions(board):
                x =  max_value(result(board, action))[0]
                if x < v:
                    v = x
                    optimal_move = action
            return v , optimal_move
        
    
    if terminal(board):
        return None
    if player(board) == X:
        return max_value(board)[1]
    else :
        return min_value(board)[1]
    
    
    
    
    raise NotImplementedError

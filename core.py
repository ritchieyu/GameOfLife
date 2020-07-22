import copy

board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]  # Initialize board


def checkneighbours(temp, i, j, state):  # Checks all surrounding cells
    counter = 0
    for y, x in [(i, j), (i+1, j), (i+2, j), (i, j+1), (i+2, j+1), (i, j+2), (i+1, j+2), (i+2, j+2)]:
        counter += temp[y][x]
    if (state == 1 and counter == 2) or counter == 3:
        return 1  
    else:
        return 0
        
            
def gameoflife(board):
        
    m = len(board)  # rows 
    n = len(board[0])  # columns 
        
    temp = copy.deepcopy(board)
        
    for i in range(m):
        temp[i].insert(n+1, 0); temp[i].insert(0, 0)

    temp.insert(0, [0]*(n+2)); temp.insert(m+1, [0]*(n+2))  # Create edge cushion that accounts for edge cases
       
    for i in range(m):
        for j in range(n):
            state = board[i][j]
            board[i][j] = checkneighbours(temp, i, j, state)  
                
    return board


print(gameoflife(board))

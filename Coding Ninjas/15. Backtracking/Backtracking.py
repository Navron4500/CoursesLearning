def croped(row,col,val ,n,board):
    
    # HORIZONTAL CHECKK
    col_check = board[row]
    if col_check.count(val) > 0:
        return False
    
    #VERTICAL CHECK
    row_check = [board[i][col] for i in range(n)]
    if row_check.count(val) > 0:
        return False

    # REGION CHECK
    smallRow, smallCol  = row%3, col%3
    
    if smallRow == 0:
        quadRow = board[row+1:row+3]
    elif smallRow == 1:
        quadRow = [board[row-1]] + [board[row+1]]
    elif smallRow == 2:
        quadRow = board[row-2:row]


    quadCol = []
    if smallCol == 0:
        ip1 = quadRow[0][col:col+3]
        ip2 =  quadRow[1][col:col+3]
    
    elif smallCol == 1:
        ip1 = [quadRow[0][col-1], quadRow[0][col+1]]
        ip2 = [quadRow[1][col-1], quadRow[1][col+1]]

    elif smallCol == 2:
        ip1 = [quadRow[0][col-2:col]]
        ip2 = [quadRow[1][col-2:col]]

    quadCol.append(ip1)
    quadCol.append(ip2)

    for ele in quadCol:
        if val in ele:
            return False


    return True


def SudokuSolver(row,col,n,board):
    if row >= n or col >= n:
        return 

    if row == n-1 and col == n-1: #FINAL ENDING
        for b in board:
            print(*b)
        print()
        return 

    # SOMETHING IS PRESENT
    if board[row][col] != 0:
        if col<n-1:
            SudokuSolver(row,col+1,n,board)
        else:
            SudokuSolver(row+1, 0, n, board)
    
    else:
        for i in range(1,10):
            if croped(row,col,i,n,board):
                board[row][col] = i
                if col<n-1:
                    SudokuSolver(row, col+1, n, board)
                else:
                    SudokuSolver(row+1, 0, n, board)
                board[row][col] = 0





board=[[2,0,0, 0,0,0, 0,6,0],
       [0,0,0, 0,7,5, 0,3,0],
       [0,4,8, 0,9,0, 1,0,0],

       [0,0,0, 3,0,0, 0,0,0],
       [3,0,0, 0,1,0, 0,0,9],
       [0,0,0, 0,0,8, 0,0,0],

       [0,0,1, 0,2,0, 5,7,0],
       [0,8,0, 7,3,0, 0,0,0],
       [0,9,0, 0,0,0, 0,0,4]]

board1=[[0,0,0, 1,0,0,   2,6,0],
       [ 1,0,0,  0,7,5,  0,3,0],
       [ 2,4,8,  0,9,0,  1,0,0],

       [3,0,0, 4,0,0, 5,0,0],
       [4,0,0, 0,1,0, 0,0,9],
       [5,0,0, 0,0,8, 0,0,0],

       [0,0,1, 7,2,0, 8,7,0],
       [7,8,0, 7,3,0, 0,0,0],
       [8,9,0, 0,0,0, 0,0,4]]

li = [[0, 0, 4, 7, 1, 0, 0, 0, 0], 
    [0, 7, 2, 8, 0, 6, 5, 0, 0], 
    [0, 0, 0, 0, 0, 5, 0, 0, 7], 
    [0, 1, 0, 6, 9, 0, 2, 0, 0], 
    [3, 9, 0, 0, 5, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 8, 5], 
    [0, 0, 1, 2, 3, 0, 8, 0, 4], 
    [0, 0, 3, 5, 0, 4, 0, 0, 2], 
    [2, 4, 0, 9, 0, 0, 0, 0, 0]
    ]


(SudokuSolver(0,0,9,li))
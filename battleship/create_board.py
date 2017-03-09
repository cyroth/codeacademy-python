#prints a 5 x 5 grid
board = []
for grid in range(5):
    grid = ["O"] *5
    board.append(grid)
def print_board(board):
    for row in board:
        print " ".join(row)
print_board(board)

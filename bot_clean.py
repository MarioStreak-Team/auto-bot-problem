#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):

    # Scan the board to find the next dirty cell
    next_dirty_cell = None
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'd':
                next_dirty_cell = (i, j)
                break
        if next_dirty_cell:
            break

    if next_dirty_cell is None:
        # No more dirty cells - stop
        print("CLEAN")
        return

    # Calculate the direction to move based on current and next cell
    dir_map = {
        (0, -1): "LEFT",
        (0, 1): "RIGHT",
        (-1, 0): "UP",
        (1, 0): "DOWN",
        (0, 0): "CLEAN"
    }
    position = (0, 0)
    if abs(next_dirty_cell[0] - posr) > 1:
        position = (1 if next_dirty_cell[0] - posr > 0 else -1, 0)
    if abs(next_dirty_cell[1] - posc) > 1:
        position = ((0, 1 if next_dirty_cell[1] - posc > 0 else -1))
    else:
        if abs(next_dirty_cell[1] - posc) == 1 and abs(next_dirty_cell[0] - posr) == 1:
            position = ((0, 1 if next_dirty_cell[1] - posr > 0 else -1))
        else:
            position = (next_dirty_cell[0] - posr, next_dirty_cell[1] - posc)
    next_dir = dir_map.get(position)
    print(next_dir)
# Tail starts here


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)

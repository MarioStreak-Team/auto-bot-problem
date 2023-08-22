def next_move(posr, posc, board):
    nearest_dirty = None
    min_distance = float('inf')

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 'd':
                distance = abs(posr - i) + abs(posc - j)
                if distance < min_distance:
                    min_distance = distance
                    nearest_dirty = (i, j)

    if nearest_dirty[1] < posc:
        print("LEFT")
    elif nearest_dirty[1] > posc:
        print("RIGHT")
    elif nearest_dirty[0] < posr:
        print("UP")
    elif nearest_dirty[0] > posr:
        print("DOWN")
    else:
        print("CLEAN")

posr, posc = map(int, input().split())
board = [input() for _ in range(5)]

next_move(posr, posc, board)

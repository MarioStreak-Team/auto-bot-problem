def nextMove(n, r, c, grid):
    bpos = (r, c)
    ppos = None
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                ppos = (i, j)
                break
    
    rd = ppos[0] - bpos[0]
    cd = ppos[1] - bpos[1]

    if rd > 0:
        return "DOWN"
    elif rd < 0:
        return "UP"
    elif cd > 0:
        return "RIGHT"
    elif cd < 0:
        return "LEFT"

n = int(input())
r, c = map(int, input().split())
grid = [input() for _ in range(n)]


move = nextMove(n, r, c, grid)
print(move)

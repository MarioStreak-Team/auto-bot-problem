def displayPathtoPrincess(N, grid):
    # Find the coordinates of the bot and the princess
    bot_position = None
    princess_position = None
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'm':
                bot_position = (i, j)
            elif grid[i][j] == 'p':
                princess_position = (i, j)

    # Determine the moves required to rescue the princess
    x_diff = princess_position[0] - bot_position[0]
    y_diff = princess_position[1] - bot_position[1]

    x_moves = "UP\n" * abs(x_diff) if x_diff < 0 else "DOWN\n" * abs(x_diff)
    y_moves = "LEFT\n" * abs(y_diff) if y_diff < 0 else "RIGHT\n" * abs(y_diff)

    # Print moves
    print(x_moves + y_moves)


# Read the input size of grid
N = int(input())

# Read the grid
grid = []
for _ in range(N):
    grid.append(list(input().strip()))
# Call the function to display path to princess
displayPathtoPrincess(N, grid)

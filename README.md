# Bot saves princess
Princess Peach is trapped in one of the four corners of a square grid. You are in the center of the grid and can move one step at a time in any of the four directions. Can you rescue the princess?

### Input format

- The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. This is followed by an NxN grid. Each cell is denoted by '-' (ascii value: 45). The bot position is denoted by 'm' and the princess position is denoted by 'p'.

- Grid is indexed using **Matrix Convention**

### Output format

- Print out the moves you will take to rescue the princess in one go. The moves must be separated by '\n', a newline. The valid moves are LEFT or RIGHT or UP or DOWN.

# BotClean

The goal of Artificial Intelligence is to create a rational agent (Artificial Intelligence 1.1.4). An agent gets input from the environment through sensors and acts on the environment with actuators. In this challenge, you will program a simple bot to perform the correct actions based on environmental input.

Meet the bot **MarkZoid**. It's a cleaning bot whose sensor is a head mounted camera and whose actuators are the wheels beneath it. It's used to clean the floor.

The bot here is positioned at the top left corner of a 5*5 grid. Your task is to move the bot to clean all the dirty cells.

### Input Format

- The first line contains two space separated integers which indicate the current position of the bot.
- The board is indexed using Matrix Convention
- 5 lines follow representing the grid. Each cell in the grid is represented by any of the following 3 characters: 'b' (ascii value 98) indicates the bot's current position, 'd' (ascii value 100) indicates a dirty cell and '-' (ascii value 45) indicates a clean cell in the grid.

Note If the bot is on a dirty cell, the cell will still have 'd' on it.

### Output Format

The output is the action that is taken by the bot in the current step, and it can be either one of the movements in 4 directions or cleaning up the cell in which it is currently located. The valid output strings are LEFT, RIGHT, UP and DOWN or CLEAN. If the bot ever reaches a dirty cell, output CLEAN to clean the dirty cell. Repeat this process until all the cells on the grid are cleaned.

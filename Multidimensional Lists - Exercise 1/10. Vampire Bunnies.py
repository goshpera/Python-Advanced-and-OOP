def find_player_pos():
    for row in range(rows):
        if "P" in matrix[row]:
            return matrix[row].index("P")


def check_valid_idx(row, col, player=False):
    global wins

    if 0 <= row < rows and 0 <= col < cols:
        return True
    if player:
        wins = True


rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]

commands = input()

wins = False
directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

player_row, player_col = find_player_pos()
matrix[player_row][player_col] = "."

for command in commands:
    player_movement_row, player_movement_col = player_row + directions[command][0], player_col + directions[command][1]

    if check_valid_idx(player_movement_row, player_movement_col, True):
        player_row, player_col = player_movement_row, player_movement_col

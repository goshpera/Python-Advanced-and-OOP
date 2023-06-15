def move(direction, steps):
    r = my_pos[0] + (directions[direction][0] * steps)  # find the row and col and add
    c = my_pos[1] + (directions[direction][1] * steps)  # direction * steps

    if not (0 <= r < size and 0 <= c < size):  # check if position is valid
        return my_pos  # if not, return previous positions
    if field[r][c] == "x":  # check if the position has a target on it
        return my_pos  # if it has, return previous position

    return [r, c]  # return new position


def shoot(direction):
    r = my_pos[0] + directions[direction][0]  # finds the row and col when we
    c = my_pos[1] + directions[direction][1]  # add the position coords with our current ones

    while 0 <= r < size and 0 <= c < size:  # while the coordinates are valid
        if field[r][c] == "x":  # check if the bullet has hit the target
            field[r][c] = "."
            return [r, c]  # returns the positions of the hit target

        r += directions[direction][0]
        c += directions[direction][1]


size = 5
field = []

targets = 0
targets_hit = 0
targets_hit_positions = []

my_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    field.append(input().split())  # creating the matrix

    if "A" in field[row]:  # then we check where is our position in the matrix
        my_pos = [row, field[row].index("A")]  # we save our position

    targets += field[row].count("x")  # we check for targets in each row and add their count value


for _ in range(int(input())):  # lines of commands to be entered
    command_info = input().split()

    if command_info[0] == "move":
        my_pos = move(command_info[1], int(command_info[2]))
    elif command_info[0] == "shoot":
        target_down_pos = shoot(command_info[1])

        if target_down_pos:
            targets_hit_positions.append(target_down_pos)
            targets_hit += 1

        if targets_hit == targets:
            print(f"Training completed! All {targets} targets hit.")
            break

if targets_hit < targets:
    print(f"Training not completed! {targets - targets_hit} targets left.")

print(*targets_hit_positions, sep="\n")

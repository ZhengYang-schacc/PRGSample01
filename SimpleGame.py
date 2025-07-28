#--------------------------------------------------------------------------
# This function prints the map in a grid format.
# Parameters:
# num_rows: Number of rows in the map.
# num_columns: Number of columns in the map.
# map: The map itself, represented as a 2D list.

# Functionality:
# The function first prints the top border of the map.
# Then, it iterates through each row and prints the contents of each cell, separated by vertical bars (|).
# After printing the contents of a row, it prints the bottom border for that row.
def print_map(num_rows,num_columns,map):
    # Print the top line
    for column in range(num_columns):
        print("+---", end = '')
    print("+")

    for row in range(num_rows):
        for column in map[row]:
            print("| {} ".format(column), end = '')
        print("|")

        for column in range(num_columns):
            print("+---", end = '')
        print("+")
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
# This function finds the position of 'T' in the map.
# Parameters:
# map: The map, a 2D list.

# Functionality:
# It iterates through each cell in the map to find the position of 'T'.
# Once 'T' is found, it breaks out of the loop and returns the position as a list [row, col].
def get_position(map):
    found = False
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'T':
                row = i
                col = j
                found = True
                break
        if found: break
    position = [row,col]
    return position
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
# This function moves 'T' in the specified direction.
# Parameters:
# map: The map, a 2D list.
# direction: The direction to move ('W' for up, 'S' for down, 'A' for left, 'D' for right).

# Functionality:
# It gets the current position of 'T' using the get_position function.
# It checks if moving in the specified direction would go out of bounds and prints an error message if so.
# If the move is valid, it updates the map by moving 'T' to the new position and setting the old position to a space ' '.
def move(map, direction):
    position = get_position(map)
    row = position[0]
    col = position[1]
    if row == 0 and direction == 'W':
        print('Sorry, you are not allowed to move up')
    elif row == len(map)-1 and direction == 'S':
        print('Sorry, you are not allowed to move down')
    elif col == 0 and direction == 'A':
        print('Sorry, you are not allowed to move left')
    elif col == len(map[0])-1 and direction == 'D':
        print('Sorry, you are not allowed to move right')
    else:
        if direction == 'W':
            map[row-1][col] = map[row][col]
        elif direction == 'S':
            map[row+1][col] = map[row][col]
        elif direction == 'A':
            map[row][col-1] = map[row][col]
        elif direction == 'D':
            map[row][col+1] = map[row][col]
        map[row][col] = ' '

#--------------------------------------------------------------------------

# map is initialized as a 4x5 grid with 'T' starting at position [0][1].
map = [ [' ', 'T', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
      ]

# num_rows and num_columns store the dimensions of the map.
num_rows = len(map)
num_columns = len(map[0])    

# The initial map is printed using the print_map function.
print_map(num_rows,num_columns,map)

#Main Loop:
# The loop prompts the user to enter a direction or 'Q' to quit.
# If 'Q' is entered, the loop breaks and the program ends.
# Otherwise, it moves 'T' in the specified direction using the move function and then prints the updated map.
while True:
    direction = input('Enter your direction or Q to quit: ').upper()
    if direction == 'Q': break
    move(map, direction)
    print_map(num_rows,num_columns,map)
print('Bye-bye!')
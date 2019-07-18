"""
some functions designed to make using
2D arrays (of chars) easier to manipulate
as if they were a coordinate plane
"""

#TODO: look over some of these functions to make sure they can exploit how python works with lists

#maybe, instead of a normal list object, we could make a new object that contians a list and has all of these functions as methods

# import only system from os (for clear function)
from os import system, name

#function to clear the screen
def clear(): 

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

#returns a fresh grid
def create_grid(xl, yl, initchar = " "):

    grid = []

    #builds grid
    for i in range(0, yl):
        grid.append([])
    for i in range(0, yl):
        for j in range(0, xl):
            grid[i].append(initchar)

    return grid

# how about a create_grid_from_file function?

#prints the grid to the screen
def print_grid(grid, should_clear = True):

    #clears the screen so that things dont keep getting printed w/o being erased
    if should_clear == True: clear()

    for i in range(0, len(grid)):
        grid_line_str = "".join(grid[i])
        print(grid_line_str)


#changes an individual character in the given grid and returns the new grid
def setchar(x, y, grid, new_char):

    changed_grid = grid
    changed_grid[y][x] = new_char
    return changed_grid

# this function draws a "line" in your array with x and y being the origin of the line
# it must be either straight up, down, left or right
def draw_line(grid, x, y, direction, length, new_char):
    if direction == "up":
        for i in range(length):
            try:
                change_char(x, y - i, grid, new_char)
            except:
                pass
    elif direction == "down":
        for i in range(length):
            try:
                change_char(x, y + i, grid, new_char)
            except:
                pass
    elif direction == "left":
        for i in range(length):
            try:
                change_char(x - i, y, grid, new_char)
            except:
                pass
    elif direction == "right":
        for i in range(length):
            try:
                change_char(x + i, y, grid, new_char)
            except:
                pass
    else:
        pass

#modifies a rectangle in a grid to be one char, has option to just do outline but defaults to doing whole rectangle
#def change_rect_by_char(x, y, xl, yl, grid, char, just_outline = False):

#modifies a rectangle in a grid to be replaced by a smaller grid
#def change_rect_by_grid(x, y, grid, smaller_grid):

#returns the character stored in grid at x, y
def getchar(grid, x, y):

    return grid[y][x]

#creates a smaller grid from a larger one
def grid_chunk(old_grid, x, y, xl, yl):

    new_grid = create_grid(xl, yl)

    #builds new grid
    for i in range(0, yl):
        for j in range(0, xl):
            new_grid = change_char(j, i, new_grid, getchar(j + x, i + y, old_grid))

    return new_grid

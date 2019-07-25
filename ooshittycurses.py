"""
a revision of the original shittycurses module to be more elegant
using the power of OOP
"""

# for clear() function
from os import system, name

# the object with all of the important methods
class Grid:

    # init
    def __init__(self):
        self.array = []
    
    # prints out the grid on the terminal/shell
    def print(self, should_clear = True):
        if should_clear == True: clear()
        for i in range(0, len(self.array)):
            grid_line_str = "".join(self.array[i])
            print(grid_line_str)
    
    # simply returns whatever character is at (x, y)
    def get_char(self, x, y):
        return self.array[y][x]

    # changes a single character in the array
    def set_char(self, x, y, new_char):
        self.array[y][x] = new_char

    # draws a line in the array, changing multiple characters
    def draw_line(self, x, y, direction, length, new_char):

        if direction == "up":
            for i in range(length):
                try:
                    self.set_char(x, y - i, new_char)
                except:
                    pass
        elif direction == "down":
            for i in range(length):
                try:
                    self.set_char(x, y + i, new_char)
                except:
                    pass
        elif direction == "left":
            for i in range(length):
                try:
                    self.set_char(x - i, y, new_char)
                except:
                    pass
        elif direction == "right":
            for i in range(length):
                try:
                    self.set_char(x + i, y, new_char)
                except:
                    pass
        else:
            pass

    # may add grid_chunk() function some time if it is needed

# class for grids not created by files
class nGrid:

    # init
    def __init__(self, xl, yl, initchar = ' '):

        self.grid = Grid()

        #builds grid
        for i in range(0, yl):
            self.grid.array.append([])
        for i in range(0, yl):
            for j in range(0, xl):
                self.grid.array[i].append(initchar)

# class for grids created from files
class fGrid:

    # init
    def __init__(self, filename, ignore_newlines = True):
        
        self.grid = []
        can_proceed = True

        try:
            file = open(filename, 'r')
        except:
            can_proceed = False
        
        if can_proceed:
            filelines = file.readlines()
            for line in filelines:
                row = []
                for char in line:
                    if char == '\n' and ignore_newlines == True: pass
                    else: row.append(row)
                self.grid.append(row)

#function to clear the terminal/shell screen
def clear(): 

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


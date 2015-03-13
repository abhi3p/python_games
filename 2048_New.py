"""
Clone of 2048 game.
"""

import poc_2048_gui  
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code   
    merge_line = [0]*len(line)
    last_number = 0
    merge_flag = False
    
    for idx in range(len(line)):
        
        if (line[idx] != 0):
            if ( line[idx] == last_number) and merge_flag == False:
                index = merge_line.index(0)
                if (index == 0):
                    merge_line[index-1] = 2*last_number
                else:
                    merge_line[index-1] = 2*last_number
                    
                last_number = line[idx]
                merge_flag = True
            else:
                index = merge_line.index(0)
                merge_line[index] = line[idx]
                
                last_number = line[idx]
                merge_flag = False
                
    return merge_line         

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.grid = self.reset()
        
        self.initial_tile_indices_dic = {UP: list(tuple([0, index]) for index in range(self.grid_width)), 
                   DOWN: list(tuple([self.grid_height-1, index]) for index in range(self.grid_width)), 
                   LEFT: list(tuple([index, 0]) for index in range(self.grid_height)), 
                   RIGHT: list(tuple([index, self.grid_width-1]) for index in range(self.grid_height)) }
                   
       # print self.indices
        
    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """       
        self.grid = [[0]*self.grid_width for _ in range(self.grid_height)]
        return self.grid
        
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid_index = []
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                grid_index.append(str(row) + str(col))
        return str(grid_index)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        initial_tile_indices = self.initial_tile_indices_dic[direction]
        offset = OFFSETS[direction]
        
        temp_list = []
        tiles_moved = False
        for indices in initial_tile_indices:
            row = indices[0]
            col = indices[1]
            temp_list = []
            temp_indices = []
            
            while (0 <= row < self.grid_height and 0 <= col < self.grid_width):
                #print "row", row, "Col", col
                temp_indices.append([row,col])
                temp_list.append(self.get_tile(row, col))
                row = row + offset[0]
                col = col + offset[1]
                
            merge_list = merge(temp_list)
            for idx in range(len(merge_list)):
                if (self.get_tile(temp_indices[idx][0],temp_indices[idx][1]) != merge_list[idx]):
                    tiles_moved = tiles_moved or True
                    
                self.set_tile(temp_indices[idx][0], temp_indices[idx][1], merge_list[idx])
         
               
        if (tiles_moved == True):
            self.new_tile()       
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        choice = [4, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        index_choice = []
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if self.get_tile(row, col) == 0:
                    index_choice.append([row, col])
                    
        random_index_choice = random.choice(index_choice)
        self.set_tile(random_index_choice[0], random_index_choice[1], random.choice(choice))
             
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self.grid[row][col] = value        

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """                
        return self.grid[row][col]
 
#my_class = TwentyFortyEight(4, 4)

#print my_class
#my_class.set_tile(3,1,100)
#temp = my_class.get_tile(3, 1)
#print temp

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

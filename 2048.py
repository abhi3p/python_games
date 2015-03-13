# 2048 game
# 

import simplegui
import random

# Global Variables
canvas_height = 300
canvas_width = 300
GRID_NO = 4

Horizontal_line = [0, 0]
Vertical_line = [0, 0] 
pos = [0, 0]
grid = [[" ", " ", " ", " "], [" ", " ", " ", " "],[" ", " ", " ", " "], [" ", " ", " ", " "]]

choice_row = range(0, GRID_NO)
choice_col = range(0, GRID_NO)
new = 0


def reset():
    global grid
    grid = [[" ", " "], [" ", " "]]
    
def get_value(x):
    if x == " ":
        return 0
    else:
        return int(x)
    
    
def str2num(x):
    for r in range(0,4):
        for c in range(0,4):
            if x[r][c] == " ":
                x[r][c] = 0
            else:
                x[r][c] = int(x[r][c])
    
    return x

def num2str(y):
    for r in range(0,4):
        for c in range(0,4):
            if y[r][c] == 0:
                y[r][c] = " "
            else:
                y[r][c] = str(y[r][c])
    
    return y    
        
    

# Handler to draw on canvas
def draw(canvas):
   global grid
   # Draw Grid Lines 
   count = 1
   while (count <= GRID_NO-1):
        canvas.draw_line([canvas_width//GRID_NO*count, 0], [canvas_width//GRID_NO*count, canvas_height], 1, "White" ) 
        canvas.draw_line([0, canvas_height//GRID_NO*count], [canvas_width, canvas_height//GRID_NO*count ], 1, "White")
        count += 1
        
   # Draw inside grids 
   for r in range(0, GRID_NO):
            for c in range(0, GRID_NO):
                    canvas.draw_text(grid[r][c], [c * canvas_width// GRID_NO + 50, r * canvas_height//GRID_NO + 50], 40, "Red" )
        
    
def generate():
    global grid
    row = random.choice(choice_row)
    col = random.choice(choice_col)
    
    print row, col
    
    #check in square in already taken
    if grid[row][col] == " ":
        grid[row][col] = "2"   
        
def keydown(key):
    global grid, GRID_NO
    row = random.choice(choice_row)
    col = random.choice(choice_col)
    
    #print row, col
    
    if key==simplegui.KEY_MAP["left"]:
       for r in range(0, GRID_NO):
            for c in range(0, GRID_NO-1):
                if (grid[r][c+1] != " "):
                    grid[r][c] = grid[r][c+1]
                    grid[r][c+1] = " "
                print r, c
                    
                #if not (c == 0):
                #    grid[r][c+1] = " "
                
        
       #if grid[row][col] == " ":
       #     grid[row][col] = "2"
                
       # for r in range(0, GRID_NO):
       #     for c in range(0, GRID_NO-1): 
       #         num_1 = get_value(grid[r][c])
       #         num_2 = get_value(grid[r][c+1])
       #         num_1 += num_2
       #         grid[r][c+1] = " "
            
       #     if not(num_1 == 0):
       #         grid[r][c] = str(num_1)   
            
       # if grid[row][col] == " ":   
       #     grid[row][col] = "2" 
            
    elif key==simplegui.KEY_MAP["right"]:
        grid[row][col] = "2" 
    elif key==simplegui.KEY_MAP["down"]:
        grid[row][col] = "2" 
    elif key==simplegui.KEY_MAP["up"]:
        grid[row][col] = "2" 
    
        
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("2048", canvas_height, canvas_width)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.add_button("generate", generate)
frame.add_button("Reset", reset)

# Start the frame animation
frame.start()


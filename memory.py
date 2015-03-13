# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global card_list, exposed, state, prev_index, prev_prev_index, counter
    card_list = range(8)
    card_list.extend(range(8))
    random.shuffle(card_list)    
    exposed = [0]*16
    state = 0 
    counter = 0 
    label.set_text('Turns = ' + str(counter))
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global card_list, exposed, state,  prev_index, prev_prev_index, counter
    position = [50, 100] 
    for index in range(16):
        if (index*position[0] < pos[0] < (index+1)*position[0]) and (0 < pos[1] < position[1]):
            if (state == 0):               
                if not(exposed[index]):	
                    exposed[index] = 1     
                    state = 1
                    prev_prev_index = index
                    prev_index = index
                    counter += 1
                    label.set_text('Turns = ' + str(counter))             
                    
            elif (state == 1):                  
                if not(exposed[index]):	
                    exposed[index] = 1   
                    state = 2   
                    prev_prev_index = prev_index
                    prev_index = index                    
            else:                
                if (card_list[prev_prev_index] != card_list[prev_index]):
                    exposed[prev_prev_index] = 0
                    exposed[prev_index] = 0
                    
                if not(exposed[index]):	
                    exposed[index] = 1
                    state = 1    
                    prev_prev_index = prev_index
                    prev_index = index   
                    counter += 1
                    label.set_text('Turns = ' + str(counter))
                
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global card_list
    text_point = [15, 60] 
    line_point1 = [0,0]
    line_point2 = [0,100]
    
    index = 0 
    for card in card_list:
        canvas.draw_text(str(card), text_point, 45, "White")
        text_point[0] += 50
        
        if (exposed[index] == 1):
            canvas.draw_polygon([(index*50,0), (index*50,100), ((index+1)*50,100), ((index+1)*50,0)], 1, "White")
        else:
            canvas.draw_polygon([(index*50,0), (index*50,100), ((index+1)*50,100), ((index+1)*50,0)], 1, "White","Green")
            
        line_point1[0] += 50
        line_point2[0] += 50        
        index += 1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric
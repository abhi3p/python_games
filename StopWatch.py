# template for "Stopwatch: The Game"


import simplegui
import random

# define global variables
time = 0 
width = 300
height = 300 
position_timer = [100, 150]
position_counter = [225, 50] 
status = False

counter_stop = 0 # counter for number of times stoped the watch
counter_stop_at_whole = 0 # counter for numbe of times stoped at whole number (1.0 ,2.0, 3.0)

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    #A:BC.D
    time = int(time)
    A = time//600       
    B = ((time/10)%60)//10
    C = ((time/10)%60)%10
    D = time%10
    
    time_str = str(A) + ':' + str(B) + str(C) + '.' + str(D)
    return time_str
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global status
    timer.start()
    status = True
    
    
def Stop():
    global counter_stop, counter_stop_at_whole, status
    timer.stop()
        
    if(status):
        counter_stop += 1
    else:
        counter_stop  = counter_stop    
        
    if (time % 10 == 0 and status):
        counter_stop_at_whole += 1
    else:
        counter_stop_at_whole = counter_stop_at_whole
    
    status = False # Set the status 
      
    
def Reset(): 
    global time, counter_stop, counter_stop_at_whole, status
    time = 0
    counter_stop = 0
    counter_stop_at_whole = 0 
    status = False
    

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
    

# define draw handler
def draw(canvas):
    global time, counter_stop, counter_stop_at_whole
    canvas.draw_text(format(time), position_timer, 50, "White")
    canvas.draw_text(str(counter_stop_at_whole) + "/" + str(counter_stop), position_counter, 25, "Red")

    
# create frame
frame = simplegui.create_frame("Stop Watch : The Game !!", width, height)
frame.set_draw_handler(draw)
frame.add_button("Start", Start, 100);
frame.add_button("Stop", Stop, 100);
frame.add_button("Reset", Reset, 100);

# register event handlers
timer = simplegui.create_timer(100, tick) 


# start frame
frame.start()



# Please remember to review the grading rubric

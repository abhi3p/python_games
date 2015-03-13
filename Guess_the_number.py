# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

# initialize global variables used in your code
secret_number = 0
min_range = 0
max_range = 100
no_of_guess = 0

# helper function to start and restart the game
def new_game():
    # remove this when you add your code    
    global secret_number, min_range, max_range, no_of_guess
    print "New Game!! Range is from 0 to", max_range
    
    secret_number = random.randrange(min_range,max_range)
        
    no_of_guess = int(math.ceil(math.log(max_range-min_range+1, 2)))
    print "Number of remaining guesses ",no_of_guess
    print "\n"


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global max_range
    max_range = 100
    new_game()    
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global max_range
    max_range = 1000    
    new_game()
        
def input_guess(guess):
    # main game logic goes here	
    global secret_number, no_of_guess
    
    guess_number = int(guess)
    print "Guess was", guess_number
        
    no_of_guess -= 1
    print "Number of remaining guesses",no_of_guess  
            
    if (guess_number > secret_number):
        print "Higher!! \n"
        if (no_of_guess == 0):
            print "You Lose !! \n"
            new_game()
        
    elif (guess_number < secret_number):        
        print "Lower!! \n"
        if (no_of_guess == 0):
            print "You Lose !! \n"
            new_game()
    else:
        print "Correct!! \n"
        new_game()
    
    
# create frame
frame = simplegui.create_frame("Guess the Number!!",200,200)

# register event handlers for control elements
frame.add_button("Range [0-100]", range100, 200)
frame.add_button("Range [0-1000]", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game and start frame
new_game()
frame.start()


# always remember to check your completed program against the grading rubric

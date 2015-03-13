# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
middle = False
outcome = ""
score = 0
result = ""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        ans = "Hand contains "	# return a string representation of a hand        
        for i in range(len(self.hand)):
            ans += (self.hand[i].get_suit() + self.hand[i].get_rank())
            ans += " "
        return ans  	# return a string representation of a hand

    def add_card(self, card):
        return self.hand.append(card)   # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0 
        count_aces = 0
        for cards in self.hand:
            rank = cards.get_rank()
            hand_value += VALUES[rank]
            if (rank == 'A'):
                count_aces += 1
                
        if (count_aces == 0):
            return hand_value
        else:
            if ( (hand_value + 10) <= 21 ):
                return (hand_value + 10)
            else:
                return hand_value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for cards in self.hand:
            cards.draw(canvas,pos)              
            pos[0] += 1.5*CARD_SIZE[0]
  
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck.append(card)

    def shuffle(self):
        # shuffle the deck 
        return random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        return self.deck.pop(-1)	# deal a card object from the deck
    
    def __str__(self):
       ans = "Deck contains "	# return a string representation of deck        
       for i in range(len(self.deck)):
           ans += (self.deck[i].get_suit() + self.deck[i].get_rank())
           ans += " "
       return ans  

#define event handlers for buttons
def deal():
    global outcome, in_play, score, result, middle  
    global my_deck, player_hand, dealer_hand
    
    outcome = "Hit or Stand ???" 
    result = ""
    
    if (middle):
        result = 'You Lose'
        outcome = 'New Deal ?'
        score -= 1  
        middle = False
    
    # Build new deck/ Restock the deck    
    my_deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
      
    # Shuffle Deck
    my_deck.shuffle()    
    
    # Create New Player Hand & Dealer Hand ( Two card to each hand) 
    for i in range(2):
        player_hand.add_card(my_deck.deal_card())
        dealer_hand.add_card(my_deck.deal_card())
        
           
    in_play = True

def hit():
    # replace with your code below 
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    global outcome, in_play, score, result, middle
    global my_deck, player_hand, dealer_hand
    
    # Add Extra card to player hand
    player_hand.add_card(my_deck.deal_card())   
    
    if (player_hand.get_value() > 21 ):
        result = 'You went Bust & Lose!!'
        outcome = 'New Deal ?'
        score -= 1
        in_play = False
                
    middle = True    
     
def stand():
    # replace with your code below
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    global outcome, in_play , result, score
    global my_deck, player_hand, dealer_hand
    
    if not(in_play):
        result = 'You went Bust !!'         
    else:
        while (dealer_hand.get_value() < 17):
            dealer_hand.add_card(my_deck.deal_card())
            
    if ( dealer_hand.get_value() > 21):   
        result = ' Dealer went bust & You Win !!'
        outcome = 'New Deal ?'
        score += 1            
    elif ( dealer_hand.get_value() >= player_hand.get_value()):
        result = ' You Lose'
        outcome = 'New Deal ?'
        score -= 1        
    else:
        result = 'You Win'
        outcome = 'New Deal ?'
        score += 1
        
    in_play = False    
 
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome, in_play , score, result
    global my_deck, player_hand, dealer_hand
    
    canvas.draw_text('BlackJack', [250, 50], 40, "Black")
    
    # Dealer part
    canvas.draw_text('Dealer', [50, 150], 30, 'White')
    dealer_hand.draw(canvas, [50, 160])    
    if (in_play):    
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50+CARD_BACK_CENTER[0], 160+CARD_BACK_CENTER[1]], CARD_BACK_SIZE )
    else:
        dealer_hand.draw(canvas, [50, 160])    
    
    # Player part
    canvas.draw_text('Player', [50, 350], 30, 'White')
    player_hand.draw(canvas, [50, 360])
        
    canvas.draw_text(outcome, [250, 350], 25, "White" )
    
    canvas.draw_text(result, [250, 150], 25, "White")
    
    canvas.draw_text('Score: '+str(score), [400, 500], 30, "Black" )
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
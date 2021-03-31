'''
BlackJack code. Milestone Project #2 for Complete Python Bootcamp From Zero to Hero by Perian-Data
udpdm1
'''

#Imports we will use in this program.
import random
from os import system, name

#GLOBAL variables for this program are defined here.

suits = ('Hearts','Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card():
    '''
    Class for attributes of a card in a deck.
    '''
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + " of " + self.suit


class Chips():
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0
        
    def __str__(self):
       return  f'{self.__class__.__name__} has total of {self.total} with bet of {self.bet}'

    def __repr__(self):
        return  f'{self.__class__.__name__} has total of {self.total} with bet of {self.bet}'
        


class Deck():
    '''
    Class for the attributes of a deck of cards
    '''
    
    def __init__(self):
        
        self.deck = []
        
        for suit in suits:
            for rank in ranks:
                #Create the Card Object
                self.deck.append(Card(suit,rank))
                
    def shuffle(self):
        
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
        

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: "+deck_comp
        

class Hand():
    '''
    Each player will have a hand of cards. This class will track the cards the player holds.
    '''
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        #card passed in
        #from Deck.deal() --> single Card(suit,rank)
        self.value += values[card.rank] #card.rank is used as key into values dictionary to find numerical value.

        #track aces
        if card.rank == "Ace":
            self.aces +=1
    
    def adjust_for_ace(self):
        
        # Ace is assumed to be 11 but if we're over 21 we consider value of 1
        # If total value > 21 and I still have an ace
        # than change ace value to 1
        # self.aces is using an integer as a bool.
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def take_bet(chips):
    
    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        
        except:
            print("Sorry, please provide an integer.")
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you do not have enough chips! You have {chips.total}')
            else:
                break


def hit(deck,hand):
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing # to control an upcoming while loop
    while True:
        x = input('Hit or Stand? Enter h or s ')
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0] == 's':
            print("Player Stands Dealer's Turn")
            playing=False
        else:
            print("Sorry, I did not understand that, please enter h or s" )
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('PLAYER WINS!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('PLAYER WINS! DEALER BUSTED!')
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()
    
def push(player,dealer):
    print('Dealer and player tie! PUSH')


while True:
    #Print an opening statement
    print("WELCOME TO BLACKJACK")

    #Create & shuffle deck
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())



    #Set up the player's chips
    player_chips = Chips()


    #Prompt the player for their bet
    take_bet(player_chips)

    #show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    while playing:

        #Prompt for player to hit or stand
        hit_or_stand(deck,player_hand)

        #Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)

        #If player's hand exceeds 21, run player_busts() and break out of loop.
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

        #If player hasn't busted, play dealer's hand until dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)

        #Show all cards
        show_all(player_hand,dealer_hand)
        #Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    print('\n Player total chips are at: {}'.format(player_chips.total))
    new_game = input("Would you like to play another hand y/n")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:

        print('Thank you for playing!')
        break


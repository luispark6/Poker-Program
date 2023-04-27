import random
import copy
class Poker:
#intializes the board and players
    def __init__(self, player_count):
        self.deck = {} #deck is in form of dictionary
        self.table_cards = [] #5 cards layed on the table
        self.player_count = player_count #amount of players playing
        self.player= {} #each players cards
        self.list = [] #list from 0-51. This is used for random generator
        for i in range(1,self.player_count+1):
            self.player[i] = [] #each player has a list that will contain two cards

        #indicator of the number of the card. Face cards represented as numbers
        card_num = 1 
        #indicator of what the suit is
        suit_indicator = 0
        for i in range(52):
            self.list.append(i)
            if suit_indicator== 0: suit = "Heart" #first 13 cards will be hearts
            if suit_indicator== 1: suit = "Diamond"#next 13 will be diamonds
            if suit_indicator== 2: suit = "Spade" #next 13 will be spades
            if suit_indicator== 3: suit = "Clove" # last 13 will be cloves
            if card_num ==1: self.deck[i] = ["Ace", suit]
            elif card_num ==11: self.deck[i] = ["Jack", suit]
            elif card_num ==12: self.deck[i] = ["Queen", suit]
            elif card_num ==13: self.deck[i] = ["King", suit]
            else: 
                self.deck[i] = [card_num, suit] #each indice of deck is a card/suit
            card_num=card_num+1 #accumulate card_num
            if card_num ==14: # goes on to the next suit and reset card number
                suit_indicator = suit_indicator+1 #update suit indicator for new suit
                card_num=1 #reset card number
        
#deals cards to players
    def deal_cards(self, no_deal):

        #no deal is gonna be the player not to deal out

        for i in range (1, self.player_count+1): #go through players and append 1st card
            if i != no_deal:
                ran_num = random.choice(self.list) #random generate a number from 0-51
                while ran_num == -1: #if the random number is -1, card not valid
                    ran_num = random.choice(self.list) #choose a random number until its valid
                self.list[ran_num] = -1 #set element ran_num to -1 to set invalid state
                self.player[i].append(self.deck[ran_num]) #append the card from deck to player
                self.deck.pop(ran_num) #pop ran_num key value because card already used

        #do it one more time so that each player has two cards
        for i in range (1, self.player_count+1):
            if i != no_deal:
                ran_num = random.choice(self.list)
                while ran_num == -1:
                    ran_num = random.choice(self.list)
                self.list[ran_num] = -1
                self.player[i].append(self.deck[ran_num])
                self.deck.pop(ran_num)
#deals three cards to table  
    def deal_flop(self):
        for i in range(3):
            ran_num = random.choice(self.list) #random generate a number from 0-51
            while ran_num == -1: #if the random number is -1, card not valid
                ran_num = random.choice(self.list) #choose a random number until its valid
            self.list[ran_num] = -1 #set element ran_num to -1 to set invalid state
            self.table_cards.append(self.deck[ran_num]) #append the card from deck to table
            self.deck.pop(ran_num) #pop ran_num key value because card already used
#deals one card to the table
    def deal_turn(self):
        ran_num = random.choice(self.list) #random generate a number from 0-51
        while ran_num == -1: #if the random number is -1, card not valid
            ran_num = random.choice(self.list) #choose a random number until its valid
        self.list[ran_num] = -1 #set element ran_num to -1 to set invalid state
        self.table_cards.append(self.deck[ran_num]) #append the card from deck to table
        self.deck.pop(ran_num) #pop ran_num key value because card already used

#this is to randomize all other players except the user's cards
    def randomize_others(self, player1):
        self.player[1].append(player1[0]) #append the desired first card to player 1
        self.player[1].append(player1[1])#append the desired second card to player 1
        #find the index of both cards of player 1 because we need to pop from self.deck
        for i in range(2):
            if player1[i][1]=="Heart": base = 0
            elif player1[i][1]=="Diamond": base = 13
            elif player1[i][1]=="Spade": base = 26
            elif player1[i][1]=="Clove": base = 39
            if type(player1[i][0]) == int: numeric = player1[i][0]-1
            else:
                if player1[i][0]=="King": numeric = 12
                elif player1[i][0]=="Queen": numeric = 11
                elif player1[i][0]=="Jack": numeric = 10
                elif player1[i][0]=="Ace":numeric = 0
            self.deck.pop(base+numeric)
            self.list[base+numeric] = -1
        #self.deck.pop(ran_num) #pop ran_num key value because card already used
        for i in range (2, self.player_count+1): #go through players and append 1st card
            ran_num = random.choice(self.list) #random generate a number from 0-51
            while ran_num == -1: #if the random number is -1, card not valid
                ran_num = random.choice(self.list) #choose a random number until its valid
            self.list[ran_num] = -1 #set element ran_num to -1 to set invalid state
            self.player[i].append(self.deck[ran_num]) #append the card from deck to player
            self.deck.pop(ran_num) #pop ran_num key value because card already used

        #do it one more time so that each player has two cards
        for i in range (2, self.player_count+1):
            ran_num = random.choice(self.list)
            while ran_num == -1:
                ran_num = random.choice(self.list)
            self.list[ran_num] = -1
            self.player[i].append(self.deck[ran_num])
            self.deck.pop(ran_num)

    
#randomizes all other players while user's card is still empty
    def randomize_other_empty(self):
        for i in range (2, self.player_count+1): #go through players and append 1st card
            ran_num = random.choice(self.list) #random generate a number from 0-51
            while ran_num == -1: #if the random number is -1, card not valid
                ran_num = random.choice(self.list) #choose a random number until its valid
            self.list[ran_num] = -1 #set element ran_num to -1 to set invalid state
            self.player[i].append(self.deck[ran_num]) #append the card from deck to player
            self.deck.pop(ran_num) #pop ran_num key value because card already used

        #do it one more time so that each player has two cards
        for i in range (2, self.player_count+1):
            ran_num = random.choice(self.list)
            while ran_num == -1:
                ran_num = random.choice(self.list)
            self.list[ran_num] = -1
            self.player[i].append(self.deck[ran_num])
            self.deck.pop(ran_num)

#clears the board given an amount of cards to be removed
    def randomize_entire_board(self, amount):
        #we copy the list because we need to maintain the original deck
        #sub_deck = self.deck.copy()
        #sub_list = self.list.copy()
        for i in range(amount):
            ran_num = random.choice(self.list) #random generate a number from 0-51
            while ran_num == -1: #if the random number is -1, card not valid
                ran_num = random.choice(self.list) #choose a random number until its valid
            self.list[ran_num] = -1 #set element ran_num to -1 to set invalid state
            self.table_cards.append(self.deck[ran_num]) #append the card from deck to table
            self.deck.pop(ran_num) #pop ran_num key value because card already used

#clears the board
    def clear_board(self):
        for i in range(5):
            self.table_cards.pop(0)

    
#clears river and turn or river
    def clear_remains(self):
        self.table_cards.pop(-1)

#adds a card to the table
    def add_card_board(self, card):
        if card[1]=="Heart": base = 0
        elif card[1]=="Diamond": base = 13
        elif card[1]=="Spade": base = 26
        elif card[1]=="Clove": base = 39
        if type(card[0]) == int: numeric = card[0]-1
        if card[0]=="King": numeric = 12
        elif card[0]=="Queen": numeric = 11
        elif card[0]=="Jack": numeric = 10
        elif card[0]=="Ace":numeric = 0
        self.list[base+numeric] = -1
        self.table_cards.append(self.deck[base+numeric])
        self.deck.pop(base+numeric)
#adds a specified hand to a specified player
    def add_hand(self, hand, player):
        for i in range(2):
            #find index of added card
            if hand[i][1]=="Heart": base = 0
            elif hand[i][1]=="Diamond": base = 13
            elif hand[i][1]=="Spade": base = 26
            elif hand[i][1]=="Clove": base = 39
            if type(hand[i][0]) == int: numeric = hand[i][0]-1
            if hand[i][0]=="King": numeric = 12
            elif hand[i][0]=="Queen": numeric = 11
            elif hand[i][0]=="Jack": numeric = 10
            elif hand[i][0]=="Ace":numeric = 0
            #card is used so card is now invalid
            self.list[base+numeric] = -1
            #append hand to user
            self.player[player].append(hand[i])
            #get rid of it from deck
            self.deck.pop(base+numeric)




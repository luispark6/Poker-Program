import random
class Poker:
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

    def deal_cards(self):
        for i in range (1, self.player_count+1): #go through players and append 1st card
            ran_num = random.choice(self.list) #random generate a number from 0-51
            while ran_num == -1: #if the random number is -1, card not valid
                ran_num = random.choice(self.list) #choose a random number until its valid
            self.list[ran_num] = -1 #set element ran_num to -1 to set invalid state
            self.player[i].append(self.deck[ran_num]) #append the card from deck to player
            self.deck.pop(ran_num) #pop ran_num key value because card already used

        #do it one more time so that each player has two cards
        for i in range (1, self.player_count+1):
            ran_num = random.choice(self.list)
            while ran_num == -1:
                ran_num = random.choice(self.list)
            self.list[ran_num] = -1
            self.player[i].append(self.deck[ran_num])
            self.deck.pop(ran_num)
        
    def deal_flop(self):
        for i in range(3):
            ran_num = random.choice(self.list) #random generate a number from 0-51
            while ran_num == -1: #if the random number is -1, card not valid
                ran_num = random.choice(self.list) #choose a random number until its valid
            self.list[ran_num] = -1 #set element ran_num to -1 to set invalid state
            self.table_cards.append(self.deck[ran_num]) #append the card from deck to table
            self.deck.pop(ran_num) #pop ran_num key value because card already used

    def deal_turn(self):
        ran_num = random.choice(self.list) #random generate a number from 0-51
        while ran_num == -1: #if the random number is -1, card not valid
            ran_num = random.choice(self.list) #choose a random number until its valid
        self.list[ran_num] = -1 #set element ran_num to -1 to set invalid state
        self.table_cards.append(self.deck[ran_num]) #append the card from deck to table
        self.deck.pop(ran_num) #pop ran_num key value because card already used
    

    


#x = Poker(4)
#print(x.deck)
#x.deal_cards()
#print(x.player)
#print(x.deck)
#x.deal_flop()
#print(x.table_cards)
#x.deal_turn()
#x.deal_turn()
#print(x.table_cards)

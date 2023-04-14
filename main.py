from Setup_deal import *
import winner
import ties_wins
import winners_circle
import probability
import copy

def main():
    while True:
        try: #used so to take a valid input from user
            num_player = int(input(("Please select the amount of players you want play with: ")))
            if num_player<2 or num_player>6: #throw on purpose if num_player not in range 2-6
                x='s'
                y=int(x)
            break #breaks if valid int is inputted
        except:
            print("Please input an integer in the range of 2-6 ")

    round1 = Poker(num_player) #basic initialization of cards, players, etc. 
    round1.deal_cards() #deals the cards to all the players in the game

    #display users cards in terminal
    print("Your cards are: "+ str(round1.player[1][0][0])+" of "+str(round1.player[1][0][1])+\
        "s || " + str(round1.player[1][1][0])+" of "+ str(round1.player[1][1][1])+"s ")
    #we need this boolean to indicate if we want to print the winners or ties. If we choose
    #to show probabilities, it will print ten thousand times if we dont set print_txt equal to false
    print_txt=True
    show_probability = input("Would you like to see your probabilities of winning preflop? y/n: ")
    while show_probability != 'y' and show_probability != "n":
        show_probability = input("Please input 'y' or 'n': ")

    #calls function to check the percentage won with your hand
    #we set round_sub = round1 because we dont want to mess with the current round we're in. We want to maintain
    #the information for the current round because we will continute to play
    #must deep copy to create an actual copy of the object
    if show_probability == 'y':
        print_txt=False
        round_sub = copy.deepcopy(round1)
        percentage = probability.probability_preflop_hidden(round_sub, num_player, print_txt)
        print("You have a "+str(percentage)+"% chance to win with cards: "+ str(round1.player[1][0][0])+" of "+str(round1.player[1][0][1])+\
        "s || " + str(round1.player[1][1][0])+" of "+ str(round1.player[1][1][1])+"s")



    #Option to show your opponents' hands
    show_card = input("Would you like to see your opponnents cards? y/n: ")
    while show_card != 'y' and show_card != "n":
        show_card = input("Please input 'y' or 'n': ")
    #if user wants to see the cards, displays them down below
    print("---------------------------------------------------")
    if show_card == 'y':
        print("\nYour cards are: "+ str(round1.player[1][0][0])+" of "+str(round1.player[1][0][1])+\
        "s || " + str(round1.player[1][1][0])+" of "+ str(round1.player[1][1][1])+"s \n")
        print("---------------------------------------------------")
        for i in range(2, num_player+1):
            print("\n")
            print("Player " + str(i) + "'s cards are: "+ str(round1.player[i][0][0])+" of "+ \
            str(round1.player[i][0][1])+"s || " + str(round1.player[i][1][0])+" of "+ \
            str(round1.player[i][1][1])+"s \n")
            print("---------------------------------------------------")
        
        show_probability1 = input("Would you like to see your probabilities of winning preflop with opponents' cards revealed? y/n: ")
        while show_probability1 != 'y' and show_probability1 != "n":
            show_probability1 = input("Please input 'y' or 'n': ")

        #if user wants to see the probabailities of winning with their cards and opponents' cards revelaed, call 
        #probability_preflop_revealed function
        if show_probability1 == 'y':
            print_txt=False
            round_sub = copy.deepcopy(round1)
            percentage = probability.probability_preflop_revealed(round_sub, num_player, print_txt)
            print("You have a "+str(percentage)+"% chance to win with cards: "+ str(round1.player[1][0][0])+" of "+str(round1.player[1][0][1])+\
            "s || " + str(round1.player[1][1][0])+" of "+ str(round1.player[1][1][1])+"s")

    #deals the flop
    round1.deal_flop()
    
    print("The flop is: "+ str(round1.table_cards[0][0])+ " of "+str(round1.table_cards[0][1])+"s")
    print("~ ~ ~ ~ ~ ~  "+ str(round1.table_cards[1][0])+ " of "+str(round1.table_cards[1][1])+"s")
    print("~ ~ ~ ~ ~ ~  "+ str(round1.table_cards[2][0])+ " of "+str(round1.table_cards[2][1])+"s")
    print("\nYour cards are: "+ str(round1.player[1][0][0])+" of "+str(round1.player[1][0][1])+\
        "s || " + str(round1.player[1][1][0])+" of "+ str(round1.player[1][1][1])+"s \n")



    show_probability2 = input("Would you like to see your probabilities of winning with the flop? y/n: ")
    while show_probability2 != 'y' and show_probability2 != 'n':
        show_probability2 = input("Please input 'y' or 'n': ")
    
    #if user wants to see the probability and the cards have been seen, then we see the probability of winning
    #based on the current cards shown
    if show_probability2 =='y' and show_card == 'y':
        print_txt=False
        round_sub = copy.deepcopy(round1)
        #two means the last two cards will be randomized while flop isnt
        percentage = probability.probability_postflop_revealed(round_sub, num_player, print_txt, 2)
        print("You have a "+str(percentage)+"% chance to win with cards: "+ str(round1.player[1][0][0])+" of "+str(round1.player[1][0][1])+\
        "s || " + str(round1.player[1][1][0])+" of "+ str(round1.player[1][1][1])+"s")


    #if user wants to see the percentage with opponents' cards hidden, we find the percentage based on 
    #randomization of other cards 
    elif show_probability2 =='y' and show_card == 'n':
        print_txt=False
        round_sub = copy.deepcopy(round1)
        #true just means we're at post flop with no turn card
        percentage = probability.probability_postflop_hidden(round_sub, num_player, print_txt, True)
        print("You have a "+str(percentage)+"% chance to win with cards: "+ str(round1.player[1][0][0])+" of "+str(round1.player[1][0][1])+\
        "s || " + str(round1.player[1][1][0])+" of "+ str(round1.player[1][1][1])+"s")

    #deals the turn
    round1.deal_turn()
    print("The turn is: "+ str(round1.table_cards[0][0])+ " of "+str(round1.table_cards[0][1])+"s")
    print("~ ~ ~ ~ ~ ~  "+ str(round1.table_cards[1][0])+ " of "+str(round1.table_cards[1][1])+"s")
    print("~ ~ ~ ~ ~ ~  "+ str(round1.table_cards[2][0])+ " of "+str(round1.table_cards[2][1])+"s")
    print("~ ~ ~ ~ ~ ~  "+ str(round1.table_cards[3][0])+ " of "+str(round1.table_cards[3][1])+"s")
    print("\nYour cards are: "+ str(round1.player[1][0][0])+" of "+str(round1.player[1][0][1])+\
        "s || " + str(round1.player[1][1][0])+" of "+ str(round1.player[1][1][1])+"s \n")


    show_probability3 = input("Would you like to see your probabilities of winning with the flop and turn? y/n: ")
    while show_probability3 != 'y' and show_probability2 != 'n':
        show_probability3 = input("Please input 'y' or 'n': ")
    #finds the probability with flop, turn and shown cards
    if show_probability3 =='y' and show_card == 'y':
        print_txt=False
        round_sub = copy.deepcopy(round1)
        #two means the last two cards will be randomized while flop isnt
        percentage = probability.probability_postflop_revealed(round_sub, num_player, print_txt, 1)
        print("You have a "+str(percentage)+"% chance to win with cards: "+ str(round1.player[1][0][0])+" of "+str(round1.player[1][0][1])+\
        "s || " + str(round1.player[1][1][0])+" of "+ str(round1.player[1][1][1])+"s")
    #finds the probability with flop, turn and no shown cards
    if show_probability3 =='y' and show_card == 'n':
        print_txt=False
        round_sub = copy.deepcopy(round1)
        #false means we're at the turn card
        percentage = probability.probability_postflop_hidden(round_sub, num_player, print_txt, False)
        print("You have a "+str(percentage)+"% chance to win with cards: "+ str(round1.player[1][0][0])+" of "+str(round1.player[1][0][1])+\
        "s || " + str(round1.player[1][1][0])+" of "+ str(round1.player[1][1][1])+"s")



    #deals the river 
    round1.deal_turn()
    print("The river is: "+ str(round1.table_cards[0][0])+ " of "+str(round1.table_cards[0][1])+"s")
    print("~ ~ ~ ~ ~ ~   "+ str(round1.table_cards[1][0])+ " of "+str(round1.table_cards[1][1])+"s")
    print("~ ~ ~ ~ ~ ~   "+ str(round1.table_cards[2][0])+ " of "+str(round1.table_cards[2][1])+"s")
    print("~ ~ ~ ~ ~ ~   "+ str(round1.table_cards[3][0])+ " of "+str(round1.table_cards[3][1])+"s")
    print("~ ~ ~ ~ ~ ~   "+ str(round1.table_cards[4][0])+ " of "+str(round1.table_cards[4][1])+"s")

    #table_cards = []
    #table_cards.append([4, "Heart"])
    #table_cards.append([7, "Spade"])
    #table_cards.append([10, "Clove"])
    #table_cards.append(["Jack", "Heart"])
    #table_cards.append([2, "Diamond"])
    #player = {}
    #player[1]=[]
    #player[1].append([3, "Heart"])
    #player[1].append([8, "Spade"])
    #player[2]=[]
    #player[2].append(["Ace", "Clove"])
    #player[2].append([9, "Heart"])
    #player[3]=[]
    #player[3].append(["Ace", "Heart"])
    #player[3].append([8, "Spade"])
    #player[4]=[]
    #player[4].append([5, "Clove"])
    #player[4].append([9, "Diamond"])
    print("\nYour cards are: "+ str(round1.player[1][0][0])+" of "+str(round1.player[1][0][1])+\
    "s || " + str(round1.player[1][1][0])+" of "+ str(round1.player[1][1][1])+"s \n")
    print("---------------------------------------------------")
    for i in range(2, num_player+1):
        print("\n")
        print("Player " + str(i) + "'s cards are: "+ str(round1.player[i][0][0])+" of "+ \
        str(round1.player[i][0][1])+"s || " + str(round1.player[i][1][0])+" of "+ \
        str(round1.player[i][1][1])+"s \n")
        print("---------------------------------------------------")
    print_txt=True
    winners_circle.winning_players(round1.player, round1.table_cards, num_player, print_txt)


    
        
          

main()
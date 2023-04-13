from Setup_deal import *
import winner
import ties_wins

def main():
    while True:
        try: #used so to take a valid input from user
            num_player = int(input(("Please select the amount of players you want play with: ")))
            if num_player<2 or num_player>6: #throw on purpose if num_player not in range 2-6
                x='s'
                y=int(x)
            break #breaks if valid int is inputted
        except:
            print("Please input an integer in the range of 2-6")

    round1 = Poker(num_player) #basic initialization of cards, players, etc. 
    round1.deal_cards() #deals the cards to all the players in the game

    #display users cards in terminal
    print("Your cards are: "+ str(round1.player[1][0][0])+" of "+str(round1.player[1][0][1])+\
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

    #deals the flop
    round1.deal_flop()
    
    print("The flop is: "+ str(round1.table_cards[0][0])+ " of "+str(round1.table_cards[0][1])+"s")
    print("~ ~ ~ ~ ~ ~  "+ str(round1.table_cards[1][0])+ " of "+str(round1.table_cards[1][1])+"s")
    print("~ ~ ~ ~ ~ ~  "+ str(round1.table_cards[2][0])+ " of "+str(round1.table_cards[2][1])+"s")
    print("\nYour cards are: "+ str(round1.player[1][0][0])+" of "+str(round1.player[1][0][1])+\
        "s || " + str(round1.player[1][1][0])+" of "+ str(round1.player[1][1][1])+"s \n")
    
    #deals the turn
    round1.deal_turn()
    print("The turn is: "+ str(round1.table_cards[0][0])+ " of "+str(round1.table_cards[0][1])+"s")
    print("~ ~ ~ ~ ~ ~  "+ str(round1.table_cards[1][0])+ " of "+str(round1.table_cards[1][1])+"s")
    print("~ ~ ~ ~ ~ ~  "+ str(round1.table_cards[2][0])+ " of "+str(round1.table_cards[2][1])+"s")
    print("~ ~ ~ ~ ~ ~  "+ str(round1.table_cards[3][0])+ " of "+str(round1.table_cards[3][1])+"s")
    print("\nYour cards are: "+ str(round1.player[1][0][0])+" of "+str(round1.player[1][0][1])+\
        "s || " + str(round1.player[1][1][0])+" of "+ str(round1.player[1][1][1])+"s \n")

    #deals the river 
    round1.deal_turn()
    print("The river is: "+ str(round1.table_cards[0][0])+ " of "+str(round1.table_cards[0][1])+"s")
    print("~ ~ ~ ~ ~ ~   "+ str(round1.table_cards[1][0])+ " of "+str(round1.table_cards[1][1])+"s")
    print("~ ~ ~ ~ ~ ~   "+ str(round1.table_cards[2][0])+ " of "+str(round1.table_cards[2][1])+"s")
    print("~ ~ ~ ~ ~ ~   "+ str(round1.table_cards[3][0])+ " of "+str(round1.table_cards[3][1])+"s")
    print("~ ~ ~ ~ ~ ~   "+ str(round1.table_cards[4][0])+ " of "+str(round1.table_cards[4][1])+"s")
    print("\nYour cards are: "+ str(round1.player[1][0][0])+" of "+str(round1.player[1][0][1])+\
        "s || " + str(round1.player[1][1][0])+" of "+ str(round1.player[1][1][1])+"s \n")

    
    #players_points = []

    #for i in range(1, num_player+1):
        #flush_indicator1=winner.flush(round1.table_cards, round1.player[i])
        #straight_indicator1= winner.straight(round1.table_cards, round1.player[i])
        #four_indicator1 = winner.four(round1.table_cards, round1.player[i])
        #three_indicator1 = winner.three(round1.table_cards, round1.player[i])
        #pair_indicator1 = winner.pair(round1.table_cards, round1.player[i])
        #if flush_indicator1[0]==True and straight_indicator1[0] == True and straight_indicator1[1] == 14:
            #players_points.append(10)
        #elif flush_indicator1[0]==True and straight_indicator1[0] == True: players_points.append(9)
        #elif four_indicator1[0] == True: players_points.append(8)
        #elif three_indicator1[0] ==True and pair_indicator1[0] == True: players_points.append(7)
        #elif flush_indicator1[0]==True: players_points.append(6)
        #elif straight_indicator1[0] == True: players_points.append(5)
        #elif three_indicator1[0] == True: players_points.append(4)
        #elif pair_indicator1[0] == True and len(pair_indicator1[1])>1: players_points.append(3)
        #elif pair_indicator1[0] == True and len(pair_indicator1[1])==1: players_points.append(2)
        #else:
            #players_points.append(1)

    table_cards = []
    
    table_cards.append([4, "Heart"])
    table_cards.append([7, "Spade"])
    table_cards.append([10, "Clove"])
    table_cards.append(["Jack", "Heart"])
    table_cards.append([2, "Diamond"])
    player = {}

    player[1]=[]
    player[1].append([3, "Heart"])
    player[1].append([8, "Spade"])
    player[2]=[]
    player[2].append(["Queen", "Clove"])
    player[2].append([3, "Heart"])
    player[3]=[]
    player[3].append([5, "Heart"])
    player[3].append([8, "Spade"])
    player[4]=[]
    player[4].append([5, "Clove"])
    player[4].append([9, "Diamond"])
    players_points = []


    for i in range(1, num_player+1):
        flush_indicator1=winner.flush(table_cards, player[i])
        straight_indicator1= winner.straight(table_cards, player[i])
        four_indicator1 = winner.four(table_cards, player[i])
        three_indicator1 = winner.three(table_cards, player[i])
        pair_indicator1 = winner.pair(table_cards, player[i])
        validity =False
        #checks condition if royal flush is valid. We pop because we only care about top 5 cards
        if flush_indicator1[0]==True and straight_indicator1[0] == True and flush_indicator1[1][-1]==14:
            if len(flush_indicator1[1]) ==7:
                flush_indicator1[1].pop(0)
                flush_indicator1[1].pop(0)
            elif len(flush_indicator1[1]) ==6:
                flush_indicator1[1].pop(0)
            indicator = 0
            for i in range(len(flush_indicator1[1])-1):
                if flush_indicator1[1][i]+1 == flush_indicator1[1][i+1]:
                    indicator = indicator+1
            if indicator >= 4:
                validity=True
                players_points.append(10)
        #checks if flush is also a straight
        if flush_indicator1[0]==True and straight_indicator1[0] == True and validity == False:
            indicator = 0
            for i in range(len(flush_indicator1[1])-1):
                if flush_indicator1[1][i]+1 == flush_indicator1[1][i+1]:
                    indicator = indicator+1
                if i==3 and flush_indicator1[1][i] == 5:
                    if flush_indicator1[1][i+1]==14:
                        indicator=indicator+1
            if indicator >=4:
                players_points.append(9)
            else:
                players_points.append(6)
        elif four_indicator1[0] == True: players_points.append(8)
        elif (three_indicator1[0] ==True and pair_indicator1[0] == True) or (three_indicator1[0]==True and len(three_indicator1[1])>1): players_points.append(7)
        elif flush_indicator1[0]==True and validity == False: 
            players_points.append(6)
        elif straight_indicator1[0] == True and validity == False: players_points.append(5)
        elif three_indicator1[0] == True and validity == False: players_points.append(4)
        elif pair_indicator1[0] == True and len(pair_indicator1[1])>1 and validity == False: players_points.append(3)
        elif pair_indicator1[0] == True and len(pair_indicator1[1])==1 and validity == False: players_points.append(2)
        else:
            if validity == False:
                players_points.append(1)




    winners_circle = []
    #index of scores are the players with the best score
    indexOfScores = []
    #bestScore is the highest score of all the player's score
    bestScore = max(players_points)
    #players_points contain the scores of each player and the index of the scores
    #is an indicator which player has that score. Since players start with 1, 
    #we need to append i+1 because i starts at 0
    
    for i in range(len(players_points)):
        if players_points[i] == bestScore:
            indexOfScores.append(i+1)
    
    if len(indexOfScores) ==1:
        print("Player "+ str(indexOfScores[0])+" wins!")
        winners_circle.append(indexOfScores[0])
        print(winners_circle)

    elif bestScore == 2:
        winners_circle = ties_wins.pair_ties(players_points, player, table_cards, indexOfScores)
    elif bestScore == 3:
        winners_circle = ties_wins.two_pair_tie(players_points, player, table_cards, indexOfScores)
        
    elif bestScore == 4:
        winners_circle = ties_wins.three_tie(players_points, player, table_cards, indexOfScores)
        print(winners_circle)
    elif bestScore == 5:
        winners_circle = ties_wins.straight_ties(players_points, player, table_cards, indexOfScores)
        print(winners_circle)
    elif bestScore == 6:
        winners_circle = ties_wins.flush_ties(players_points, player, table_cards, indexOfScores)
    elif bestScore == 7:
        winners_circle= ties_wins.fullhouse_ties(players_points, player, table_cards, indexOfScores)
    elif bestScore == 8:
        winners_circle = ties_wins.four_ties(players_points, player, table_cards, indexOfScores)
    elif bestScore == 9:
        winners_circle = ties_wins.straight_flush_ties(players_points, player, table_cards, indexOfScores)
    elif bestScore == 10:
        sent = "Players "
        for i in range(len(indexOfScores)):
            winners_circle.append(indexOfScores[i])
            sent = sent+ str(indexOfScores[i])
            if i != len(indexOfScores)-1:
                sent=sent+" and "
        sent=sent + " tied!"
        print(sent)
    else:
        winners_circle = ties_wins.high_tie(players_points, player, table_cards, indexOfScores)
        
          

main()
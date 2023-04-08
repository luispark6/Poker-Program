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
    
    table_cards.append([2, "Heart"])
    table_cards.append([4, "Spade"])
    table_cards.append([7, "Clove"])
    table_cards.append(["Ace", "Diamond"])
    table_cards.append(["Jack", "Heart"])
    player = {}
    player[1]=[]
    player[1].append(["Jack", "Diamond"])
    player[1].append([7, "Diamond"])
    player[2]=[]
    player[2].append(["Ace", "Heart"])
    player[2].append(["Ace", "Heart"])
    player[3]=[]
    player[3].append(["Jack", "Clove"])
    player[3].append(["Jack", "Heart"])
    player[4]=[]
    player[4].append([4, "Clove"])
    player[4].append(["King", "Diamond"])
    players_points = []

    for i in range(1, num_player+1):
        flush_indicator1=winner.flush(table_cards, player[i])
        straight_indicator1= winner.straight(table_cards, player[i])
        four_indicator1 = winner.four(table_cards, player[i])
        three_indicator1 = winner.three(table_cards, player[i])
        pair_indicator1 = winner.pair(table_cards, player[i])
        if flush_indicator1[0]==True and straight_indicator1[0] == True and straight_indicator1[1] == 14:
            players_points.append(10)
        elif flush_indicator1[0]==True and straight_indicator1[0] == True: players_points.append(9)
        elif four_indicator1[0] == True: players_points.append(8)
        elif (three_indicator1[0] ==True and pair_indicator1[0] == True) or (three_indicator1[0]==True and len(three_indicator1[1])>1): players_points.append(7)
        elif flush_indicator1[0]==True: players_points.append(6)
        elif straight_indicator1[0] == True: players_points.append(5)
        elif three_indicator1[0] == True: players_points.append(4)
        elif pair_indicator1[0] == True and len(pair_indicator1[1])>1: players_points.append(3)
        elif pair_indicator1[0] == True and len(pair_indicator1[1])==1: players_points.append(2)
        else:
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

          


            

            
    


main()
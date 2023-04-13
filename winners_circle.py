from Setup_deal import *
import winner
import ties_wins


def winning_players(player, table_cards, num_player, print_txt):
    players_points = []
    for i in range(1, num_player+1):
        flush_indicator1=winner.flush(table_cards, player[i])
        straight_indicator1= winner.straight(table_cards, player[i])
        four_indicator1 = winner.four(table_cards, player[i])
        three_indicator1 = winner.three(table_cards,player[i])
        pair_indicator1 = winner.pair(table_cards,player[i])
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
        if print_txt ==True:
            print("Player "+ str(indexOfScores[0])+" wins!")
        winners_circle.append(indexOfScores[0])

    elif bestScore == 2:
        winners_circle = ties_wins.pair_ties(players_points, player, table_cards, indexOfScores, print_txt)
    elif bestScore == 3:
        winners_circle = ties_wins.two_pair_tie(players_points, player, table_cards, indexOfScores, print_txt)
        
    elif bestScore == 4:
        winners_circle = ties_wins.three_tie(players_points, player, table_cards, indexOfScores, print_txt)
    elif bestScore == 5:
        winners_circle = ties_wins.straight_ties(players_points, player, table_cards, indexOfScores, print_txt)
    elif bestScore == 6:
        winners_circle = ties_wins.flush_ties(players_points, player, table_cards, indexOfScores, print_txt)
    elif bestScore == 7:
        winners_circle= ties_wins.fullhouse_ties(players_points, player, table_cards, indexOfScores, print_txt)
    elif bestScore == 8:
        winners_circle = ties_wins.four_ties(players_points, player, table_cards, indexOfScores, print_txt)
    elif bestScore == 9:
        winners_circle = ties_wins.straight_flush_ties(players_points, player, table_cards, indexOfScores, print_txt)
    elif bestScore == 10:
        sent = "Players "
        for i in range(len(indexOfScores)):
            winners_circle.append(indexOfScores[i])
            sent = sent+ str(indexOfScores[i])
            if i != len(indexOfScores)-1:
                sent=sent+" and "
        sent=sent + " tied!"
        if print_txt ==True:
            print(sent)
    else:
        winners_circle = ties_wins.high_tie(players_points, player, table_cards, indexOfScores, print_txt)

    return winners_circle
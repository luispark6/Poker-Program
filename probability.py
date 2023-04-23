from Setup_deal import *
import winner
import ties_wins
import winners_circle



#probability of winning with your cards without seeing other card's opponents
def probability_preflop_hidden(round1, num_player, print_txt):
    #deals out the flop, turn and river
    user_wins = 0
    round1.deal_flop()
    round1.deal_turn()
    round1.deal_turn()
    #see who the winner is based on first deal out
    list = winners_circle.winning_players(round1.player, round1.table_cards, num_player, print_txt)
    if len(list)==1 and list[0]==1:
        #accumulate the wins
        user_wins = user_wins+1
    #proceed to play 10000 different rounds with your current card
    for i in range(10000):
        roundx = Poker(num_player)
        roundx.randomize_others(round1.player[1])
        roundx.deal_flop()
        roundx.deal_turn()
        roundx.deal_turn()
        list = winners_circle.winning_players(roundx.player, roundx.table_cards, num_player, print_txt)
        #if user is in the list and is the only one in the list, user has won this round
        if len(list)==1 and list[0]==1:
            user_wins = user_wins+1
    #find the percentage and truncate
    percentage = user_wins/10001
    percentage = percentage*100
    percentage = float(f'{percentage:.4f}')
    return percentage


def probability_preflop_revealed(round1, num_player, print_txt):
    #accumulated wins from user
    user_wins = 0
    #see who the winner is based on first deal out
    for i in range(10000):
        #randomize the board
        round1.randomize_entire_board(5)
        #check who the winner is
        list = winners_circle.winning_players(round1.player, round1.table_cards, num_player, print_txt)
        #if user is in the list and is the only one in the list, user has won this round
        if len(list)==1 and list[0]==1:
            user_wins = user_wins+1
        #clear the board
        round1.clear_board()
    #calculate the percentage
    percentage = user_wins/10000
    percentage = percentage*100
    percentage = float(f'{percentage:.4f}')
    return percentage


def probability_postflop_revealed(round1, num_player, print_txt, indicator):
    #accumulated wins from user
    user_wins = 0
    #see who the winner is based on first deal out
    for i in range(10000):
        #randomize last #(indicators) cards
        round1.randomize_entire_board(indicator)
        #check who the winner is
        list = winners_circle.winning_players(round1.player, round1.table_cards, num_player, print_txt)
        #if user is in the list and is the only one in the list, user has won this round
        if len(list)==1 and list[0]==1:
            user_wins = user_wins+1
        #clear the last two cards on board
        if indicator ==2:
            round1.clear_remains(False)
        else:
            round1.clear_remains(True)
    #calculate the percentage
    percentage = user_wins/10000
    percentage = percentage*100
    percentage = float(f'{percentage:.4f}')
    return percentage


def probability_postflop_hidden(round1, num_player, print_txt, indicator):
    randomize = 5 - indicator 


    #if indicator ==True:
        #if true, then only three cards remain the same on board and we 
        #randomize the next two
        #same_board = 3
        #randomize = 2
    #else:
        #same_board = 4
       # randomize = 1
    #accumulated wins from user

    
    user_wins = 0
    for i in range(10000):
        #create new poker object
        roundx = Poker(num_player)
        #append the flop into board because the flop should be the same every iteration
        for i in range(indicator):
            roundx.add_card_board(round1.table_cards[i])
        #randomize the the next two cards
        roundx.randomize_entire_board(randomize)
        #randomize other players' card except user's
        roundx.randomize_others(round1.player[1])
        #find the winners
        list = winners_circle.winning_players(roundx.player, roundx.table_cards, num_player, print_txt)
        #if user is the only one in the list, then user wins
        if len(list)==1 and list[0]==1:
            user_wins = user_wins+1
    percentage = user_wins/10000
    percentage = percentage*100
    percentage = float(f'{percentage:.4f}')
    return percentage



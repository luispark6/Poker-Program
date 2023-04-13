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
    for i in range(1000000):
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
    percentage = user_wins/1000001
    percentage = percentage*100
    percentage = float(f'{percentage:.4f}')
    return percentage


def probability_preflop_revealed(round1, num_player, print_txt):
    #accumulated wins from user
    user_wins = 0
    #see who the winner is based on first deal out
    for i in range(1000000):
        #randomize the board
        round1.randomize_entire_board()
        #check who the winner is
        list = winners_circle.winning_players(round1.player, round1.table_cards, num_player, print_txt)
        #if user is in the list and is the only one in the list, user has won this round
        if len(list)==1 and list[0]==1:
            user_wins = user_wins+1
        #clear the board
        round1.clear_board()
    #calculate the percentage
    percentage = user_wins/1000000
    percentage = percentage*100
    percentage = float(f'{percentage:.4f}')
    return percentage
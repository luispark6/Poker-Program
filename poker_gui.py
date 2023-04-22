from operator import truediv
from os import environ
from re import L
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from Setup_deal import *
import winners_circle
import probability
import copy
import time
import sys
import os


def rect(screen):
    #both cards bottom middle
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(505, 660, 90, 115), 5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(605, 660, 90, 115),5) 
    #both cards in bottom left
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(150, 575, 90, 115), 5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(250, 575, 90, 115),5) 
    #both cards middle left
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(0, 342, 90, 115), 5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(100, 342, 90, 115),5) 
    #both cards top middle
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(505, 0, 90, 115), 5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(605, 0, 90, 115),5) 
    #both cards top left
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(150, 100, 90, 115), 5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(250, 100, 90, 115),5) 
    #both cards in bottom right
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(960, 575, 90, 115), 5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(860, 575, 90, 115),5) 
    #both cards middle right
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(1110, 342, 90, 115), 5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(1010, 342, 90, 115),5) 
    #both cards in bottom right
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(960, 100, 90, 115), 5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(860, 100, 90, 115),5) 
    #cards on the board
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(365, 330, 90, 115),5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(460, 330, 90, 115),5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(555, 330, 90, 115),5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(650, 330, 90, 115),5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(745, 330, 90, 115),5) 

def addplayer():
    #make a dictionary with all needed information for all add player buttons
    player = {}
    font = pygame.font.SysFont('Arial', 15, bold = True)
    surf = font.render('Add Player +', True, 'white')
    addplayer1 = pygame.Rect(197, 710, 94, 20)
    addplayer2 = pygame.Rect(47, 477, 94, 20)
    addplayer3 = pygame.Rect(552, 135, 94, 20)
    addplayer4 = pygame.Rect(197, 235, 94, 20)
    addplayer5 = pygame.Rect(907, 710, 94, 20)
    addplayer6 = pygame.Rect(1055, 477, 94, 20)
    addplayer7 = pygame.Rect(907, 235, 94, 20)
    player["player2"]= [font, surf, addplayer1]
    player["player3"] = [font, surf, addplayer2]
    player["player5"] = [font, surf, addplayer3]
    player["player4"] = [font, surf, addplayer4]
    player["player8"] = [font, surf, addplayer5]
    player["player7"] = [font, surf, addplayer6]
    player["player6"] = [font, surf, addplayer7]
    return player

def init_addcard():
    #make a dictinoary with all needed information to make a button that displays
    #and adds cards for player 1 and the board
    add_card = {}
    font = pygame.font.SysFont('Arial', 15, bold = True)
    surf = font.render('', True, 'white')
    user_button1 = pygame.Rect(510, 665, 80, 105)
    user_button2 = pygame.Rect(610, 665, 80, 105)
    board_card1 = pygame.Rect(370, 335, 80, 105)
    board_card2 = pygame.Rect(465, 335, 80, 105)
    board_card3 = pygame.Rect(560, 335, 80, 105)
    board_card4 = pygame.Rect(655, 335, 80, 105)
    board_card5 = pygame.Rect(750, 335, 80, 105)
    add_card["user1"]= [font, surf, user_button1]
    add_card["user2"]= [font, surf, user_button2]
    add_card["board1"]= [font, surf, board_card1]
    add_card["board2"]= [font, surf, board_card2]
    add_card["board3"]= [font, surf, board_card3]
    add_card["board4"]= [font, surf, board_card4]
    add_card["board5"]= [font, surf, board_card5]
    return add_card

def addcard(player_info):
    #this will take in the info of the add player button. it will see which outlined cards need
    #to be added to add_card dictionary. 
    if player_info[2].x ==197 and player_info[2].y == 710:
        card1 = pygame.Rect(155, 580, 80, 105)
        card2 =  pygame.Rect(255, 580, 80, 105)
    elif player_info[2].x ==47:
        card1 = pygame.Rect(5, 347, 80, 105)
        card2 =  pygame.Rect(105, 347, 80, 105)
    elif player_info[2].x ==552:
        card1 = pygame.Rect(510, 5, 80, 105)
        card2 =  pygame.Rect(610, 5, 80, 105)
    elif player_info[2].x ==197:
        card1 = pygame.Rect(155, 105, 80, 105)
        card2 =  pygame.Rect(255, 105, 80, 105)
    elif player_info[2].x ==907 and player_info[2].y ==710:
        card1 = pygame.Rect(965, 580, 80, 105)
        card2 =  pygame.Rect(865, 580, 80, 105)

    elif player_info[2].x ==1055:
        card1 = pygame.Rect(1115, 347, 80, 105)
        card2 =  pygame.Rect(1015, 347, 80, 105)

    elif player_info[2].x ==907:
        card1 = pygame.Rect(965, 105, 80, 105)
        card2 =  pygame.Rect(865, 105, 80, 105)
    list = []
    list.append(card1)
    list.append(card2)
    return list


def main():
    board= 0 
    playerss = 0
    user =0
    num_player = 1
    copy_indicator=False
    pop_indicator = True
    #this will be used to display cards in ascending order in interface
    value_cards=["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", 'default']
    FPS_CLOCK = pygame.time.Clock()
    #intializing the game
    pygame.init()
    #setting dimensions of display
    screen = pygame.display.set_mode((1200, 775))
    #name
    pygame.display.set_caption("Poker")
    #displays green background
    screen.fill([0,128,0])
    running = True
    #indicator that checks if a slot has been chosen
    slot_chosen = False
    #unsorted cards will be the png files in unsorted order
    unsorted_cards = []
    #this will iterate through the file and append the file names in unsorted_cards
    rect(screen)
    directory = 'cards'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        unsorted_cards.append(f)
    #intiailzing sorted_cards. This will append the png files from Ace-King in image form for pygame
    sorted_cards=[]
    #this will be used later to indicate which card has been chosen
    listOfcards = []
    #value cards go in ascending order, so we append to sorted_cards from smallest to biggest
    #font and surf for the add_card
    font = pygame.font.SysFont('Arial', 15, bold = True)
    surf = font.render('', True, 'white')
    #indicator if hand has begun
    play_hand = False
    font2 = pygame.font.SysFont('Arial', 18, bold = True)
    begin_game_text = font.render('Please add players before starting the hand', True, 'white')
    for i in range(len(value_cards)):
        for j in range(len(unsorted_cards)):
            if value_cards[i] in unsorted_cards[j]:
                sorted_cards.append(pygame.image.load(unsorted_cards[j]))
                listOfcards.append(unsorted_cards[j])
    deal_randoms = False
    begin_game_bool =False
    #accumulator for how many popped cards
    x_y_acc= 0
    #returns a dictionaries of all things needed to make a add player button
    player = addplayer()
    blank_card = sorted_cards[52]
    #add_card will contain all available add card buttons. We are intiliazing in 
    #the line below
    add_card = init_addcard()
    #this will be used to indicate which number player has been added
    add_player_num = 1
    show_cards=False
    #this will contain the player in which the user picks the card for
    card_player =[]
    #list of all chosen cards
    all_chosen_cards = []
    remove = []
    temp = []
    removal=0
    chosen_card = []
    chosen_card2=[]
    #button to play the hand
    begin_text = font2.render('Play Hand!', True, 'white')
    begin_button = pygame.Rect(556, 450, 95, 22)
    hidden_cards = pygame.Rect(425, 450, 325, 22)
    deal_randoms_display = True
    card = {}
    while running:    #checks each event and see if it should quit
        #screen fill makes bacground green
        screen.fill([0,128,0])
        #draws all the empty slots
        rect(screen)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):
                    running = False
            elif (event.type == pygame.QUIT):
                return
            #if we click on start game, begin the game. There must be atleast 2 players
            if event.type == pygame.MOUSEBUTTONDOWN:
                if begin_button.collidepoint(event.pos) and add_player_num!=1:
                    round1 = Poker(num_player)
                    play_hand=True
            if event.type == pygame.MOUSEBUTTONDOWN and show_cards==False and play_hand==False:
                #iterate through each add player button if we press down on the mouse
                for i in player:
                    #if we pressed down on the mouse and it happens to colllide with one of the players, 
                    #go in the if statement
                    if player[i][2].collidepoint(event.pos):
                        num_player=num_player+1
                        #update the player number
                        add_player_num = add_player_num +1
                        #these are the keys of each player and their cards
                        player_num1 = "Player"+str(add_player_num)+"first_card"
                        player_num2 = "Player"+str(add_player_num)+"second_card"
                        #when we call addcards, it takes in the information of the add_player button we have just selected
                        #we then figure out the coordinates of both the card positions for the player and append it in a list
                        list = addcard(player[i])
                        #adding the key and value into the add_card dictionary because we want this person's card slot to be 
                        #a button now
                        add_card[player_num1] = [font, surf, list[0]]
                        add_card[player_num2] = [font, surf, list[1]]
                        #we add this into a list called remove because these are all keys that we want to remvoe from player
                        remove.append(i)
                        break
                #finds the indice of the card picked when the cards are popped up. indice should range from 0,0 - 10,3
                #anything else is not valid
            if event.type == pygame.MOUSEBUTTONDOWN and show_cards == True:
                pos = pygame.mouse.get_pos()
                indiceX = (pos[0]-180)//60
                indiceY = (pos[1]-200)//90
                #if the indices youve chosen is an indice where a card is located, then go in this if statement
                #it should display the card for the proper player, get rid of the button option for card, and get rid
                #of the card from the display
                #finds the one dimenesional indice for the card
                base = indiceY*13
                indice = base + indiceX +indiceY

                if indice<len(sorted_cards)-1:
                    one_card = sorted_cards.pop(indice)
                    all_chosen_cards.append(one_card)
                    card_removed= listOfcards.pop(indice)
                    show_cards = False
                    chosen_card.append(removal3)
                    chosen_card2.append(removal2)
                    #this appends all chosen cards to the table/players
                    for i in round1.deck:
                        if str(round1.deck[i][0]) in card_removed and round1.deck[i][1] in card_removed:
                            if playerss !=0:
                                card[playerss].append(round1.deck[i])
                                playerss = 0
                            elif user !=0:
                                card[user].append(round1.deck[i])
                                user = 0
                            elif board!=0:
                                card[board].append(round1.deck[i])
                                board = 0

                    pop_player = 0
                    #adds all cards to the poker class for players and table_cards
                    for i in card:
                        if "Player" in i and len(card[i])==2:
                            round1.add_hand(card[i], int(i[6]))
                            pop_player = i
                        elif "user" in i and len(card[i])==2:
                            round1.add_hand(card[i], 1)
                            pop_player =i
                        
                        elif "board" in i:
                            round1.add_card_board(card[i][0])
                            pop_player =i
                    if pop_player !=0:
                        card.pop(pop_player)
            #remove contains all player add buttons that have been clicked. We dont need these buttons
            #anymore because we just clicked them
            elif show_cards ==False and play_hand==False :
                for i in remove:
                    #i[2] contains player numbers
                    temp.append([player[i][2], add_player_num])
                    player.pop(i)
                    remove=[]
            #if we click a add_card button, turn show_cards to true and append the key
            #card player. i contains the player and which card that has been chosen
            elif play_hand==True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in add_card:
                        if add_card[i][2].collidepoint(event.pos):
                            show_cards =True
                            if "Player" in i:
                                #slices it so that the the key is 'player#'
                                playerss = i[0:7]
                                #if playerss doesnt exist in the dictionary, make it a key with value of list
                                if playerss not in card:
                                    card[playerss] = []
                            #if key has "user" in it, then have 'user' as key for dictionary 'card'
                            elif "user" in i:
                                #slices it so that the the key is 'player#'
                                user = i[0:4]
                                #if playerss doesnt exist in the dictionary, make it a key with value of list
                                if user not in card:
                                    card[user] = []

                            elif "board" in i:
                                #slices it so that the the key is 'player#'
                                board = i[0:5]
                                #if playerss doesnt exist in the dictionary, make it a key with value of list
                                if board not in card:
                                    card[board] = []
    
                            removal = i
                            removal2 = add_card[i][2]
                            removal3 = add_card[i][1] 
                            if i !="user1" and i!="user2" and i!="board1" and i!="board2" and i!="board3" and i!="board4" and i!="board5":
                                deal_randoms_display=False
                            break


            


            #this will be an indicator if we choose random card for opponents
            if event.type == pygame.MOUSEBUTTONDOWN and show_cards==False and play_hand==True and deal_randoms == False and deal_randoms_display!=False:
                if begin_game_bool == False:
                    begin_game_bool=True
                elif hidden_cards.collidepoint(event.pos):
                    deal_randoms=True
                    deal_randoms_display=False

        a,b = pygame.mouse.get_pos()
        #if show_cards == False and play_hand==True:
            #for i in add_card:
                #if add_card[i][2].x<= a <add_card[i][2].x+90 and add_card[i][2].y <= b <= add_card[i][2].y+115:
                    #static = static+1
                    #pygame.draw.rect(screen, (180, 180, 180), add_card[i][2])
                    #break

        #loops through player which is information for each button, and if mouse is on top of any 
        #of the add player buttons, highlight
        if show_cards == False:
            for i in player:
                if player[i][2].x<= a <player[i][2].x+94 and player[i][2].y <= b <= player[i][2].y+20:
                    pygame.draw.rect(screen, (180, 180, 180), player[i][2])
                else:
                    pygame.draw.rect(screen, (0,128,0), player[i][2])
                #loops over players and displays all the buttons
           
                screen.blit(player[i][1],(player[i][2].x, player[i][2].y))
            #displays face down card
            screen.blit(pygame.transform.scale(blank_card, (90, 115)), (270, 330))
            #for each add_card button, if cursor is over it, highlight it 
            #displays all the player numbers that have been added
            for i in temp:
                surf2 = font.render('     Player '+str(i[1]), True, 'white')
                screen.blit(surf2,(i[0].x, i[0].y))
        #display the empty card slots buttons
        #display chosen cards

        for i in range(len(chosen_card)):
            screen.blit(pygame.transform.scale(all_chosen_cards[i], (80,105)), (chosen_card2[i].x, chosen_card2[i].y))
            
        #if true, display the cards
        if show_cards == True:
            pygame.draw.rect(screen, (0,128,0), removal2)
            x=180
            y=200
            for i in range(len(sorted_cards)):
                screen.blit(pygame.transform.scale(sorted_cards[i], (60, 90)), (x, y))
                x=x+60
                if i ==13 or i == 27 or i == 41:
                    y=y+90
                    x=180
            if removal !=0:
                add_card.pop(removal)
            removal=0
        
        #need to add the player before we start the hand
        if add_player_num==1:
            begin_game_text = font2.render('Please add players before starting the hand', True, 'white')
            screen.blit(begin_game_text,(420, 280))

        #if we're not currently playing the hand, provide a button to start the game if wanted
        if begin_button.x<= a <begin_button.x+95 and begin_button.y <= b <= begin_button.y+22 and play_hand==False:
            pygame.draw.rect(screen, (180, 180, 180), begin_button)
        elif play_hand==False:
            pygame.draw.rect(screen, (0,128,0), begin_button)
        if play_hand==False:
            screen.blit(begin_text,(begin_button.x, begin_button.y)) 

        if deal_randoms_display==True:
        
            randomize_text = font2.render('Give opponents random hidden cards', True, 'white')
            if hidden_cards.x<= a < hidden_cards.x+325 and  hidden_cards.y <= b <=  hidden_cards.y+22 and play_hand ==True and show_cards==False:
                pygame.draw.rect(screen, (180,180,180), hidden_cards)
            elif play_hand==True and show_cards==False:
                pygame.draw.rect(screen, (0,128,0), hidden_cards)
            if play_hand==True and show_cards==False:
                screen.blit(randomize_text,(hidden_cards.x, hidden_cards.y)) 


        #will display the random cards
        if deal_randoms ==True:
            if copy_indicator == False:
                add_card_copy = add_card.copy()
                copy_indicator=True
            for i in add_card_copy:
                if i !="user1" and i!="user2" and i!="board1" and i!="board2" and i!="board3" and i!="board4" and i!="board5":
                    screen.blit(pygame.transform.scale(blank_card, (80,105)), (add_card_copy[i][2].x, add_card_copy[i][2].y))
                    if pop_indicator == True:
                        add_card.pop(i)
            pop_indicator=False
            



            




        pygame.display.update()
    


main()
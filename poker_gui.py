from operator import truediv
from os import environ
from re import L
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from Setup_deal import *
import winners_circle
import probability
import copy
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
#make a dictionary with all needed information for all add player buttons
def addplayer():
    
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
#initializes the buttons for adding cards to players and board
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
#finds the probabilty of each possible position of the hand
def find_probability(round1, deal_randoms):
    if len(round1.table_cards) == 0 and deal_randoms==True:
        round_sub = copy.deepcopy(round1)
        percentage = probability.probability_preflop_hidden(round_sub, round1.player_count, False)
    elif len(round1.table_cards) == 0 and deal_randoms==False:
        round_sub = copy.deepcopy(round1)
        percentage = probability.probability_preflop_revealed(round_sub, round1.player_count, False)
    elif len(round1.table_cards) == 1 and deal_randoms==True:
        round_sub = copy.deepcopy(round1)
        percentage = probability.probability_postflop_hidden(round_sub, round1.player_count, False,  1)
    elif len(round1.table_cards) == 1 and deal_randoms==False:
        round_sub = copy.deepcopy(round1)
        percentage = probability.probability_postflop_revealed(round_sub, round1.player_count, False,  4)
    elif len(round1.table_cards) == 2 and deal_randoms==True:
        round_sub = copy.deepcopy(round1)
        percentage = probability.probability_postflop_hidden(round_sub, round1.player_count, False,  2)
    elif len(round1.table_cards) == 2 and deal_randoms==False:
        round_sub = copy.deepcopy(round1)
        percentage = probability.probability_postflop_revealed(round_sub, round1.player_count, False,  3)
    elif len(round1.table_cards) == 3 and deal_randoms==True:
        round_sub = copy.deepcopy(round1)
        percentage = probability.probability_postflop_hidden(round_sub, round1.player_count, False,  3)
    elif len(round1.table_cards) == 3 and deal_randoms==False:
        round_sub = copy.deepcopy(round1)
        percentage = probability.probability_postflop_revealed(round_sub, round1.player_count, False,  2)
    elif len(round1.table_cards) == 4 and deal_randoms==True:
        round_sub = copy.deepcopy(round1)
        percentage = probability.probability_postflop_hidden(round_sub, round1.player_count, False,  4)
    elif len(round1.table_cards) == 4 and deal_randoms==False:
        round_sub = copy.deepcopy(round1)
        percentage = probability.probability_postflop_revealed(round_sub, round1.player_count, False,  1)  

    elif len(round1.table_cards) == 5 and deal_randoms==True:
        round_sub = copy.deepcopy(round1)
        percentage = probability.proability_allcards_hidden(round_sub, round1.player_count, False)        

    return percentage
#returns the info of the player based on the add player button
#it will return which outlined cards need to be added to add_card dictionary. 
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
#this will play and display the GUI
def play():
    # All Flags 
    reveal_cards_flag = False # flags if user wants to reveal opponent's hidden cards
    dont_add_flag = False #flag for if user len(cards) is not 0 or 2
    winning_flag = False #flag that indicates if winner has been determined
    waiting_flag = False #flag that indicates if we're currently calculating probabiltiy
    player_flag = False #flag that indicates if each player has two cards
    copy_indicator=False #flag that indicates if add_card dictionary has been copied
    pop_indicator = True #flags if we have popped all random cards from add_card
    running = True #determines if the game is running
    play_hand = False #determines if poker object intitalized/indicates start of game
    deal_randoms = False #indicates if the opponents cards are randomly dealt and hidden
    begin_game_bool =False #indicates start of game of random cards dealt
    show_cards=False #indicates if all cards are displayed to be picked from
    deal_randoms_display = True #indicates if the button for deal randoms is displayed
    random_cards = {} #keys are players and values are hidden cards that are random 
    #percentage will be the probability of winning. We set to -1 because we set it 
    #at a invalid state
    percentage = -1 
    #will contain information of board cards
    board= 0 
    #playerss will be string 'player#' key for the dictionary 'cards
    playerss = 0
    #will be either user1 or user2 to indicate which of the user's cards to addcard to
    user =0
    #indicates number of players in the round
    num_player = 1
    #this will be used to display cards in ascending order in interface
    value_cards=["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", \
        "King", 'default']
    FPS_CLOCK = pygame.time.Clock()
    #intializing the game
    pygame.init()
    #setting dimensions of display
    screen = pygame.display.set_mode((1200, 775))
    #name
    pygame.display.set_caption("Poker")
    #displays green background
    screen.fill([0,128,0])
    #indicator that checks if a slot has been chosen
    #unsorted cards will be the png files in unsorted order
    unsorted_cards = []
    #this will iterate through the file and append the file names in unsorted_cards
    rect(screen)
    directory = 'Playing_Cards'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        unsorted_cards.append(f)
    #intiailzing sorted_cards. This will append the png files from Ace-King in image 
    #form for pygame
    sorted_cards=[]
    #this will be used later to indicate which card has been chosen
    listOfcards = []
    #value cards go in ascending order, so we append to sorted_cards from smallest
    #to biggest
    #font and surf for the add_card
    font = pygame.font.SysFont('Arial', 15, bold = True)
    surf = font.render('', True, 'white')
    #font and text to tell user to add players
    font2 = pygame.font.SysFont('Arial', 18, bold = True)
    begin_game_text = font.render('Please add players before starting the hand', True, 'white')
    #appends cards from A-K to listOfcards and card images from A-K to sorted cards
    for i in range(len(value_cards)):
        for j in range(len(unsorted_cards)):
            if value_cards[i] in unsorted_cards[j]:
                sorted_cards.append(pygame.image.load(unsorted_cards[j]))
                listOfcards.append(unsorted_cards[j])
    #returns a dictionaries of all things needed to make a add player button
    player = addplayer()
    #setting the blank card equal to the image of the face down card
    blank_card = sorted_cards[52]
    #add_card will contain all available information for each add card first indice will 
    #hold the font info, second indice holds the surface info, and third holds rectangle info
    add_card = init_addcard()
    #add_player_num keeps track of number of players in game
    add_player_num = 1
    #list of all chosen cards
    all_chosen_cards = []
    #remove will contain all keys we need to remove from 'player' dictionary
    remove = []
    #will contain the information of the just popped information from player
    temp = []
    #removal will contain which add_card button that was just clicked
    removal=0
    #contains all surfaces of the chosen card
    chosen_card = []
    #contiains all rectangle information for each chosen card
    chosen_card2=[]
    #All information below are rectangle, font, and text information for display
    reveal_cards =  pygame.Rect(535, 550, 95, 22) 
    begin_text = font2.render('Play Hand!', True, 'white')
    reset_text = font2.render('Reset!', True, 'red')
    reset_button = pygame.Rect(20, 20, 55, 20)
    begin_button = pygame.Rect(556, 450, 95, 22)
    hidden_cards = pygame.Rect(425, 450, 325, 22)
    find_prob = pygame.Rect(365, 450, 450, 22)
    find_prob_text = font2.render('Click Here To Calculate Your Percentage of Winning!', True, 'white')
    
    card = {}
    percent_button = pygame.Rect(510, 640, 90, 20)
    while running:    #checks each event and see if it should quit
        #screen fill makes bacground green
        screen.fill([0,128,0])
        #draws all the empty slots of cards
        rect(screen)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):
                    #quits if we click escape
                    return False
            elif (event.type == pygame.QUIT):
                #quits if we click x button in top right
                return False
            #if we click on start game, begin the game. There must be atleast 2 players
            if event.type == pygame.MOUSEBUTTONDOWN and play_hand == False:
                if begin_button.collidepoint(event.pos) and add_player_num!=1:
                    round1 = Poker(num_player)
                    play_hand=True
            #finds which add player button you clicked and adds player number and creates
            #add card button for that player
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
            #if cards are being chosen and the user clicks on the screen
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
                #if the indice of where you picked is in the bounds of sorted_cards, we know the user clicked on
                #one of the cards. This means we need to use the chosen card and add it to the player's hand
                if indice<len(sorted_cards)-1 and indice > -1:
                    #getting rid of the card we picked because should not be in the deck anymore
                    one_card = sorted_cards.pop(indice)
                    #appending the all_chosen_cards which are all the image cards we've chosen
                    all_chosen_cards.append(one_card)
                    #storing what card was just popped from listOfcards
                    card_removed= listOfcards.pop(indice)
                    #after we click on a valid indice, we don't want to display the cards anymore because
                    #we just picked a card
                    show_cards = False
                    chosen_card.append(removal3)
                    chosen_card2.append(removal2)
                    #this appends all chosen cards to the dictionary. If that player, user, or table_card
                    #doesn't already have cards, create a new key value 
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
                        if len(card[i])==1:
                            dont_add_flag= True
                        else:
                            dont_add_flag= False
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
            elif play_hand==True and event.type == pygame.MOUSEBUTTONDOWN:
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
                            #if user doesnt exist in the dictionary, make it a key with value of list
                            if user not in card:
                                
                                card[user] = []

                        elif "board" in i:
                            #slices it so that the the key is 'player#'
                            board = i[0:5]
                            #if board doesnt exist in the dictionary, make it a key with value of list
                            if board not in card:
                               
                                card[board] = []

                        removal = i
                        removal2 = add_card[i][2]
                        removal3 = add_card[i][1] 
                        if i !="user1" and i!="user2" and i!="board1" and i!="board2" and i!="board3" and i!="board4" and i!="board5":
                            deal_randoms_display=False
                
                        break
            
            #if we click on find probability, display the calculating text 
            if (event.type == pygame.MOUSEBUTTONDOWN and player_flag == True): 
                if find_prob.collidepoint(event.pos):
                    waiting = font2.render('Calculating.............', True, 'white')
                    screen.blit(waiting,(540, 300))
                    #pygame.draw.rect(screen, (0,128,0), waiting_button)
                    #this will later be used to indicate if we should find the probaility 
                    waiting_flag=True
    
            #this will be an indicator if we choose random card for opponents
            if event.type == pygame.MOUSEBUTTONDOWN and show_cards==False and play_hand==True and deal_randoms == False and \
                deal_randoms_display!=False and dont_add_flag==False:
                if begin_game_bool == False:
                    begin_game_bool=True
            #if we give cards hidden cards, we call the method that does so for the class poker, then set the indicators
                elif hidden_cards.collidepoint(event.pos):
                    round1.randomize_other_empty()
                    #setting all used randomized hidden cards in list of cards and sorted cards equal to 0 because we dont
                    #need those cards anymore because they're already used
                    flag = 0
                    for i in round1.player:
                        if flag !=0:
                            for j in range(len(listOfcards)):
                                if listOfcards[j] !=0 and str(round1.player[i][0][0]) in listOfcards[j] and round1.player[i][0][1] in listOfcards[j] :
                                    listOfcards[j]=0
                                    if i not in random_cards:
                                        random_cards[i] = []
                                    random_cards[i].append(sorted_cards[j])
                                    
                                    sorted_cards[j] = 0
                                elif listOfcards[j] !=0 and str(round1.player[i][1][0]) in listOfcards[j] and round1.player[i][1][1] in listOfcards[j] \
                                    and listOfcards[j] !=0:
                                    listOfcards[j]=0
                                    if i not in random_cards:
                                        random_cards[i] = []
                                    random_cards[i].append(sorted_cards[j])
                                    sorted_cards[j] = 0
                        else:
                            flag=1

                    #removes all cards from the sorted cards deck because they are being used now
                    acc = 0
                    for i in range(len(listOfcards)):
                        if listOfcards[acc]==0:
                            listOfcards.pop(acc)
                            sorted_cards.pop(acc)
                        else:
                            acc=acc+1
                    deal_randoms=True
                    deal_randoms_display=False


            #if we reveal cards, then deal_randoms is now set to false because we now see the cards
            if event.type == pygame.MOUSEBUTTONDOWN and play_hand==True and deal_randoms == True and reveal_cards_flag ==True and \
                reveal_cards.collidepoint(event.pos):
                deal_randoms = False



            #resets the game
            if event.type == pygame.MOUSEBUTTONDOWN and reset_button.collidepoint(event.pos):
                return True
                     
        a,b = pygame.mouse.get_pos()

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
            #print(all_chosen_cards)
            screen.blit(pygame.transform.scale(all_chosen_cards[i], (80,105)), (chosen_card2[i].x, chosen_card2[i].y))
            

        #reveals the cards to the table
        if deal_randoms == False and reveal_cards_flag ==True:
            for i in range(2, round1.player_count+1):
                card1 = random_cards[i][0]
                card2 = random_cards[i][1]
                string1 = "Player" + str(i) + "first_card"
                string2= "Player" + str(i) + "second_card"
                screen.blit(pygame.transform.scale(card1, (80,105)), (random_cards[string1][2].x, random_cards[string1][2].y))
                screen.blit(pygame.transform.scale(card2, (80,105)), (random_cards[string2][2].x, random_cards[string2][2].y))
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

        #if we've dealed hidden cards and the user either has 0 or two cards, display a button that will reveal the cards
        if play_hand ==True and deal_randoms_display==True and dont_add_flag ==False:        
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
                        random_cards[i]=add_card.pop(i)
            pop_indicator=False


        #displays the find probability button if conditions are met
        if (play_hand==True and len(round1.table_cards) < 5 and show_cards == False and deal_randoms == False)\
            or play_hand == True and show_cards == False and deal_randoms == True:
            if player_flag == False:
                player_acc = 0
                for i in round1.player:
                    if len(round1.player[i])==2:
                        player_acc =player_acc+1

            if player_acc == round1.player_count:
                
                player_flag = True
                pygame.draw.rect(screen, (0,128,0), find_prob)
                screen.blit(find_prob_text,(find_prob.x, find_prob.y)) 
        
        #if user clicked to find the percentage and show cards is false, then display the percentage of winning
        if percentage != -1 and show_cards == False and winning_flag ==False:
            percent_display = str(percentage) + "% of Winning "
            percent_text = font2.render(percent_display, True, 'white')
            screen.blit(percent_text,(percent_button.x, percent_button.y)) 
        
        #if all cards are layed out on table and all cards are revealed, display the winner
        if play_hand ==True and len(round1.table_cards) == 5 and deal_randoms == False:
            if winning_flag == False:
                player_acc = 0
                for i in round1.player:
                    if len(round1.player[i])==2:
                        player_acc =player_acc+1
            if winning_flag==False and player_acc == round1.player_count:
                #finds the player that won
                winner = winners_circle.winning_players(round1.player, round1.table_cards, round1.player_count, False)
                winning_flag=True
                text = font2.render("Winner!", True, 'green')
            if winning_flag ==True:
                for i in temp:
                    if i[1] in winner:
                        pygame.draw.rect(screen, (0,128,0), i[0])
                        screen.blit(text,(i[0].x+15, i[0].y)) 
                if 1 in winner:
                    screen.blit(text,(percent_button.x+50, percent_button.y -10)) 


            
        #if we're in the hand and players have hidden cards, always have a reveal card button
        if play_hand == True and deal_randoms == True:
            
            if reveal_cards_flag ==False:
                player_acc = 0
                for i in round1.player:
                        if len(round1.player[i])==2:
                            player_acc =player_acc+1
            if player_acc == round1.player_count:
                reveal_cards_flag = True
            if player_acc == round1.player_count and reveal_cards_flag ==True:
                percent_text = font2.render("Reveal Cards", True, 'white')
                screen.blit(percent_text,(reveal_cards.x, reveal_cards.y)) 

        screen.blit(reset_text, (reset_button.x, reset_button.y))    
        pygame.display.update()
        #if we've clicked to find probability, find the probablity in the background
        if waiting_flag ==True:
            percentage = find_probability(round1, deal_randoms)
            waiting_flag = False







    



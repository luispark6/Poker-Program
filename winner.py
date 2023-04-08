
def straight(table_cards, player):
    ordered_7 = {}
    player_list=[]
    face = 0
    #sets table card value to integer if its a face card
    for i in range(5):
        if table_cards[i][0] == "Ace": face = 1 
        elif table_cards[i][0] == "King": face = 13
        elif table_cards[i][0] == "Queen": face = 12
        elif table_cards[i][0] == "Jack": face = 11
        if face !=0:
            player_list.append(int(face))
            face= 0
        else: 
            player_list.append(int(table_cards[i][0]))
    #sets player cards to integer values and appends it to a list
    face = 0
    if player[0][0] == "Ace": face=1
    elif player[0][0] == "King": face=13
    elif player[0][0] == "Queen": face=12
    elif player[0][0] == "Jack": face=11
    if face !=0:
        player_list.append(int(face))
        face= 0
    else:
        player_list.append(int(player[0][0]))

    if player[1][0] == "Ace": face=1
    elif player[1][0] == "King": face=13
    elif player[1][0] == "Queen": face=12
    elif player[1][0] == "Jack": face=11
    if face !=0:
        player_list.append(int(face))
        face= 0
    else:
        player_list.append(int(player[1][0]))
    #calls quick sort on list 
    quickSort(player_list, 0, len(player_list)-1)
    straight_indicator = 0
    high_index =0 
    #indicates if a straight has been hit
    for i in range (len(player_list)-1):
        if player_list[i+1] == 13:
            if player_list[0]==1:
                straight_indicator = straight_indicator + 1
                
        if player_list[i]+1 == player_list[i+1]:
            straight_indicator = straight_indicator + 1
        elif player_list[i] == player_list[i+1]:
            straight_indicator=straight_indicator
        else:
            straight_indicator = 0
        if straight_indicator >3:
            high_index = i+1
    if high_index!=0:
        if player_list[high_index]==13 and player_list[0]==1:
            high_card = 14
        else:
            high_card = player_list[high_index]
        #returns True and the high card of the straight
        return [True, high_card]
    
    #returns False if straight has not been hit
    return [False, 0]




#checks for four of a kind
def four(table_cards, player):
    match = {
    }
    #appends the frequency of each card on the table in a dictionary
    for i in range(5):
        if table_cards[i][0] in match:
            match[table_cards[i][0]] = match[table_cards[i][0]]+1
        else:

            match[table_cards[i][0]] = 1
    #appends the frequency of the player's card in a dictionary
    if player[0][0] in match:
         match[player[0][0]]= match[player[0][0]]+1
    else:
        match[player[0][0]]=1
    if player[1][0] in match:
         match[player[1][0]]= match[player[1][0]]+1
    else:
        match[player[1][0]]=1
    card = 0
    #checks if frequency ever reaches four
    for i in match:
        if match[i]==4:
            #set the four of a kind to card
            card= i
            #break
    if card == 0:
        return [False, None]
    #sort the list now
    ordered_list_previous = high_card(table_cards, player)
    #pops all cards part of the four of a kind
    ordered_list = [value for value in ordered_list_previous if value !=card]

    #if there is a four of a kind, return True, card with four of a kind, and high card
   
    return[True, i , ordered_list[-1]]

def three(table_cards, player):
    match = {
    }
    #appends the frequency of each card on the table in a dictionary
    for i in range(5):
        if table_cards[i][0] in match:
            match[table_cards[i][0]] = match[table_cards[i][0]]+1
        else:

            match[table_cards[i][0]] = 1
     #appends the frequency of the player's card in a dictionary
    if player[0][0] in match:
        match[player[0][0]]= match[player[0][0]]+1
    else:
        match[player[0][0]]=1
    if player[1][0] in match:
         match[player[1][0]]= match[player[1][0]]+1
    else:
        match[player[1][0]]=1
     #checks if frequency ever reaches three
    card = []
    for i in match:
        if match[i]==3:
            #if frequency is three, set card = the card with three of a kind
            card.append(i)
    #if no three of a kind, return
    if card == []:
        return [False, None]
    #quantify face cards so we can sort them
    for i in range(len(card)):
        if card[i] == "King": card[i]=13
        elif card[i] == "Queen": card[i]=12
        elif card[i] == "Jack": card[i]=11
        elif card[i] == "Ace": card[i]=14
    quickSort(card, 0, len(card)-1)
    #pop all cards that are part of the three of a kind
    ordered_list_previous = high_card(table_cards, player)
    #We dont need to return the high cards for two three of a kind because
    #if we have two three of a kinds, then we have a full house, so we take
    #the highest three of a kind, and the other three of a kind will be counted 
    #as a pair
    if len(card)!=1:
        return [True, card, []]
    ordered_list = [value for value in ordered_list_previous if value not in card ]
    #if there is a three of a kind, return True, card with three of a kind, and two high cards
    #card should only have one element because this is the case for only one three of a kind
    return [True, card, [ordered_list[-1], ordered_list[-2]]]
def pair(table_cards, player):

    match = {
    }
    #appends the frequency of each card on the table in a dictionary
    for i in range(5):
        if table_cards[i][0] in match:
            match[table_cards[i][0]] = match[table_cards[i][0]]+1
        else:

            match[table_cards[i][0]] = 1
    #appends the frequency of the player's card in a dictionary
    if player[0][0] in match:
         match[player[0][0]]= match[player[0][0]]+1
    else:
        match[player[0][0]]=1
    if player[1][0] in match:
         match[player[1][0]]= match[player[1][0]]+1
    else:
        match[player[1][0]]=1
    list = []

    for i in match:
        #appends the pair to list
        if match[i]==2:
            list.append(i)
    #quantify face cards
    for i in range(len(list)):
        if list[i] == "King": list[i]=13
        elif list[i] == "Queen": list[i]=12
        elif list[i] == "Jack": list[i]=11
        elif list[i] == "Ace": list[i]=14
    #pops all values that are a pair value
    ordered_list_previous = high_card(table_cards, player)
    if len(list)==2:
        ordered_list = [value for value in ordered_list_previous if value != list[0] and value !=list[1]]
    if len(list)==1:
        ordered_list = [value for value in ordered_list_previous if value != list[0]]
    if len(list)==3:
        quickSort(list, 0, len(list)-1)
        list.pop(0)
        ordered_list = [value for value in ordered_list_previous if value != list[0] and value!=list[1]]
    if len(list)==1:
        return [True, list, [ordered_list[-1], ordered_list[-2], ordered_list[-3]]]
    #if there is a two pair, quicksort the list so that the last index is the higher
    #pair and return the 1 other high card and list
    elif len(list) == 2:
        #if there is a pair, return true and list of pairs
        quickSort(list, 0, len(list)-1)
        return [True, list, [ordered_list[-1]]]
    #if there are three pairs, then pop the smallest pair, then return list and the one
    #other high card 
    elif len(list)==3:
        return [True, list, [ordered_list[-1]]]
    #return false if no pairs
    return [False, list]



def flush(table_cards, player):
    suit = "Nothing"
    hit = False
    flush= {"Heart": [], "Diamond": [], "Clove": [], "Spade": []}
    #appends the players' card to index suit. 
    flush[player[0][1]].append(player[0][0])
    flush[player[1][1]].append(player[1][0])
   #appends table cards to index 'suit'
    for i in range(5):
        flush[table_cards[i][1]].append(table_cards[i][0])
    # if there are more than 4 items in a suit, we have found a flush
    for i in flush:
        if len(flush[i])>4:
            suit = i
            hit = True

    if hit == True:
        for i in range(len(flush[suit])):
            #quanitfy the face cards
            if flush[suit][i] == "King": flush[suit][i] =13
            if flush[suit][i] == "Queen": flush[suit][i] =12
            if flush[suit][i] == "Jack": flush[suit][i] =11
            if flush[suit][i] == "Ace": flush[suit][i] =14
        #quick sort the cards with flush
        quickSort(flush[suit], 0, len(flush[suit])-1)
        #return true and the high card of flush
        return [hit, flush[suit][-1]]
    else:
        #return false and empty list if no flush
        return[hit, suit]


def high_card(table_card, player):
    list=[]
    #quantify face cards and add to list. 
    for i in range(5):
        if table_card[i][0] == "King": list.append(13)
        elif table_card[i][0] == "Queen": list.append(12)
        elif table_card[i][0] == "Jack": list.append(11)
        elif table_card[i][0] == "Ace": list.append(14)
        else:
            list.append(table_card[i][0])
    for i in range(2):
        if player[i][0] == "King": list.append(13)
        elif player[i][0] == "Queen": list.append(12)
        elif player[i][0] == "Jack": list.append(11)
        elif player[i][0] == "Ace": list.append(14)
        else:
            list.append(player[i][0])
    #sort the list
    
    quickSort(list, 0, len(list)-1)
    #return the list
    return list


def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]
    # pointer for greater element
    i = low - 1
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    # Return the position from where partition is done
    return i + 1
# function to perform quicksort
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
 
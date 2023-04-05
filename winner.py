

def ordered_7(table_cards, player, player_count):
    ordered_7 = {}
    player_list=[]
    face = 0
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
    #for i in range(1, player_count+1):
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
    print(player_list)
    quickSort(player_list, 0, len(player_list)-1)

    return player_list


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
 
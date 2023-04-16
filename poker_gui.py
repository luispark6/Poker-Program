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


def addplayer():
    #create all buttons. Total should be 7
    player = {}
    font = pygame.font.SysFont('Arial', 15, bold = True)
    surf = font.render('Add Player +', True, 'white')
    addplayer1 = pygame.Rect(197, 710, 94, 20)
    player["player1"]= [font, surf, addplayer1]
    #player["player2"]= [font, surf, addplayer1]
    return player


def main():
    #this will be used to display cards in ascending order in interface
    value_cards=["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
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
    #unsorted cards will be the png files in unsorted order
    unsorted_cards = []
    #this will iterate through the file and append the file names in unsorted_cards
    rect(screen)
    directory = 'cards'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        unsorted_cards.append(f)
    #intiailzing sorted_cards. This will append the png files from Ace-King
    sorted_cards=[]
    #value cards go in ascending order, so we append to sorted_cards from smallest to biggest
    
    for i in range(len(value_cards)):
        for j in range(len(unsorted_cards)):
            if value_cards[i] in unsorted_cards[j]:
                sorted_cards.append(pygame.image.load(unsorted_cards[j]))
    #returns a dictionaries of all things needed to make a button
    player = addplayer()
    while running:    #checks each event and see if it should quit
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):
                    running = False
            elif (event.type == pygame.QUIT):
                return
        a,b = pygame.mouse.get_pos()
        #idea is loop through all of player and see if player button is hovered over
        if player["player1"][2].x<= a <player["player1"][2].x+94 and player["player1"][2].y <= b <= player["player1"][2].y+20:
            pygame.draw.rect(screen, (180, 180, 180), player["player1"][2])
        else:
            pygame.draw.rect(screen, (0,128,0), player["player1"][2])
        
        screen.blit(player["player1"][1],(player["player1"][2].x, player["player1"][2].y))
        
        pygame.display.update()
main()
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


def main():
    #intializing the game
    FPS_CLOCK = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((1200, 775))
    pygame.display.set_caption("Poker")
    AceofClubs = pygame.image.load("cards/Ace of Clubs.png")
    x= 0
    y=695
    screen.fill([0,128,0])
    pygame.display.flip()
    running = True
    list = []
    directory = 'cards'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(f)
            list.append(pygame.image.load(f))

    j= 0
    while running:    #checks each event and see if it should quit
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):
                    running = False
            elif (event.type == pygame.QUIT):
                return
            if j ==0:
                for i in range(len(list)):
                    j=1
                    screen.blit(pygame.transform.scale(list[i], (60, 70)), (x,y))
                    x=x+60
                    if i == 20 or i==40:
                        y=y-70
                        x=0
                pygame.display.update()
        pygame.display.update()





main()
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


def main():
    #intializing the game
    FPS_CLOCK = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((1000, 775))
    pygame.display.set_caption("Poker")
    screen.fill([0,128,0])
    pygame.display.flip()

    running = True
    while running:    #checks each event and see if it should quit

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):
                    running = False
            elif (event.type == pygame.QUIT):
                return






main()
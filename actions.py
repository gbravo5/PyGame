import pygame
from pygame.locals import *
import sys
import random

def move_forward(self):
    gameover = False
    while not gameover:
        # manage events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.coordinates_participant[0] +=  random.randint(1, 6)
        if self.coordinates_participant[0] >= self.finishline:
            gameover = True
        # update
        self.update()
        # refresh
        self.refresh()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
def move_all_direction(self):
    gameover = False
    while not gameover:
        # manage events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_UP:          
                    # up arrow
                    self.coordinates_participant[1] -=  5
                elif event.key == K_DOWN:
                    # down arrow
                    self.coordinates_participant[1] +=  5
                elif event.key == K_LEFT:
                    # left arrow
                    self.coordinates_participant[0] -=  5
                elif event.key == K_RIGHT:
                    # right arrow
                    self.coordinates_participant[0] +=  5
                else:
                    pass
        # update
        self.update()
        # refresh
        self.refresh()
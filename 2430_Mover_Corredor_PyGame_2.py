import pygame
from pygame.locals import *
import sys
import random

class Game():

    # assumptions:
    
    # 1.- screen:
        # size
    screen_size = width, height = 640, 480
        # title
    game_title = 'Mover_Corredor_PyGame'
        # background
    coordinates_background = 0, 0
    game_background = 'images/circuito.png'

    
    # 2.- participants:
    
    participants  = ('fish', 'moray', 'octopus', 'smallball', 'turtle', 'prawn')
    
    startline = 5/100 * width
    finishline = 95/100 * width
    
    def __init__(self):
        
        # 1.- screen:
        # a) create
        self.screen = pygame.display.set_mode(self.screen_size)
        # b) customize
            # title
        pygame.display.set_caption(self.game_title)
            # background
        self.background = pygame.image.load(self.game_background)
        
        # 2.- participants:
        
        ix_participant = random.randint(0, len(self.participants) -1)
        
        x_coordinate_participant = self.startline
        y_coordinate_participant = 1/2 * self.height
        
        self.name = self.participants[ix_participant]
        self.custome = pygame.image.load('images/{}.png'.format(self.name))
        self.coordinates_participant = [x_coordinate_participant, y_coordinate_participant]


    def update(self):
        # a) draw screen
        self.screen.blit(self.background, self.coordinates_background)
        # b) draw runner
        self.screen.blit(self.custome, self.coordinates_participant)
        
    def refresh(self):
        pygame.display.flip()
        
     # actions
    
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
        
if __name__ == '__main__':
    
    pygame.init()
    play = Game()
    #play.move_all_direction()
    play.move_forward()
    
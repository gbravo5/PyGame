import pygame
import actions
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
        actions.move_forward(self)
                    
    def move_all_direction(self):
        actions.move_all_direction(self)
        
if __name__ == '__main__':
    
    pygame.init()
    play = Game()
    play.move_all_direction()
    #play.move_forward()
    
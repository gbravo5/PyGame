import pygame
import sys
import random

class Runner():
    
    def __init__(self, nb_participants):
        self.__nb_participants = nb_participants
        # maximum number of participants = 6
        images = ('images\001-fish.png', '005-moray.png', '003-octopus.png','006-smallball.png', '002-turtle.png', '004-prawn.png')
        participants = ('fish', 'moray', 'octopus', 'smallball', 'turtle', 'prawn')
        x_coordinate_participant = self.__startline
        y_coordinate_participant = (0.15 * height, 0.30 * height, 0.45 * height, 0.60 * height, 0.75 * height, 0.90 * height)
        
        for i in range(self.__nb_participants):
            # participants setup:
            self.__name = participants[i]
            self.__participant = pygame.image.load(images[i])
            self.__coordinates_participant = x_coordinate_participant, y_coordinate_participant[i]

    def move(self):
        # x_coordinate
        self.__coordinates_participant[0] +=  random.randint(1, 6)    
                  
class Game():
    
    listofparticipants = []
    
    def __init__(self):
        
        # 1.- screen setup:
        # a) create
        size = width, height = 640, 480
        self.__screen = pygame.display.set_mode(size)
        # b) customize
            # title
        pygame.display.set_caption('Carrera_PyGame')
            # background
        self.__background = pygame.image.load("images\circuito_2.png")
            # start_finish_lines
        self.__startline = 5/100 * width
        self.__finishline = 95/100 * width
            
        
        # 2.- load participants:
        
        runner = Runner()
        
        
        
    
    def compete(self):
    
        winner = False
        
        while not winner:  
            # manage events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
        
            # update
                # a) screen
                # t = 0
            self.__coordinates_background = x_coordinate_background, y_coordinate_background = 0, 0
            self.__screen.blit(self.__background, self.__coordinates_background)
                # t
                
                # b) runners
                
            self.__screen.blit(self.__participant, coordinates_participant)
                
            
            x_coordinate_participants += 3
            if x_coordinate_participants >= 250:
               winner = True
            
            # refresh
            pygame.display.flip()
            
               
        sys.exit()

if __name__ == '__main__':
    
    pygame.init()
    race = Game()
    race.compete()
        
        
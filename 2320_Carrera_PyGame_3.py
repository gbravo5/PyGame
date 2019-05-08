import pygame
import sys
import random

class Runner():
    
    def __init__(self, i, startline, height):
        
        # maximum number of participants = 6
        __participants = ('fish', 'moray', 'octopus', 'smallball', 'turtle', 'prawn')
        
        __x_coordinate_participant = startline
        __y_coordinate_participant = (0.15 * height, 0.30 * height, 0.45 * height, 0.60 * height, 0.75 * height, 0.90 * height)
        
        self.name = __participants[i]
        self.custome = pygame.image.load('images/{}.png'.format(__participants[i]))
        self.coordinates_participant = [__x_coordinate_participant, __y_coordinate_participant[i]]

    def move(self):
        # x_coordinate
        self.coordinates_participant[0] +=  random.randint(1, 6)
 

class Game():
    
    listofrunners = []
    
    def __init__(self, nb_participants):
        self.__nb_participants = nb_participants
        # 1.- screen:
        # a) create
        size = __width, __height = 640, 480
        self.__screen = pygame.display.set_mode(size)
        # b) customize
            # title
        pygame.display.set_caption('Carrera_PyGame')
            # background
        self.__background = pygame.image.load("images/circuito_2.png")
            # start_finish_lines
        self.__startline = 5/100 * __width
        self.__finishline = 95/100 * __width
        # 2.- participants:
        # class Runner() ---> create + customize each participant
        for i in range(self.__nb_participants):
            runner = Runner(i, self.__startline, __height)
            # refill listofparticipants
            self.listofrunners.append(runner)
   
    def compete(self):
        winner = False
        while not winner:
            # manage events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            for runner in self.listofrunners:
                runner.move()
                if runner.coordinates_participant[0] >= self.__finishline:
                    print('the runner {} has won'.format(runner.name))
                    winner = True
                    break
            # update
                # a) draw screen
            self.__coordinates_background = 0, 0
            self.__screen.blit(self.__background, self.__coordinates_background)
                # b) draw runners
            for runner in self.listofrunners:
                self.__screen.blit(runner.custome, runner.coordinates_participant)
            # refresh
            pygame.display.flip()


if __name__ == '__main__':
    
    pygame.init()
    race = Game(4)
    race.compete()    
        
# blit ()        
#        draw one image onto another
#        blit(source, dest, area=None, special_flags = 0)
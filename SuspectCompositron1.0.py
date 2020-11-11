#Suspect Compositron 2000

import pygame
import sys
import FaceParts

pygame.init() #starts er up

screen = pygame.display.set_mode((800,480))

####################### VARIABLES SETUP ##############################
finished = False #while-loop breaker-outer



#######################ARTWORK SETUP ##############################

#BACKGROUND - load, scale to match the screen size, blit to screen at 0,0
#backgroundImage = pygame.image.load("background.png")
#backgroundImage = pygame.transform.scale(backgroundImage, (900,700))
#screen.blit(backgroundImage, (0,0))
#blank out screen between printings of rectangle
black = (0,0,0)
white = (255,255,255)
screen.fill(black)

#start point and w/h of background rectangle for faces
rect1X = 10
rect1Y = 10
rect1W = 380
rect1H = 460

faces = [["4Scalp.png", "4Eyes.png","4Nose.png","4Mouth.png","4Chin.png","4earL.png","4earR.png"],
         ["16Scalp.png", "16Eyes.png","16Nose.png","16Mouth.png","16Chin.png","16earL.png","16earR.png"]
         ]
print (faces[0][0])

forehead = pygame.image.load(faces[0][0])
#forehead = pygame.transform.scale(forehead, (264,108))
forehead = forehead.convert_alpha()




#######################################################################


######################## MAIN LOOP START #############################

while finished == False:
    
#EVENT LISTENER
    for event in pygame.event.get(): #all-events object.  get returns array
        #CHECK FOR QUIT
        if event.type == pygame.QUIT: #also getting collects garbage
            finished = True  #exit while loop and game

    #blank out screen between printings of rectangle
    screen.fill(black)

    #Print square that goes behind photo pieces
    rectOne = pygame.Rect(rect1X, rect1Y, rect1W, rect1H)
    pygame.draw.rect(screen, white, rectOne)

    #print face parts
    screen.blit(forehead, (20,20))

    #UPDATE display
    pygame.display.flip()


#################### END OF WHILE LOOP EXIT #######################
print ("exited while loop")

#the below freezes in idle but might work if called from terminal
#pygame.QUIT

#the below doesn't work
#sys.exit()

#this works but does a verify pop-up box
quit()

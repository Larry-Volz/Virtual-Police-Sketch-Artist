#Suspect Compositron 2000

import pygame
import sys
import FaceParts
import random

pygame.init() #starts er up

screen = pygame.display.set_mode((800,480))

####################### VARIABLES SETUP ##############################
finished = False #while-loop breaker-outer



#######################ARTWORK SETUP ##############################

#BACKGROUND - load, scale to match the screen size, blit to screen at 0,0
#backgroundImage = pygame.image.load("background.png")
#backgroundImage = pygame.transform.scale(backgroundImage, (900,700))
#screen.blit(backgroundImage, (0,0))
#blank out screen between re-printings/changing of pictures
black = (0,0,0)
white = (255,255,255)
screen.fill(black)
reDraw = 0

#start point and w/h of background rectangle for faces
rect1X = 10
rect1Y = 10
rect1W = 380
rect1H = 460

#start point and w/h of background rectangle for file number output
rect2X = 10 + 410
rect2Y = 480 - 80
rect2W = 360
rect2H = 60

#font for file number output

font = pygame.font.SysFont("times new roman",40)
font2 = pygame.font.SysFont("times new roman",25)
font3 = pygame.font.SysFont("times new roman",18)

#Random Beginning face:
#numberOfFaces should be the actual # of faces -1
numberOfFaces = 2
whichScalp = random.randint(0,numberOfFaces)
whichEyes = random.randint(0,numberOfFaces)
whichNose = random.randint(0,numberOfFaces)

#print("whichScalp: ", whichScalp)
#print("whichEyes: ", whichEyes)
#print("whichNose: ", whichNose)

#later do this with objects where with each facial feature you can also can include relative
#width and center to center them beneath the panel above them
faces = [["4Scalp.png", 264, 108,"04",
          "4Eyes.png",276, 103,"04",
          "4Nose.png", 297, 66,"04",
          "4Mouth.png",297, 64,"04",
          "4Chin.png",298, 67,"04",
          "4earL.png",264, 108,"04",
          "4earR.png",264, 108,"04"],
         ["16Scalp.png",322, 108,"16",
          "16Eyes.png",320, 108,"16",
          "16Nose.png",285, 60,"16",
          "16Mouth.png",264, 108,"16",
          "16Chin.png",264, 108,"16",
          "16earL.png",264, 108,"16",
          "16earR.png",264, 108,"16"],
         ["19Scalp.png",300,123,"19",
          "19Eyes.png",300,84,"19",
          "19Nose.png",298,74,"19",
          "19Mouth.png",300,50,"19",
          "19Chin.png",299,67,"19",
          "19earL.png",264, 108,"16",
          "19earR.png",264, 108,"16"]
         ]
###################### PRINT A FACE FUNCTIONS #############################

    
def outputForehead(whichScalp):
    
    #foreheadW = (imageW,imageH)
    foreheadW = (faces[whichScalp][1],faces[whichScalp][2])

    #beginning X for where to output it
    foreheadX = (380-faces[whichScalp][1])/2

    #calculations to output forehead
    forehead = pygame.image.load(faces[whichScalp][0])
    forehead = pygame.transform.scale(forehead, foreheadW)
    forehead = forehead.convert_alpha()

    #send to screen
    screen.blit(forehead, (foreheadX,20))

    #print("scalp #: "+faces[whichScalp][3])


def outputEyes(whichScalp, whichEyes):

    #get info for the element above this (forehead)
    forehead = pygame.image.load(faces[whichScalp][0])

    #beginning X for where to output eyes
    outputX = (380-faces[whichEyes][5])/2
    
    #beginning Y for where to output eyes (from previous element height)
    eyesStartH = forehead.get_height()+20
    
    #get preferred dimension of eyes from array
    eyesDim = (faces[whichEyes][5],faces[whichEyes][6])
    
    #calculations to output eyes
    eyes = pygame.image.load(faces[whichEyes][4])
    eyes = pygame.transform.scale(eyes, eyesDim)
    eyes = eyes.convert_alpha()

    #noseH = eyesStartH+eyes.get_height()
    
    #send to screen
    screen.blit(eyes, ((outputX),eyesStartH))

    #print("eyes #: " + faces[whichEyes][7])

def outputNose(whichScalp, whichEyes,whichNose):

    #get fileName for the elements above this
    #forehead = pygame.image.load(faces[whichScalp][0])
    #eyes = pygame.image.load(faces[whichEyes][3])

    #beginning X for where to output nose
    outputX = (380-faces[whichNose][9])/2
    
    #beginning Y for where to output nose (from previous element height)
    noseStartH = faces[whichScalp][2] + faces[whichEyes][6] + 20
    
    #get preferred dimension of nose from array
    noseDim = (faces[whichNose][9],faces[whichNose][10])
    
    #calculations to output eyes
    nose = pygame.image.load(faces[whichNose][8])
    nose = pygame.transform.scale(nose, noseDim)
    nose = nose.convert_alpha()
    
    #send to screen
    screen.blit(nose, ((outputX),noseStartH))

#################### PRE-GAME SCREEN PRINT##########################


#blank out screen between printings 
screen.fill(black)

#Print square that goes behind photo pieces
rectOne = pygame.Rect(rect1X, rect1Y, rect1W, rect1H)
pygame.draw.rect(screen, white, rectOne)

#print top right text
IPTFOutput = font2.render("Inter-precinct Task Force", True,(white))
IPTFOutput2 = font3.render("Suspect Composite Sketch Generator", True,(white))

screen.blit(IPTFOutput,(rect2X+10, 20))
screen.blit(IPTFOutput2,(rect2X+10, 45))

#Print square and file number output
rectTwo = pygame.Rect(rect2X, rect2Y, rect2W, rect2H)
pygame.draw.rect(screen, white, rectTwo)

fileNumber = faces[whichScalp][3] + faces[whichEyes][7] + faces[whichNose][11]
fileNumberRender = font.render(fileNumber, True, (black))
screen.blit(fileNumberRender,(rect2X+10,rect2Y+10))

#output badge
#badge dimensions = (imageW,imageH)
badgeDim = (240, 280)

#calculations to output badge
badge = pygame.image.load("police_badge.png")
badge = pygame.transform.scale(badge, badgeDim)
badge = badge.convert_alpha()

#send badge to screen
screen.blit(badge, (rect2X+40, 80))


#output initial face
outputForehead(whichScalp)
outputEyes(whichScalp, whichEyes)
outputNose(whichScalp, whichEyes,whichNose)

    
#UPDATE display
pygame.display.flip()


######################## MAIN LOOP START #############################

while finished == False:
    
    #EVENT LISTENER
    for event in pygame.event.get(): #all-events object.  get returns array
        #CHECK FOR QUIT
        if event.type == pygame.QUIT: #also getting collects garbage
            finished = True  #exit while loop and game

    ###CHECK FOR MOUSE CLICKING ON FOREHEAD ###
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            #print ("MOUSE CLICKED AT")
            #print (mx,my)

            leftEdge = (380-faces[whichScalp][1])/2
            rightEdge = (380-faces[whichScalp][1])/2 + faces[whichScalp][1]
            topEdge = 20
            bottomEdge = 20 + faces[whichScalp][2]

            if mx >= leftEdge and mx <= rightEdge and my >= topEdge and my <= bottomEdge:
                print("clicked on the SCALP")
                whichScalp +=1
                reDraw = 1
                if whichScalp > numberOfFaces:
                    whichScalp = 0

    ###CHECK FOR MOUSE CLICKING ON EYES ###
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            #print ("MOUSE CLICKED AT")
            #print (mx,my)

            leftEdge = outputX = (380-faces[whichEyes][5])/2
            rightEdge = outputX = leftEdge + faces[whichEyes][5]
            topEdge = 20 + faces[whichScalp][2]
            bottomEdge = topEdge + faces[whichEyes][6]

            if mx >= leftEdge and mx <= rightEdge and my >= topEdge and my <= bottomEdge:
                #print("clicked on the EYES")
                whichEyes +=1
                reDraw = 1
                if whichEyes > numberOfFaces:
                    whichEyes = 0

        ###CHECK FOR MOUSE CLICKING ON NOSE ###
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            #print ("MOUSE CLICKED AT")
            #print (mx,my)

            leftEdge = outputX = (380-faces[whichNose][9])/2
            rightEdge = outputX = leftEdge + faces[whichNose][9]
            topEdge = 20 + faces[whichScalp][2] + faces[whichEyes][6]
            bottomEdge = topEdge + faces[whichNose][6]

            if mx >= leftEdge and mx <= rightEdge and my >= topEdge and my <= bottomEdge:
                #print("clicked on the NOSE")
                whichNose +=1
                reDraw = 1
                if whichNose > numberOfFaces:
                    whichNose = 0


############################ RE-DRAW SCREEN ###############################

        if reDraw == 1:
            #blank out screen between printings of rectangle
            screen.fill(black)

            #Print square that goes behind photo pieces
            rectOne = pygame.Rect(rect1X, rect1Y, rect1W, rect1H)
            pygame.draw.rect(screen, white, rectOne)

            #Print square and file number output
            rectTwo = pygame.Rect(rect2X, rect2Y, rect2W, rect2H)
            pygame.draw.rect(screen, white, rectTwo)

            #print top right text
            IPTFOutput = font2.render("Inter-precinct Task Force", True,(white))
            IPTFOutput2 = font3.render("Suspect Composite Sketch Generator", True,(white))
            
            screen.blit(IPTFOutput,(rect2X+10, 20))
            screen.blit(IPTFOutput2,(rect2X+10, 45))

            fileNumber = faces[whichScalp][3] + faces[whichEyes][7] + faces[whichNose][11]
            fileNumberRender = font.render(fileNumber, True, (black))
            screen.blit(fileNumberRender,(rect2X+10,rect2Y+10))

            #output badge
            #badge dimensions = (imageW,imageH)
            badgeDim = (240, 280)

            #calculations to output badge
            badge = pygame.image.load("police_badge.png")
            badge = pygame.transform.scale(badge, badgeDim)
            badge = badge.convert_alpha()

            #send badge to screen
            screen.blit(badge, (rect2X+40, 80))


            outputForehead(whichScalp)
            outputEyes(whichScalp, whichEyes)
            outputNose(whichScalp, whichEyes,whichNose)

    
            #UPDATE display
            pygame.display.flip()

            reDraw = 0


#################### END OF WHILE LOOP EXIT #######################
#print ("exited while loop")

#the below freezes in idle but might work if called from terminal
#pygame.QUIT

#the below doesn't work
#sys.exit()

#this works but does a verify pop-up box
quit()






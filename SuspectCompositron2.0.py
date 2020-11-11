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

#font for text outputs

font = pygame.font.SysFont("times new roman",40)
font2 = pygame.font.SysFont("times new roman",25)
font3 = pygame.font.SysFont("times new roman",18)
fontFaceOptions = pygame.font.SysFont("times new roman", 14)

#Random Beginning face:
#numberOf____ should be the actual # of ____ -1
numberOfHeads = 2
numberOfWigs = 5 #one extra to take into account bald as option 5
numberOfEyes = 2
numberOfEars = 1
numberOfNoses = 4
numberOfLips = 2
whichHead = random.randint(0,numberOfHeads)
whichWig = random.randint(0,numberOfWigs)
whichEyes = random.randint(0,numberOfEyes)
print("whichEyes",whichEyes)
whichEars = random.randint(0,numberOfEars)
whichNose = random.randint(0,numberOfNoses)
whichLips = random.randint(0,numberOfLips)


heads = ["Head-1.png","Head-2.png","Head-3.png"]
wigs = ["Hair-1.png","Hair-2.png","Hair-3.png","Hair-4.png","Hair-5.png"]
ears = ["Ears-1.png","Ears-2.png"]
eyes = ["Eyes-1.png","Eyes-2.png","Eyes-3.png","Eyes-4.png","Eyes-5.png"]
noses = ["Nose-1.png","Nose-2.png","Nose-3.png","Nose-4.png","Nose-5.png"]
lips = ["Lips-1.png","Lips-2.png","Lips-3.png"]

#changeFaceText = "Change | Change | Change | Change | Change | Change"
changeFaceText2 ="Head    | Hair    |  Ears     |  Eyes   |  Nose    |  Mouth"
###################### PRINT A FACE FUNCTIONS #############################

    
def outputHead(whichHead):
    
 #calculations to output head
    head = pygame.image.load(heads[whichHead])
    head = pygame.transform.scale(head, (440,480))
    head = head.convert_alpha()

    #send to screen
    screen.blit(head, (-30,20))
    

def outputWig(whichWig):

    if whichWig !=5:
        #calculations to output hair
        wig = pygame.image.load(wigs[whichWig])
        wig = pygame.transform.scale(wig, (440,480))
        wig = wig.convert_alpha()

        #send to screen
        screen.blit(wig, (-30,20))

def outputEars(whichEars):

    ear = pygame.image.load(ears[whichEars])
    ear = pygame.transform.scale(ear, (440,480))
    ear = ear.convert_alpha()

    #send to screen
    screen.blit(ear, (-30,20))

def outputEyes(whichEyes):
    
 #calculations to output eye
    eye = pygame.image.load(eyes[whichEyes])
    eye = pygame.transform.scale(eye, (440,480))
    eye = eye.convert_alpha()

    #send to screen
    screen.blit(eye, (-30,20))


def outputNose(whichNose):
    #calculations to output nose
    nose = pygame.image.load(noses[whichNose])
    nose = pygame.transform.scale(nose, (440,480))
    nose = nose.convert_alpha()

    #send to screen
    screen.blit(nose, (-30,20))

def outputLips(whichLips):
    #calculations to output nose
    mouth = pygame.image.load(lips[whichLips])
    mouth = pygame.transform.scale(mouth, (440,480))
    mouth = mouth.convert_alpha()

    #send to screen
    screen.blit(mouth, (-30,20))



#################### PRE-GAME SCREEN PRINT##########################


#blank out screen between printings 
screen.fill(black)

#Print square that goes behind photo pieces
rectOne = pygame.Rect(rect1X, rect1Y, rect1W, rect1H)
pygame.draw.rect(screen, white, rectOne)

#Print face changing options
#faceChangeRender = fontFaceOptions.render(changeFaceText, True,(black))
#screen.blit(faceChangeRender,(rect1X+10, rect1Y+420))
faceChangeRender = fontFaceOptions.render(changeFaceText2, True,(black))
screen.blit(faceChangeRender,(rect1X+40, rect1Y+410))


#print top right text
IPTFOutput = font2.render("Inter-precinct Task Force", True,(white))
IPTFOutput2 = font3.render("Suspect Composite Sketch Generator", True,(white))

screen.blit(IPTFOutput,(rect2X+10, 20))
screen.blit(IPTFOutput2,(rect2X+10, 45))

#Print square and file number output
rectTwo = pygame.Rect(rect2X, rect2Y, rect2W, rect2H)
pygame.draw.rect(screen, white, rectTwo)

fileNumber = str(whichHead+1)+str(whichWig+1)+str(whichEars+1)+str(whichEyes+1)+str(whichNose+1)+str(whichLips+1)
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
outputHead(whichHead)
outputWig(whichWig)
outputEars(whichEars)
outputEyes(whichEyes)
outputNose(whichNose)
outputLips(whichLips)

    
#UPDATE display
pygame.display.flip()


######################## MAIN LOOP START #############################

while finished == False:
    
    #EVENT LISTENER
    for event in pygame.event.get(): #all-events object.  get returns array
        #CHECK FOR QUIT
        if event.type == pygame.QUIT: #also getting collects garbage
            finished = True  #exit while loop and game

    ###CHECK FOR MOUSE CLICKING ON HEAD ###
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            #print ("MOUSE CLICKED AT")
            #print (mx,my)

            leftEdge = 51
            rightEdge = 78
            topEdge = 424
            bottomEdge = 432

            if mx >= leftEdge and mx <= rightEdge and my >= topEdge and my <= bottomEdge:
                print("clicked on the HEAD")
                whichHead = whichHead + 1
                reDraw = 1
                if whichHead > numberOfHeads:
                    whichHead = 0

    ###CHECK FOR MOUSE CLICKING ON HAIR ###
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            #print ("MOUSE CLICKED AT")
            #print (mx,my)

            leftEdge = 102
            rightEdge = 126
            topEdge = 421
            bottomEdge = 431

            if mx >= leftEdge and mx <= rightEdge and my >= topEdge and my <= bottomEdge:
                print("clicked on the HAIR")
                whichWig = whichWig + 1
                reDraw = 1
                if whichWig > numberOfWigs:
                    whichWig = 0
                    
    ###CHECK FOR MOUSE CLICKING ON EARS ###
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            #print ("MOUSE CLICKED AT")
            #print (mx,my)

            leftEdge = 151
            rightEdge = 177
            topEdge = 422
            bottomEdge = 432

            if mx >= leftEdge and mx <= rightEdge and my >= topEdge and my <= bottomEdge:
                print("clicked on the EARS")
                whichEars = whichEars + 1
                reDraw = 1
                if whichEars > numberOfEars:
                    whichEars = 0
                    
    ###CHECK FOR MOUSE CLICKING ON EYES ###
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            #print ("MOUSE CLICKED AT")
            #print (mx,my)

            leftEdge = 210
            rightEdge = 236
            topEdge = 422
            bottomEdge = 432

            if mx >= leftEdge and mx <= rightEdge and my >= topEdge and my <= bottomEdge:
                print("clicked on the EYES")
                whichEyes = whichEyes + 1
                reDraw = 1
                if whichEyes > numberOfEyes:
                    whichEyes = 0

###CHECK FOR MOUSE CLICKING ON NOSE ###
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            #print ("MOUSE CLICKED AT")
            #print (mx,my)

            leftEdge = 258
            rightEdge = 289
            topEdge = 422
            bottomEdge = 432

            if mx >= leftEdge and mx <= rightEdge and my >= topEdge and my <= bottomEdge:
                print("clicked on the NOSE")
                whichNose = whichNose + 1
                reDraw = 1
                if whichNose > numberOfNoses:
                    whichNose = 0

###CHECK FOR MOUSE CLICKING ON MOUTH ###
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            print ("MOUSE CLICKED AT")
            print (mx,my)

            leftEdge = 314
            rightEdge = 352
            topEdge = 422
            bottomEdge = 432

            if mx >= leftEdge and mx <= rightEdge and my >= topEdge and my <= bottomEdge:
                print("clicked on the NOSE")
                whichLips = whichLips + 1
                reDraw = 1
                if whichLips > numberOfLips:
                    whichLips = 0



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

            fileNumber = str(whichHead+1)+str(whichWig+1)+str(whichEars+1)+str(whichEyes+1)+str(whichNose+1)+str(whichLips+1)
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

            #output face to screen
            outputHead(whichHead)
            outputWig(whichWig)
            outputEars(whichEars)
            outputEyes(whichEyes)
            outputNose(whichNose)
            outputLips(whichLips)

            #Print face changing options
            faceChangeRender = fontFaceOptions.render(changeFaceText2, True,(black))
            screen.blit(faceChangeRender,(rect1X+40, rect1Y+410))

    
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






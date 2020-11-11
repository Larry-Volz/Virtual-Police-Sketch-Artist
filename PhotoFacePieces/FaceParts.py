#A class to define faces for the SuspectCompositron2000
#Should contain all variables for all the parts of each face
#including forehead, eyes, nose, mouth, chin and ears to start
#later may do it differently for sketches instead of photos
#

class FaceParts():
    #arguments are filenames of each facial part
    # , scalp, eyes, nose, mouth, chin, earL, earR
    def __init__(self, scalp):
        self.scalp = pygame.image.load(scalp)
        
        #self.eyes = eyes
        #self.nose = nose
        #self.mouth = mouth
        #self.chin = chin
        #self.earL = earL
        #self.earR = earT

    def getScalp():
        returnString = "fileName = " + self.scalp
        return (returnString)
        #return scalp.get_size()



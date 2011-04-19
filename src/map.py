import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.actor import Actor

class map:
    "class modeling the map"
    
    name = "no name"
    skin = ""
    
    def __init__(self, name, pos, scale, skin, sky, stars):
        self.name = name
        self.skin = skin
        self.model = loader.loadModel(skin)   
        self.model.setPos(pos[0], pos[1], pos[2])
        self.model.setScale(scale[0], scale[1], scale[2])
        self.model.reparentTo(render)
        
        self.sky = loader.loadModel(sky)
        self.sky_tex = loader.loadTexture(stars)
        self.sky.setTexture(self.sky_tex, 1)
        self.sky.setScale(scale[0]+100, scale[1]+100, scale[2]+100)
        self.sky.setPos(pos[0], pos[1], pos[2])
        self.sky.reparentTo(render)
        
    def setPosition(self, pos):
        self.model.setPos(pos)    
        
    def getPosition(self):
        return self.position
    
    def setScale(self, scale):
        self.model.setScale(scale)

    def getScale(self):
        return self.scale    
    
    def setSkin(self, skin):
        self.skin = skin

    def getSkin(self):
        return self.skin    
    
    def getModel(self):
        return self.model
    
    def info(self):
        return "Class map"+ str(self.name) +" , "+\
               "Skin:  "+ str(self.skin)
        
if (__name__ == "__main__"):
    print map.__doc__
    m = map("my map", [0, 0, 0], [0, 0, 0], "")
    print m.info()               
        

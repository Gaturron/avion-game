'''
Created on 05/01/2011

@author: fernando
'''
import direct.directbase.DirectStart
from pandac.PandaModules import *
import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject

class camera:
    "class modeling the camera"
    pos = [0, 0, 0]
        
    def __init__(self, model, name):
        self.model = model   
        
        self.cam = Camera(name)  
        self.cam1 = render.attachNewNode(self.cam)
        self.cam1.setName("camera "+name) 
        
        self.goWith = 1
        self.a = 0
            
    def move(self):
        if(self.goWith):
            #TODO: fix the soft camera
            difx = self.pos[0] - self.model.getX()
            dify = self.pos[1] - self.model.getY()     
            difz = self.pos[2] - self.model.getZ()  
            
            self.pos[0] = self.model.getX()
            self.pos[1] = self.model.getY()
            self.pos[2] = self.model.getZ()
            
            difx = 0
            dify = 0
            difz = 0
                                   
            self.cam1.setPos(self.model, difx*150, -150 + dify*150, 30-difz*150)
            #self.cam1.setPos(self.model, 0, -150, 30)
            self.cam1.lookAt(self.model)
        else:
            self.cam1.setHpr(self.model, 0,0,self.a)
        
    def setGoWith(self, a):
        self.goWith = a
    
    def getCamera(self):
        return self.cam1
    
    def moveForward(self):
        self.cam1.setPos(self.cam1,0, 5, 0)
        
    def moveBackward(self):
        self.cam1.setPos(self.cam1,0, -5, 0)
        
    def moveRight(self, model):
        self.a = self.a+2 
            
    def moveLeft(self, model):
        self.a = self.a-2
         
if (__name__ == "__main__"):
    print camera.__doc__
    
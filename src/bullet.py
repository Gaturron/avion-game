'''
Created on 10/01/2011

@author: fernando
'''
import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.actor import Actor
import os, sys

damage = 5
speed = 30
scale=[0.01,0.01,0.01]

class bullet:
    "class modeling the bullets"

    def __init__(self, model, dir):
        mydir = os.path.dirname(sys.path[0])
        mydir = Filename.fromOsSpecific(mydir).getFullpath()
        mydir = mydir + "/models/bombs/bullet.egg"
        
        self.model = loader.loadModel(mydir)
        self.model.setScale(scale[0], scale[1], scale[2])
        self.model.setPos(model, 0, 8, 0)
        self.model.reparentTo(render)
        
        self.model.setHpr(dir)
    
    def delete(self):
        self.model.detachNode()
    
    def getModel(self):
        return self.model
    
    def setPos(self, pos):
        pass
    
    def setHpr(self, dir):
        self.model.setHpr(dir[0], dir[1], dir[2])
        
    def move(self):
        self.model.setPos(self.model,0,speed, 0)
        
    def getDamage(self):
        return damage
        
if(__name__ == "__main__"):
    print bullet.__doc__
        

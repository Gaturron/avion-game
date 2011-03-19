'''
Created on 06/03/2011

@author: fernando
'''
import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.actor import Actor
import os, sys, random

import math

from direct.task import Task
from particles import *

damage = 20
scale=[0.08,0.08,0.08]
time_to_live = 50000

class bomb:
    "class modeling the bombs"
    
    speed = 35

    def __init__(self, model, dir, x = 0, y = 0, z = 0):
        mydir = os.path.dirname(sys.path[0])
        mydir = Filename.fromOsSpecific(mydir).getFullpath()
        mydir = mydir + "/models/bombs/bomb.egg"
        
        self.model = loader.loadModel(mydir)
        self.model.setScale(scale[0], scale[1], scale[2])
        self.model.setPos(x, y, z)
        
        self.model.setHpr(dir)
                
        self.kill = 0
        self.active = 0
        self.timeGoStraight=0
        self.deltaPos = [0,0,0]
        
    #procedure to destroy
    def kill_myself(self, task):
        if(self.kill): Task.done    
        if(task.time > time_to_live):
            self.model.detachNode()
            x = self.model.getX()
            y = self.model.getY()
            z = self.model.getZ() 
            part = particles(x,y,z)
            taskMgr.add(part.particleSmoke,"parSmoke") 
            return Task.done
        else: 
            return Task.cont
    
    def activate(self, target):
        self.target = target
        #self.model.detachNode()
        self.model.reparentTo(render)
        taskMgr.add(self.kill_myself, "kill_myself")
        self.active = 1
            
    def delete(self):
        self.kill = 1
        self.model.detachNode()
        #self.model.removeNode()
        
    def getModel(self):
        return self.model
    
    def setPos(self, pos):
        pass
    
    def setHpr(self, dir):
        self.model.setHpr(dir[0], dir[1], dir[2])
        
    def move(self):
        if (self.active):
            if(self.timeGoStraight == 30): 
                
                difX = math.floor(math.fabs(self.model.getX() - self.target.getModel().getX())) 
                self.deltaPos[0] = random.randrange(difX*5, difX*6+1)
                
                difY = math.floor(math.fabs(self.model.getY() - self.target.getModel().getY())) 
                self.deltaPos[1] = random.randrange(difY*5, difY*6+1)
                
                difZ = math.floor(math.fabs(self.model.getZ() - self.target.getModel().getZ())) 
                self.deltaPos[2] = random.randrange(difZ*5, difZ*6+1)
              
            elif(self.timeGoStraight > 30):  
                self.model.lookAt(self.target.getModel(), self.deltaPos[0], self.deltaPos[1],self.deltaPos[2])  
            
                for i in range(0, 3):
                    if (self.deltaPos[i] < 0): self.deltaPos[i] += 1
                    if (self.deltaPos[i] > 0): self.deltaPos[i] -= 1
                        
            self.timeGoStraight = self.timeGoStraight+1
            self.model.setPos(self.model, 0, self.speed, 0)
        
    def getDamage(self):
        return damage
        
if(__name__ == "__main__"):
    print bomb.__doc__
import random
import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.actor import Actor
from panda3d.core import *

import math

from dynamicObject import *

from particles import *

#ranges and deltas
range_move = 55
delta_move = 5

range_angleR = 0
delta_angleR = 4

delta_angleH = 2
delta_angleV = 2

range_speed = 2
delta_speed = 0.8

class aircraft:
    "class modeling the aircraft"

    name = "no name"
    skin = ""
    
    power = 100
    speed = 2
    
    fall = 0
    
    def __init__(self, name, pos, scale, skin, c):
        self.name = name
        self.skin = skin
        self.model = loader.loadModel(skin)
        self.model.setScale(scale[0], scale[1], scale[2])
        self.model.setPos(pos[0], pos[1], pos[2])
        self.model.reparentTo(render)
        self.model.clearTexture()
        
        #texture
        self.myTexture = loader.loadTexture("White_a.png")
        self.myTexture.setWrapU(Texture.WMBorderColor)
        self.myTexture.setWrapV(Texture.WMBorderColor)
        
        ts = TextureStage('ts-'+str(self.name))
        ts.setMode(TextureStage.MBlend)
        
        vec = Vec4(c, 1-c, c, 1)
        
        ts.setColor(vec)
        print str(vec)
        print "real color: "+str(ts.getColor())
        print "pepe: "+ts.getName()
        
        #TODO: fixme same texture for both aircrafts 
        self.model.setTexture(ts, self.myTexture)
        
        self.bomb1= None
        self.bomb2= None
        
        self.target = None
        
    def set_target(self, target):
        self.target = target
        
    def shoot_bomb(self):
        if(str(self.bomb1.getModel().getParent()) != "(empty)"): 
            x = self.model.getX()
            y = self.model.getY()
            z = self.model.getZ()
            self.objects.create_light(x, y, z)
            self.bomb1.activate(self.target)
        else:
            if(str(self.bomb2.getModel().getParent()) != "(empty)"): 
                x = self.model.getX()
                y = self.model.getY()
                z = self.model.getZ()
                self.objects.cerate_light(x, y, z)
                self.bomb2.activate(self.target)
            
    def move_left(self):
        self.incAngleH()
        if (self.model.getR() > -range_move):
            self.model.setR(self.model.getR() - delta_move)
                  
    def move_right(self):
        self.decAngleH()
        if (self.model.getR() < range_move):
            self.model.setR(self.model.getR() + delta_move)    
        
    def getSkin(self):
        return self.skin    
        
    def setPos(self, pos):    
        self.model.setPos(pos)
    
    def getPos(self):
        return self.model.getPos()
        
    def setScale(self, scale):
        self.model.setScale(scale)
        
    def getScale(self):
        return self.model.getScale()
    
    def setAngleR(self, ang):
        self.model.setR(ang)
    
    def getAngleR(self):
        return self.model.getR()
    
    def decAngleR(self):
        if (self.model.getR() >= range_angleR):
            self.model.setR(self.model.getR() - delta_angleR)   
        if (self.model.getR() <= range_angleR):
            self.model.setR(self.model.getR() + delta_angleR)
            
    def incAngleH(self):
        self.model.setH(self.model.getH() + delta_angleH) 
    
    def decAngleH(self):
        self.model.setH(self.model.getH() - delta_angleH) 
    
    def setAngleH(self, ang):
        self.model.setH(ang) 
        
    def getAngleH(self):
        return self.model.getH()   
    
    def incAngleV(self):
        self.model.setP(self.model.getP() + delta_angleV) 
    
    def decAngleV(self):
        self.model.setP(self.model.getP() - delta_angleV)
        
    def getAngleV(self):
        return self.model.getP()
    
    def shake(self):
        h = random.randrange(0, 4)
        p = random.randrange(0, 4)
        r = random.randrange(0, 4)
        
        self.model.setHpr(self.model.getH()+h, self.model.getP()+p, self.model.getR()+r )
    
    def incSpeed(self):
        if(0 < self.speed < range_speed):
            self.speed = self.speed + delta_speed
            
    def decSpeed(self):
        if(0 < self.speed < range_speed):
            self.speed = self.speed - delta_speed
    
    def getSpeed(self):
        return self.speed
             
    def decPower(self, val):
        self.power = self.power - val
    
        #check if it is destroyed
        if(self.power < 0):
            self.fall = 1
    
    def getModel(self):
        return self.model
    
    def setObjects(self, obj):
        self.objects = obj
        self.bomb1 = self.objects.createBomb(self.model, self.model.getHpr(), 10, 4, -1.5)
        self.bomb1.getModel().reparentTo(self.model)
        self.bomb1.getModel().clearTexture()
        
        self.bomb2 = self.objects.createBomb(self.model, self.model.getHpr(), -10, 4, -1.5)
        self.bomb2.getModel().reparentTo(self.model)
        self.bomb2.getModel().clearTexture()
        
        #TODO: fixme why do not clear bombs textures?
        
    def shoot(self):
        self.objects.createBullet(self.getModel(), self.getModel().getHpr())
            
    def stop(self):
        self.speed = 0
        
    def move(self):
        
        print "a: "+str(self.bomb1.getModel().getParent())
        
        if(self.fall):
            self.model.setPos(self.model,0,self.speed, -8)
        else:
            self.model.setPos(self.model,0,self.speed, 0)
            
    def info(self):
        return "Class aircraft: "+ str(self.name) +" , "+\
                   "Position: "+ str(self.model.getPos())+", "+\
                   "Speed: "+ str(self.speed)+", "+\
                   "Power: "+ str(self.power) 
                       
if (__name__ == "__main__"):
    print aircraft.__doc__
    c = aircraft("my plane", [0, 0, 0], [0, 0, 0], "")
    print c.info()
    c.move()
    print c.info()
    c.move()
    print c.info()
    c.move()
    print c.info()
    c.incAngleH()
    c.move()
    print c.info()    
    c.incAngleH()
    c.move()
    print c.info()
    c.incAngleH()
    c.move()
    print c.info()
    print "program starts"
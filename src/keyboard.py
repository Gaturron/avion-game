'''
Created on 05/01/2011

@author: fernando
'''
import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.DirectObject import DirectObject
import sys

from direct.task import Task

time_shoot_bomb = 2

class keyboard(DirectObject):
    "class modeling the input"
    
    keyMap1 = {"left":0, "right":0, "accel":0, "break":0, "fire":0}
    keyMap2 = {"left":0, "right":0, "accel":0, "break":0, "fire":0}
    
    def __init__(self, aircraft1, aircraft2, camera1, camera2):
        
        self.aircraft1 = aircraft1
        self.fire = 0
        
        self.aircraft2 = aircraft2
        self.camera1 = camera1
        self.camera2 = camera2
        
        self.accept("escape", sys.exit)
        self.accept("arrow_left", self.setKey1, ["left",1])
        self.accept("arrow_right", self.setKey1, ["right",1])
        self.accept("arrow_up", self.setKey1, ["accel", 1])
        self.accept("arrow_down", self.setKey1, ["break", 1])
        self.accept("arrow_left-up", self.setKey1, ["left",0])
        self.accept("arrow_right-up", self.setKey1, ["right",0])
        self.accept("arrow_up-up", self.setKey1, ["accel", 0])
        self.accept("arrow_down-up", self.setKey1, ["break", 0])
        
        self.accept("a", self.setKey2, ["left",1])
        self.accept("d", self.setKey2, ["right",1])
        self.accept("w", self.setKey2, ["accel", 1])
        self.accept("s", self.setKey2, ["break", 1])
        self.accept("f", self.setKey2, ["fire", 1])
        self.accept("a-up", self.setKey2, ["left",0])
        self.accept("d-up", self.setKey2, ["right",0])
        self.accept("w-up", self.setKey2, ["accel", 0])
        self.accept("s-up", self.setKey2, ["break", 0])
        self.accept("f-up", self.setKey2, ["fire", 0])
    
        self.isEnable = [1,1]
    
    def input(self):
        if (self.isEnable[0]):
            if (self.keyMap1["left"]!=0):  self.aircraft1.move_left()
            if (self.keyMap1["right"]!=0): self.aircraft1.move_right()
            if (self.keyMap1["accel"]!=0): self.aircraft1.decAngleV()
            if (self.keyMap1["break"]!=0): self.aircraft1.incAngleV()
            if (self.keyMap1["left"] == 0 and self.keyMap1["right"] == 0):
                self.aircraft1.decAngleR()
        else:
            if (self.keyMap1["left"]!=0):  self.camera1.moveLeft(self.aircraft1.getModel())
            if (self.keyMap1["right"]!=0): self.camera1.moveRight(self.aircraft1.getModel())
            if (self.keyMap1["accel"]!=0): self.camera1.moveForward()
            if (self.keyMap1["break"]!=0): self.camera1.moveBackward()
            
            
        if (self.isEnable[1]):
            if (self.keyMap2["left"]!=0):  self.aircraft2.move_left()
            if (self.keyMap2["right"]!=0): self.aircraft2.move_right()
            if (self.keyMap2["accel"]!=0): self.aircraft2.decAngleV()
            if (self.keyMap2["break"]!=0): self.aircraft2.incAngleV()
            if (self.keyMap2["fire"]!=0): 
                if (not self.fire):
                    self.aircraft2.shoot()
                    taskMgr.add(self.shoot_bomb,"shoot_bomb") 
                    self.fire = 1
                    
            if (self.keyMap2["fire"]==0): 
                if (self.fire):
                    self.fire = 0
                
            if (self.keyMap2["left"] == 0 and self.keyMap2["right"] == 0):
                self.aircraft2.decAngleR()
                
        else:
            if (self.keyMap2["left"]!=0):  self.camera2.moveLeft(self.aircraft2.getModel())
            if (self.keyMap2["right"]!=0): self.camera2.moveRight(self.aircraft2.getModel())
            if (self.keyMap2["accel"]!=0): self.camera2.moveForward()
            if (self.keyMap2["break"]!=0): self.camera2.moveBackward()
            
    def shoot_bomb(self, task): 
        if(self.keyMap2["fire"] == 0): return Task.done
        if(task.time > time_shoot_bomb):
            if(self.keyMap2["fire"] != 0):self.aircraft2.shoot_bomb()
            return Task.done
        else: 
            return Task.cont
    
    def disablePlayer(self, i):
        self.isEnable[i-1] = 0
            
    #Records the state of the arrow keys
    def setKey1(self, key, value):
        self.keyMap1[key] = value 
          
    def setKey2(self, key, value):
        self.keyMap2[key] = value 
        
if (__name__ == "__main__"):
    print keyborad.__doc__
    
'''
Created on 10/01/2011

@author: fernando
'''
import direct.directbase.DirectStart
from pandac.PandaModules import BaseParticleEmitter,BaseParticleRenderer
from pandac.PandaModules import PointParticleFactory,SpriteParticleRenderer
from pandac.PandaModules import LinearNoiseForce,DiscEmitter
from pandac.PandaModules import TextNode
from pandac.PandaModules import AmbientLight,DirectionalLight
from pandac.PandaModules import Point3,Vec3,Vec4
from pandac.PandaModules import Filename
from direct.particles.Particles import Particles
from direct.particles.ParticleEffect import ParticleEffect
from direct.particles.ForceGroup import ForceGroup
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
import sys
from collision import *
from bullet import *
from bomb import *
from particles import *
from lights import *

class dynamicObject:
    "class modeling dynamics objects"
    
    def __init__(self, collision, keyboard, aircraft1, aircraft2, camera1, camera2, map):
        self.bullets = []
        self.collision = collision
        
        self.aircraft1 = aircraft1
        self.aircraft2 = aircraft2 
        
        self.map = map
        
        self.camera1 = camera1
        self.camera2 = camera2
        
        self.keyboard = keyboard
        
        self.lights = lights()
                
        #particle system
        base.enableParticles()
        
    def create_light(self, x, y, z):
        self.lights.createLightShot(x, y, z)
        
    def createFlasher(self, x, y, z):
        self.lights.createFlasher(x, y, z)
        
    def createFlasherFromModel(self, model, name, x, y, z):
        self.lights.createFlasherFromModel(model, name, x, y, z)
        
    def destroyFlasherFromModel(self, model):
        self.lights.destroyFlasherFromModel(model)
                  
    def createBullet(self, model, hpr):
        self.bullet = bullet(model, hpr)
        self.collision.addCollisionToBullet(self.bullet)
    
        self.bullets.append(self.bullet)
    
        x = model.getX()
        y = model.getY()
        z = model.getZ()
        
        self.create_light(x,y,z)
        
    def createBomb(self, model, hpr, x = 0, y = 0, z = 0):
        self.bomb = bomb(model, hpr, x, y, z)
        self.collision.addCollisionToBullet(self.bomb)
    
        self.bullets.append(self.bomb)
        
        return self.bomb
    
    def move(self):
        for bullet in self.bullets:
            bullet.move() 
                        
        #aircraft which collide with map must be deleted
        #collision queue
        queue = self.collision.getCollisionsFromAircraft(1)
        for i in range(queue.getNumEntries()):
            entry = queue.getEntry(i)
            
            #collision with map
            if(entry.getIntoNodePath().getName() == "" or
               entry.getIntoNodePath().getName() == "cnode2"):
                self.aircraft1.destroy()
                self.destroyFlasherFromModel(self.aircraft1.getModel())
                self.keyboard.disablePlayer(1)
                self.camera1.setGoWith(0)
                x = self.aircraft1.getModel().getX()
                y = self.aircraft1.getModel().getY()
                z = self.aircraft1.getModel().getZ()
                part = particles(x,y,z)
                part.taskSmokering() 
                
            if(entry.getIntoNodePath().getName() == "cnodeI"):
                self.aircraft1.getModel().lookAt(self.map)
                self.aircraft1.shake()
                
        #collision queue        
        queue = self.collision.getCollisionsFromAircraft(2)
        for i in range(queue.getNumEntries()):
            entry = queue.getEntry(i)
            
            #collision with map
            if(entry.getIntoNodePath().getName() == "" or
               entry.getIntoNodePath().getName() == "cnode1"):
                self.aircraft2.destroy()
                self.destroyFlasherFromModel(self.aircraft2.getModel())
                self.keyboard.disablePlayer(2)
                self.camera2.setGoWith(0)
                x = self.aircraft2.getModel().getX()
                y = self.aircraft2.getModel().getY()
                z = self.aircraft2.getModel().getZ()
                part = particles(x, y, z)
                part.taskSmokering()
            
            if(entry.getIntoNodePath().getName() == "cnodeI"):
                self.aircraft2.getModel().lookAt(self.map.getModel())
                self.aircraft2.shake()
                
        #bullet which collide with something must be deleted
        for bullet in self.bullets:
            if (self.collision.getNumCollisionsFromBullet(bullet) != 0): 
                                
                x = bullet.getModel().getX()
                y = bullet.getModel().getY()
                z = bullet.getModel().getZ()
                
                #self.create_light(x,y,z)
                
                val = bullet.getDamage()
                                
                #collision queue
                queue = self.collision.getCollisionsFromBullet(bullet)
                for i in range(queue.getNumEntries()):
                    entry = queue.getEntry(i)
                    
                    #collision with plane
                    if(entry.getIntoNodePath().getName() == "cnode1"):
                        part = particles(x, y, z)
                        part.taskSmoke()
                        
                        self.aircraft1.decPower(val)
                        self.aircraft1.shake()
                        
                    if(entry.getIntoNodePath().getName() == "cnode2"):
                        part = particles(x, y, z)
                        part.taskSmoke()
                        
                        self.aircraft2.decPower(val)
                        self.aircraft2.shake()
                        
                    #collision with invesion
                    if(entry.getIntoNodePath().getName() == "cnodeI"):
                        pass
                    
                    #collision with map
                    if(entry.getIntoNodePath().getName() == ""):
                        part = particles(x, y, z)
                        part.taskDust()
                        
                    #collision with bullet
                    if(entry.getIntoNodePath().getName() == "cnodeT"):
                        part = particles(x, y, z)
                        part.taskSmoke()
                               
                self.bullets.remove(bullet) 
                bullet.delete()
                                
if(__name__ == "__main__"):
    print dynamicObject.__doc__
        

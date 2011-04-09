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
from direct.task import Task

class particles:
    "class modeling particles"
    
    def __init__(self, x, y, z):
        
        #TODO: solo cargar lo que se va a usar en ese momento, no cargar todos los archivos para solo usar uno
        self.smokering = ParticleEffect()
        self.smokering.loadConfig(Filename('smokering.ptf'))
        self.smoke = ParticleEffect()
        self.smoke.loadConfig(Filename('smoke.ptf'))
        self.smoke2 = ParticleEffect()
        self.smoke2.loadConfig(Filename('smoke2.ptf'))
        self.dust = ParticleEffect()
        self.dust.loadConfig(Filename('dust.ptf'))  
        self.steam = ParticleEffect()
        self.steam.loadConfig(Filename('steam.ptf'))
        
        self.setPos(x, y, z)
    
    def setPos(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def particleSmokering(self, task):

        self.smokering.accelerate(0.2)
        if (task.time == 0):
            self.smokering.enable()
            self.smokering.setPos(self.x,self.y,self.z)
            self.smokering.start(render)        
            return task.cont   
        if task.time < 0.5:
            return task.cont
        if 0.5 < task.time < 0.6:
            self.smokering.softStop()
            return task.cont
        if task.time > 0.6:
            if self.smokering.isEnabled():
                self.smokering.disable()
                #self.smokering.cleanup()
            return task.done
        
    def particleSmoke(self, task):
        
        if (task.time == 0):
            self.smoke.enable()            
            self.smoke.setPos(self.x,self.y,self.z)
            self.smoke.start(render)        
            return task.cont   
        if task.time < 0.08:
            return task.cont
        if 0.08 < task.time < 0.4:
            self.smoke.softStop()
            return task.cont
        if task.time > 0.4:
            if self.smoke.isEnabled():
                self.smoke.disable()
                #self.smoke.cleanup()
            return task.done
        
    def particleDust(self, task):
        
        if (task.time == 0):
            self.dust.enable()
            self.dust.setPos(self.x,self.y,self.z)
            self.dust.start(render)        
            return task.cont   
        if task.time < 0.08:
            return task.cont
        if 0.08 < task.time < 0.4:
            self.dust.softStop()
            return task.cont
        if task.time > 0.4:
            if self.dust.isEnabled():
                self.dust.disable()
                #self.dust.cleanup()
            return task.done
        
    def particleSmoke2(self, task):
        if (task.time == 0):
            self.smoke2.enable()
            self.smoke2.start(render)
            return task.cont
        if task.time < 0.08:
            return task.cont
        if 0.08 < task.time < 0.4:
            self.smoke2.softStop()
            return task.cont
        if (task.time > 0.4):
            if self.smoke2.isEnabled():
                self.smoke2.disable()
            return task.done
    
    def setPosSmokeRocket(self, model):
        self.smoke2.setPos(model, 0,-5, 2)
        
    def particleSteam(self, model, start):
        if(start):
            self.steam.enable()
            self.steam.start(model, render)
        else:
            self.steam.disable()
            self.steam.softStop()
        
if (__name__ == "__main__"):
    print particles.__doc__
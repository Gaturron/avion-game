import direct.directbase.DirectStart
from pandac.PandaModules import *
import math

class lights:
    "class modeling lights"
    
    def __init__(self):
        self.flashers = []
        taskMgr.add(self.flasher, "flasher")
    
    def createLightShot(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        taskMgr.add(self.lightShot, "lightShot")
                
    def createFlasherFromModel(self, model, name, x, y, z):
       
        self.flasher = render.attachNewNode(PointLight('flasher'+name))
        self.flasher.reparentTo(model)
        self.flasher.setPos(model, x, y, z)
        self.flasher.node().setColor( Vec4( .1, 0, 0, 1 ) )
        self.flasher.node().setAttenuation( Vec3( .1, 0.04, 0.0 ) ) 
        render.setLight(self.flasher)
               
        self.flashers.append([self.flasher, name, "on"])
        
    def destroyFlasherFromModel(self, name):    
        for flasher in self.flashers:
            if (flasher[1] == name): flasher[2] = "off"
    
    def setPos(self, model, x, y, z):
        self.model = model
        self.x = x
        self.y = y
        self.z = z
        
    def lightShot(self, task):
        if (task.time == 0):
            self.plnp = render.attachNewNode(PointLight('plight'+str(self.x)+str(self.y)+str(self.z)))
            self.plnp.setPos(self.x, self.y, self.z)
            render.setLight(self.plnp)
            return task.cont
        elif (task.time > 0.08):
            if render.hasLight(self.plnp):
                render.clearLight(self.plnp)
            self.plnp.detachNode()
            return task.done
        else:
            return task.cont
        
    def flasher(self, task):
        for flasher in self.flashers:
            if(flasher[2] == "off"): 
                if render.hasLight(flasher[0]):
                    render.clearLight(flasher[0])
                flasher[0].detachNode()
        return task.cont
        
if (__name__ == "__main__"):
    print lights.__doc__
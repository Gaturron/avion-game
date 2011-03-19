import direct.directbase.DirectStart
from pandac.PandaModules import *
import math

class lights:
    "class modeling lights"
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def setPos(self, model, x, y, z):
        self.model = model
        self.x = x
        self.y = y
        self.z = z
        
    def lightShot(self, task):
        if (task.time == 0):
            self.plnp = render.attachNewNode(PointLight('plight'))
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
        if (task.time == 0):
            self.flasher = render.attachNewNode(PointLight('flasher'))
            self.flasher.reparentTo(self.model)
            self.flasher.setPos(self.model, self.x, self.y, self.z)
            self.flasher.node().setColor( Vec4( .1, 0, 0, 1 ) )
            self.flasher.node().setAttenuation( Vec3( .1, 0.04, 0.0 ) ) 
            render.setLight(self.flasher)
            return task.cont
        else:
            return task.cont    
        
if (__name__ == "__main__"):
    print lights.__doc__
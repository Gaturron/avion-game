import direct.directbase.DirectStart
from pandac.PandaModules import *

class lights:
    "class modeling lights"
    
    def __init__(self, x, y, z):
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
        
if (__name__ == "__main__"):
    print lights.__doc__
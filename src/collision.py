'''
Created on 07/01/2011

@author: fernando
'''

from direct.showbase.ShowBase import ShowBase
import direct.directbase.DirectStart
from panda3d.core import *

radius = 10

class collision():
    "class modeling colisions"
    
    Queue = []
    BulletQueues = []
    
    def __init__(self, map, aircraft1, aircraft2, debug):
        
        self.debug = debug
        
        #collision between aircrafts
        self.model1 = aircraft1.getModel()
        
        self.cs1b = CollisionSphere(0, -6, 0, radius)
        self.cs1f = CollisionSphere(0, 8, 0, radius-4)
        self.cnodePath1 = self.model1.attachNewNode(CollisionNode('cnode1'))
        self.cnodePath1.node().addSolid(self.cs1b)
        self.cnodePath1.node().addSolid(self.cs1f)
        self.cnodePath1.setCollideMask(BitMask32(0x2))
        if(self.debug): self.cnodePath1.show()
        
        self.model2 = aircraft2.getModel()
        
        self.cs2b = CollisionSphere(0, -6, 0, radius)
        self.cs2f = CollisionSphere(0, 8, 0, radius-4)
        self.cnodePath2 = self.model2.attachNewNode(CollisionNode('cnode2'))
        self.cnodePath2.node().addSolid(self.cs2b)
        self.cnodePath2.node().addSolid(self.cs2f)
        self.cnodePath2.setCollideMask(BitMask32(0x2))
        if(self.debug): self.cnodePath2.show()
  
        #collision between floor and aircraft
        self.map = map.getModel()
        self.map.setCollideMask(BitMask32(0x2))
        
        self.ci = CollisionInvSphere(0, 0, 0, 200)
        self.cnodePathI = self.map.attachNewNode(CollisionNode('cnodeI'))
        self.cnodePathI.node().addSolid(self.ci)
        self.cnodePathI.setCollideMask(BitMask32(0x2))
        if(self.debug): self.cnodePathI.show()
  
        #traverser
        base.cTrav = CollisionTraverser('collTrav')
        
        self.Queue = []
        
        self.Queue1 = CollisionHandlerQueue()
        base.cTrav.addCollider(self.cnodePath1, self.Queue1)
        self.Queue.append(self.Queue1)
        
        self.Queue2 = CollisionHandlerQueue()
        base.cTrav.addCollider(self.cnodePath2, self.Queue2)
        self.Queue.append(self.Queue2)

        
                
        if(self.debug): base.cTrav.showCollisions(render)
                
    def addCollisionToBullet(self, bullet):
        self.model = bullet.getModel()
        
        self.ct = CollisionSphere(0, 20, 0, 6)
        self.cnodePathT = self.model.attachNewNode(CollisionNode('cnodeT'))
        self.cnodePathT.node().addSolid(self.ct)
        
        self.cnodePathT.setCollideMask(BitMask32(0x2))
        if(self.debug): self.cnodePathT.show()
        
        self.QueueB = CollisionHandlerQueue()
        base.cTrav.addCollider(self.cnodePathT, self.QueueB)
        self.BulletQueues.append([self.model, self.QueueB])
        
    def getCollisionsFromAircraft(self, value):
        return self.Queue[value-1]
        
    def getCollisionsFromBullets(self): 
        for queue in self.BulletQueues:   
            for i in range(queue[1].getNumEntries()):
                entry = queue[1].getEntry(i)
                #print "Bullets "+" "+str(entry.getFromNodePath().getName())
    
    def getCollisionsFromBullet(self, bullet): 
        for queue in self.BulletQueues:
            if(queue[0] == bullet.getModel()):
                return queue[1]                

    def getNumCollisionsFromBullet(self, bullet):
        return self.getCollisionsFromBullet(bullet).getNumEntries()
        
if (__name__ == "__main__"):
    print collision.__doc__
    
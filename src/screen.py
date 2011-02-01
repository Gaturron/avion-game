'''
Created on 06/01/2011

@author: fernando
'''

import direct.directbase.DirectStart

class screen:
    "class modeling the screen"
    
    def __init__(self, cam1, cam2):
        
        self.cam1 = cam1.getCamera()
        
        dr = base.camNode.getDisplayRegion(0)
        dr.setActive(0)
        
        window = dr.getWindow() 
        
        dr1 = window.makeDisplayRegion(0.5, 1, 0, 1)
        dr1.setSort(dr.getSort())
        dr1.setCamera(self.cam1) 
        
        self.cam2 = cam2.getCamera()
        
        dr2 = window.makeDisplayRegion(0, 0.5, 0, 1)
        dr2.setSort(dr.getSort())
        dr2.setCamera(self.cam2) 
    
if (__name__ == "__main__"):
    print screen.__doc__

from generator.compositescreenitem import CompositeScreenItem
import math
import numpy as np



class BoxLineBox(CompositeScreenItem):
    
    def __init__(self, listpos1, listpos2, maxLineLength=20):
        #print("init")
        self.maxLineLength = maxLineLength
        self.listpos1=listpos1
        self.listpos2=listpos2
        
    def startpt(self, sdl):
        return sdl[self.listpos1]
    
    def endpt(self, sdl):
        return sdl[self.listpos2]
    
    def arrowscalar(self, sdl):
        #print("getArrowScalar")
        return [self.six(sdl) - self.eix(sdl), self.siy(sdl)- self.eiy(sdl)]
    
    def dxdy(self, sdl):
        #print("getDXDY")
        h2 = (self.maxLineLength  - self.linelength(sdl))/2
        xy = self.AO(sdl)
        theta = math.acos(xy[1]/self.linelength(sdl))
        sx = math.sin(theta)
        cy = math.cos(theta)
        xd = abs(sx*h2)*np.sign(xy[0])
        yd = abs(cy*h2)*np.sign(xy[1])
        #print( sx, cy, xd, yd)
        return [xd,yd]
    
    def dx2dy2(self, sdl):
        #print("getDX2DY2")
        h2 = (self.maxLineLength  - self.linelength(sdl))/2
        xy = self.AO2(sdl)
        theta = math.acos(xy[1]/self.linelength(sdl))
        sx = math.sin(theta)
        cy = math.cos(theta)
        xd = abs(sx*h2)*np.sign(xy[0])
        yd = abs(cy*h2)*np.sign(xy[1])
        #print( sx, cy, xd, yd)
        return [xd,yd]
        
    def linelength(self, sdl):
        #print("getLineLngth")
        ao = self.AO(sdl)
        a = ao[0]
        o = ao[1]
        h = math.sqrt(a*a+o*o)
        return h
    
    def AO(self, sdl):
        xd =  self.eix(sdl) - self.six(sdl)
        yd =  self.eiy(sdl) - self.siy(sdl)
        return [xd,yd]
    
    def AO2(self, sdl): 
        xd2 =  self.six(sdl) - self.eix(sdl)  
        yd2 = self.siy(sdl) - self.eiy(sdl) 
        return [xd2,yd2]
    
    def six(self, sdl):
        return (self.startpt(sdl).xbottomleft + self.startpt(sdl).internalposx)
    
    def siy(self, sdl):
        return (self.startpt(sdl).ybottomleft + self.startpt(sdl).internalposy)
    
    def eix(self, sdl):
        return (self.endpt(sdl).xbottomleft + self.endpt(sdl).internalposx)
    
    def eiy(self, sdl):
        return (self.endpt(sdl).ybottomleft + self.endpt(sdl).internalposy)
    
        
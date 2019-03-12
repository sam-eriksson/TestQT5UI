from generator.screenitemfactory import ScreenItemFactory as ScreenItemFactory
from generator.testitems import TestItems
from generator.testitems2 import TestItems2
from generator.overlapindicator import OverlapIndicator
import numpy.random as rnd
import random
from generator.boxlinebox import BoxLineBox as BoxLineBox
from generator.randomgenerator import RandomGenerator


class ScreenDefinition():
    
    def __init__(self, widthInPixels, heightInPixels, jitterlow, jitterhigh, incrementer, cleanupcycles):
        #print("init")
        self.screenDefList = []
        self.overlapList =[]
        self.compositeList =[]
        self.overlap = True
        self.widthInPixels = widthInPixels
        self.heightInPixels = heightInPixels
        self.jitterlow = jitterlow
        self.jitterhigh = jitterhigh
        self.incrementer = incrementer
        self.cleanupcycles = cleanupcycles
        
    def testItems(self):
        print("testItems")
        ti = TestItems()
        self.screenDefList = ti.testItems()
        self.compositeList = ti.compositeItems()
       
    def randomGenerate(self, numberOfItems):
        rg = RandomGenerator(numberOfItems, self.heightInPixels, self.widthInPixels)
        self.compositeList = rg.compositeList
        self.screenDefList = rg.screenDefList

    def cleanUp(self):
        if self.overlap == True:
            self.adjustLineLength()
            self.checkIfOverlap()
            count=0
            if len(self.overlapList)<1:
                self.overlap = False
                return
            while count<self.cleanupcycles:
                self.spreadOut()
                self.adjustLineLength()
                self.checkIfOverlap()
                if len(self.overlapList)<1:
                    count=self.cleanupcycles
                    self.overlap = False
                
                #print("count :",count)
                count = count +1
        
    def spreadOut(self):
        #check if square 1 center is closer to one screen corner or not
        #check if square 2 center is closer to one screen corner or not
        #if both are in same screen corner move away from that corner
        #box furthest from corner moves out if no space toward corner
        #direction determined by overlap corner
        #print("spreadOut")
        i = 0
        for overlap in self.overlapList:
            i=i+1
            item = self.screenDefList[overlap.posn-1]
            item2 = self.screenDefList[overlap.posn2-1]
            increment = round(rnd.exponential(self.incrementer,1).tolist()[0])
            jitter = round(rnd.normal(self.jitterlow,self.jitterhigh))
            if overlap.corner == 1 :
                #print("spread overlap", overlap.corner)
                overlapX = item.xbottomleft +item.width - item2.xbottomleft
                overlapY = item.ybottomleft + item.height - item2.ybottomleft
                fairshiftX = int(round(overlapX/2))
                fairshiftY = int(round(overlapY/2))
                moveX = max(item.xbottomleft - fairshiftX - increment, 0)
                moveY = max(item.ybottomleft - fairshiftY - increment, 0)
                self.overlapList[i-1].x = moveX
                self.overlapList[i-1].y = moveY
            elif overlap.corner == 3 :
                #print("spread overlap", overlap.corner)
                overlapX = item2.xbottomleft +item2.width - item.xbottomleft
                overlapY = item2.ybottomleft + item2.height - item.ybottomleft
                fairshiftX = int(round(overlapX/2))
                fairshiftY = int(round(overlapY/2))
                moveX = min(item.xbottomleft + fairshiftX + increment, self.widthInPixels-item.width)
                moveY = min(item.ybottomleft + fairshiftY + increment, self.heightInPixels-item.height)
                self.overlapList[i-1].x = moveX
                self.overlapList[i-1].y = moveY
            elif overlap.corner == 2:
                #print("spread overlap", overlap.corner)
                overlapX = item.xbottomleft +item.width - item2.xbottomleft
                overlapY = item2.ybottomleft + item2.height - item.ybottomleft
                fairshiftX = int(round(overlapX/2))
                fairshiftY = int(round(overlapY/2))
                moveX = max(item.xbottomleft - fairshiftX - increment, 0)
                moveY = min(item.ybottomleft + fairshiftY + increment, self.heightInPixels-item.height)
                self.overlapList[i-1].x = moveX
                self.overlapList[i-1].y = moveY
            elif overlap.corner == 4:
                #print("spread overlap", overlap.corner)
                overlapX = item2.xbottomleft +item2.width - item.xbottomleft
                overlapY = item.ybottomleft + item.height - item2.ybottomleft
                fairshiftX = int(round(overlapX/2))
                fairshiftY = int(round(overlapY/2))
                moveX = min(item.xbottomleft + fairshiftX + increment, self.widthInPixels-item.width)
                moveY = max(item.ybottomleft - fairshiftY - increment, 0)
                self.overlapList[i-1].x = moveX
                self.overlapList[i-1].y = moveY
            elif overlap.corner == 5:
                #print("spread overlap", overlap.corner)
                overlapY = item.ybottomleft + item.height - item2.ybottomleft
                fairshiftY = int(round(overlapY/2))
                moveX = max(min(item.xbottomleft + jitter, self.widthInPixels -item.width),0)
                moveY = max(item.ybottomleft - fairshiftY - increment, 0)
                self.overlapList[i-1].x = moveX
                self.overlapList[i-1].y = moveY
            elif overlap.corner == 6:
                #print("spread overlap", overlap.corner)
                overlapY = item2.ybottomleft + item2.height - item.ybottomleft
                fairshiftY = int(round(overlapY/2))
                moveX = max(min(item.xbottomleft + jitter, self.widthInPixels -item.width),0)
                moveY = min(item.ybottomleft + fairshiftY + increment, self.heightInPixels-item.height)
                self.overlapList[i-1].x = moveX
                self.overlapList[i-1].y = moveY
            elif overlap.corner == 7:
                #print("spread overlap", overlap.corner)
                overlapX = item2.xbottomleft + item2.width - item.xbottomleft
                fairshiftX = int(round(overlapX/2))
                moveX = min(item.xbottomleft + fairshiftX + increment, self.widthInPixels-item.width)
                moveY = max(min(item.ybottomleft + jitter, self.heightInPixels -item.height),0)
                self.overlapList[i-1].x = moveX
                self.overlapList[i-1].y = moveY
            elif overlap.corner == 8:
                #print("spread overlap", overlap.corner)
                overlapX = item.xbottomleft + item.width - item2.xbottomleft
                fairshiftX = int(round(overlapX/2))
                moveX = max(item.xbottomleft - fairshiftX - increment, 0)
                moveY = max(min(item.ybottomleft + jitter, self.heightInPixels -item.height),0)
                self.overlapList[i-1].x = moveX
                self.overlapList[i-1].y = moveY
        i=0
        #overlap list did double duty in as we read which corner overlapped we used the x and y to store new
        #locations for the boxes
        for overlap in self.overlapList:
            self.screenDefList[overlap.posn-1].xbottomleft = overlap.x
            self.screenDefList[overlap.posn-1].ybottomleft = overlap.y
            i=i+1                
                
    def checkIfOverlap(self):
        #print("checkIfOverlap")
        self.overlapList.clear()
        i=0
        for items in self.screenDefList: #defines what we are checking
            i=i+1
            j=0
            for items2 in self.screenDefList:
                j=j+1
                if (
                        ((items.ybottomleft <= items2.ybottomleft and
                        items.ybottomleft + items.height >= items2.ybottomleft + items2.height) or
                        (items.ybottomleft >= items2.ybottomleft and
                        items.ybottomleft + items.height <= items2.ybottomleft + items2.height)) and
                        items.xbottomleft + items.width > items2.xbottomleft  and
                        items.xbottomleft + items.width < items2.xbottomleft + items2.width
                        ):
                    #print("check overlap 8")
                    self.overlapList.append(OverlapIndicator(items2.xbottomleft, items2.ybottomleft, 8, i, j))
                elif (
                        ((items.ybottomleft <= items2.ybottomleft and
                        items.ybottomleft + items.height >= items2.ybottomleft + items2.height) or
                        (items.ybottomleft >= items2.ybottomleft and
                        items.ybottomleft + items.height <= items2.ybottomleft + items2.height)) and
                        items.xbottomleft < items2.xbottomleft + items2.width and
                        items.xbottomleft + items.width >items2.xbottomleft + items2.width
                        ):
                    #print("check overlap 7")
                    self.overlapList.append(OverlapIndicator(items2.xbottomleft, items2.ybottomleft, 7, i, j))
                elif (
                        ((items.xbottomleft >= items2.xbottomleft and
                        items.xbottomleft + items.width <= items2.xbottomleft + items2.width) or
                        (items.xbottomleft <= items2.xbottomleft and
                        items.xbottomleft + items.width >= items2.xbottomleft + items2.width)) and
                        items.ybottomleft > items2.ybottomleft and
                        items.ybottomleft < items2.ybottomleft + items2.height
                        ):
                    #print("check overlap 6")
                    self.overlapList.append(OverlapIndicator(items2.xbottomleft, items2.ybottomleft, 6, i, j))
                elif (
                        ((items.xbottomleft >= items2.xbottomleft and
                        items.xbottomleft + items.width <= items2.xbottomleft + items2.width) or
                        (items.xbottomleft <= items2.xbottomleft and
                        items.xbottomleft + items.width >= items2.xbottomleft + items2.width)) and
                        items.ybottomleft + items.height > items2.ybottomleft and
                        items.ybottomleft + items.height < items2.ybottomleft + items2.height
                        ):
                    #print("check overlap 5")
                    self.overlapList.append(OverlapIndicator(items2.xbottomleft, items2.ybottomleft, 5, i, j))
                elif (
                        items.xbottomleft < items2.xbottomleft and
                        items.xbottomleft + items.width > items2.xbottomleft and
                        items.ybottomleft < items2.ybottomleft and
                        items.ybottomleft + items.height > items2.ybottomleft
                       ):
                    #print("check overlap 1")
                    self.overlapList.append(OverlapIndicator(items.xbottomleft 
                                                             +items.width, items.ybottomleft +items.height ,1, i, j))
                elif  (
                        items.xbottomleft < items2.xbottomleft and
                        items.xbottomleft + items.width > items2.xbottomleft and
                        items.ybottomleft < items2.ybottomleft + items2.height and
                        items.ybottomleft + items.height > items2.ybottomleft + items2.height 
                        ):
                    #print("check overlap 2")
                    self.overlapList.append(OverlapIndicator(items.xbottomleft + items.width, items.ybottomleft, 2, i, j))
                elif  (
                        items.xbottomleft < items2.xbottomleft + items2.width and
                        items.xbottomleft + items.width > items2.xbottomleft + items2.width and
                        items.ybottomleft < items2.ybottomleft + items2.height and
                        items.ybottomleft + items.height > items2.ybottomleft + items2.height
                        ):
                    #print("check overlap 3")
                    self.overlapList.append(OverlapIndicator(items.xbottomleft, items.ybottomleft ,3, i,j))
                elif  (
                        items.xbottomleft < items2.xbottomleft +items2.width and
                        items.xbottomleft + items.width > items2.xbottomleft +items2.width and
                        items.ybottomleft < items2.ybottomleft and
                        items.ybottomleft + items.height > items2.ybottomleft
                        ):
                    #print("check overlap 4")
                    self.overlapList.append(OverlapIndicator(items.xbottomleft, items.ybottomleft +items.height, 4, i, j))
    
    
    def adjustLineLength(self):                
        ## Adjust to line length
        for line in self.compositeList:
            if line.maxLineLength < line.linelength(self.screenDefList):
                #print("adjust line length")
                tx1 = self.screenDefList[line.listpos1].xbottomleft + line.dxdy(self.screenDefList)[0]
                ty1 = self.screenDefList[line.listpos1].ybottomleft + line.dxdy(self.screenDefList)[1]
                tx2 = self.screenDefList[line.listpos2].xbottomleft + line.dx2dy2(self.screenDefList)[0]
                ty2 = self.screenDefList[line.listpos2].ybottomleft + line.dx2dy2(self.screenDefList)[1]
                
                self.screenDefList[line.listpos1].xbottomleft = int(round(tx1))
                self.screenDefList[line.listpos1].ybottomleft = int(round(ty1))
                self.screenDefList[line.listpos2].xbottomleft = int(round(tx2))
                self.screenDefList[line.listpos2].ybottomleft = int(round(ty2))

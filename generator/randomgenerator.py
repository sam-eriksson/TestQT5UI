import random
from generator.boxlinebox import BoxLineBox
from generator.screenitemfactory import ScreenItemFactory
from generator.labelofscritm import LabelOfScrItm as LabelOfScrItm
from generator.menugroup import MenuGroup


class RandomGenerator():
    
    def __init__(self, numberOfItems, heightInPixels, widthInPixels):
        print("randomGenerate")
        print("numberOfItems ",  numberOfItems)
        print("heightInPixels ", heightInPixels)
        print("widthInPixels ",widthInPixels)
        print("Total Area:", heightInPixels*widthInPixels)
        self.screenDefList = []
        self.compositeList = []
        totalitemsarea=0
        scritem = ScreenItemFactory()
        for i in range(numberOfItems):
            itemkey = random.randint(1,3)
            item = scritem.screenItem(itemkey)
            if item.TYPE == MenuGroup.MENUGROUP:
                z=0
            else:
                item.height = int(round(item.minimumHeight 
                             + ((heightInPixels - item.minimumHeight ) 
                                * .15* random.randint(5, 100)/100))
                             )
                item.width = int(round(item.minimumWidth
                + ((widthInPixels -item.minimumWidth) 
                   * .15 * random.randint(5,100)/100))
                )
            item.internalposx = random.randint(round(item.width/4), 3*round(item.width/4) )
            item.internalposy = random.randint(round(item.height/4), 3*round(item.height/4) )
            item.xbottomleft = random.randint(0, widthInPixels-item.width)
            item.ybottomleft = random.randint(0, heightInPixels-item.height)
            totalitemsarea = totalitemsarea + item.height * item.width
            self.screenDefList.append(item)
        print("Total Items Area:", totalitemsarea)
        print("Percentage coverage:", (100*totalitemsarea)/(heightInPixels*widthInPixels))
        self.compositeList.clear()
        pos = 0
        length = len(self.screenDefList)
        temp = []
        for j in self.screenDefList:
            item = scritem.screenItem(LabelOfScrItm.LABELOFITEM)
            item.setScrItm(j)
            item.height = 22 #(11)
            item.width = 80 #(7)
            item.internalposx = random.randint(round(item.width/4), 3*round(item.width/4) )
            item.internalposy = random.randint(round(item.height/4), 3*round(item.height/4) )
            
            item.xbottomleft = random.randint(0, widthInPixels-item.width)
            item.ybottomleft = random.randint(0, heightInPixels-item.height)
            temp.append(item)
            blb = BoxLineBox(length+pos, pos , 130)
            self.compositeList.append(blb)
            pos=pos+1
        self.screenDefList.extend(temp)

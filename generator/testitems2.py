from generator.screenitemfactory import ScreenItemFactory as ScreenItemFactory
import random
from generator.boxlinebox import BoxLineBox as BoxLineBox

class TestItems2():
    
    def __init__(self):
        #print("__init__")
        self.screenDefList =[]
        
    def testItems(self):
        scritem = ScreenItemFactory()
        item = scritem.screenItem(1)
        item.height = 50
        item.width = 150
        item.xbottomleft = 90
        item.ybottomleft = 40
        item.itemnumber = 1
        item.internalposx = 30
        item.internalposy = 30
        self.screenDefList.append(item)
        
        print("testItem")
        scritem2 = ScreenItemFactory()
        item2 = scritem2.screenItem(1)
        item2.height = 50
        item2.width = 100
        item2.xbottomleft = 290
        item2.ybottomleft = 40
        item2.itemnumber = 2
        item2.internalposx = 30
        item2.internalposy = 30
        self.screenDefList.append(item2)
        
        
        return self.screenDefList
    
    def compositeItems(self):
        compositeList = []
        blb = BoxLineBox(0, 1, 160)
        compositeList.append(blb)
        return compositeList
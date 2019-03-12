from generator.screenitemfactory import ScreenItemFactory as ScreenItemFactory
from generator.boxlinebox import BoxLineBox as BoxLineBox

class TestItems():
    
    def __init__(self):
        #print("__init__")
        self.screenDefList =[]
        
    def testItems(self):
        print("testItem")
        scritem2 = ScreenItemFactory()
        item2 = scritem2.screenItem(1)
        item2.height = 50
        item2.width = 60
        item2.xbottomleft = 50
        item2.ybottomleft = 100
        self.screenDefList.append(item2)
        
        scritem = ScreenItemFactory()
        item = scritem.screenItem(1)
        item.height = 150
        item.width = 50
        item.xbottomleft = 70
        item.ybottomleft = 40
        self.screenDefList.append(item)
        
        scritem3 = ScreenItemFactory()
        item3 = scritem3.screenItem(1)
        item3.height = 150
        item3.width = 60
        item3.xbottomleft = 200
        item3.ybottomleft = 40
        self.screenDefList.append(item3)
        
        scritem4 = ScreenItemFactory()
        item4 = scritem4.screenItem(1)
        item4.height = 50
        item4.width = 50
        item4.xbottomleft = 230
        item4.ybottomleft = 100
        self.screenDefList.append(item4)
        
        
        scritem5 = ScreenItemFactory()
        item5 = scritem5.screenItem(1)
        item5.height = 50
        item5.width = 50
        item5.xbottomleft = 50
        item5.ybottomleft = 240
        self.screenDefList.append(item5)
        
        scritem6 = ScreenItemFactory()
        item6 = scritem6.screenItem(1)
        item6.height = 50
        item6.width = 50
        item6.xbottomleft = 70
        item6.ybottomleft = 240
        self.screenDefList.append(item6)
        
        scritem7 = ScreenItemFactory()
        item7 = scritem7.screenItem(1)
        item7.height = 40
        item7.width = 40
        item7.xbottomleft = 150
        item7.ybottomleft = 210
        self.screenDefList.append(item7)
        
        scritem8 = ScreenItemFactory()
        item8 = scritem8.screenItem(1)
        item8.height = 40
        item8.width = 40
        item8.xbottomleft = 170
        item8.ybottomleft = 240
        self.screenDefList.append(item8)
        
        scritem9 = ScreenItemFactory()
        item9 = scritem9.screenItem(1)
        item9.height = 40
        item9.width = 40
        item9.xbottomleft = 270
        item9.ybottomleft = 210
        self.screenDefList.append(item9)
        
        scritem10 = ScreenItemFactory()
        item10 = scritem10.screenItem(1)
        item10.height = 40
        item10.width = 40
        item10.xbottomleft = 250
        item10.ybottomleft = 240
        self.screenDefList.append(item10)
        
        scritem11 = ScreenItemFactory()
        item11 = scritem11.screenItem(1)
        item11.height = 40
        item11.width = 40
        item11.xbottomleft = 370
        item11.ybottomleft = 240
        self.screenDefList.append(item11)
        
        scritem12 = ScreenItemFactory()
        item12 = scritem12.screenItem(1)
        item12.height = 40
        item12.width = 40
        item12.xbottomleft = 350
        item12.ybottomleft = 210
        self.screenDefList.append(item12)
        
        scritem13 = ScreenItemFactory()
        item13 = scritem13.screenItem(1)
        item13.height = 40
        item13.width = 40
        item13.xbottomleft = 370
        item13.ybottomleft = 320
        self.screenDefList.append(item13)
        
        scritem14 = ScreenItemFactory()
        item14 = scritem14.screenItem(1)
        item14.height = 40
        item14.width = 40
        item14.xbottomleft = 350
        item14.ybottomleft = 330
        self.screenDefList.append(item14)
        
        scritem15 = ScreenItemFactory()
        item15 = scritem15.screenItem(1)
        item15.height = 40
        item15.width = 70
        item15.xbottomleft = 50
        item15.ybottomleft = 320
        self.screenDefList.append(item15)
        
        scritem16 = ScreenItemFactory()
        item16 = scritem16.screenItem(1)
        item16.height = 40
        item16.width = 40
        item16.xbottomleft = 70
        item16.ybottomleft = 330
        self.screenDefList.append(item16)
        
        scritem17 = ScreenItemFactory()
        item17 = scritem17.screenItem(1)
        item17.height = 40
        item17.width = 70
        item17.xbottomleft = 150
        item17.ybottomleft = 340
        self.screenDefList.append(item17)
        
        scritem18 = ScreenItemFactory()
        item18 = scritem18.screenItem(1)
        item18.height = 40
        item18.width = 40
        item18.xbottomleft = 170
        item18.ybottomleft = 330
        self.screenDefList.append(item18)
        
        scritem19 = ScreenItemFactory()
        item19 = scritem19.screenItem(1)
        item19.height = 40
        item19.width = 40
        item19.xbottomleft = 250
        item19.ybottomleft = 340
        item19.internalposx = 30
        item19.internalposy = 30
        self.screenDefList.append(item19)
        
        scritem20 = ScreenItemFactory()
        item20 = scritem20.screenItem(1)
        item20.height = 40
        item20.width = 40
        item20.xbottomleft = 250
        item20.ybottomleft = 330
        item20.internalposx = 30
        item20.internalposy = 30
        self.screenDefList.append(item20)
        
        return self.screenDefList
        
    def compositeItems(self):
        compositeList = []
        blb = BoxLineBox(18, 19, 160)
        compositeList.append(blb)
        return compositeList

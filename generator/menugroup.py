from generator.screenitem import ScreenItem as ScreenItem
from generator.textgen import TextGen
from generator.menuitem import MenuItem
import random

class MenuGroup(ScreenItem):
    TYPE=1
    MENUGROUP =1

    def __init__(self):
        super(MenuGroup,self).__init__()
        self.menuItems = []
        self.horizontal = True
        self.choices = [True, False]
        self.randomInitOfMenuItems(random.randint(1,3))
        self.txt = "PLACEHOLDER"
        tg = TextGen()
        self.txt = tg.randomText()
    
    def randomInitOfMenuItems(self,  num):
        self.number = num
        self.horizontal = random.choice(self.choices)
        for i in range(num):
            mi = MenuItem()
            mi.height = 20
            mi.width = 100
            if (self.horizontal) : 
                self.width = self.width + mi.width
                mi.horizontal = self.horizontal
                self.height = 20
            else:
                mi.horizontal = self.horizontal
                self.height = self.height + mi.height
                self.width = 100
            self.menuItems.append(mi)
            
        
    def label(self):
        return "MENU GROUP"
    
    def text(self):
        return self.txt
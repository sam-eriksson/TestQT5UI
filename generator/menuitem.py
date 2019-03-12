from generator.screenitem import ScreenItem as ScreenItem
from generator.textgen import TextGen

class MenuItem(ScreenItem):
    TYPE=4
    MENUITM=4

    def __init__(self):
        super(MenuItem,self).__init__()
        self.minimumHeight = 50
        self.minimumWidth = 100
        self.maximumHeight = 80
        self.maximumWidth = 150
        self.horizontal = True
        self.txt = "PLACEHOLDER"
        tg = TextGen()
        self.txt = tg.randomText()

    def test(self):
        print("test")
        
    def label(self):
        return "MENU ITEM"
    
    def text(self):
        return self.txt
    
    def changex(self):
        if self.horizontal:
            return self.width
        return 0
    
    def changey(self):
        if self.horizontal:
            return 0
        return self.height
    
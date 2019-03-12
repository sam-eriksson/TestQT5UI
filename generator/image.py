from generator.screenitem import ScreenItem
from generator.textgen import TextGen

class Image(ScreenItem):
    TYPE=2
    IMAGE=2
    
    def __init__(self):
        super(Image,self).__init__()
        self.txt = "PLACEHOLDER"
        tg = TextGen()
        self.txt = tg.randomText()
    
    def test(self):
        print("test")
    
    def label(self):
        return "IMAGE"
    
    def text(self):
        return self.txt
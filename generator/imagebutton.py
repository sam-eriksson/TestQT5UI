from generator.screenitem import ScreenItem as ScreenItem
from generator.textgen import TextGen

class ImageButton(ScreenItem):
    TYPE=3
    IMAGEBUTTON=3
    
    def __init__(self):
        super(ImageButton,self).__init__()
        self.txt = "PLACEHOLDER"
        tg = TextGen()
        self.txt = tg.randomText()
         
    def test(self):
        print("test")

    def label(self):
        return "IMAGE BUTTON"
    
    def text(self):
        return self.txt
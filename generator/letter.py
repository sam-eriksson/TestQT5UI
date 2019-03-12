from generator.screenitem import ScreenItem as ScreenItem

class Letter(ScreenItem):
    TYPE=6
    LETTER=6
    
    def __init__(self):
        #print("init")
        super(Letter,self).__init__()
        self.txt=''
        self.height = 11
        self.width = 7
        
    def text(self):
        return self.txt
        
    
from generator.screenitem import ScreenItem as ScreenItem
from generator.letter import Letter as Letter

class LabelOfScrItm(ScreenItem):
    TYPE=5
    LABELOFITEM=5
    
    def __init__(self):
        super(LabelOfScrItm,self).__init__()

        
    def setScrItm(self, scritm):
        self.labelOfScrItm  = scritm
    
    def text(self):
        return self.labelOfScrItm.label()+"\n"+self.labelOfScrItm.text()
    
    def letters(self):
        listletter = []
        txt = self.text()
        rows = txt.count('\n')
        letter = Letter()
        x = self.xbottomleft
        y = self.ybottomleft + (rows*letter.height)
        lastchar =''
        for c in txt:
            letter = Letter()
            letter.txt = c
            if len(listletter)<1:
                letter.xbottomleft = x
                letter.ybottomleft = y
            elif lastchar == '\n':
                x = self.xbottomleft
                letter.xbottomleft = x
                letter.ybottomleft = y - letter.height
            else:
                letter.xbottomleft = int(round(x + letter.width))
                letter.ybottomleft = y
            x = letter.xbottomleft
            y = letter.ybottomleft
            listletter.append(letter)
            lastchar = c
        return listletter
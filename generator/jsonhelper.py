from generator.screendefinition import ScreenDefinition
from generator.labelofscritm import LabelOfScrItm
from generator.screenitemfactory import ScreenItemFactory as sif
import json

class JsonHelper():
    # composite
    #  label
    #   letters (n)
    #    letter
    #     value
    #     coordinates
    #      x,y,x1,y1,x2,y2,x3,y3
    #    word
    #     value
    #     coordinates
    #      x,y,x1,y1,x2,y2,x3,y3
    #  image
    #   coordinates
    #    x,y,x1,y1,x2,y2,x3,y3
    #  imagebutton
    #   coordinates
    #    x,y,x1,y1,x2,y2,x3,y3
    #  menugroup
    #   coordinates
    #    x,y,x1,y1,x2,y2,x3,y3
    #  menuitem (n)
    #   coordinates
    #    x,y,x1,y1,x2,y2,x3,y3
    def __init__(self):
        #print("__init__")
        z=0
    
    def encode(self, filename, sd, figurewidth, figureheight, dpi):
        print ("encode")
        composites = []
        for item in sd.compositeList:
            label = sd.screenDefList[item.listpos1]
            scrobj = sd.screenDefList[item.listpos2]

            
            word= {"VALUE" : label.text(),
                   "COORDINATES" : {"X": label.xbottomleft,
                                    "Y": label.ybottomleft,
                                    "X1": label.xbottomleft,
                                    "Y1": label.ybottomleft + label.height,
                                    "X2": label.xbottomleft + label.width,
                                    "Y2": label.ybottomleft + label.height,
                                    "X3": label.xbottomleft + label.width,
                                    "Y3": label.ybottomleft, 
                                    "IX": label.internalposx,
                                    "IY": label.internalposy} 
                   }
            letters = label.letters()
            listletters = []
            for letter in letters:
                jletter= { "LETTER" : {
                    "VALUE" : letter.text(),
                    "COORDINATES" : {"X": letter.xbottomleft,
                                    "Y": letter.ybottomleft,
                                    "X1": letter.xbottomleft,
                                    "Y1": letter.ybottomleft + letter.height,
                                    "X2": letter.xbottomleft + letter.width,
                                    "Y2": letter.ybottomleft + letter.height,
                                    "X3": letter.xbottomleft + letter.width,
                                    "Y3": letter.ybottomleft} 
                    }
                }
                listletters.append(jletter)
            
            dictitem = {sif.labels[label.TYPE] :
                            {"LETTERS": listletters,
                             "WORD" : word },
                            sif.labels[scrobj.TYPE] :
                            {"COORDINATES" : {"X": scrobj.xbottomleft,
                                              "Y": scrobj.ybottomleft,
                                              "X1": scrobj.xbottomleft,
                                              "Y1": scrobj.ybottomleft + scrobj.height,
                                              "X2": scrobj.xbottomleft + scrobj.width,
                                              "Y2": scrobj.ybottomleft + scrobj.height,
                                              "X3": scrobj.xbottomleft + scrobj.width,
                                              "Y3": scrobj.ybottomleft, 
                                              "IX": scrobj.internalposx,
                                              "IY": scrobj.internalposy}
                             }
                            }
            composite = {"COMPOSITE" : dictitem}
            composites.append(composite)
        data = {"SCREEN" : composites,
                "FIGUREHEIGHT" : figureheight,
                "FIGUREWIDTH": figurewidth,
                "DPI" : dpi}    
        str = json.dumps(data)
        text_file = open(filename+".json", "w")
        text_file.write(str)
        text_file.close()
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from generator.screendefinition import ScreenDefinition
from generator.boxlinebox import BoxLineBox as BoxLineBox
from generator.menugroup import MenuGroup  as MenuGroup
from generator.menuitem import MenuItem as MenuItem
from generator.imagebutton import ImageButton as ImageButton
from generator.image import Image as Image
from generator.labelofscritm import LabelOfScrItm as LabelOfScrItm
import random
from generator.jsonhelper import JsonHelper as JsonHelper

class RenderScreen():
    
    def __init__(self, directory, filename, numberOfItems, dpi, widthInches,
                  heightInches, jitterlow, jitterhigh, incrementer, cleanupcycles, showcleanup, screenDefinition):
        #print("__init__")
        self.directory = directory
        self.numberOfItems = numberOfItems
        self.dpi = dpi
        self.widthInches = widthInches
        self.heightInches = heightInches
        self.widthInPixels = widthInches * dpi
        self.heightInPixels = heightInches * dpi
        self.jitterlow = jitterlow
        self.jitterhigh = jitterhigh
        self.incrementer = incrementer
        self.cleanupcycles = cleanupcycles
        self.showcleanup = showcleanup
        self.figurewidth = widthInches
        self.figureheight = heightInches
        self.filename = filename
        self.screenDefinition = screenDefinition
        
    def renderScreen(self):
        print("renderScreen")
        fig = plt.figure(figsize = (self.figurewidth,self.figureheight))
        ax = fig.add_axes([0, 0, 1, 1])
        sdl = self.screenDefinition.screenDefList
        for item in sdl:  
            if item.TYPE == LabelOfScrItm.LABELOFITEM:
                ax.text((item.xbottomleft)/self.widthInPixels,
                         (item.ybottomleft)/self.heightInPixels,
                         item.text(), fontname='Monospace')
            elif item.TYPE == MenuGroup.MENUGROUP:
                p = patches.Rectangle(
                    (item.xbottomleft/self.widthInPixels, item.ybottomleft/self.heightInPixels),
                     item.width/self.widthInPixels, item.height/self.heightInPixels,
                    fill=False, transform=ax.transAxes, clip_on=False
                    )
                ax.add_patch(p)
                changex = 0
                changey = 0
                for mi in item.menuItems:
                    p = patches.Rectangle(
                    ((item.xbottomleft+ changex)/self.widthInPixels ,
                      (item.ybottomleft+ changey)/self.heightInPixels),
                    mi.width/self.widthInPixels,
                     mi.height/self.heightInPixels,
                    fill=False, transform=ax.transAxes, clip_on=False
                    )
                    ax.add_patch(p)
                    changex = changex + mi.changex()
                    changey = changey + mi.changey()
            else:
                p = patches.Rectangle(
                    (item.xbottomleft/self.widthInPixels, item.ybottomleft/self.heightInPixels),
                     item.width/self.widthInPixels, item.height/self.heightInPixels,
                    fill=False, transform=ax.transAxes, clip_on=False
                    )
                ax.add_patch(p)
        for line in self.screenDefinition.compositeList:
            p = patches.Arrow(line.six(sdl)/self.widthInPixels,
                               line.siy(sdl)/self.heightInPixels,
                                -line.arrowscalar(sdl)[0]/self.widthInPixels,
                                 -line.arrowscalar(sdl)[1]/self.heightInPixels,
                                  width=10/self.widthInPixels
                                 )
            ax.add_patch(p)
        if (False):
            for overlap in self.screenDefinition.overlapList:
                print("plot")
                p1 = patches.Circle((overlap.x/self.widthInPixels, overlap.y/self.heightInPixels),radius=.01)
                ax.add_patch(p1)

            self.screenDefinition.cleanUp()
            sdl = self.screenDefinition.screenDefList
            for item in sdl:
                p = patches.Rectangle(
                    (item.xbottomleft/self.widthInPixels, item.ybottomleft/self.heightInPixels),
                     item.width/self.widthInPixels, item.height/self.heightInPixels,
                     fill=False, transform=ax.transAxes, clip_on=False, linestyle=":"
                    )
                ax.add_patch(p)
            for line in self.screenDefinition.compositeList:
                print("got here")
                p = patches.Arrow(line.six(sdl)/self.widthInPixels,
                               line.siy(sdl)/self.heightInPixels,
                                -line.arrowscalar(sdl)[0]/self.widthInPixels,
                                 -line.arrowscalar(sdl)[1]/self.heightInPixels,
                                      width=10/self.widthInPixels, color='r'
                                     )
                ax.add_patch(p)
        ax.set_axis_off()
        plt.show()

    def saveScreen(self):
        print("saveScreen")

        
import random
from generator.renderscreen import RenderScreen as RenderScreen
from generator.jsonhelper import JsonHelper as JsonHelper
from generator.screendefinition import ScreenDefinition

class RenderScreens(): 
    def __init__(self, directory, numberOfScreens, numberOfItemsOnScreenMax,
                 numberOfItemsOnScreenMin, dpi, widthInches, heightInches, testScreen, randomScreen,
                 jitterlow, jitterhigh, incrementer, cleanupcycles, render):
        #print("__init__")
        self.directory = directory
        self.numberOfScreens = numberOfScreens
        self.numberOfItemsOnScreenMax = numberOfItemsOnScreenMax
        self.numberOfItemsOnScreenMin  = numberOfItemsOnScreenMin
        self.dpi = dpi
        self.widthInches = widthInches
        self.heightInches = heightInches
        self.testScreen = testScreen
        self.randomScreen = randomScreen
        self.jitterlow = jitterlow
        self.jitterhigh = jitterhigh
        self.incrementer = incrementer
        self.cleanupcycles = cleanupcycles
        self.render = render
    
    def renderScreens(self):
        print("renderScreens")
        for scrnum in range(self.numberOfScreens):   
            numberOfItems = random.randint(self.numberOfItemsOnScreenMin,
                                            self.numberOfItemsOnScreenMax)
            filename = str(scrnum)
            widthInPixels = self.widthInches * self.dpi
            heightInPixels = self.heightInches * self.dpi
            figurewidth = self.widthInches
            figureheight = self.heightInches
            screenDefinition = ScreenDefinition(widthInPixels,
                                     heightInPixels,
                                      self.jitterlow,
                                       self.jitterhigh,
                                        self.incrementer,
                                         self.cleanupcycles)
            rs = RenderScreen(self.directory, filename, numberOfItems, self.dpi, self.widthInches,
                               self.heightInches, self.jitterlow, self.jitterhigh,
                                self.incrementer, self.cleanupcycles, self.testScreen, screenDefinition) 

            if self.testScreen:
                screenDefinition.testItems()
            if self.randomScreen:
                screenDefinition.randomGenerate(numberOfItems)
                screenDefinition.cleanUp()        
            if self.render:
                rs.renderScreen()
            else:
                jh = JsonHelper()
                jh.encode(self.directory
                          +filename,
                          screenDefinition,
                          figurewidth,
                          figureheight,
                          self.dpi)
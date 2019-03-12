import random
from generator.screendefinition import ScreenDefinition
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

class AnimateScreen(): 
       
    def __init__(self, directory, numberOfItemsOnScreenMax,
                 numberOfItemsOnScreenMin, dpi, widthInches, heightInches,
                 jitterlow, jitterhigh, incrementer, cleanupcycles):
        #
        self.numberOfItems = random.randint(numberOfItemsOnScreenMin, numberOfItemsOnScreenMax)
        self.figurewidth = widthInches
        self.figureheight = heightInches
        self.dpi = dpi
        self.width = self.figurewidth * self.dpi
        self.height = self.figureheight * self.dpi
        
        self.screenDefinition = ScreenDefinition(self.width, self.height, jitterlow, jitterhigh, incrementer, cleanupcycles)
        self.screenDefinition.randomGenerate(self.numberOfItems)
        #
        self.fig = plt.figure(figsize = (self.figurewidth,self.figureheight))
        # create the axes
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        # create rectangles
        i=0
        self.rect= []
        for item in self.screenDefinition.screenDefList:
            self.rect.append( (patches.Rectangle(
                (item.xbottomleft/self.width, item.ybottomleft/self.height),
                 item.width/self.width, item.height/self.height,
                fill=False, visible=True
                )) )
            self.ax.add_patch(self.rect[i])
            i=i+1    
        self.call_animation()
        plt.show()
    
    def init(self):
        #print("init")
        return self.rect 
        
    # animation function
    def animate(self, i):
        self.screenDefinition.cleanUp()
        sdl = self.screenDefinition
        for x in range(0, len(self.rect)):
            self.rect[x].set_xy((sdl.screenDefList[x].xbottomleft/self.width,
                                 sdl.screenDefList[x].ybottomleft/self.height))        
        return self.rect

    def call_animation(self):
        # call the animator function
        self.anim = FuncAnimation(self.fig, self.animate, frames=12000,
                                init_func= self.init,
                                interval=1, blit=True, repeat=False)
    
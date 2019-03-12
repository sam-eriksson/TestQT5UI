from render.jsonloader import JsonLoader as JsonLoader
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from os import listdir
from os.path import isfile, join

class Render():
    
    def __init__(self, directory):
        self.directory= directory
        self.j = JsonLoader(self.directory)
        
    def render(self, save):    
        print("render")
        listfiles = self.listthefiles()
        count=0
        for filename in listfiles:
            self.renderloop(filename, count, save)
            count=count+1

    def renderloop(self, filename, count, save):
        self.dict = self.j.load(filename)
        self.dpi = self.dict['DPI']
        self.figurewidth = self.dict['FIGUREWIDTH']
        self.figureheight = self.dict['FIGUREHEIGHT']
        self.widthInPixels = self.dpi * self.figurewidth
        self.heightInPixels = self.dpi * self.figureheight
        fig = plt.figure(figsize = (self.figurewidth,self.figureheight))
        ax = fig.add_axes([0, 0, 1, 1])
        composites = self.dict['SCREEN']
        for item in composites:
            two = item['COMPOSITE']
            if 'LABEL' in two: 
                label = two['LABEL']
                word = label['WORD']
                text = word['VALUE']
                coordinates = word['COORDINATES']
                letters = label['LETTERS']
                for lett in letters:
                    letter = lett['LETTER']
                    value = letter['VALUE']
                    coordinates2 = letter['COORDINATES']
                    xx= coordinates2['X']
                    yy= coordinates2['Y']
                    xx1= coordinates2['X1']
                    yy1= coordinates2['Y1']
                    xx2= coordinates2['X2']
                    yy2= coordinates2['Y2']
                    xx3= coordinates2['X3']
                    yy3= coordinates2['Y3']
                    #p = patches.Rectangle(
                        #(xx/self.widthInPixels, yy/self.heightInPixels),
                        #(xx3-xx)/self.widthInPixels, (yy2-yy)/self.heightInPixels,
                        #fill=False, transform=ax.transAxes, clip_on=False)
                    ax.text(xx/self.widthInPixels,
                            yy/self.heightInPixels,
                            value, fontname='Monospace')
                    
                x= coordinates['X']
                y= coordinates['Y']
                x1= coordinates['X1']
                y1= coordinates['Y1']
                x2= coordinates['X2']
                y2= coordinates['Y2']
                x3= coordinates['X3']
                y3= coordinates['Y3']
                six = x + coordinates['IX']
                siy = y + coordinates['IY']
                #p = patches.Circle((six/self.widthInPixels,
                   #siy/self.heightInPixels),1/self.heightInPixels, color='r')
                    
                #ax.add_patch(p)
                #ax.text(x/self.widthInPixels,
                 #y/self.heightInPixels,
                 #text, fontname='Monospace')
                #p = patches.Rectangle(
                #(x/self.widthInPixels, y/self.heightInPixels),
                #(x3-x)/self.widthInPixels, (y2-y)/self.heightInPixels,
                #fill=False, transform=ax.transAxes, clip_on=False)
                #ax.add_patch(p)  
            if 'IMAGE' in two:
                scritem = two['IMAGE']
            elif 'IMAGEBUTTON' in two:
                scritem = two['IMAGEBUTTON']
            elif 'MENU' in two:
                scritem = two['MENU']
            elif 'MENUGROUP' in two :
                scritem = two['MENUGROUP']
             
            coordinates = scritem['COORDINATES']
            x= coordinates['X']
            y= coordinates['Y']
            x1= coordinates['X1']
            y1= coordinates['Y1']
            x2= coordinates['X2']
            y2= coordinates['Y2']
            x3= coordinates['X3']
            y3= coordinates['Y3']
            eix = x + coordinates['IX']
            eiy = y + coordinates['IY']
            #p = patches.Circle((eix/self.widthInPixels,
                   #eiy/self.heightInPixels),1/self.heightInPixels, color='r')
                    
            #ax.add_patch(p)
            p = patches.Rectangle(
                (x/self.widthInPixels, y/self.heightInPixels),
                (x3-x)/self.widthInPixels, (y2-y)/self.heightInPixels,
                fill=False, transform=ax.transAxes, clip_on=False)
            ax.add_patch(p)
            p = patches.Arrow(six/self.widthInPixels,
                           siy/self.heightInPixels,
                            -(six-eix)/self.widthInPixels,
                             -(siy-eiy)/self.heightInPixels,
                              width=10/self.widthInPixels
                             )
            ax.add_patch(p)
        ax.set_axis_off()
        if save:
            imgfilename=str(count) + ".png"
            plt.savefig(self.directory
                        +imgfilename,
                        format="png", dpi=80)
            plt.close()
        else: 
            plt.show()

    def listthefiles(self):
        listoffiles= [f for f in listdir(self.directory) if isfile(join(self.directory, f))]
        jsonlist = list(filter(lambda item: item.endswith(".json") , listoffiles))
        jsonlist.sort(key = lambda x: int( x.split('.')[0]) )
        return jsonlist
        
from generator.menugroup import MenuGroup  as MenuGroup
from generator.menuitem import MenuItem as MenuItem
from generator.imagebutton import ImageButton as ImageButton
from generator.image import Image as Image
from generator.labelofscritm import LabelOfScrItm as LabelOfScrItm
from generator.letter import Letter as Letter

class ScreenItemFactory():
 
    labels = {MenuGroup.MENUGROUP : 'MENUGROUP',
              MenuItem.MENUITM : 'MENUITEM',
              ImageButton.IMAGEBUTTON : 'IMAGEBUTTON',
              LabelOfScrItm.LABELOFITEM : 'LABEL',
              Image.IMAGE: 'IMAGE'}
 
    def __init__(self):
        #print("init")
        z=0
    
    def screenItem(self,  key):
        if key == MenuGroup.MENUGROUP:
            return MenuGroup()
        elif key == MenuItem.MENUITM :
            return MenuItem()
        elif key == ImageButton.IMAGEBUTTON:
            return ImageButton()
        elif key == Image.IMAGE : 
            return Image()
        elif key == LabelOfScrItm.LABELOFITEM:
            return LabelOfScrItm()
        elif key == Letter.LETTER:
            return Letter()
        
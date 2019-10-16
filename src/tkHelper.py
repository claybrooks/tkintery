import tkinter as tk
from dataclasses import dataclass
import xml.etree.ElementTree as ET

tabSpace = '    '

#----------------------------------------------------------------------------------------------------------------------
# tkHelper
#______________________________________________________________________________________________________________________
class tkHelper(object):
   
    nameToType = {
        'Button':       tk.Button,
        'Canvas':       tk.Canvas,
        'Checkbutton':  tk.Checkbutton,
        'Entry':        tk.Entry,
        'Frame':        tk.Frame,
        'Label':        tk.Label,
        'Listbox':      tk.Listbox,
        'Menu':         tk.Menu,
        'Menubutton':   tk.Menubutton,
        'Message':      tk.Message,
        'Radiobutton':  tk.Radiobutton,
        'Scale':        tk.Scale,
        'Scrollbar':    tk.Scrollbar,
        'Text':         tk.Text,
        'Toplevel':     tk.Toplevel,
        'LabelFrame':   tk.LabelFrame,
        'PanedWindow':  tk.PanedWindow,
        'Spinbox':      tk.Spinbox,
        'OptionMenu':   tk.OptionMenu,
    }

    typeToName = {}
    for key, item in nameToType.items():
        typeToName[item] = key

        
    ignoreList = ['name', 
                  'x', 
                  'y', 
                  'width', 
                  'height',
                  'relx',
                  'rely',
                  'relwidth',
                  'relheight',
                  'saveOptions',
                  'command',]

    _defaultXML = {
        'x'     : 0,
        'y'     : 0,
        'rely'  : 0,
        'relx'  : 0,
    }
     
    #------------------------------------------------------------------------------------------------------------------
    # analyzePath
    #__________________________________________________________________________________________________________________
    @staticmethod
    def analyzePath(path):

        tokens = path.split(':')
        toplevel = tokens[0]
        subpath = ':'.join(tokens[1:])

        return len(tokens), toplevel, subpath
    
    #------------------------------------------------------------------------------------------------------------------
    # extractPath
    #__________________________________________________________________________________________________________________
    @staticmethod
    def extractPath(path):
        tokens = path.split(':')

        return tokens[0], ':'.join(tokens[1:-1]), tokens[-1]
    
    #------------------------------------------------------------------------------------------------------------------
    # writeLine
    #__________________________________________________________________________________________________________________
    @staticmethod
    def writeLine(line, f):
        f.write(line + '\n')
        
    #------------------------------------------------------------------------------------------------------------------
    # generateClass
    #__________________________________________________________________________________________________________________
    @staticmethod
    def generateClass(item, f, level):
        tkHelper.writeLine(tabSpace*level + f'class {item._name}(object):', f)

    #------------------------------------------------------------------------------------------------------------------
    # generateCode
    #__________________________________________________________________________________________________________________
    @staticmethod
    def generateInit(item, f, level):

        fullPath = item.getFullPath()

        tokens = fullPath.split(':')

        name = tokens[-1]
        framePath = ':'.join(tokens[1:-1])

        tkHelper.writeLine(tabSpace*(level+1) + f'def __init__(self):', f)
        tkHelper.writeLine(tabSpace*(level+2) + f'self.name      = "{name}"', f)
        tkHelper.writeLine(tabSpace*(level+2) + f'self.framePath = "{framePath}"', f)
        tkHelper.writeLine(tabSpace*(level+2) + f'self.fullPath  = "{fullPath}"', f)
        
    #------------------------------------------------------------------------------------------------------------------
    # generateCodeFromItem
    #__________________________________________________________________________________________________________________
    @staticmethod
    def generateCodeFromItem(item, f, level):
        tkHelper.generateClass(item, f, level)
        tkHelper.generateInit(item, f, level)

    #------------------------------------------------------------------------------------------------------------------
    # generateCodeFromFrame
    #__________________________________________________________________________________________________________________
    @staticmethod
    def generateCodeFromFrame(frame, f, level):
        
        tkHelper.generateClass(frame, f, level)

        for child in frame.getFrames().values():
            tkHelper.generateCodeFromFrame(child, f, level+1)

        # now put all of our items in the init
        for item in frame.getItems():
            tkHelper.generateCodeFromItem(item, f, level+1)
        
        tkHelper.generateInit(frame, f, level)

        parentClassPath = 'AutoGen.'+frame.getFullPath(delim='.')
        for childFrame in frame.getFrames().values():
            tkHelper.writeLine(tabSpace*(level+1+1) + f'self.{childFrame._name} = {parentClassPath}.{childFrame._name}()', f)

        for item in frame.getItems():
            tkHelper.writeLine(tabSpace*(level+1+1) + f'self.{item._name} = {parentClassPath}.{item._name}()', f)

    #------------------------------------------------------------------------------------------------------------------
    # generateCodeFromWindow
    #__________________________________________________________________________________________________________________
    @staticmethod
    def generateCodeFromWindow(window, f, level):
        
        tkHelper.generateClass(window, f, level)

        # iterate over each frame in window
        for key,frame in window.getFrames().items():
            tkHelper.generateCodeFromFrame(frame, f, level+1)

        tkHelper.generateInit(window, f, level)

        for key,frame in window.getFrames().items():
            tkHelper.writeLine(tabSpace*(level+1+1) + f'self.{frame._name} = AutoGen.{window._name}.{frame._name}()', f)

    #------------------------------------------------------------------------------------------------------------------
    # generateCodeFromApplication
    #__________________________________________________________________________________________________________________
    @staticmethod
    def generateCodeFromApplication(tkApp):

        with open ('src/GUI_Autogen.py', 'w+') as f:
            tkHelper.writeLine('class AutoGen(object):', f)
            
            level = 1

            # iterate over each window in our application
            for key,window in tkApp.getWindows().items():
                tkHelper.generateCodeFromWindow(window, f, level)

            tkHelper.writeLine(tabSpace*level + f'def __init__(self, tkApp):', f)

            # iterate over each window in our application and instantiate the window object
            for key,window in tkApp.getWindows().items():
                tkHelper.writeLine(tabSpace*(level+1) + f'self.{window._name} = AutoGen.{window._name}()', f) 
                
            # now iterate through the windows again, and get the items.  This time, look for items
            # that have _codeName set, and then make the helper code
            for windowKey,window in tkApp.getWindows().items():
                items = window.getItems()
                for item in items:
                    if item._codeName != '':

                        fullPathCode    = 'self.' + item.getFullPath(delim='.') + '.fullPath'
                        framePathCode   = 'self.' + item.getFullPath(delim='.') + '.framePath'
       
                        tkHelper.writeLine(tabSpace*(level+1) + f'self.{item._codeName}_framePath    = {framePathCode}', f)
                        tkHelper.writeLine(tabSpace*(level+1) + f'self.{item._codeName}_fullPath     = {fullPathCode}', f)
                        tkHelper.writeLine(tabSpace*(level+1) + f'self.{item._codeName}_windowName   = \'{windowKey}\'', f)
                        tkHelper.writeLine(tabSpace*(level+1) + f'self.{item._codeName}_name         = \'{item._name}\'', f)
                        tkHelper.writeLine(tabSpace*(level+1) + f'self.{item._codeName}_Tk           = tkApp.getItemFromWindow(self.{item._codeName}_windowName, self.{item._codeName}_framePath, self.{item._codeName}_name)', f)

    #------------------------------------------------------------------------------------------------------------------
    # loadXML
    #__________________________________________________________________________________________________________________
    @staticmethod
    def loadXML(ele, key, default=''):
        value = ele.getAttribute(key)

        if value == None:
            if value in tkHelper._defaultXML.keys():
                value = tkHelper._defaultXML[key]
            else:
                value = default

        return value


#----------------------------------------------------------------------------------------------------------------------
# placeData
#______________________________________________________________________________________________________________________
class placeData(object):
    def __init__(self):
        self._data = {
            'x'         : 0,
            'y'         : 0,
            'width'     : 0,
            'height'    : 0,
            'relx'      : 0.0,
            'rely'      : 0.0,
            'relwidth'  : 0.0,
            'relheight' : 0.0,
        }
    
    #------------------------------------------------------------------------------------------------------------------
    # get_x
    #__________________________________________________________________________________________________________________
    def get_x(self):
        return self._data['x']
    
    #------------------------------------------------------------------------------------------------------------------
    # get_y
    #__________________________________________________________________________________________________________________
    def get_y(self):
        return self._data['y']
    
    #------------------------------------------------------------------------------------------------------------------
    # get_width
    #__________________________________________________________________________________________________________________
    def get_width(self):
        return self._data['width']
    
    #------------------------------------------------------------------------------------------------------------------
    # get_height
    #__________________________________________________________________________________________________________________
    def get_height(self):
        return self._data['height']
    
    #------------------------------------------------------------------------------------------------------------------
    # get_relx
    #__________________________________________________________________________________________________________________
    def get_relx(self):
        return self._data['relx']
    
    #------------------------------------------------------------------------------------------------------------------
    # get_rely
    #__________________________________________________________________________________________________________________
    def get_rely(self):
        return self._data['rely']
    
    #------------------------------------------------------------------------------------------------------------------
    # get_relwidth
    #__________________________________________________________________________________________________________________
    def get_relwidth(self):
        return self._data['relwidth']
    
    #------------------------------------------------------------------------------------------------------------------
    # get_relheight
    #__________________________________________________________________________________________________________________
    def get_relheight(self):
        return self._data['relheight']
    #------------------------------------------------------------------------------------------------------------------
    # deepCopy
    #__________________________________________________________________________________________________________________
    def deepCopy(self, pos):
        for key in self._data:
            self._data[key] = pos._data[key]
        
    #------------------------------------------------------------------------------------------------------------------
    # deepCopy
    #__________________________________________________________________________________________________________________
    def loadFromValues(self, **kwargs):
        for key, value in kwargs.items():
            if key not in self._data:
                print (f'Invalid Key: {key} for tkHelper.PlaceData.loadFromValues')
                continue

            self._data[key] = value

    #------------------------------------------------------------------------------------------------------------------
    # loadFromElement
    #__________________________________________________________________________________________________________________
    def loadFromElement(self, ele):
        for key in self._data:
            self._data[key] = type(self._data[key])(tkHelper.loadXML(ele, key, self._data[key]))
        
    #------------------------------------------------------------------------------------------------------------------
    # saveToElement
    #__________________________________________________________________________________________________________________
    def saveToElement(self, ele):
        for key,value in self._data.items():
            ele.set(key, f'{value}')

#----------------------------------------------------------------------------------------------------------------------
# indent
#______________________________________________________________________________________________________________________
def indent(elem, level=0, more_sibs=False):
    tab='    '
    i = "\n"
    if level:
        i += (level-1) * tab
    num_kids = len(elem)
    if num_kids:
        if not elem.text or not elem.text.strip():
            elem.text = i + tab
            if level:
                elem.text += tab
        count = 0
        for kid in elem:
            indent(kid, level+1, count < num_kids - 1)
            count += 1
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
            if more_sibs:
                elem.tail += tab
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
            if more_sibs:
                elem.tail += tab
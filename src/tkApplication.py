import tkinter as tk
from tkEditor import tkEditor
import xml.etree.ElementTree as ET

from tkWindow import tkWindow

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

#----------------------------------------------------------------------------------------------------------------------
# MainApplication
#______________________________________________________________________________________________________________________
class tkApplication(object):

    MAIN_WINDOW = 'Main'

    def __init__(self, fullPathToFile):
        # Hold all of the windows of the application
        self._tkWindows = {}

        # create our tk root
        self._root = tk.Tk()
        self._root.geometry("500x500")

        # create our main window
        self._tkWindows[tkApplication.MAIN_WINDOW] = tkWindow(tk.Frame, tkApplication.MAIN_WINDOW, self._root, self)
        self._mainWindow = self._tkWindows[tkApplication.MAIN_WINDOW]
        
        self._mainWindow._tk.pack(side="top", fill="both", expand=True)

        self._callbackPaths = {}
        self._callbackTypes = {}

        self._updateCallbacks = []
        self._updateRateInMs = 16

        self.loadXML(fullPathToFile)

        self._root.after(self._updateRateInMs, self.__HandleUpdate)


    #------------------------------------------------------------------------------------------------------------------
    # _reportEvent
    #__________________________________________________________________________________________________________________
    def _reportEvent(self, windowName, framePath, itemName, *args):
       
        # first arg is always the type
        if len(args) == 0:
            return

        type = args[0]

        if type not in self._callbackTypes.keys():
            return

        path = ':'.join([windowName, framePath, itemName])

        # just send the last item for things that match exactly
        exactPathMessage = path.split(':')[-1]

        callbackType = self._callbackTypes[type]

        # process exact matches
        if path in callbackType.keys():
            for callback in callbackType[path]:
                callback(exactPathMessage, *args)

        # now we need to process any subsets
        for key, list in callbackType.items():
            if path.startswith(key) and path != key and key != '':

                # strip out the part of the path that the user registered for
                subsetPathMessage = path[len(key)+1:]

                for callback in list:
                    callback(subsetPathMessage, *args)
            elif key == '':
                for callback in list:
                    callback(path, *args)
        
    #------------------------------------------------------------------------------------------------------------------
    # registerToolbarCallback
    #__________________________________________________________________________________________________________________
    def registerCallback(self, path, typeFilter, callback):

        if typeFilter not in self._callbackTypes.keys():
            self._callbackTypes[typeFilter] = {}

        callbackType = self._callbackTypes[typeFilter]

        if path not in callbackType.keys():
            callbackType[path] = []

        callbackType[path].append(callback)
       
    #------------------------------------------------------------------------------------------------------------------
    # registerToolbarCallback
    #__________________________________________________________________________________________________________________
    def registerCallbackFromItem(self, tkItem, typeFilter, callback):
        
        # get the tkitems path
        path = tkItem.getPath()

        self.registerCallback(path, typeFilter, callback)

    #------------------------------------------------------------------------------------------------------------------
    # registerUpdateCallback
    #__________________________________________________________________________________________________________________
    def registerUpdateCallback(self,callback):
        self._updateCallbacks.append(callback)

    #------------------------------------------------------------------------------------------------------------------
    # setUpdateRate
    #__________________________________________________________________________________________________________________
    def setUpdateRate(self, updateRateInMs):
        self._updateRateInMs = updateRateInMs

    #------------------------------------------------------------------------------------------------------------------
    # __HandleUpdate
    #__________________________________________________________________________________________________________________
    def __HandleUpdate(self):
        for callback in self._updateCallbacks:
            callback()

        self._root.after(self._updateRateInMs, self.__HandleUpdate)
    #------------------------------------------------------------------------------------------------------------------
    # showWindow
    #__________________________________________________________________________________________________________________
    def toggleWindowVisibility(self, windowName):
        win = self.getWindow(windowName)

        # early out check
        if win == None:
            return None

        win.toggleVisibility()
    #------------------------------------------------------------------------------------------------------------------
    # open
    #__________________________________________________________________________________________________________________
    def open(self):
        pass
    
    #------------------------------------------------------------------------------------------------------------------
    # getFhelpocus
    #__________________________________________________________________________________________________________________
    def help(self):
        pass
    
    #------------------------------------------------------------------------------------------------------------------
    # exit
    #__________________________________________________________________________________________________________________
    def exit(self):
        pass

    #------------------------------------------------------------------------------------------------------------------
    # getFocus
    #__________________________________________________________________________________________________________________
    def getFocus(self):
        return self._root.focus_get()
    
    #------------------------------------------------------------------------------------------------------------------
    # getMainWindow
    #__________________________________________________________________________________________________________________
    def getMainWindow(self):
        return self._mainWindow
    
    #------------------------------------------------------------------------------------------------------------------
    # getWindow
    #__________________________________________________________________________________________________________________
    def getWindow(self, windowName):
        if windowName not in self._tkWindows.keys():
            print (f'Unknown window name: {windowName}')
            return None

        return self._tkWindows[windowName]
    
    #------------------------------------------------------------------------------------------------------------------
    # getWindows
    #__________________________________________________________________________________________________________________
    def getWindows(self):
        return self._tkWindows

    #------------------------------------------------------------------------------------------------------------------
    # getNumWindows
    #__________________________________________________________________________________________________________________
    def getNumWindows(self):
        return len(self._tkWindows.keys())
    
    #------------------------------------------------------------------------------------------------------------------
    # getWindowNames
    #__________________________________________________________________________________________________________________
    def getWindowNames(self):
        return self._tkWindows.keys()

    #------------------------------------------------------------------------------------------------------------------
    # getNumItemsInWindow
    #__________________________________________________________________________________________________________________
    def getNumFramesInWindow(self, windowName):

        win = self.getWindow(windowName)

        # early out check
        if win == None:
            return None

        return win.getNumFrames()

    #------------------------------------------------------------------------------------------------------------------
    # getRoot
    #__________________________________________________________________________________________________________________
    def getRoot(self):
        return self._root
        
    #------------------------------------------------------------------------------------------------------------------
    # addWindow
    #__________________________________________________________________________________________________________________
    def addWindow(self):
        name = f'tkWindow_{self.getNumWindows()}'
        self._tkWindows[name] = tkWindow(tk.Toplevel, name, self._root, self)
   
    #------------------------------------------------------------------------------------------------------------------
    # getFrameFromWindow
    #__________________________________________________________________________________________________________________
    def getFrameFromWindow(self, windowName, framePath):
        
        win = self.getWindow(windowName)

        # early out check
        if win == None:
            return None

        return win.getFrame(framePath)
    
    #------------------------------------------------------------------------------------------------------------------
    # getFramesFromWindow
    #__________________________________________________________________________________________________________________
    def getFramesFromWindow(self, windowName):

        win = self.getWindow(windowName)

        if win == None:
            return []

        return win.getFrames()

    #------------------------------------------------------------------------------------------------------------------
    # addFrameToWindow
    #__________________________________________________________________________________________________________________
    def addFrameToWindow(self, windowName, framePath, x, y, w, h):
        
        win = self.getWindow(windowName)

        # early out check
        if win == None:
            return False

        # add the item to the window
        return win.addFrame(itemName, framePath, x, y, w, h)
        
    #------------------------------------------------------------------------------------------------------------------
    # configureFrameInWindow
    #__________________________________________________________________________________________________________________
    def configureFrameInWindow(self, windowName, framePath, key, value):
        win = self.getWindow(windowName)

        if win == None:
            return

        win.configureFrame(framePath, key, value)
        
    #------------------------------------------------------------------------------------------------------------------
    # getItemFromWindow
    #__________________________________________________________________________________________________________________
    def getItemFromWindow(self, windowName, framePath, itemName):

        win = self.getWindow(windowName)

        if win == None:
            return None

        return win.getItem(framePath, itemName)
        
    #------------------------------------------------------------------------------------------------------------------
    # getMenubar
    #__________________________________________________________________________________________________________________
    def getMenubar(self, windowName):
         
        win = self.getWindow(windowName)
        
        if win == None:
            return None

        return win.getMenubar()
         
    #------------------------------------------------------------------------------------------------------------------
    # getItemsFromWindow
    #__________________________________________________________________________________________________________________
    def getItemsFromWindow(self, windowName):

        win = self.getWindow(windowName)

        if win == None:
            return

        return win.getItems()

    #------------------------------------------------------------------------------------------------------------------
    # loadXML
    #__________________________________________________________________________________________________________________
    def loadXML(self, fullPathToFile):
        tree = ET.parse(fullPathToFile)
        root = tree.getroot()

        # run through the window list
        windows = root.findall('Window')

        for window in windows:
            
            name = window.get('name')
            xsize = int(window.get('xsize'))
            ysize = int(window.get('ysize'))

            if name == tkApplication.MAIN_WINDOW:
                tkW = self._mainWindow
            else:
                self._tkWindows[name] = tkWindow(tk.Toplevel, name, self._root, self)
                tkW = self._tkWindows[name]

            tkW.loadXML(window, name, xsize, ysize)

    #------------------------------------------------------------------------------------------------------------------
    # saveXML
    #__________________________________________________________________________________________________________________
    def saveXML(self):
        # create our root element
        root = ET.Element('root')

        # now, iterate over each window and ask them to save
        for key, window in self._tkWindows.items():
            window.saveXML(root)

        # get the tree
        indent(root)
        tree = ET.ElementTree(root)

        tree.write('GUI.xml')

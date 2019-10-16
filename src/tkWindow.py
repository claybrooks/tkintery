import tkinter as tk
import xml.etree.ElementTree as ET

from tkHelper import tkHelper
from tkHelper import placeData

from tkMenubar import tkMenubar
from tkFrame import tkFrame
from tkOptionMenu import tkOptionMenu

class tkWindow(object):
    #------------------------------------------------------------------------------------------------------------------
    # __init__
    #__________________________________________________________________________________________________________________
    def __init__(self, type, name, parent, app, *args, **kwargs):

        self._type      = type
        self._name      = name
        self._parent    = parent
        self._isVisible = True
        self._app       = app

        # we don't have a menu bar yet
        self._menubar = None

        # create the underlying tk object
        self._tk = type(parent)
        self._tk.focus_set()

        # a window only has frames
        self._dictTkFrames = {}
          
    #------------------------------------------------------------------------------------------------------------------
    # getPath
    #__________________________________________________________________________________________________________________
    def getFullPath(self, delim=':'):
        return self._name
    
    #------------------------------------------------------------------------------------------------------------------
    # _reportEvent
    #__________________________________________________________________________________________________________________
    def _reportEvent(self, framePath, itemName, *args):
        self._app._reportEvent(self._name, framePath, itemName, *args)

    #------------------------------------------------------------------------------------------------------------------
    # _getWindow
    #__________________________________________________________________________________________________________________
    def _getWindow(self):
        if self._name == self._app.MAIN_WINDOW:
            return self._parent
        else:
            return self._tk
    
    #------------------------------------------------------------------------------------------------------------------
    # quit
    #__________________________________________________________________________________________________________________
    def toggleVisibility(self):
        
        window = self._getWindow()

        if window.winfo_ismapped():
            window.update()
            window.withdraw()
        else:
            window.update()
            window.deiconify()
    
    #------------------------------------------------------------------------------------------------------------------
    # addToolbar
    #__________________________________________________________________________________________________________________
    def addMenubar(self, name, items):
        if self._menubar == None:
            self._menubar = tkMenubar(self, name)

    #------------------------------------------------------------------------------------------------------------------
    # addItem
    #__________________________________________________________________________________________________________________
    def addFrame(self, framePath, pos):

        numTokens, toplevel, subpath = tkHelper.analyzePath(framePath)

        # we only have one path
        if numTokens == 1:

            # we don't expect this to exist yet
            if toplevel in self._dictTkFrames.keys():
                print (f'Frame: {toplevel} already exists within window {self._name}')
                return False

            # create the frame
            self._dictTkFrames[toplevel] = tkFrame(toplevel, self, self._tk, pos)
        else:

            # we expect this to exist
            if toplevel not in self._dictTkFrames.keys():
                print (f'Frame: {toplevel} does not exist within window {self._name}')
                return False

            # pass along the remainder of the path 
            self._dictTkFrames[toplevel].addFrame(subpath, pos)

        return True
        
    #------------------------------------------------------------------------------------------------------------------
    # addItem
    #__________________________________________________________________________________________________________________
    def addItem(self, framePath, itemName, itemType, pos):

        numTokens, toplevel, subpath = tkHelper.analyzePath(framePath)

        if toplevel not in self._dictTkFrames.keys():
            print (f'AddItem: Unknown frame {toplevel} in window {self._name}')
            return

        self._dictTkFrames[toplevel].addItem(subpath, itemName, itemType, pos)
    #------------------------------------------------------------------------------------------------------------------
    # getNumItems
    #__________________________________________________________________________________________________________________
    def getNumFrames(self):
        return len(self._dictTkFrames.keys())
    
    #------------------------------------------------------------------------------------------------------------------
    # getItem
    #__________________________________________________________________________________________________________________
    def getFrame(self, framePath):
        
        numTokens, toplevel, subpath = tkHelper.analyzePath(framePath)

        # we should at least have toplevel in our tkframes dict
        if toplevel not in self._dictTkFrames.keys():
            print (f'Unknown item: "{toplevel}" in window "{self._name}"')
            return None

        # only one token in path, just return this frame
        if numTokens == 1:
            return self._dictTkFrames[toplevel]
        # we have a deeper path, hand it off to the frame to handle
        else:
            return self._dictTkFrames[toplevel].getFrame(subpath)
    
    #------------------------------------------------------------------------------------------------------------------
    # getFrames
    #__________________________________________________________________________________________________________________
    def getFrames(self):
        return self._dictTkFrames
    
    #------------------------------------------------------------------------------------------------------------------
    # getItem
    #__________________________________________________________________________________________________________________
    def getItem(self, framePath, itemName):

        numTokens, toplevel, subpath = tkHelper.analyzePath(framePath)

        if toplevel not in self._dictTkFrames.keys():
            return None

        # we don't have a subpath, so it is this frame
        return self._dictTkFrames[toplevel].getItem(subpath, itemName)
    
    #------------------------------------------------------------------------------------------------------------------
    # getItems
    #__________________________________________________________________________________________________________________
    def getItems(self):

        items = []

        # iterate through each frame we have
        for value in self._dictTkFrames.values():
            items.extend(value.getAllItems())

        return items

    #------------------------------------------------------------------------------------------------------------------
    # getNumItems
    #__________________________________________________________________________________________________________________
    def getNumItems(self):
        return len(self.getItems())

    #------------------------------------------------------------------------------------------------------------------
    # getMenubar
    #__________________________________________________________________________________________________________________
    def getMenubar(self):
        return self._menubar

    #------------------------------------------------------------------------------------------------------------------
    # configureFrame
    #__________________________________________________________________________________________________________________
    def configureFrame(self, framePath, key, value):
        
        numTokens, toplevel, subpath = tkHelper.analyzePath(framePath)

        # the frame should exist within this window
        if toplevel not in self._dictTkFrames.keys():
            print (f'Unknown Frame: {toplevel} in window "{self._name}"')
            return

        # we only have one token, just configure it
        if numTokens == 1:
            self._dictTkFrames[toplevel].configureItem(key, value)
        # we have a path with multiple tokens, pass along to tkFrame to handle
        else:
            self._dictTkFrames[toplevel].configureItem(key, value, subpath)
        
    #------------------------------------------------------------------------------------------------------------------
    # saveGUI
    #__________________________________________________________________________________________________________________
    def saveXML(self, root):

        # create our subelement
        window = ET.SubElement(root, 'Window')

        # set the metedata of this window
        window.set('name', self._name)
        window.set('xsize', str(self._tk.winfo_width()))
        window.set('ysize', str(self._tk.winfo_height()))

        # save our menubar if we have one
        if self._menubar != None:
            self._menubar.saveXML(window)

        # iterate over all of our gui objects to get their xml representation
        for name, object in self._dictTkFrames.items():
            object.saveXML(window)

    #------------------------------------------------------------------------------------------------------------------
    # loadGUI
    #__________________________________________________________________________________________________________________
    def loadXML(self, window, name, xsize, ysize):

        # save the provided name
        self._name = name

        # build the geometry string
        #geoString = f'{xsize}x{ysize}'

        self._getWindow().geometry(f'{xsize}x{ysize}')

        # see if we have a menubar
        if window.hasMenubar():
            # create it
            self._menubar = tkMenubar(self, window.getMenubar().getAttributeName())

            #configure it
            self._menubar.loadXML(window.getMenubar())
        
        # iterate over all of the frame
        for frame in window.getFrames():

            # retrieve metadata for the child
            name = frame.getAttributeName()

            pos = placeData()
            pos.loadFromElement(frame)

            if self.addFrame(name, pos) == True:
                self._dictTkFrames[name].loadXML(frame)
import tkinter as tk

from tkHelper import tkHelper
from tkHelper import placeData

import xml.etree.ElementTree as ET

class tkItem(object):
    #------------------------------------------------------------------------------------------------------------------
    # __init__
    #__________________________________________________________________________________________________________________
    def __init__(self, type, name, parent, pos):
        self._parent    = parent
        self._type      = type
        self._name      = name
        self._pos       = placeData()

        # create ourselves
        self._tk = None
        self._create()
        self.updatePosition(pos)

        # lets capture all of the possible default options we have, this makes resetting easier
        self._defaultOptions = {}

        for option in self._tk.config().keys():
            self._defaultOptions[option] = self._tk[option]

        # bind to things
        self._tk.bind('<Enter>',            lambda event : self._parent._reportItemEvent(self._name, 'enter',   self, event))
        self._tk.bind('<Leave>',            lambda event : self._parent._reportItemEvent(self._name, 'leave',   self, event))
        self._tk.bind('<Motion>',           lambda event : self._parent._reportItemEvent(self._name, 'motion',  self, event))
        self._tk.bind('<ButtonPress-1>',    lambda event : self._parent._reportItemEvent(self._name, 'press',   self, event))
        self._tk.bind('<ButtonRelease-1>',  lambda event : self._parent._reportItemEvent(self._name, 'release', self, event))
        self._tk.bind('<KeyRelease>',       lambda event : self._parent._reportItemEvent(self._name, 'keyPress',self, event))

        # bind to a command if possible
        try:
            self._tk['command'] = lambda *args: self._parent._reportItemEvent(self._name, 'command', self, *args)
        except Exception as e:
            print ('Item: ' + self._name + ', Type: ' + tkHelper.typeToName[self._type] + ', Error: ' + str(e))

        self._configuredOptions = {}
        
        self._codeName = ''

    #------------------------------------------------------------------------------------------------------------------
    # getFullPath
    #__________________________________________________________________________________________________________________
    def getFullPath(self):
        return ':'.join([self._parent.getFullPath(), self._name])
    
    #------------------------------------------------------------------------------------------------------------------
    # getFramePath
    #__________________________________________________________________________________________________________________
    def getFramePath(self):
        return self.getFullPath()[1:-1]

    #------------------------------------------------------------------------------------------------------------------
    # get
    #__________________________________________________________________________________________________________________
    def get(self):
        return self._tk.get()
    
    #------------------------------------------------------------------------------------------------------------------
    # getWidth
    #__________________________________________________________________________________________________________________
    def getWidth(self):
        return self._tk.winfo_width()
    
    #------------------------------------------------------------------------------------------------------------------
    # getHeight
    #__________________________________________________________________________________________________________________
    def getHeight(self):
        return self._tk.winfo_height()

    #------------------------------------------------------------------------------------------------------------------
    # _create
    #__________________________________________________________________________________________________________________
    def _create(self):
        self._tk = self._type(self._parent)
        
    #------------------------------------------------------------------------------------------------------------------
    # updatePositionFromValues
    #__________________________________________________________________________________________________________________
    def updatePositionFromValues(self, save=True, **kwargs):
        # create a new pos object so we can pass it off to updatePosition
        newPos = placeData()
        newPos.loadFromValues(**kwargs)

        # run through normal updatePosition function
        self.updatePosition(newPos, save)

    #------------------------------------------------------------------------------------------------------------------
    # updatePosition
    #__________________________________________________________________________________________________________________
    def updatePosition(self, pos, save=True):

        # save incoming pos to our internal state
        if save:
            self._pos.deepCopy(pos)
            
        # place the object
        self._tk.place(x            = pos.get_x(), 
                   y            = pos.get_y(), 
                   width        = pos.get_width(),
                   height       = pos.get_height(),
                   relx         = pos.get_relx(),
                   rely         = pos.get_rely(),
                   relwidth     = pos.get_relwidth(),
                   relheight    = pos.get_relheight())
       
    #------------------------------------------------------------------------------------------------------------------
    # getType
    #__________________________________________________________________________________________________________________
    def getType(self):
        return self._type
    
    #------------------------------------------------------------------------------------------------------------------
    # getTkItem
    #__________________________________________________________________________________________________________________
    def getTkItem(self):
        return self._tk
    
    #------------------------------------------------------------------------------------------------------------------
    # configureItem
    #__________________________________________________________________________________________________________________
    def configureItem(self, key, value=''):
        try:

            # no value was provided, look up the default option for this key
            if value == '':
                value = self._defaultOptions[key]

            self._tk[key] = value

            # also update what we save out to the xml
            if key in self._configuredOptions.keys():
                self._configuredOptions[key] = value

        except Exception as e:
            print (e)

    #------------------------------------------------------------------------------------------------------------------
    # setEnabled
    #__________________________________________________________________________________________________________________
    def setEnabled(self, val):
        state = 'normal'
        if val == False:
            state = 'disabled'

        try:
            self._tk.config(state=state)
        except Exception as e:
            pass
        
    #------------------------------------------------------------------------------------------------------------------
    # loadXML
    #__________________________________________________________________________________________________________________
    def loadXML(self, item):
        # pass through the rest of the things from the xml
        for key,value in item.attributes():
            if key in tkHelper.ignoreList:
                continue

            if key == 'codeName':
                self._codeName = value
            else:
                # configure as described in the xml
                self.configureItem(key, value)
                self._configuredOptions[key] = value

    #------------------------------------------------------------------------------------------------------------------
    # saveGUI
    #__________________________________________________________________________________________________________________
    def saveXML(self, root):
        ele = ET.SubElement(root, tkHelper.typeToName[self._type])
        
        ele.set('name', self._name)

        self._pos.saveToElement(ele)

        # now go through all of our configured options
        for key,value in self._configuredOptions.items():
            ele.set(key, value)

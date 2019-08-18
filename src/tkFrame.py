
import tkinter as tk
import xml.etree.ElementTree as ET

from tkItem import tkItem
from tkOptionMenu import tkOptionMenu
from tkCheckbutton import tkCheckbutton

from tkHelper import tkHelper
from tkHelper import placeData

#----------------------------------------------------------------------------------------------------------------------
# tkFrame
#______________________________________________________________________________________________________________________
class tkFrame(tk.Frame):
    
    #------------------------------------------------------------------------------------------------------------------
    # __init__
    #__________________________________________________________________________________________________________________
    def __init__(self, name, parent, tkParent, pos):

        # init the frame aspect
        tk.Frame.__init__(self, tkParent)

        self._name      = name
        self._parent    = parent
        self._tkParent  = tkParent
        self._pos       = pos

        # lets capture all of the possible default options we have, this makes resetting easier
        self._defaultOptions = {}
        for option in self.config().keys():
            self._defaultOptions[option] = self[option]

        # bind to things
        self.bind('<Enter>',            lambda event : self._parent._reportEvent(self._name, '', 'enter',   self, event))
        self.bind('<Leave>',            lambda event : self._parent._reportEvent(self._name, '', 'leave',   self, event))
        self.bind('<Motion>',           lambda event : self._parent._reportEvent(self._name, '', 'motion',  self, event))
        self.bind('<ButtonPress-1>',    lambda event : self._parent._reportEvent(self._name, '', 'press',   self, event))
        self.bind('<ButtonRelease-1>',  lambda event : self._parent._reportEvent(self._name, '', 'release', self, event))

        # things to write back out to the xml
        self._configuredOptions = {}

        # this frame can contain tkItems
        self._dictTkItems = {}

        # this frame can also contain other frames
        self._dictTkFrames = {}
        
        # some things require special constructors
        self._specialItems = {
            'OptionMenu': tkOptionMenu,   
            'Checkbutton': tkCheckbutton, 
        }
        
        self.updatePosition(self._pos)
        
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
    # getWidth
    #__________________________________________________________________________________________________________________
    def getWidth(self):
        return self.winfo_width()
    
    #------------------------------------------------------------------------------------------------------------------
    # getHeight
    #__________________________________________________________________________________________________________________
    def getHeight(self):
        return self.winfo_height()

    #------------------------------------------------------------------------------------------------------------------
    # _reportItemEvent
    #__________________________________________________________________________________________________________________
    def _reportItemEvent(self, itemName, *args):
        self._parent._reportEvent(self._name, itemName, *args)
        
    #------------------------------------------------------------------------------------------------------------------
    # _reportEvent
    #__________________________________________________________________________________________________________________
    def _reportEvent(self, framePath, itemName, *args):
        self._parent._reportEvent(':'.join([self._name, framePath]), itemName, *args)
        
    #------------------------------------------------------------------------------------------------------------------
    # updatePosition
    #__________________________________________________________________________________________________________________
    def updatePosition(self, pos, save = True):

        # save incoming pos to our internal state
        if save:
            self._pos.deepCopy(pos)
            
        # place the object
        self.place(x            = pos.get_x(), 
                   y            = pos.get_y(), 
                   width        = pos.get_width(),
                   height       = pos.get_height(),
                   relx         = pos.get_relx(),
                   rely         = pos.get_rely(),
                   relwidth     = pos.get_relwidth(),
                   relheight    = pos.get_relheight())

    #------------------------------------------------------------------------------------------------------------------
    # analyzePath
    #__________________________________________________________________________________________________________________
    def analyzePath(self, path):

        tokens = path.split(':')
        toplevel = tokens[0]
        subpath = ':'.join(tokens[1:])

        return len(tokens), toplevel, subpath

    #------------------------------------------------------------------------------------------------------------------
    # addItem
    #__________________________________________________________________________________________________________________
    def addFrame(self, framePath, pos):

        numTokens, toplevel, subpath = tkHelper.analyzePath(framePath)

        # we only have one path
        if numTokens == 1:

            # we don't expect this to exist yet
            if toplevel in self._dictTkFrames.keys():
                print (f'Frame: {toplevel} already exists within frame {self._name}')
                return False

            # create the frame
            self._dictTkFrames[toplevel] = tkFrame(toplevel, self, self, pos)
        else:

            # we expect this to exist
            if toplevel not in self._dictTkFrames.keys():
                print (f'Frame: {toplevel} does not exist within frame {self._name}')
                return False

            # pass along the remainder of the path 
            self._dictTkFrames[toplevel].addFrame(subpath, pos)

        return True
        
    #------------------------------------------------------------------------------------------------------------------
    # getNumItems
    #__________________________________________________________________________________________________________________
    def getNumFrames(self):
        return len(self._dictTkFrames.keys())
    
    #------------------------------------------------------------------------------------------------------------------
    # getFrame
    #__________________________________________________________________________________________________________________
    def getFrame(self, framePath):
        
        numTokens, toplevel, subpath = tkHelper.analyzePath(framePath)

        # we should at least have toplevel in our tkframes dict
        if toplevel not in self._dictTkFrames.keys():
            print (f'Unknown item: "{toplevel}" in frame "{self._name}"')
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
    # configureItem
    #__________________________________________________________________________________________________________________
    def configureItem(self, key, value = '', path = ''):

        # there is more to the path
        if path != '':
            numTokens, toplevel, subpath = tkHelper.analyzePath(path)

            # our toplevel is in our dict
            if toplevel in self._dictTkFrames.keys():

                # pass off to the frame
                self._dictTkFrames[toplevel].configureFrame(key, value, subpath)

            # our toplevel is in our items
            elif toplevel in self._dictTkItems.keys():

                # pass off to the item
                self._dictTkItems[toplevel].configureItem(key, value)

        # there is nothing to this path, so configure the frame
        else:
            try:
                # no value was provided, look up the default option for this key
                if value == '':
                    value = self._defaultOptions[key]

                self[key] = value
            except Exception as e:
                print (e)

    #------------------------------------------------------------------------------------------------------------------
    # addItem
    #__________________________________________________________________________________________________________________
    def addItem(self, framePath, itemName, itemType, pos):
        

        if itemType not in tkHelper.nameToType.keys():
            print(f'ItemType: {itemType} is not supported by window {self._name}')
            return False
        
        numTokens, toplevel, subpath = tkHelper.analyzePath(framePath)

        # set some stuff up
        toCreate = tkItem

        if itemType in self._specialItems.keys():
            toCreate = self._specialItems[itemType]

        # we are adding directly to this frame
        if numTokens == 1:
            self._dictTkItems[itemName] = toCreate(tkHelper.nameToType[itemType], itemName, self, pos)
        
        # we have a frame path
        else:


            if toplevel not in self._dictTkFrames.keys():
                print (f'Unknown Frame {toplevel} in frame {self._name}')
                return False

            self._dictTkFrames[toplevel].addItem(subpath, itemName, itemType, pos)
            
        return True
        
    #------------------------------------------------------------------------------------------------------------------
    # getNumItems
    #__________________________________________________________________________________________________________________
    def getNumItems(self):
        return len(self._dictTkItems.keys())
    
    #------------------------------------------------------------------------------------------------------------------
    # getItem
    #__________________________________________________________________________________________________________________
    def getItem(self, framePath, itemName):

        # this is no frame path
        if framePath == '':
            if itemName not in self._dictTkItems.keys():
                return None
            else:
                return self._dictTkItems[itemName]
        # there is a frame path
        else:
            numTokens, toplevel, subpath = tkHelper.analyzePath(framePath)

            # top level is a frame
            if toplevel in self._dictTkFrames.keys():
                return self._dictTkFrames[toplevel].getItem(subpath, itemName)
            else:
                print (f'Unknown Frame: "{toplevel}" in frame "{self._name}"')
                return None
    #------------------------------------------------------------------------------------------------------------------
    # getItems
    #__________________________________________________________________________________________________________________
    def getItems(self):
        return [value for key,value in self._dictTkItems.items()]

    #------------------------------------------------------------------------------------------------------------------
    # getAllItems
    #__________________________________________________________________________________________________________________
    def getAllItems(self):

        items = self.getItems()

        # iterate through each frame we have
        for key,value in self._dictTkFrames.items():
            items.extend(value.getItems())

        return items

    #------------------------------------------------------------------------------------------------------------------
    # loadXML
    #__________________________________________________________________________________________________________________
    def loadXML(self, frame):
        
        # iterate through all the frames
        for child in frame.getFrames():

            # name should always exist
            name    = child.getAttributeName()

            if name in self._dictTkFrames.keys():
                print (f'Frame: {name} already in frame {self._name}')
                continue

            pos = placeData()
            pos.loadFromElement(child)

            # create the new frame
            self._dictTkFrames[name] = tkFrame(name, self, self, pos)

            # pass along to the frame
            self._dictTkFrames[name].loadXML(child)

        # iterate through all the things in this xml list
        for key,child in frame.subElements():

            # ignore frames
            if key == 'Frame':
                continue
                
            name    = child.getAttributeName()
            tag = child.getTag()

            pos = placeData()
            pos.loadFromElement(child)

            # see if we support this
            if tag not in tkHelper.nameToType.keys():
                print (f'{tag} is not support for frames')

            if self.addItem('', name, tag, pos):
                self._dictTkItems[name].loadXML(child)

    #------------------------------------------------------------------------------------------------------------------
    # saveXML
    #__________________________________________________________________________________________________________________
    def saveXML(self, root):

        ele = ET.SubElement(root, 'Frame')
        
        ele.set('name', self._name)

        # save our position data to the element
        self._pos.saveToElement(ele)

        # now go through all of our configured options
        for key,value in self._configuredOptions.items():
            ele.set(key, value)

        # now go through all of our tkItems
        for key,value in self._dictTkItems.items():
            value.saveXML(ele)

        # now do this to any other frames we may have
        for key,value in self._dictTkFrames.items():
            value.saveXML(ele)
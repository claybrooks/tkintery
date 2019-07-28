import tkinter as tk
from tkDropdown import tkDropdown
import xml.etree.ElementTree as ET

#----------------------------------------------------------------------------------------------------------------------
# Toolbar
#______________________________________________________________________________________________________________________
class tkMenubar(tk.Menu):
    
    typeMap = {
        'Radio':tk.Radiobutton
    }

    #------------------------------------------------------------------------------------------------------------------
    # __init__
    #__________________________________________________________________________________________________________________
    def __init__(self, parent, name, *args, **kwargs):
        
        # init ourselves
        tk.Menu.__init__(self, parent._getWindow(), tearoff=0)

        self._name = name

        # this map holds a list of items for the drop down
        self._dropDownMap = {}

        self._nameToIndex = {}

        # store the parent
        self._parent = parent

        # tell parent that we are a menu bar
        self._parent._getWindow().config(menu=self)

        self._relief = self['relief']

    #------------------------------------------------------------------------------------------------------------------
    # reportEvent
    #__________________________________________________________________________________________________________________
    def _reportEvent(self, path, itemName, *args):
        self._parent._reportEvent(':'.join([self._name, path]), itemName, *args)

    #----------------------------------------------------------------------------------------------------------------------
    # registerCallback
    #______________________________________________________________________________________________________________________
    def registerCallback(self, path, callback):

        #invalid path
        if path not in self._dropDownMap.keys():
            return

        if path not in self._toolbarCallbacks.keys():
            self._toolbarCallbacks[path] = []

        self._toolbarCallbacks[path].append(callback)

    #----------------------------------------------------------------------------------------------------------------------
    # saveGUI
    #______________________________________________________________________________________________________________________
    def onClick(self, path):

        menuPath = ':'.join(path.split(':')[:-1])
        itemClicked = path.split(':')[-1]

        if menuPath not in self._toolbarCallbacks.keys():
            return

        for callback in self._toolbarCallbacks[menuPath]:
            callback(path)
    
    #----------------------------------------------------------------------------------------------------------------------
    # setCanEdit
    #______________________________________________________________________________________________________________________
    def setCanEdit(self, can):
        pass

    #----------------------------------------------------------------------------------------------------------------------
    # getDropdown
    #______________________________________________________________________________________________________________________
    def getDropdown(self, path):
        # there may be ':' in the mpath
        tokens = path.split(':')

        # we are at the shortest path
        if len(tokens) == 1:
            if tokens[0] in self._dropDownMap:
                return self._dropDownMap[tokens[0]]
            else:
                return None

        # see if the first token is valid
        if tokens[0] in self._dropDownMap:
            self._dropDownMap[tokens[0]].getDropdown(':'.join(tokens[1:]))
        else:
            return None
        
    #----------------------------------------------------------------------------------------------------------------------
    # setEnabled
    #______________________________________________________________________________________________________________________
    def setEnabled(self, enabled):
        pass
    
    #----------------------------------------------------------------------------------------------------------------------
    # configureItem
    #______________________________________________________________________________________________________________________
    def configureItem(self, key, value=''):
        pass

    #----------------------------------------------------------------------------------------------------------------------
    # addDropdown
    #______________________________________________________________________________________________________________________
    def addDropdown(self, name, items):
        
        # we have nesting
        if ':' in name:
            tokens = name.split(':')

            # get the parent
            firstParent = tokens[0]
            rest = ':'.join(tokens[1:])

            # see if we have it
            if firstParent not in self._dropDownMap.keys():
                return

            self._dropDownMap[firstParent].addItems(rest, items)

        else:
            # we already have data for this
            if name in self._dropDownMap.keys():
                self._dropDownMap[name].addItems(name, items)
            else:
                self._dropDownMap[name] = tkDropdown(self, name, items)

                curIdx = len(self._nameToIndex.keys())
                self._nameToIndex[name] = curIdx

    #----------------------------------------------------------------------------------------------------------------------
    # saveGUI
    #______________________________________________________________________________________________________________________
    def saveXML(self, root):
        # create our subelement
        toolbar = ET.SubElement(root, 'Menubar')
        toolbar.set('name', self._name)

        # iterate over all of our gui objects to get their xml representation
        for name, dropdown in self._dropDownMap.items():
            dropdown.saveGUI(toolbar)

    #----------------------------------------------------------------------------------------------------------------------
    # loadGUI
    #______________________________________________________________________________________________________________________
    def loadXML(self, toolbarData):
        
        dropdowns = toolbarData.findall('Dropdown')

        for dropdown in dropdowns:

            dropdownName = dropdown.get('name')

            saveOptions = dropdown.get('saveOptions')
            if saveOptions == None:
                saveOptions = True

            dropdownItems = []
            for child in dropdown:
                dropdownItems.append([child.get('name'), child.get('type'), saveOptions])

            self.addDropdown(dropdownName, dropdownItems)
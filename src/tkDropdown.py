import tkinter as tk
import xml.etree.ElementTree as ET

class tkDropdown(tk.Menu):
    
    #----------------------------------------------------------------------------------------------------------------------
    # __init__
    #______________________________________________________________________________________________________________________
    def __init__(self, parent, name, items):
        # init ourselves
        tk.Menu.__init__(self, parent, tearoff=0)

        #store stuff
        self._parent = parent
        self._name = name

        # set up some vars
        self._dropDownMap = {}
        self._nameToIndex = {}
        self._nameToType = {}
        self._toolbarCallbacks = {}

        # add in the intial set
        self.addItems(name, items)

        # add as cascade to the parent
        parent.add_cascade(label=name, menu=self)
    
    #------------------------------------------------------------------------------------------------------------------
    # getName
    #__________________________________________________________________________________________________________________
    def getPath(self):
        if self._parent._name == 'Menubar':
            return self._name
        else:
            return self._parent.getPath() + ':' + self._name
        
    #------------------------------------------------------------------------------------------------------------------
    # setEnabled
    #__________________________________________________________________________________________________________________
    def setEnabled(path, enabled):
        pass

    #------------------------------------------------------------------------------------------------------------------
    # _reportItemEvent
    #__________________________________________________________________________________________________________________
    def _reportItemEvent(self, itemName, *args):
        self._parent._reportEvent(self._name, itemName, *args)
        
    #------------------------------------------------------------------------------------------------------------------
    # _reportEvent
    #__________________________________________________________________________________________________________________
    def _reportEvent(self, path, itemName, *args):
        self._parent._reportEvent(':'.join([self._name, path]), itemName, *args)

    #----------------------------------------------------------------------------------------------------------------------
    # addItem
    #______________________________________________________________________________________________________________________
    def addItem(self, label, type, saveOptions=True):

        self._nameToIndex[label] = len(self._nameToIndex.keys())
        self._nameToType[label] = type
        self._saveOptions = saveOptions

        if type == 'cascade':
            self._dropDownMap[label] = tkDropdown(self, label, [])
        else:
            # add our dropdown
            self.add(itemType=type, label=label, command=lambda label=f'{label}', type='click': self._reportItemEvent(label, type))
            
    #----------------------------------------------------------------------------------------------------------------------
    # getDropdown
    #______________________________________________________________________________________________________________________
    def getDropdown(self, path):
        # there may be ':' in the mpath
        tokens = path.split(':')

        # we are at the shortest path
        if len(tokens) == 1:
            if tokens[0] in self._dropDownItemMap:
                return self._dropDownItemMap[tokens[0]]
            else:
                return None

        # see if the first token is valid
        if tokens[0] in self._dropDownItemMap:
            self._dropDownItemMap[tokens[0]].getDropdown(':'.join(tokens[1:]))
        else:
            return None

    #----------------------------------------------------------------------------------------------------------------------
    # addItems
    #______________________________________________________________________________________________________________________
    def addItems(self, name, items):

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
            # this name already exists
            if name in self._dropDownMap.keys():
                self._dropDownMap[name].addItems(name, items)
            else:
                for props in items:

                    # extract data
                    label = props[0]
                    type = props[1]
                    saveOptions = props[2]

                    # add the item
                    self.addItem(label, type, saveOptions)
    
    #----------------------------------------------------------------------------------------------------------------------
    # saveGUI
    #______________________________________________________________________________________________________________________
    def saveGUI(self, root):
        
        # create a dropdown section
        dropdown = ET.SubElement(root, 'Dropdown')
        dropdown.set('name', self.getPath())
        
        if self._saveOptions:
            for key, index in self._nameToIndex.items():
                item = ET.SubElement(dropdown, 'Item')

                item.set('name', key)
                item.set('type', self._nameToType[key])
                
            # iterate over all dropdowns we own
            for key, dropDown in self._dropDownMap.items():

                # pass in the root, which is menubar.
                # it is saved as a flat list in the XML
                dropDown.saveGUI(root)
        else:
            dropdown.set('saveOptions', 'false')

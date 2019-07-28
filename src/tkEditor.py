
from tkHelper import tkHelper
from tkHelper import placeData

import tkinter as tk
#from GUI_Autogen import AutoGen#
#from Trigger import AutoGen
import configparser
import os

class tkEditor(object):
    
    #------------------------------------------------------------------------------------------------------------------
    # __init__
    #__________________________________________________________________________________________________________________
    def __init__(self, tkApp):

        self._tkApp = tkApp

        # create our autogen'ed tree structure        
        self._autogen = AutoGen()

        # save off some windows
        self._editor = self._autogen.Editor

        # save off some helpful editor items.
        self._snapGridSlider    = self._editor.Frame.snapGridSlider
        self._coordSubmit       = self._editor.Frame.placement.Stats.coord_submit
        self._submitConfig      = self._editor.Frame.reconfig.submitConfig

        self._windowSelection   = self._editor.Frame.ItemSelection.windowSelection
        self._frameSelection    = self._editor.Frame.ItemSelection.framePathSelection
        self._itemSelection     = self._editor.Frame.ItemSelection.itemSelection

        self._entryX            = self._editor.Frame.placement.Stats.entry_x
        self._entryY            = self._editor.Frame.placement.Stats.entry_y
        self._entryWidth        = self._editor.Frame.placement.Stats.entry_width
        self._entryHeight       = self._editor.Frame.placement.Stats.entry_height

        self._windowSelectionTk = tkApp.getItemFromWindow(self._editor._name, self._windowSelection._framePath, self._windowSelection._name)
        self._frameSelectionTk  = tkApp.getItemFromWindow(self._editor._name, self._frameSelection._framePath,  self._frameSelection._name)
        self._itemSelectionTk   = tkApp.getItemFromWindow(self._editor._name, self._itemSelection._framePath,   self._itemSelection._name)

        self._entryXTk          = tkApp.getItemFromWindow(self._editor._name, self._entryX._framePath,      self._entryX._name)
        self._entryYTk          = tkApp.getItemFromWindow(self._editor._name, self._entryY._framePath,      self._entryY._name)
        self._entryWidthTk      = tkApp.getItemFromWindow(self._editor._name, self._entryWidth._framePath,  self._entryWidth._name)
        self._entryHeightTk     = tkApp.getItemFromWindow(self._editor._name, self._entryHeight._framePath, self._entryHeight._name)

        self._config = configparser.ConfigParser()
        # no lower casing!
        # source: https://stackoverflow.com/questions/19359556/configparser-reads-capital-keys-and-make-them-lower-case
        self._config.optionxform = str
        self._config.read("C:\\Users\\clay_\Programming\\Git\\WeinerSchnitzel\\GUI\\config.cfg")

        # register for all editor updates
        self._tkApp.registerCallback('Editor:Menubar:Edit:New',     'click',    self._handleEditorNewItem)
        self._tkApp.registerCallback('Editor:Menubar:File:Save',    'click',    self._handleSave)
        self._tkApp.registerCallback('Editor:Menubar:File:Open',    'click',    self._handleOpen)
        self._tkApp.registerCallback('Editor:Menubar:File:Close',   'click',    self._handleClose)
        self._tkApp.registerCallback('Editor:Menubar:Edit:Enabled', 'click',    self._handleEditEnabled)
        self._tkApp.registerCallback('Editor:Menubar:Edit:Code Gen', 'click',   lambda *args : tkHelper.generateCodeFromApplication(self._tkApp))

        self._tkApp.registerCallback(self._snapGridSlider._fullPath,    'command', self._handleSnapGridSlider)
        self._tkApp.registerCallback(self._coordSubmit._fullPath,       'press',   self._handleSubmitCoordinates)
        self._tkApp.registerCallback(self._submitConfig._fullPath,      'press',   self._handleSubmitConfig)

        self._tkApp.registerCallback(self._entryX._fullPath,        'keyPress', self._handleSubmitCoordinates)
        self._tkApp.registerCallback(self._entryY._fullPath,        'keyPress', self._handleSubmitCoordinates)
        self._tkApp.registerCallback(self._entryWidth._fullPath,    'keyPress', self._handleSubmitCoordinates)
        self._tkApp.registerCallback(self._entryHeight._fullPath,   'keyPress', self._handleSubmitCoordinates)

        # bind to specific events for all
        self._tkApp.registerCallback('', 'press',   self._handleOnPress)
        self._tkApp.registerCallback('', 'release', self._handleOnRelease)
        self._tkApp.registerCallback('', 'enter',   self._handleOnEnter)
        self._tkApp.registerCallback('', 'leave',   self._handleOnLeave)
        self._tkApp.registerCallback('', 'motion',  self._handleOnMotion)

        # get our window stuff
        self._windowNames = self._tkApp.getWindowNames()

        # some state
        self._editorEnabled = False
        self._inEdit        = False
        self._snap          = 0
        self._proposedPos   = placeData()

        # for the object that we are editing
        self._capturedX = 0
        self._capturedY = 0

        self._isMoving      = False
        self._isResizing    = False

        # get our dropdowns
        self._tkApp.registerCallback(self._windowSelection._fullPath,   'command', self._handleWindowSelection)
        self._tkApp.registerCallback(self._frameSelection._fullPath,    'command', self._handleFrameSelection)
        self._tkApp.registerCallback(self._itemSelection._fullPath,     'command', self._handleItemSelection)

        # set the window options
        self._windowSelectionTk.setOptions(self._windowNames)

        self._editorMenubar = self._tkApp.getMenubar('Editor')
        self._edit          = self._editorMenubar.getDropdown('Edit')

        self._supportedClasses = [[key, 'command', False] for key,value in self._config.items('tkClasses') if value == 'true']

        self._edit.addItems('New', self._supportedClasses)

        # set up some default things
        self._defaultX      = self._config.getint('Default', 'x')
        self._defaultY      = self._config.getint('Default', 'y')
        self._defaultWidth  = self._config.getint('Default', 'width')
        self._defaultHeight = self._config.getint('Default', 'height')

        self._highlightQueue = []
      
    #------------------------------------------------------------------------------------------------------------------
    # _handleWindowSelection
    #__________________________________________________________________________________________________________________
    def extractArgs(self, *args):
        return args[0], args[1], args[2:]

    #------------------------------------------------------------------------------------------------------------------
    # _handleEntryXKey
    #__________________________________________________________________________________________________________________
    def _handleEntryXKey(self, path, *args):
        self.__h
    #------------------------------------------------------------------------------------------------------------------
    # _handleSubmitCoordinates
    #__________________________________________________________________________________________________________________
    def _handleSubmitCoordinates(self, path, *args):

        if self._editorEnabled:
            return

        command, item, args = self.extractArgs(*args)
        
        item = self._tkApp.getItemFromWindow(self._windowSelectionTk.get(), self._frameSelectionTk.get(), self._itemSelectionTk.get())

        if item == None:
            return

        try:
            item.updatePositionFromValues(x     = int(self._entryXTk.get()),
                                          y     = int(self._entryYTk.get()),
                                          width = int(self._entryWidthTk.get()),
                                          height= int(self._entryHeightTk.get()))
        except Exception as E:
            pass
        
    #------------------------------------------------------------------------------------------------------------------
    # _handleWindowSelection
    #__________________________________________________________________________________________________________________
    def _handleSubmitConfig(self, path, *args):

        if self._itemSelection.get() == '':
            return

        command, item, args = self.extractArgs(*args)
        
        item = self._tkApp.getItemFromWindow(self._windowSelectionTk.get(), self._frameSelectionTk.get(), self._itemSelectionTk.get())

        item.configureItem(self.configKey.get(), self.configValue.get())

    #------------------------------------------------------------------------------------------------------------------
    # _handleWindowSelection
    #__________________________________________________________________________________________________________________
    def _handleWindowSelection(self, path, *args):

        command, item, args = self.extractArgs(*args)

        allFrames = self._tkApp.getFramesFromWindow(args[0])

        self._frameSelectionTk.setOptions(allFrames)
        self._itemSelectionTk.setOptions([])

    #------------------------------------------------------------------------------------------------------------------
    # _handleFrameSelection
    #__________________________________________________________________________________________________________________
    def _handleFrameSelection(self, path, *args):
        
        command, item, args = self.extractArgs(*args)

        frame = self._tkApp.getFrameFromWindow(self._windowSelectionTk.get(), args[0])

        items = [x for x in frame._dictTkItems.keys()]

        self._itemSelectionTk.setOptions(items)
    
    #------------------------------------------------------------------------------------------------------------------
    # _handleItemSelection
    #__________________________________________________________________________________________________________________
    def _setEntryText(self, entry, text):
        entry._tk.delete(0,tk.END)
        entry._tk.insert(0,text)
        return

    #------------------------------------------------------------------------------------------------------------------
    # _handleItemSelection
    #__________________________________________________________________________________________________________________
    def _handleItemSelection(self, path, *args):
        
        command, item, args = self.extractArgs(*args)

        item = self._tkApp.getItemFromWindow(self._windowSelectionTk.get(), self._frameSelectionTk.get(), args[0])

        self._setEntryText(self._entryXTk, str(item._pos.get_x()))
        self._setEntryText(self._entryYTk, str(item._pos.get_y()))
        self._setEntryText(self._entryWidthTk, str(item._pos.get_width()))
        self._setEntryText(self._entryHeightTk, str(item._pos.get_height()))


    #------------------------------------------------------------------------------------------------------------------
    # _handleEditEnabledCheckbox
    #__________________________________________________________________________________________________________________
    def _enableEditView(self, _tk, enabled):

        if enabled:
            _tk.configureItem('borderwidth', '3')
        else:
            _tk.configureItem('borderwidth')

    #------------------------------------------------------------------------------------------------------------------
    # _handleEditEnabledCheckbox
    #__________________________________________________________________________________________________________________
    def _handleEditEnabled(self, path, *args):

        self._editorEnabled = False if self._editorEnabled else True

        for win in self._tkApp.getWindowNames():
            for item in self._tkApp.getItemsFromWindow(win):
                try:
                    item.setEnabled(not self._editorEnabled)
                    self._enableEditView(item, self._editorEnabled)
                except Exception as e:
                    pass

    #------------------------------------------------------------------------------------------------------------------
    # _handleEditorNewItem
    #__________________________________________________________________________________________________________________
    def _handleEditorNewItem(self, path, *args):
        
        win = self._tkApp.getWindow(self._windowSelectionTk.get())

        if win == None:
            return

        # now get the selected frame path
        framePath = self._frameSelectionTk.get()

        if framePath == '':
            return

        numItems = win.getNumItems()

        itemName = f'tkEditorNewObject_{numItems}'
        
        newPos = placeData()
        newPos.x        = self._defaultX
        newPos.y        = self._defaultY
        newPos.width    = self._defaultWidth
        newPos.height   = self._defaultHeight

        # we are treating path as the type, this is due to how we registered for the callbacks to this function
        if path in self._config:
            newPos.x       = self._config.getint(path, 'x',      fallback=newPos.x)
            newPos.y       = self._config.getint(path, 'y',      fallback=newPos.y)
            newPos.width   = self._config.getint(path, 'width',  fallback=newPos.width)
            newPos.height  = self._config.getint(path, 'height', fallback=newPos.height)


        if win.addItem(framePath, itemName, path, newPos):
            # be sure to enable the editing view if we are edit enabled
            _tk = self._tkApp.getItemFromWindow(win, itemName)
            self._enableEditView(_tk, self._editorEnabled)
    
    #------------------------------------------------------------------------------------------------------------------
    # _handleEdit
    #__________________________________________________________________________________________________________________
    def _handleEdit(self, item, event):
        
        # get some mouse information
        globalX, globalY = event.x_root, event.y_root
        relX, relY = event.x, event.y

        if self._snap != 1:
            globalX = int(globalX/self._snap) * self._snap
            globalY = int(globalY/self._snap) * self._snap
            relX    = int(relX/self._snap) * self._snap
            relY    = int(relY/self._snap) * self._snap

        # we are not currently in edit
        if self._inEdit == False:

            self._capturedX = globalX
            self._capturedY = globalY

            self._inEdit = True
            
            self._proposedPos.deepCopy(item._pos)

            # figure if we are resizing or not
            if relX > (item.getWidth() / 2.0):
                self._isResizing = True
            else:
                self._isMoving = True

        diffX = globalX - self._capturedX
        diffY = globalY - self._capturedY

        if self._isMoving:
            self._proposedPos.loadFromValues(x = item._pos.get_x() + diffX,
                                            y = item._pos.get_y() + diffY)
        else:
            self._proposedPos.loadFromValues(width = item._pos.get_width() + diffX,
                                            height = item._pos.get_height() + diffY)
        
        item.updatePosition(self._proposedPos, False)

    #------------------------------------------------------------------------------------------------------------------
    # _handleSave
    #__________________________________________________________________________________________________________________
    def _handleSave(self, path, *args):
        self._tkApp.saveXML()

    #------------------------------------------------------------------------------------------------------------------
    # _handleSave
    #__________________________________________________________________________________________________________________
    def _handleOpen(self, path, *args):
        pass

    #------------------------------------------------------------------------------------------------------------------
    # _handleSave
    #__________________________________________________________________________________________________________________
    def _handleClose(self, path, *args):
        pass
    
    #------------------------------------------------------------------------------------------------------------------
    # _handleOnEntry
    #__________________________________________________________________________________________________________________
    def setHoverView(self, item, should):

        if should:
            item.configureItem('background', 'black')
        else:
            item.configureItem('background')

    #------------------------------------------------------------------------------------------------------------------
    # _handleOnEntry
    #__________________________________________________________________________________________________________________
    def _handleOnEnter(self, path, *args):
        
        if not self._editorEnabled or self._isMoving or self._isResizing:
            return
        
        command, item, args = self.extractArgs(*args)
        
        self.setHoverView(item, True)

        # now, if there was a prev, undo the background
        if len(self._highlightQueue) > 0:
            self.setHoverView(self._highlightQueue[-1], False)

        self._highlightQueue.append(item)

    #------------------------------------------------------------------------------------------------------------------
    # _handleOnLeave
    #__________________________________________________________________________________________________________________
    def _handleOnLeave(self, path, *args):
        
        if self._editorEnabled == False or self._inEdit == True:
            return

        command, item, args = self.extractArgs(*args)
        
        self.setHoverView(item, False)

        # get the top of the highlight queue and reapply the background
        self._highlightQueue = self._highlightQueue[:-1]

        if len(self._highlightQueue) > 0:
            self.setHoverView(self._highlightQueue[-1], True)

    #------------------------------------------------------------------------------------------------------------------
    # _handleOnMotion
    #__________________________________________________________________________________________________________________
    def _handleOnMotion(self, path, *args):
        if self._editorEnabled == False:
            return

        if self._inEdit:

            command, item, args = self.extractArgs(*args)

            self._handleEdit(item, args[0])

    #------------------------------------------------------------------------------------------------------------------
    # _handleOnPress
    #__________________________________________________________________________________________________________________
    def _handleOnPress(self, path, *args):

        if self._editorEnabled == False:
            return
        
        command, item, args = self.extractArgs(*args)

        self._handleEdit(item, args[0])

    #------------------------------------------------------------------------------------------------------------------
    # _handleOnRelease
    #__________________________________________________________________________________________________________________
    def _handleOnRelease(self, path, *args):

        if self._editorEnabled == False or self._inEdit == False:
            return
        
        command, item, args = self.extractArgs(*args)

        self._inEdit = False

        item.updatePosition(self._proposedPos)

        self._isMoving = False
        self._isResizing = False

    #------------------------------------------------------------------------------------------------------------------
    # _handleSnapGridSlider
    #__________________________________________________________________________________________________________________
    def _handleSnapGridSlider(self, path, *args):
        
        command, item, args = self.extractArgs(*args)

        level = int(args[0])

        if level <= 0:
            level = 1

        self._snap = level
from tkItem import tkItem
import tkinter as tk

#----------------------------------------------------------------------------------------------------------------------
# __init__
#______________________________________________________________________________________________________________________
class tkCheckbutton(tkItem):
    
    #------------------------------------------------------------------------------------------------------------------
    # __init__
    #__________________________________________________________________________________________________________________
    def __init__(self, type, name, parent, pos):

        # create internals first
        self._var = tk.BooleanVar()

        # this will trigger _create()
        tkItem.__init__(self, type, name, parent, pos)

    #------------------------------------------------------------------------------------------------------------------
    # __init__
    #__________________________________________________________________________________________________________________
    def _create(self):
        self._tk = self._type(self._parent, text="", variable=self._var)

    #------------------------------------------------------------------------------------------------------------------
    # get
    #__________________________________________________________________________________________________________________
    def set(self, val):
        return self._var.set(val)

    #------------------------------------------------------------------------------------------------------------------
    # get
    #__________________________________________________________________________________________________________________
    def get(self):
        return self._var.get()
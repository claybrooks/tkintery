from tkItem import tkItem
import tkinter as tk

#----------------------------------------------------------------------------------------------------------------------
# __init__
#______________________________________________________________________________________________________________________
class tkOptionMenu(tkItem):
    
    #------------------------------------------------------------------------------------------------------------------
    # __init__
    #__________________________________________________________________________________________________________________
    def __init__(self, type, name, parent, pos):

        # create internals first
        self._var = tk.StringVar()

        # this will trigger _create()
        tkItem.__init__(self, type, name, parent, pos)

    #------------------------------------------------------------------------------------------------------------------
    # __init__
    #__________________________________________________________________________________________________________________
    def _create(self):
        self._tk = self._type(self._parent, self._var, "")
        
    #------------------------------------------------------------------------------------------------------------------
    # setOptions
    #__________________________________________________________________________________________________________________
    def setOptions(self, newOptions):
        # Reset var and delete all old options
        self._var.set('')
        self._tk['menu'].delete(0, 'end')

        # Insert list of new options (tk._setit hooks them up to var)
        for choice in newOptions:
            self._tk['menu'].add_command(label=choice, command=tk._setit(self._var, choice, lambda *args: self._parent._reportItemEvent(self._name, 'command', self, *args)))

    #------------------------------------------------------------------------------------------------------------------
    # getSelectedOption
    #__________________________________________________________________________________________________________________
    def get(self):
        return self._var.get()
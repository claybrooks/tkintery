from tkinter import Menu, RAISED, Menubutton, Widget, _setit, TclError

'''
This is a small modification to the already existing tk.OptionMenu.
As it stands, optionmenu does not allow for a 'name' variable
'''
class OptionMenu(Menubutton):
    """OptionMenu which allows the user to select a value from a menu."""

    def __init__(self, master, variable, value, name, *values, **kwargs):
        """Construct an optionmenu widget with the parent MASTER, with
        the resource textvariable set to VARIABLE, the initially selected
        value VALUE, the other menu values VALUES and an additional
        keyword argument command."""
        kw = {"borderwidth": 2, "textvariable": variable,
              "indicatoron": 1, "relief": RAISED, "anchor": "c",
              "highlightthickness": 2}
        Widget.__init__(self, master, "menubutton", kw)
        self.widgetName = 'tk_optionMenu'
        menu = self.__menu = Menu(self, name="menu", tearoff=0)
        self.menuname = menu._w
        # 'command' is the only supported keyword
        callback = kwargs.get('command')
        
        # UPDATE, ALLOW FOR NAME
        self._name = name

        if 'command' in kwargs:
            del kwargs['command']

        if kwargs:
            raise TclError('unknown option -'+kwargs.keys()[0])
        menu.add_command(label=value,
                 command=_setit(variable, value, callback))
        for v in values:
            menu.add_command(label=v,
                     command=_setit(variable, v, callback))
        self["menu"] = menu

    def __getitem__(self, name):
        if name == 'menu':
            return self.__menu
        return Widget.__getitem__(self, name)

    def destroy(self):
        """Destroy this widget and the associated menu."""
        Menubutton.destroy(self)
        self.__menu = None
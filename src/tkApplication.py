import json
import tkinter as tk

########################################################################################################################
#
########################################################################################################################
class tkApplication(object):

    tkObjMap = {
        'Button':       tk.Button,
        'Canvas':       tk.Canvas,
        'Checkbutton':  tk.Checkbutton,
        'Entry':        tk.Entry,
        'Frame':        tk.Frame,
        'Label':        tk.Label,
        'Listbox':      tk.Listbox,
        'Menu':         tk.Menu,
        'Menubutton':   tk.Menubutton,
        'Message':      tk.Message,
        'Radiobutton':  tk.Radiobutton,
        'Scale':        tk.Scale,
        'Scrollbar':    tk.Scrollbar,
        'Text':         tk.Text,
        'Toplevel':     tk.Toplevel,
        'LabelFrame':   tk.LabelFrame,
        'PanedWindow':  tk.PanedWindow,
        'Spinbox':      tk.Spinbox,
        'OptionMenu':   tk.OptionMenu,
    }

    ####################################################################################################################
    #
    ####################################################################################################################
    def __init__(self, file):
        
        # create the root object
        self._root = None

        # save off the file
        self._file = file

        # this is our update rate
        self._updatePeriodInMillis = 30

        # everyone listening for updates
        self._updateCycleListeners = []

        # menu callbacks
        self._menuCallbacks = {}

        # load the gui
        self.loadGUI(file)

        self._root.after(self._updatePeriodInMillis, self.__process)

    ####################################################################################################################
    #
    ####################################################################################################################
    def start(self):
        self._root.mainloop()
        
    ####################################################################################################################
    #
    ####################################################################################################################
    def loadGUI(self, file):
        
        if self._root == None:
            self._root = tk.Tk()

        for child in self._root.winfo_children():
            child.delete()

        try:
            with open(file, 'r') as file:
                config = json.load(file)
        except Exception as e:
            print (f'Exception while loading GUI: {e}')
            return

        size="500x500"
        if 'size' in config.keys():
            size = config['size']

        self._root.geometry(size)

        if 'menu' in config:
            self.__loadMenu(config['menu'])

        if 'frames' in config:
            self.__loadFrames(config['frames'])

    ####################################################################################################################
    #
    ####################################################################################################################
    def attachToUpdateCycle(self, callback):
        if callback != None and callback not in self._updateCycleListeners:
            self._updateCycleListeners.append(callback)

    ####################################################################################################################
    #
    ####################################################################################################################
    def attachToUserInput(self, path, callback):
        try:
            tkItem = self._root.nametowidget(path)
            tkItem.config(command=callback)
        except Exception as e:
            print (f'Exception attaching to user input: {e}')

    ####################################################################################################################
    #
    ####################################################################################################################
    def attachToMenuInput(self, path, callback):
        try:
            self._menuCallbacks[path].append(callback)
        except Exception as e:
            print (f'Exception attaching to menu input: {e}')

    ####################################################################################################################
    #
    ####################################################################################################################
    def __process(self):

        for callback in self._updateCycleListeners:
            callback()

        self._root.after(self._updatePeriodInMillis, self.__process)

    ####################################################################################################################
    #
    ####################################################################################################################
    def __loadMenu(self, menuConfig):
        
        name = menuConfig['name']

        self._menubar = tk.Menu(self._root, name=name)

        if 'tabs' in menuConfig.keys():
            self.__loadMenuTabs(menuConfig['tabs'], self._menubar)

        self._root.config(menu=self._menubar)

    ####################################################################################################################
    #
    ####################################################################################################################
    def __loadMenuTabs(self, menuTabConfig, root=None):

        if root == None:
            root = self._menubar

        for tabEntry, tabConfig in menuTabConfig.items():
            print (f'Processing Menu Tab: {tabEntry}')

            name = tabConfig['name']
            menu = tk.Menu(self._menubar, tearoff=0, name=name)

            if 'entries' in tabConfig.keys():
                self.__loadTabEntries(tabConfig['entries'], menu)

            root.add_cascade(label=tabEntry, menu=menu)

    ####################################################################################################################
    #
    ####################################################################################################################
    def __loadTabEntries(self, entries, menu):

        for entry in entries:
            name = '.'.join(self.__getName(menu))
            name = name+'.'+entry

            if name not in self._menuCallbacks.keys():
                self._menuCallbacks[name] = []
                
            callable = lambda name=name: self.__menuCommandCallback(name)
            menu.add_command(label=entry, command=callable)

    ####################################################################################################################
    #
    ####################################################################################################################
    def __getName(self, tkItem):
        if tkItem.master == None:
            return []

        parentTokens = self.__getName(tkItem.master)
        parentTokens.append(tkItem._name)

        return parentTokens

    ####################################################################################################################
    #
    ####################################################################################################################
    def __menuCommandCallback(self, name, *args, **kwargs):
        if name in self._menuCallbacks.keys():
            for callback in self._menuCallbacks[name]:
                callback()
                
    ####################################################################################################################
    #
    ####################################################################################################################
    def __loadFrames(self, framesConfig, root=None):
        
        if root == None:
            root = self._root

        for frameName, frameConfig in framesConfig.items():
            print (f'Loading Frame: {frameName}')

            frame = tk.Frame(root, name=frameName)

            if 'location' in frameConfig.keys():
                frame.place(**frameConfig['location'])

            if 'config' in frameConfig.keys():
                frame.config(**frameConfig['config'])

            if 'items' in frameConfig.keys():
                self.__loadItems(frameConfig['items'], frame)

            if 'frames' in frameConfig.keys():
                self.__loadFrames(frameConfig['frames'], frame)
            
    ####################################################################################################################
    #
    ####################################################################################################################
    def __loadItems(self, itemsConfig, root=None):
        
        if root == None:
            root = self._root

        for itemType, itemConfig in itemsConfig.items():
            
            name = itemConfig['name']
            
            print (f'Loading Item: {name}')

            if itemType not in tkApplication.tkObjMap.keys():
                print (f'Invalid Type: {name}:{itemType}')

            tkItem = tkApplication.tkObjMap[itemType](root, name=name)

            if 'config' in itemConfig.keys():
                tkItem.config(**itemConfig['config'])

            if 'location' in itemConfig.keys():
                tkItem.place(**itemConfig['location'])

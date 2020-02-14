import json
import tkinter as tk

# custom class imports
import application.optionmenu as optionmenu

########################################################################################################################
#
########################################################################################################################
class Application(object):

    nameToClass = {
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
        'OptionMenu':   optionmenu.OptionMenu,
    }

    classToName = {}
    for key,value in nameToClass.items():
        classToName[value] = key

    ####################################################################################################################
    #
    ####################################################################################################################
    def __init__(self, file):
        
        # create the root object
        self._root = tk.Tk()

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
    def reloadGUI(self):

        for child in self._root.winfo_children():
            child.delete()

        self.loadGUI(self._file)

    ####################################################################################################################
    #
    ####################################################################################################################
    def loadGUI(self, file):
        
        try:
            with open(file, 'r') as file:
                config = json.load(file)
        except Exception as e:
            print (f'Exception while loading GUI: {e}')
            return

        # the root of the config file is an array consisting of window information
        for windowConfig in config['windows']:
            self.__loadWindowFromConfig(windowConfig)
                
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
            item = self.itemFromPath(path)
            item.config(command=callback)
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
    def itemFromPath(self, path):
        if 'mainWindow.' in path:
            path = path.replace('mainWindow.', '')

        return self._root.nametowidget(path)

    ####################################################################################################################
    #
    ####################################################################################################################
    def __jsonGet(self, json, key, default=None):

        try:
            return json[key]
        except KeyError:
            if default == None:
                raise KeyError
            return default

    ####################################################################################################################
    #
    ####################################################################################################################
    def __jsonPop(self, json, key, default=None):

        toRet = self.__jsonGet(json, key, default)
        if key in json.keys():
            del json[key]

        return toRet

    ####################################################################################################################
    #   A Window Configuration has the following keys
    #   'name': Name of the window.  Must start with lower case letter.  At least one window must be named 'mainWindow'
    #   'size': Specifies size of the window
    #   'config': A dictionary containing key value pairs for the window
    #   'items': an array of children to load into the window
    ####################################################################################################################
    def __loadWindowFromConfig(self, jsonConfig):

        # extract anything that won't get passed to constructor
        items   = self.__jsonPop(jsonConfig, 'items',   [])
        menu    = self.__jsonPop(jsonConfig, 'menubar', {})
        config  = self.__jsonPop(jsonConfig, 'config',  {})
        title   = self.__jsonPop(jsonConfig, 'title')
        size    = self.__jsonPop(jsonConfig, 'size')

        # if the name is 'mainWindow', the window will be the root that got passed in.  If it is anything other than
        # 'mainWindow', create a top level as the child of root.  The code will treat windows as siblings, even though
        # in memory they are stored as children.
        if jsonConfig['name'] == 'mainWindow':
            window = self._root
        else:
            window = tk.Toplevel(master=self._root, cnf=config, **jsonConfig)

        # set the title
        window.title(title)

        # set the size
        window.geometry(size)

        # load the menu into the window
        self.__loadMenubarFromConfig(menu, window)

        # load in the items into the window
        for item in items:
            self.__loadItemFromConfig(item, window)
            
    ####################################################################################################################
    #   Every itemConfig can have the following keys, items marked with * are optional
    #   name: Name of this widget
    #   place: the place dictionary for this widget
    #   *items: Any children belonging to this widget (Only acceptable for Frame types)
    #   
    ####################################################################################################################
    def __loadItemFromConfig(self, itemConfig, root):
        
        # extract anything from this config that will not get passed to constructor
        items       = self.__jsonPop(itemConfig, 'items', [])
        place       = self.__jsonPop(itemConfig, 'place')
        typeName    = self.__jsonPop(itemConfig, 'type')
        config      = self.__jsonPop(itemConfig, 'config')

        type = Application.nameToClass[typeName]

        print (f'loading: {itemConfig["name"]}')
        item = type(master=root, cnf=config, **itemConfig)

        item.place(**place)

        for child in items:
            self.__loadItemFromConfig(itemConfig=child, root=item)

    ####################################################################################################################
    #
    ####################################################################################################################
    def __loadMenubarFromConfig(self, menubarConfig, root):
        
        # we have an empty menu, just ignore this
        if menubarConfig == {}:
            return

        menubar = tk.Menu(master=root)

        for item in menubarConfig:
            self.__loadMenuFromConfig(item, menubar)

        root.config(menu=menubar)

    ####################################################################################################################
    #   Each menuConfig can have the following keys, those marked with * are optional
    #   name: Name of the menu item
    #   *items: Any child menu items to nest
    #   *config: Any configuration necessary for this menu
    #   *type: Assumed type will be command if it has no children.  If it has children, assumed type will be another
    #          menu.  If the type is something other than menu and it has children, the type will be ignored. 
    ####################################################################################################################
    def __loadMenuFromConfig(self, menuConfig, root):

        items   = self.__jsonPop(menuConfig, 'items',   [])
        cnf     = self.__jsonPop(menuConfig, 'config',  {})
        type    = self.__jsonPop(menuConfig, 'type',    '')
        label   = self.__jsonPop(menuConfig, 'label')
        name    = self.__jsonPop(menuConfig, 'name')

        # create the menu
        menu = tk.Menu(root, cnf=cnf, **menuConfig)

        if len(items) > 0:
            for item in items:
                self.__loadMenuFromConfig(item, menu)
            root.add_cascade(label=label, menu=menu)
        else:
            typeFunc = root.add_command

            if type == 'checkbutton':
                typeFunc = root.add_checkbutton
            elif type == 'radiobutton':
                typeFunc = root.add_radiobutton
                
            typeFunc(label=label, command=lambda name=name: self.__menuCommandCallback(name))

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
    def __getName(self, item):
        if item.master == None:
            return []

        parentTokens = self.__getName(item.master)
        parentTokens.append(item._name)

        return parentTokens

    ####################################################################################################################
    #
    ####################################################################################################################
    def __menuCommandCallback(self, name, *args, **kwargs):
        if name in self._menuCallbacks.keys():
            for callback in self._menuCallbacks[name]:
                callback()

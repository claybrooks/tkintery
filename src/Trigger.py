class AutoGen(object):
    class Main(object):
        class Frame(object):
            def __init__(self):
                _name      = "Frame"
                _framePath = ""
                _fullPath  = "Main:Frame"
            class tkEditorNewObject_0(object):
                def __init__(self):
                    _name      = "tkEditorNewObject_0"
                    _framePath = "Frame"
                    _fullPath  = "Main:Frame:tkEditorNewObject_0"
            self.tkEditorNewObject_0: tkEditorNewObject_0()
        self.Frame: Frame()
        def __init__(self):
            _name      = "Main"
            _framePath = ""
            _fullPath  = "Main"
    class ItemWindow(object):
        class ItemSelection(object):
            def __init__(self):
                _name      = "ItemSelection"
                _framePath = ""
                _fullPath  = "ItemWindow:ItemSelection"
            class windowSelection(object):
                def __init__(self):
                    _name      = "windowSelection"
                    _framePath = "ItemSelection"
                    _fullPath  = "ItemWindow:ItemSelection:windowSelection"
            self.windowSelection: windowSelection()
            class framePathSelection(object):
                def __init__(self):
                    _name      = "framePathSelection"
                    _framePath = "ItemSelection"
                    _fullPath  = "ItemWindow:ItemSelection:framePathSelection"
            self.framePathSelection: framePathSelection()
            class itemSelection(object):
                def __init__(self):
                    _name      = "itemSelection"
                    _framePath = "ItemSelection"
                    _fullPath  = "ItemWindow:ItemSelection:itemSelection"
            self.itemSelection: itemSelection()
        self.ItemSelection: ItemSelection()
        def __init__(self):
            _name      = "ItemWindow"
            _framePath = ""
            _fullPath  = "ItemWindow"
    class Editor(object):
        class Frame(object):
            class ItemSelection(object):
                def __init__(self):
                    _name      = "ItemSelection"
                    _framePath = "Frame"
                    _fullPath  = "Editor:Frame:ItemSelection"
                class windowSelection(object):
                    def __init__(self):
                        _name      = "windowSelection"
                        _framePath = "Frame:ItemSelection"
                        _fullPath  = "Editor:Frame:ItemSelection:windowSelection"
                self.windowSelection: windowSelection()
                class framePathSelection(object):
                    def __init__(self):
                        _name      = "framePathSelection"
                        _framePath = "Frame:ItemSelection"
                        _fullPath  = "Editor:Frame:ItemSelection:framePathSelection"
                self.framePathSelection: framePathSelection()
                class itemSelection(object):
                    def __init__(self):
                        _name      = "itemSelection"
                        _framePath = "Frame:ItemSelection"
                        _fullPath  = "Editor:Frame:ItemSelection:itemSelection"
                self.itemSelection: itemSelection()
            class placement(object):
                class Stats(object):
                    def __init__(self):
                        _name      = "Stats"
                        _framePath = "Frame:placement"
                        _fullPath  = "Editor:Frame:placement:Stats"
                    class label_x(object):
                        def __init__(self):
                            _name      = "label_x"
                            _framePath = "Frame:placement:Stats"
                            _fullPath  = "Editor:Frame:placement:Stats:label_x"
                    self.label_x: label_x()
                    class label_y(object):
                        def __init__(self):
                            _name      = "label_y"
                            _framePath = "Frame:placement:Stats"
                            _fullPath  = "Editor:Frame:placement:Stats:label_y"
                    self.label_y: label_y()
                    class label_width(object):
                        def __init__(self):
                            _name      = "label_width"
                            _framePath = "Frame:placement:Stats"
                            _fullPath  = "Editor:Frame:placement:Stats:label_width"
                    self.label_width: label_width()
                    class label_height(object):
                        def __init__(self):
                            _name      = "label_height"
                            _framePath = "Frame:placement:Stats"
                            _fullPath  = "Editor:Frame:placement:Stats:label_height"
                    self.label_height: label_height()
                    class entry_x(object):
                        def __init__(self):
                            _name      = "entry_x"
                            _framePath = "Frame:placement:Stats"
                            _fullPath  = "Editor:Frame:placement:Stats:entry_x"
                    self.entry_x: entry_x()
                    class entry_y(object):
                        def __init__(self):
                            _name      = "entry_y"
                            _framePath = "Frame:placement:Stats"
                            _fullPath  = "Editor:Frame:placement:Stats:entry_y"
                    self.entry_y: entry_y()
                    class entry_width(object):
                        def __init__(self):
                            _name      = "entry_width"
                            _framePath = "Frame:placement:Stats"
                            _fullPath  = "Editor:Frame:placement:Stats:entry_width"
                    self.entry_width: entry_width()
                    class entry_height(object):
                        def __init__(self):
                            _name      = "entry_height"
                            _framePath = "Frame:placement:Stats"
                            _fullPath  = "Editor:Frame:placement:Stats:entry_height"
                    self.entry_height: entry_height()
                    class coord_submit(object):
                        def __init__(self):
                            _name      = "coord_submit"
                            _framePath = "Frame:placement:Stats"
                            _fullPath  = "Editor:Frame:placement:Stats:coord_submit"
                    self.coord_submit: coord_submit()
                class configure(object):
                    def __init__(self):
                        _name      = "configure"
                        _framePath = "Frame:placement"
                        _fullPath  = "Editor:Frame:placement:configure"
                    class placeConfigKey(object):
                        def __init__(self):
                            _name      = "placeConfigKey"
                            _framePath = "Frame:placement:configure"
                            _fullPath  = "Editor:Frame:placement:configure:placeConfigKey"
                    self.placeConfigKey: placeConfigKey()
                    class placeConfigValue(object):
                        def __init__(self):
                            _name      = "placeConfigValue"
                            _framePath = "Frame:placement:configure"
                            _fullPath  = "Editor:Frame:placement:configure:placeConfigValue"
                    self.placeConfigValue: placeConfigValue()
                    class submitPlaceConfig(object):
                        def __init__(self):
                            _name      = "submitPlaceConfig"
                            _framePath = "Frame:placement:configure"
                            _fullPath  = "Editor:Frame:placement:configure:submitPlaceConfig"
                    self.submitPlaceConfig: submitPlaceConfig()
                def __init__(self):
                    _name      = "placement"
                    _framePath = "Frame"
                    _fullPath  = "Editor:Frame:placement"
                self.Stats: Stats()
                self.configure: configure()
            class reconfig(object):
                def __init__(self):
                    _name      = "reconfig"
                    _framePath = "Frame"
                    _fullPath  = "Editor:Frame:reconfig"
                class configKey(object):
                    def __init__(self):
                        _name      = "configKey"
                        _framePath = "Frame:reconfig"
                        _fullPath  = "Editor:Frame:reconfig:configKey"
                self.configKey: configKey()
                class configValue(object):
                    def __init__(self):
                        _name      = "configValue"
                        _framePath = "Frame:reconfig"
                        _fullPath  = "Editor:Frame:reconfig:configValue"
                self.configValue: configValue()
                class submitConfig(object):
                    def __init__(self):
                        _name      = "submitConfig"
                        _framePath = "Frame:reconfig"
                        _fullPath  = "Editor:Frame:reconfig:submitConfig"
                self.submitConfig: submitConfig()
            class InnerFrame(object):
                def __init__(self):
                    _name      = "InnerFrame"
                    _framePath = "Frame"
                    _fullPath  = "Editor:Frame:InnerFrame"
            def __init__(self):
                _name      = "Frame"
                _framePath = ""
                _fullPath  = "Editor:Frame"
            class snapGridSlider(object):
                def __init__(self):
                    _name      = "snapGridSlider"
                    _framePath = "Frame"
                    _fullPath  = "Editor:Frame:snapGridSlider"
            self.snapGridSlider: snapGridSlider()
            self.ItemSelection: ItemSelection()
            self.placement: placement()
            self.reconfig: reconfig()
            self.InnerFrame: InnerFrame()
        self.Frame: Frame()
        def __init__(self):
            _name      = "Editor"
            _framePath = ""
            _fullPath  = "Editor"
    def __init__(self, tkApp):
        Main: Main()
        ItemWindow: ItemWindow()
        Editor: Editor()
        self.configKey_framePath    = self.ditor.Frame.reconfig.configKe_framePath
        self.configKey_fullPath     = self.Editor.Frame.reconfig.configKey_fullPath
        self.configKey_windowName   = Editor
        self.configKey_name         = configKey
        self.configKey_Tk           = tkApp.getItemFromWindow(self.configKey_windowName, self.configKey_framePath, self.configKey_name)

class AutoGen(object):
    class Main(object):
        class Frame(object):
            def __init__(self):
                self.name      = "Frame"
                self.framePath = ""
                self.fullPath  = "Main:Frame"
        def __init__(self):
            self.name      = "Main"
            self.framePath = ""
            self.fullPath  = "Main"
            self.Frame = AutoGen.Main.Frame()
    class ItemWindow(object):
        class ItemSelection(object):
            def __init__(self):
                self.name      = "ItemSelection"
                self.framePath = ""
                self.fullPath  = "ItemWindow:ItemSelection"
        def __init__(self):
            self.name      = "ItemWindow"
            self.framePath = ""
            self.fullPath  = "ItemWindow"
            self.ItemSelection = AutoGen.ItemWindow.ItemSelection()
    class Editor(object):
        class Frame(object):
            class ItemSelection(object):
                def __init__(self):
                    self.name      = "ItemSelection"
                    self.framePath = "Frame"
                    self.fullPath  = "Editor:Frame:ItemSelection"
            class placement(object):
                class Stats(object):
                    class label_x(object):
                        def __init__(self):
                            self.name      = "label_x"
                            self.framePath = "Frame:placement:Stats"
                            self.fullPath  = "Editor:Frame:placement:Stats:label_x"
                    class label_y(object):
                        def __init__(self):
                            self.name      = "label_y"
                            self.framePath = "Frame:placement:Stats"
                            self.fullPath  = "Editor:Frame:placement:Stats:label_y"
                    class label_width(object):
                        def __init__(self):
                            self.name      = "label_width"
                            self.framePath = "Frame:placement:Stats"
                            self.fullPath  = "Editor:Frame:placement:Stats:label_width"
                    class label_height(object):
                        def __init__(self):
                            self.name      = "label_height"
                            self.framePath = "Frame:placement:Stats"
                            self.fullPath  = "Editor:Frame:placement:Stats:label_height"
                    class entry_x(object):
                        def __init__(self):
                            self.name      = "entry_x"
                            self.framePath = "Frame:placement:Stats"
                            self.fullPath  = "Editor:Frame:placement:Stats:entry_x"
                    class entry_y(object):
                        def __init__(self):
                            self.name      = "entry_y"
                            self.framePath = "Frame:placement:Stats"
                            self.fullPath  = "Editor:Frame:placement:Stats:entry_y"
                    class entry_width(object):
                        def __init__(self):
                            self.name      = "entry_width"
                            self.framePath = "Frame:placement:Stats"
                            self.fullPath  = "Editor:Frame:placement:Stats:entry_width"
                    class entry_height(object):
                        def __init__(self):
                            self.name      = "entry_height"
                            self.framePath = "Frame:placement:Stats"
                            self.fullPath  = "Editor:Frame:placement:Stats:entry_height"
                    class coord_submit(object):
                        def __init__(self):
                            self.name      = "coord_submit"
                            self.framePath = "Frame:placement:Stats"
                            self.fullPath  = "Editor:Frame:placement:Stats:coord_submit"
                    def __init__(self):
                        self.name      = "Stats"
                        self.framePath = "Frame:placement"
                        self.fullPath  = "Editor:Frame:placement:Stats"
                        self.label_x = AutoGen.Editor.Frame.placement.Stats.label_x()
                        self.label_y = AutoGen.Editor.Frame.placement.Stats.label_y()
                        self.label_width = AutoGen.Editor.Frame.placement.Stats.label_width()
                        self.label_height = AutoGen.Editor.Frame.placement.Stats.label_height()
                        self.entry_x = AutoGen.Editor.Frame.placement.Stats.entry_x()
                        self.entry_y = AutoGen.Editor.Frame.placement.Stats.entry_y()
                        self.entry_width = AutoGen.Editor.Frame.placement.Stats.entry_width()
                        self.entry_height = AutoGen.Editor.Frame.placement.Stats.entry_height()
                        self.coord_submit = AutoGen.Editor.Frame.placement.Stats.coord_submit()
                class configure(object):
                    class placeConfigKey(object):
                        def __init__(self):
                            self.name      = "placeConfigKey"
                            self.framePath = "Frame:placement:configure"
                            self.fullPath  = "Editor:Frame:placement:configure:placeConfigKey"
                    class placeConfigValue(object):
                        def __init__(self):
                            self.name      = "placeConfigValue"
                            self.framePath = "Frame:placement:configure"
                            self.fullPath  = "Editor:Frame:placement:configure:placeConfigValue"
                    class submitPlaceConfig(object):
                        def __init__(self):
                            self.name      = "submitPlaceConfig"
                            self.framePath = "Frame:placement:configure"
                            self.fullPath  = "Editor:Frame:placement:configure:submitPlaceConfig"
                    def __init__(self):
                        self.name      = "configure"
                        self.framePath = "Frame:placement"
                        self.fullPath  = "Editor:Frame:placement:configure"
                        self.placeConfigKey = AutoGen.Editor.Frame.placement.configure.placeConfigKey()
                        self.placeConfigValue = AutoGen.Editor.Frame.placement.configure.placeConfigValue()
                        self.submitPlaceConfig = AutoGen.Editor.Frame.placement.configure.submitPlaceConfig()
                class label_x(object):
                    def __init__(self):
                        self.name      = "label_x"
                        self.framePath = "Frame:placement:Stats"
                        self.fullPath  = "Editor:Frame:placement:Stats:label_x"
                class label_y(object):
                    def __init__(self):
                        self.name      = "label_y"
                        self.framePath = "Frame:placement:Stats"
                        self.fullPath  = "Editor:Frame:placement:Stats:label_y"
                class label_width(object):
                    def __init__(self):
                        self.name      = "label_width"
                        self.framePath = "Frame:placement:Stats"
                        self.fullPath  = "Editor:Frame:placement:Stats:label_width"
                class label_height(object):
                    def __init__(self):
                        self.name      = "label_height"
                        self.framePath = "Frame:placement:Stats"
                        self.fullPath  = "Editor:Frame:placement:Stats:label_height"
                class entry_x(object):
                    def __init__(self):
                        self.name      = "entry_x"
                        self.framePath = "Frame:placement:Stats"
                        self.fullPath  = "Editor:Frame:placement:Stats:entry_x"
                class entry_y(object):
                    def __init__(self):
                        self.name      = "entry_y"
                        self.framePath = "Frame:placement:Stats"
                        self.fullPath  = "Editor:Frame:placement:Stats:entry_y"
                class entry_width(object):
                    def __init__(self):
                        self.name      = "entry_width"
                        self.framePath = "Frame:placement:Stats"
                        self.fullPath  = "Editor:Frame:placement:Stats:entry_width"
                class entry_height(object):
                    def __init__(self):
                        self.name      = "entry_height"
                        self.framePath = "Frame:placement:Stats"
                        self.fullPath  = "Editor:Frame:placement:Stats:entry_height"
                class coord_submit(object):
                    def __init__(self):
                        self.name      = "coord_submit"
                        self.framePath = "Frame:placement:Stats"
                        self.fullPath  = "Editor:Frame:placement:Stats:coord_submit"
                class placeConfigKey(object):
                    def __init__(self):
                        self.name      = "placeConfigKey"
                        self.framePath = "Frame:placement:configure"
                        self.fullPath  = "Editor:Frame:placement:configure:placeConfigKey"
                class placeConfigValue(object):
                    def __init__(self):
                        self.name      = "placeConfigValue"
                        self.framePath = "Frame:placement:configure"
                        self.fullPath  = "Editor:Frame:placement:configure:placeConfigValue"
                class submitPlaceConfig(object):
                    def __init__(self):
                        self.name      = "submitPlaceConfig"
                        self.framePath = "Frame:placement:configure"
                        self.fullPath  = "Editor:Frame:placement:configure:submitPlaceConfig"
                def __init__(self):
                    self.name      = "placement"
                    self.framePath = "Frame"
                    self.fullPath  = "Editor:Frame:placement"
                    self.Stats = AutoGen.Editor.Frame.placement.Stats()
                    self.configure = AutoGen.Editor.Frame.placement.configure()
                    self.label_x = AutoGen.Editor.Frame.placement.label_x()
                    self.label_y = AutoGen.Editor.Frame.placement.label_y()
                    self.label_width = AutoGen.Editor.Frame.placement.label_width()
                    self.label_height = AutoGen.Editor.Frame.placement.label_height()
                    self.entry_x = AutoGen.Editor.Frame.placement.entry_x()
                    self.entry_y = AutoGen.Editor.Frame.placement.entry_y()
                    self.entry_width = AutoGen.Editor.Frame.placement.entry_width()
                    self.entry_height = AutoGen.Editor.Frame.placement.entry_height()
                    self.coord_submit = AutoGen.Editor.Frame.placement.coord_submit()
                    self.placeConfigKey = AutoGen.Editor.Frame.placement.placeConfigKey()
                    self.placeConfigValue = AutoGen.Editor.Frame.placement.placeConfigValue()
                    self.submitPlaceConfig = AutoGen.Editor.Frame.placement.submitPlaceConfig()
            class reconfig(object):
                class configKey(object):
                    def __init__(self):
                        self.name      = "configKey"
                        self.framePath = "Frame:reconfig"
                        self.fullPath  = "Editor:Frame:reconfig:configKey"
                class configValue(object):
                    def __init__(self):
                        self.name      = "configValue"
                        self.framePath = "Frame:reconfig"
                        self.fullPath  = "Editor:Frame:reconfig:configValue"
                class submitConfig(object):
                    def __init__(self):
                        self.name      = "submitConfig"
                        self.framePath = "Frame:reconfig"
                        self.fullPath  = "Editor:Frame:reconfig:submitConfig"
                def __init__(self):
                    self.name      = "reconfig"
                    self.framePath = "Frame"
                    self.fullPath  = "Editor:Frame:reconfig"
                    self.configKey = AutoGen.Editor.Frame.reconfig.configKey()
                    self.configValue = AutoGen.Editor.Frame.reconfig.configValue()
                    self.submitConfig = AutoGen.Editor.Frame.reconfig.submitConfig()
            class InnerFrame(object):
                def __init__(self):
                    self.name      = "InnerFrame"
                    self.framePath = "Frame"
                    self.fullPath  = "Editor:Frame:InnerFrame"
            class label_x(object):
                def __init__(self):
                    self.name      = "label_x"
                    self.framePath = "Frame:placement:Stats"
                    self.fullPath  = "Editor:Frame:placement:Stats:label_x"
            class label_y(object):
                def __init__(self):
                    self.name      = "label_y"
                    self.framePath = "Frame:placement:Stats"
                    self.fullPath  = "Editor:Frame:placement:Stats:label_y"
            class label_width(object):
                def __init__(self):
                    self.name      = "label_width"
                    self.framePath = "Frame:placement:Stats"
                    self.fullPath  = "Editor:Frame:placement:Stats:label_width"
            class label_height(object):
                def __init__(self):
                    self.name      = "label_height"
                    self.framePath = "Frame:placement:Stats"
                    self.fullPath  = "Editor:Frame:placement:Stats:label_height"
            class entry_x(object):
                def __init__(self):
                    self.name      = "entry_x"
                    self.framePath = "Frame:placement:Stats"
                    self.fullPath  = "Editor:Frame:placement:Stats:entry_x"
            class entry_y(object):
                def __init__(self):
                    self.name      = "entry_y"
                    self.framePath = "Frame:placement:Stats"
                    self.fullPath  = "Editor:Frame:placement:Stats:entry_y"
            class entry_width(object):
                def __init__(self):
                    self.name      = "entry_width"
                    self.framePath = "Frame:placement:Stats"
                    self.fullPath  = "Editor:Frame:placement:Stats:entry_width"
            class entry_height(object):
                def __init__(self):
                    self.name      = "entry_height"
                    self.framePath = "Frame:placement:Stats"
                    self.fullPath  = "Editor:Frame:placement:Stats:entry_height"
            class coord_submit(object):
                def __init__(self):
                    self.name      = "coord_submit"
                    self.framePath = "Frame:placement:Stats"
                    self.fullPath  = "Editor:Frame:placement:Stats:coord_submit"
            class placeConfigKey(object):
                def __init__(self):
                    self.name      = "placeConfigKey"
                    self.framePath = "Frame:placement:configure"
                    self.fullPath  = "Editor:Frame:placement:configure:placeConfigKey"
            class placeConfigValue(object):
                def __init__(self):
                    self.name      = "placeConfigValue"
                    self.framePath = "Frame:placement:configure"
                    self.fullPath  = "Editor:Frame:placement:configure:placeConfigValue"
            class submitPlaceConfig(object):
                def __init__(self):
                    self.name      = "submitPlaceConfig"
                    self.framePath = "Frame:placement:configure"
                    self.fullPath  = "Editor:Frame:placement:configure:submitPlaceConfig"
            class configKey(object):
                def __init__(self):
                    self.name      = "configKey"
                    self.framePath = "Frame:reconfig"
                    self.fullPath  = "Editor:Frame:reconfig:configKey"
            class configValue(object):
                def __init__(self):
                    self.name      = "configValue"
                    self.framePath = "Frame:reconfig"
                    self.fullPath  = "Editor:Frame:reconfig:configValue"
            class submitConfig(object):
                def __init__(self):
                    self.name      = "submitConfig"
                    self.framePath = "Frame:reconfig"
                    self.fullPath  = "Editor:Frame:reconfig:submitConfig"
            def __init__(self):
                self.name      = "Frame"
                self.framePath = ""
                self.fullPath  = "Editor:Frame"
                self.ItemSelection = AutoGen.Editor.Frame.ItemSelection()
                self.placement = AutoGen.Editor.Frame.placement()
                self.reconfig = AutoGen.Editor.Frame.reconfig()
                self.InnerFrame = AutoGen.Editor.Frame.InnerFrame()
                self.label_x = AutoGen.Editor.Frame.label_x()
                self.label_y = AutoGen.Editor.Frame.label_y()
                self.label_width = AutoGen.Editor.Frame.label_width()
                self.label_height = AutoGen.Editor.Frame.label_height()
                self.entry_x = AutoGen.Editor.Frame.entry_x()
                self.entry_y = AutoGen.Editor.Frame.entry_y()
                self.entry_width = AutoGen.Editor.Frame.entry_width()
                self.entry_height = AutoGen.Editor.Frame.entry_height()
                self.coord_submit = AutoGen.Editor.Frame.coord_submit()
                self.placeConfigKey = AutoGen.Editor.Frame.placeConfigKey()
                self.placeConfigValue = AutoGen.Editor.Frame.placeConfigValue()
                self.submitPlaceConfig = AutoGen.Editor.Frame.submitPlaceConfig()
                self.configKey = AutoGen.Editor.Frame.configKey()
                self.configValue = AutoGen.Editor.Frame.configValue()
                self.submitConfig = AutoGen.Editor.Frame.submitConfig()
        def __init__(self):
            self.name      = "Editor"
            self.framePath = ""
            self.fullPath  = "Editor"
            self.Frame = AutoGen.Editor.Frame()
    def __init__(self, tkApp):
        self.Main = AutoGen.Main()
        self.ItemWindow = AutoGen.ItemWindow()
        self.Editor = AutoGen.Editor()
        self.placeConfigKey_framePath    = self.Editor.Frame.placement.configure.placeConfigKey.framePath
        self.placeConfigKey_fullPath     = self.Editor.Frame.placement.configure.placeConfigKey.fullPath
        self.placeConfigKey_windowName   = 'Editor'
        self.placeConfigKey_name         = 'placeConfigKey'
        self.placeConfigKey_Tk           = tkApp.getItemFromWindow(self.placeConfigKey_windowName, self.placeConfigKey_framePath, self.placeConfigKey_name)

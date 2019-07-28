class AutoGen(object):
    def __init__(self, tkApp):
        # NAMES
        self.tkEditorNewObject_0_name = 'tkEditorNewObject_0'
        self.windowSelection_name     = 'windowSelection'
        self.framePathSelection_name  = 'framePathSelection'
        self.itemSelection_name       = 'itemSelection'
        self.snapGridSlider_name      = 'snapGridSlider'
        self.windowSelection_name     = 'windowSelection'
        self.framePathSelection_name  = 'framePathSelection'
        self.itemSelection_name       = 'itemSelection'
        self.label_x_name             = 'label_x'
        self.label_y_name             = 'label_y'
        self.label_width_name         = 'label_width'
        self.label_height_name        = 'label_height'
        self.entry_x_name             = 'entry_x'
        self.entry_y_name             = 'entry_y'
        self.entry_width_name         = 'entry_width'
        self.entry_height_name        = 'entry_height'
        self.coord_submit_name        = 'coord_submit'
        self.placeConfigKey_name      = 'placeConfigKey'
        self.placeConfigValue_name    = 'placeConfigValue'
        self.submitPlaceConfig_name   = 'submitPlaceConfig'
        self.configKey_name           = 'configKey'
        self.configValue_name         = 'configValue'
        self.submitConfig_name        = 'submitConfig'
        
        # WINDOW PATHS
        self.tkEditorNewObject_0_windowPath = '.'
        self.windowSelection_windowPath     = 'Editor'
        self.framePathSelection_windowPath  = 'Editor'
        self.itemSelection_windowPath       = 'Editor'
        self.snapGridSlider_windowPath      = 'Editor'
        self.label_x_windowPath             = 'Editor'
        self.label_y_windowPath             = 'Editor'
        self.label_width_windowPath         = 'Editor'
        self.label_height_windowPath        = 'Editor'
        self.entry_x_windowPath             = 'Editor'
        self.entry_y_windowPath             = 'Editor'
        self.entry_width_windowPath         = 'Editor'
        self.entry_height_windowPath        = 'Editor'
        self.coord_submit_windowPath        = 'Editor'
        self.placeConfigKey_windowPath      = 'Editor'
        self.placeConfigValue_windowPath    = 'Editor'
        self.submitPlaceConfig_windowPath   = 'Editor'
        self.configKey_windowPath           = 'Editor'
        self.configValue_windowPath         = 'Editor'
        self.submitConfig_windowPath        = 'Editor'
        
        # FRAME PATHS
        self.tkEditorNewObject_0_framePath = 'Frame'
        self.windowSelection_framePath     = 'Frame:ItemSelection'
        self.framePathSelection_framePath  = 'Frame:ItemSelection'
        self.itemSelection_framePath       = 'Frame:ItemSelection'
        self.snapGridSlider_framePath      = 'Frame'
        self.label_x_framePath             = 'Frame:placement:Stats'
        self.label_y_framePath             = 'Frame:placement:Stats'
        self.label_width_framePath         = 'Frame:placement:Stats'
        self.label_height_framePath        = 'Frame:placement:Stats'
        self.entry_x_framePath             = 'Frame:placement:Stats'
        self.entry_y_framePath             = 'Frame:placement:Stats'
        self.entry_width_framePath         = 'Frame:placement:Stats'
        self.entry_height_framePath        = 'Frame:placement:Stats'
        self.coord_submit_framePath        = 'Frame:placement:Stats'
        self.placeConfigKey_framePath      = 'Frame:placement:configure'
        self.placeConfigValue_framePath    = 'Frame:placement:configure'
        self.submitPlaceConfig_framePath   = 'Frame:placement:configure'
        self.configKey_framePath           = 'Frame:reconfig'
        self.configValue_framePath         = 'Frame:reconfig'
        self.submitConfig_framePath        = 'Frame:reconfig'
        
        # FULL PATHS
        self.tkEditorNewObject_0_fullPath = '.:Frame:tkEditorNewObject_0'
        self.windowSelection_fullPath     = 'Editor:Frame:ItemSelection:windowSelection'
        self.framePathSelection_fullPath  = 'Editor:Frame:ItemSelection:framePathSelection'
        self.itemSelection_fullPath       = 'Editor:Frame:ItemSelection:itemSelection'
        self.snapGridSlider_fullPath      = 'Editor:Frame:snapGridSlider'
        self.label_x_fullPath             = 'Editor:Frame:placement:Stats:label_x'
        self.label_y_fullPath             = 'Editor:Frame:placement:Stats:label_y'
        self.label_width_fullPath         = 'Editor:Frame:placement:Stats:label_width'
        self.label_height_fullPath        = 'Editor:Frame:placement:Stats:label_height'
        self.entry_x_fullPath             = 'Editor:Frame:placement:Stats:entry_x'
        self.entry_y_fullPath             = 'Editor:Frame:placement:Stats:entry_y'
        self.entry_width_fullPath         = 'Editor:Frame:placement:Stats:entry_width'
        self.entry_height_fullPath        = 'Editor:Frame:placement:Stats:entry_height'
        self.coord_submit_fullPath        = 'Editor:Frame:placement:Stats:coord_submit'
        self.placeConfigKey_fullPath      = 'Editor:Frame:placement:configure:placeConfigKey'
        self.placeConfigValue_fullPath    = 'Editor:Frame:placement:configure:placeConfigValue'
        self.submitPlaceConfig_fullPath   = 'Editor:Frame:placement:configure:submitPlaceConfig'
        self.configKey_fullPath           = 'Editor:Frame:reconfig:configKey'
        self.configValue_fullPath         = 'Editor:Frame:reconfig:configValue'
        self.submitConfig_fullPath        = 'Editor:Frame:reconfig:submitConfig'
        
        # GET ITEMS
        self.tkEditorNewObject_0 = tkApp.getItemFromWindow(self.tkEditorNewObject_0_windowPath, self.tkEditorNewObject_0_framePath, self.tkEditorNewObject_0_name)
        self.windowSelection     = tkApp.getItemFromWindow(self.windowSelection_windowPath, self.windowSelection_framePath, self.windowSelection_name)
        self.framePathSelection  = tkApp.getItemFromWindow(self.framePathSelection_windowPath, self.framePathSelection_framePath, self.framePathSelection_name)
        self.itemSelection       = tkApp.getItemFromWindow(self.itemSelection_windowPath, self.itemSelection_framePath, self.itemSelection_name)
        self.snapGridSlider      = tkApp.getItemFromWindow(self.snapGridSlider_windowPath, self.snapGridSlider_framePath, self.snapGridSlider_name)
        self.windowSelection     = tkApp.getItemFromWindow(self.windowSelection_windowPath, self.windowSelection_framePath, self.windowSelection_name)
        self.framePathSelection  = tkApp.getItemFromWindow(self.framePathSelection_windowPath, self.framePathSelection_framePath, self.framePathSelection_name)
        self.itemSelection       = tkApp.getItemFromWindow(self.itemSelection_windowPath, self.itemSelection_framePath, self.itemSelection_name)
        self.label_x             = tkApp.getItemFromWindow(self.label_x_windowPath, self.label_x_framePath, self.label_x_name)
        self.label_y             = tkApp.getItemFromWindow(self.label_y_windowPath, self.label_y_framePath, self.label_y_name)
        self.label_width         = tkApp.getItemFromWindow(self.label_width_windowPath, self.label_width_framePath, self.label_width_name)
        self.label_height        = tkApp.getItemFromWindow(self.label_height_windowPath, self.label_height_framePath, self.label_height_name)
        self.entry_x             = tkApp.getItemFromWindow(self.entry_x_windowPath, self.entry_x_framePath, self.entry_x_name)
        self.entry_y             = tkApp.getItemFromWindow(self.entry_y_windowPath, self.entry_y_framePath, self.entry_y_name)
        self.entry_width         = tkApp.getItemFromWindow(self.entry_width_windowPath, self.entry_width_framePath, self.entry_width_name)
        self.entry_height        = tkApp.getItemFromWindow(self.entry_height_windowPath, self.entry_height_framePath, self.entry_height_name)
        self.coord_submit        = tkApp.getItemFromWindow(self.coord_submit_windowPath, self.coord_submit_framePath, self.coord_submit_name)
        self.placeConfigKey      = tkApp.getItemFromWindow(self.placeConfigKey_windowPath, self.placeConfigKey_framePath, self.placeConfigKey_name)
        self.placeConfigValue    = tkApp.getItemFromWindow(self.placeConfigValue_windowPath, self.placeConfigValue_framePath, self.placeConfigValue_name)
        self.submitPlaceConfig   = tkApp.getItemFromWindow(self.submitPlaceConfig_windowPath, self.submitPlaceConfig_framePath, self.submitPlaceConfig_name)
        self.configKey           = tkApp.getItemFromWindow(self.configKey_windowPath, self.configKey_framePath, self.configKey_name)
        self.configValue         = tkApp.getItemFromWindow(self.configValue_windowPath, self.configValue_framePath, self.configValue_name)
        self.submitConfig        = tkApp.getItemFromWindow(self.submitConfig_windowPath, self.submitConfig_framePath, self.submitConfig_name)

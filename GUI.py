from application.application import Application

import argparse
import os
import sys

########################################################################################################################
#
########################################################################################################################
def runApp(args):
    app = Application(args.guiConfig)

    app.attachToUserInput('mainWindow.mainFrame.mainButton', onMainButtonPushed)
    app.attachToUserInput('secondWindow.mainFrame.mainButton', onMainButtonPushed)

    # now run our app
    app.start()

########################################################################################################################
#
########################################################################################################################
def onMainButtonPushed(*args, **kwargs):
    print (f'onMainButtonPushed!')

########################################################################################################################
#
########################################################################################################################
def onFileOpenClicked(*args, **kwargs):
    print (f'onFileOpenClicked!')

########################################################################################################################
#
########################################################################################################################
def validateArgs(options):
    valid = True

    if options.guiConfig != "":
        valid &= os.path.isfile(options.guiConfig)

    return valid

########################################################################################################################
#
########################################################################################################################
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--guiConfig', 
                         dest="guiConfig",
                         action='store', 
                         required=False, 
                         default='',
                         metavar='GUICONFIG',
                         help='GUI Layout XML file')

    options = parser.parse_args(sys.argv[1:])

    if validateArgs(options) == False:
        return -1

    runApp(options)
    
########################################################################################################################
#
########################################################################################################################
if __name__ == "__main__":
    main()
from src.tkApplication import tkApplication
from src.tkEditor import tkEditor
from src.tkHelper import tkHelper

import argparse
import os
import sys

#----------------------------------------------------------------------------------------------------------------------
# runApp
#______________________________________________________________________________________________________________________
def runApp(args):
    app = tkApplication(args.guiConfig)

    # create our editor handling code
    if args.generateCode == True:
        tkHelper.generateCodeFromApplication(app)

    if args.enableEditing:
        editor = tkEditor(app)

    # now run our app
    app.getRoot().mainloop()


#----------------------------------------------------------------------------------------------------------------------
# validateArgs
#______________________________________________________________________________________________________________________
def validateArgs(options):
    valid = True

    if options.guiConfig != "":
        valid &= os.path.isfile(options.guiConfig)

    return valid

#----------------------------------------------------------------------------------------------------------------------
# main
#______________________________________________________________________________________________________________________
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--guiConfig', 
                         dest="guiConfig",
                         action='store', 
                         required=False, 
                         default='',
                         metavar='GUICONFIG',
                         help='GUI Layout XML file')
    
    parser.add_argument('--enableEditing', 
                         dest="enableEditing",
                         action='store_true', 
                         required=False,
                         default=False,
                         help='Turns on editing ability for GUI')

    parser.add_argument('--generateCode',
                        dest='generateCode',
                        action='store_true',
                        required=False,
                        help='Tells the Program to just generate code, nothing else')

    options = parser.parse_args(sys.argv[1:])

    if validateArgs(options) == False:
        return -1

    runApp(options);
    
#----------------------------------------------------------------------------------------------------------------------
# __name__
#______________________________________________________________________________________________________________________
if __name__ == "__main__":
    main()
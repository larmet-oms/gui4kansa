# import UI and tools to run powershell

import os
import subprocess, sys


# setup variables

HOSTNAME = str(os.getenv('COMPUTERNAME', 'defaultvalue'))
CUR_DIR = os.getcwd()
MODULES = cd + '\\Modules'
CONFIG_FILE = MODULES + '\\modules.conf'

# setup various OOP functions


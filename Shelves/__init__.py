# Maya initializer shelf command
# Add this directory to paya python path

import sys

PROJECT_DIR = '/Users/sachabest/Documents/gits/cis099'
PIP_ROOT = '/Applications/Autodesk/maya2016/Maya.app/Contents/MacOS'

if PROJECT_DIR not in sys.path:
	sys.path.insert(0, PROJECT_DIR)
	print "Path to project files added to sys.path"

if PIP_ROOT not in sys.path:
	sys.path.insert(0, PIP_ROOT)
	print "Path to pip files added to sys.path"

reload(FrameServer)
reload(MayaApp)
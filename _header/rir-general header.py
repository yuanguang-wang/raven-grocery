# https://www.rhino3d.com/inside/revit/1.0/guides/rir-ghpython

import clr
clr.AddReference('System.Core')
clr.AddReference('RhinoInside.Revit')
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI')

from System import Enum, Action

import rhinoscriptsyntax as rs

import Rhino
import RhinoInside

import Grasshopper
from Grasshopper.Kernel import GH_RuntimeMessageLevel as RML

from RhinoInside.Revit import Revit, Convert

# add extensions methods as well
# this allows calling .ToXXX() convertor methods on Revit objects
clr.ImportExtensions(Convert.Geometry)

from Autodesk.Revit import DB

# access to Revit as host
REVIT_VERSION = Revit.ActiveUIApplication.Application.VersionNumber

# access the active document object
doc = Revit.ActiveDBDocument

# a few utility methods
def show_warning(msg):
    ghenv.Component.AddRuntimeMessage(RML.Warning, msg)

def show_error(msg):
    ghenv.Component.AddRuntimeMessage(RML.Error, msg)

def show_remark(msg):
    ghenv.Component.AddRuntimeMessage(RML.Remark, msg)

# write your code here
# ...

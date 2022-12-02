import clr
import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')
import System
from System import Array
from System.Collections.Generic import *
clr.AddReference('ProtoGeometry')
import Autodesk.DesignScript.Geometry as DSG
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager 
from RevitServices.Transactions import TransactionManager 

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")

import Autodesk 
import Autodesk.Revit.DB as DB
import Autodesk.Revit.UI as UI

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication 
app = uiapp.Application 
uidoc = uiapp.ActiveUIDocument

#######OK NOW YOU CAN CODE########
# The inputs to this node will be stored as a list in the IN variables.

opt = DB.Options()

def originCompare(ox, oy, oz, cx, cy, cz):
	if ox - cx < 0.01:
		if oy - cy < 0.01:
			if oz - cz > 4:
				return True
	return False
		

targetPanels = UnwrapElement(IN[0])
cw = UnwrapElement(IN[1])
cg = cw.CurtainGrid
cPanelID = cg.GetPanelIds()
cPanel = []
		
TransactionManager.Instance.EnsureInTransaction(doc)

for i in range(len(cPanelID)):
	cPanel.append(doc.GetElement(cPanelID[i]))


for i in range(len(targetPanels)):
	panelOrigin = targetPanels[i].Transform.Origin
	ox = panelOrigin.X
	oy = panelOrigin.Y
	oz = panelOrigin.Z
	
	replacedPanels = []
	
	for j in range(len(cPanel)):
	
		cPanelO = cPanel[j].Transform.Origin
		cx = cPanelO.X
		cy = cPanelO.Y
		cz = cPanelO.Z
		
		volume = cPanel[j].LookupParameter("Volume").AsDouble()
		
		if originCompare(ox, oy, oz, cx, cy, cz) == True:
			if volume < 1.5:
				cPanel[j].Symbol = targetPanels[i].Symbol

TransactionManager.Instance.TransactionTaskDone()	
	
	
# Place your code below this line

# Assign your output to the OUT variable.
OUT = 0

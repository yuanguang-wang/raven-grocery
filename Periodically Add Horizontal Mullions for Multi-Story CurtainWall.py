import sys
import clr

clr.AddReference('ProtoGeometry')
clr.AddReference('RevitAPI')

import Autodesk.Revit.DB as DB
import Autodesk.DesignScript.Geometry as DS

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager 
from RevitServices.Transactions import TransactionManager 

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication 
app = uiapp.Application 
uidoc = uiapp.ActiveUIDocument



TransactionManager.Instance.EnsureInTransaction(doc)

wall = UnwrapElement(IN[0])
newZ = UnwrapElement(IN[1])
mullionType = UnwrapElement(IN[2])

cg = wall.CurtainGrid
cgl = []

startPoint = wall.Location.Curve.ToProtoType().PointAtParameter(0.5)

for i in range(len(newZ)):
	newpt = DS.Point.ByCoordinates(startPoint.X, startPoint.Y, newZ[i])
	cgl.append(cg.AddGridLine(True, newpt.ToXyz(), False))
	
for i in range(len(cgl)):
	cgl[i].AddMullions(cgl[i].FullCurve, mullionType, False)
	

TransactionManager.Instance.TransactionTaskDone()


#OUT = wall.Location.Curve.ToProtoType()
OUT = 0

import sys
import clr

clr.AddReference('ProtoGeometry')
clr.AddReference('RevitAPI')

import Autodesk.Revit.DB as DB

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager 
from RevitServices.Transactions import TransactionManager 

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication 
app = uiapp.Application 
uidoc = uiapp.ActiveUIDocument

TransactionManager.Instance.EnsureInTransaction(doc)

cs = UnwrapElement(IN[0])
para = IN[1]
val = str(IN[2])


Eid = DB.ElementTransformUtils.CopyElement(doc, cs.Id, DB.XYZ())[0]
clone = doc.GetElement(Eid)

gridOrigin = []
gridOriginXYZ = []
gridCloneXYZ = []
vec = []

clUid = clone.CurtainGrid.GetUGridLineIds()

for i in range(len(clUid)):
	gridCloneXYZ.append(doc.GetElement(clUid[i]).FullCurve.GetEndPoint(0))
		
paraObj = cs.LookupParameter(para)
paraObj.SetValueString(val)

csUid = cs.CurtainGrid.GetUGridLineIds()

for i in range(len(csUid)):
	gridOrigin.append(doc.GetElement(csUid[i]))
	gridOrigin[i].Pinned = False
	gridOriginXYZ.append(gridOrigin[i].FullCurve.GetEndPoint(0))
	vec.append(gridCloneXYZ[i] - gridOriginXYZ[i])
	gridOrigin[i].Location.Move(vec[i])

doc.Delete(Eid)

TransactionManager.Instance.TransactionTaskDone()

OUT = vec
#OUT = paraObj.AsValueString()

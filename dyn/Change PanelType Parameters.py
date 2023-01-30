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

panel = UnwrapElement(IN[0])
type = panel.PanelType
OUT = type
thick = type.LookupParameter("Thickness")
off = type.LookupParameter("Offset")

thick.SetValueString("40")
off.SetValueString("-20")

TransactionManager.Instance.TransactionTaskDone()


#OUT = wall.Location.Curve.ToProtoType()
OUT = 0

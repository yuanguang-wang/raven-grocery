import clr

clr.AddReference('System.Core')
clr.AddReference('RhinoInside.Revit')
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI')

from System import Enum
from RhinoInside.Revit import Revit, Convert
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

doc = Revit.ActiveDBDocument
dataEnteringNode = IN
tg = Transaction(doc, 'Change Material')

def materialreplacer (mtlid, origin, keyword):
	param_name = []
	for i in range(len(origin)):
		param_name.append(origin[i].Definition.Name)
		if keyword in param_name[i]:
			result = origin[i].Set(mtlid)
	return result


def materialfinder (collector, string):
	target_material = []
	for i in range(len(collector)):
		collector_name = collector[i].Name
		if string in collector_name:
			target_material.append(collector[i])
	return target_material


tg.Start()

test = 0

type_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_CurtainWallPanels).WhereElementIsElementType().ToElements()
type_name = []
planter_pattern = []

for i in range(len(type_collector)):
	type_name = type_collector[i].LookupParameter('Type Name').AsString()
	if "Pattern" in type_name:
		test = test + 1
		planter_pattern.append(type_collector[i])

material_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Materials).WhereElementIsNotElementType().ToElements()

spandrel = materialfinder (material_collector, 'Spandrel')[0]
lower_piece = materialfinder (material_collector, 'Lower Piece')[0]

for i in range(len(planter_pattern)):
	spy = planter_pattern[i]
	spy_param = list(planter_pattern[i].Parameters)
	OUT = materialreplacer (lower_piece.Id, spy_param, 'Lower')

tg.Commit()

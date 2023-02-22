# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import scriptcontext as sc
import Rhino

import clr
clr.AddReference("System.Xml")
from System.Collections.Generic import List, Dictionary

dir_path = r"Q:\210002-00\CADD\Model\3D\Rhino\Commiercial\Detail model\Retail By Building\Material"
dir_list = os.listdir(dir_path)

dir_list_filtered = []
for i in range(len(dir_list)):
    if 'rmtl' in dir_list[i]:
        dir_list_filtered.append(dir_list[i])

for j in range(len(dir_list_filtered)):
    file_path = r'"Q:\210002-00\CADD\Model\3D\Rhino\Commiercial\Detail model\Retail By Building\Material\{}"'.format(dir_list_filtered[j])
    print(file_path)
    
    mt_list = []
    mt_name = []
    
    Rhino.RhinoApp.RunScript("""-_Materials
    _Options
    _LoadFromFile
    {0}
    _Enter
    _Enter
    """.format(file_path), False)
    
    t = False
    mt = sc.doc.RenderMaterials
    
    for i in range(mt.Count - 1):
        if mt.Item[i].Name in mt.Item[mt.Count - 1].Name:
            mt.BeginChange(Rhino.Render.RenderContent.ChangeContexts.Script)
            mt.Item[i].MatchData(mt.Item[mt.Count - 1])
            mt.EndChange()
            t = True
    
    if t == True:
        mt.Remove(mt.Item[mt.Count - 1])


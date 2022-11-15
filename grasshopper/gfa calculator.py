"""
Input: 
    brep_tree: Brep, as [tree data] (graft required)
               Brep could be single surface or polysurface, but the bottom face must be horizontal
OutPut:
    btmFace: the geometry of bottom face/surface
    gfa: area of the bottom face    
"""
 
import rhinoscriptsyntax as rs
import Rhino
 
class gfaCltr:
 
    def __init__(self, brep):
        self.brep = brep
        self.btmFace = []
        self.gfa = 0
 
    def polysrf(self):
        explodedBreps = rs.ExplodePolysurfaces(self.brep)
        ptZ = []
        for i in range(len(explodedBreps)):
            ptZ.append(rs.coerce3dpoint(rs.SurfaceAreaCentroid(explodedBreps[i])[0]).Z)
 
        ptZZ = []
        for i in range(len(ptZ)):
            ptZZ.append(ptZ[i])
        ptZZ.sort()
        min = ptZZ[0]
        minindexlist = []
 
        for i in range(len(explodedBreps)):
            if ptZ[i] == min:
                minindexlist.append(i)
 
        for i in range(len(minindexlist)):
            self.btmFace.append(explodedBreps[minindexlist[i]])
 
        for i in range(len(self.btmFace)):
            self.gfa += rs.SurfaceArea(self.btmFace[i])[0]
 
    def singlesrf(self):
        if rs.IsSurfacePlanar(self.brep):
            self.btmFace = self.brep
            self.gfa = rs.SurfaceArea(self.brep)[0]
 
    def run(self):
        if rs.IsPolysurface(self.brep):
            self.polysrf()
        else:
            self.singlesrf()
 
gfaFinder = gfaCltr(brep_tree)
gfaFinder.run()
 
btmFace = gfaFinder.btmFace
gfa = gfaFinder.gfa
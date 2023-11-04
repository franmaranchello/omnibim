from pxr import Usd, UsdGeom, Sdf

class Element(UsdGeom.Xform):
    """ A custom USD schema for a BIM element. """
    
    def __init__(self, stage, path):
        super().__init__(stage.DefinePrim(path, 'Element'))
        self.costAttr = self.GetPrim().CreateAttribute('cost', Sdf.ValueTypeNames.Float, True)
        self.manufacturerAttr = self.GetPrim().CreateAttribute('manufacturer', Sdf.ValueTypeNames.String, True)

    def SetCost(self, cost):
        self.costAttr.Set(cost)

    def SetManufacturer(self, manufacturer):
        self.manufacturerAttr.Set(manufacturer)

    def GetCost(self):
        return self.costAttr.Get()

    def GetManufacturer(self):
        return self.manufacturerAttr.Get()

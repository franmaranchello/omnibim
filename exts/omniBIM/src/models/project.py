class Project(UsdGeom.Xform):
    """ A custom USD schema for a BIM project. """
    
    def __init__(self, stage, path):
        super().__init__(stage.DefinePrim(path, 'Project'))
        self.nameAttr = self.GetPrim().CreateAttribute('name', Sdf.ValueTypeNames.String, True)
        self.addressAttr = self.GetPrim().CreateAttribute('address', Sdf.ValueTypeNames.String, True)

    def SetName(self, name):
        self.nameAttr.Set(name)

    def SetAddress(self, address):
        self.addressAttr.Set(address)

    def GetName(self):
        return self.nameAttr.Get()

    def GetAddress(self):
        return self.addressAttr.Get()
from pxr import Usd, Sdf
from omni.ui import scene as sc
from Models.element import Element 
from Models.project import Project  

# Assuming you have a UI model and sidebar defined as in the previous examples
from ui_model import BIMDataModel
from ui_sidebar import BIMSidebar

# Initialize the stage
stage = Usd.Stage.CreateNew('MyProject.usda')

# Instantiate the UI model
bim_data_model = BIMDataModel()

# Define the UI layout and logic
class BIMExtension:
    def __init__(self, model, stage):
        self.model = model
        self.stage = stage
        self.sidebar = BIMSidebar(model)

# Instantiate the extension
bim_extension = BIMExtension(bim_data_model, stage)

# Add the sidebar to the workspace
sc.Workspace.add(bim_extension.sidebar, label="BIM Data", sidebar=True)

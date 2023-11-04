from pxr import Usd, Sdf
from omni.ui import window, Workspace, Model, ValueModel, scene as ui_scene, Color
from Models.element import Element 
from Models.project import Project  

# Create a model for the UI to interact with
class BIMDataModel(Model):
    def __init__(self):
        super().__init__()
        self.element_cost = ValueModel(0.0)
        self.element_manufacturer = ValueModel("")
        self.project_name = ValueModel("")
        self.project_address = ValueModel("")

# Instantiate the model
bim_data_model = BIMDataModel()

# Define the UI layout
class BIMSidebar:
    def __init__(self, model):
        self.model = model
        self.build_ui()

    def build_ui(self):
        with ui_scene.Hierarchy(window, "BIM Sidebar"):
            with ui_scene.VStack():
                ui_scene.Label("Element Data", alignment=ui_scene.Alignment.CENTER)
                with ui_scene.HStack():
                    ui_scene.Label("Cost:")
                    ui_scene.FloatField(model=self.model.element_cost)
                with ui_scene.HStack():
                    ui_scene.Label("Manufacturer:")
                    ui_scene.StringField(model=self.model.element_manufacturer)

                ui_scene.Label("Project Data", alignment=ui_scene.Alignment.CENTER)
                with ui_scene.HStack():
                    ui_scene.Label("Name:")
                    ui_scene.StringField(model=self.model.project_name)
                with ui_scene.HStack():
                    ui_scene.Label("Address:")
                    ui_scene.StringField(model=self.model.project_address)

                ui_scene.Spacer(height=10)
                ui_scene.Button("Create Element", clicked_fn=self.create_element)
                ui_scene.Button("Create Project", clicked_fn=self.create_project)

    def create_element(self):
        # Generate a unique path for the new element
        element_path = Sdf.Path(f'/MyProject/Element_{len(self.stage.GetPrimAtPath("/MyProject").GetChildren()) + 1}')
        # Create a new Element in the USD stage
        element = Element(self.stage, element_path)
        element.SetCost(self.model.element_cost.value)
        element.SetManufacturer(self.model.element_manufacturer.value)
        # Save changes
        self.stage.GetRootLayer().Save()

    def create_project(self):
        # Generate a unique path for the new project
        project_path = Sdf.Path(f'/MyProject/Project_{len(self.stage.GetPseudoRoot().GetChildren()) + 1}')
        # Create a new Project in the USD stage
        project = Project(self.stage, project_path)
        project.SetName(self.model.project_name.value)
        project.SetAddress(self.model.project_address.value)
        # Save changes
        self.stage.GetRootLayer().Save()

# Create the sidebar
bim_sidebar = BIMSidebar(bim_data_model)

# Add the sidebar to the workspace
workspace = Workspace.get_default()
workspace.add(bim_sidebar, label="BIM Data", sidebar=True)

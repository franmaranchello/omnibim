from pxr import Usd, Sdf
from omni.ui import window, Workspace, Model, ValueModel, scene as ui_scene, Color

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
        # Logic to create a new Element in the USD stage
        # ...

    def create_project(self):
        # Logic to create a new Project in the USD stage
        # ...

# Create the sidebar
bim_sidebar = BIMSidebar(bim_data_model)

# Add the sidebar to the workspace
workspace = Workspace.get_default()
workspace.add(bim_sidebar, label="BIM Data", sidebar=True)

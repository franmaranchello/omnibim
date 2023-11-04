from pxr import Usd, Sdf
from omni.kit.ui import DeclarativeUI
from omni.kit.commands import execute
from Models.element import Element
from Models.project import Project

class OmniBIMExtension:
    def __init__(self, ui):
        self._window = ui
        self._stage = None

    def create_element(self, cost, manufacturer):
        if not self._stage:
            self._stage = Usd.Stage.CreateNew('MyProject.usda')
        element_path = Sdf.Path('/MyProject/Element1')
        element = Element(self._stage, element_path)
        element.SetCost(cost)
        element.SetManufacturer(manufacturer)

    def create_project(self, name, address):
        if not self._stage:
            self._stage = Usd.Stage.CreateNew('MyProject.usda')
        project_path = Sdf.Path('/MyProject')
        project = Project(self._stage, project_path)
        project.SetName(name)
        project.SetAddress(address)

# UI Callbacks
def on_create_element_pressed():
    # Get data from UI
    cost = ...
    manufacturer = ...
    # Create element
    my_extension.create_element(cost, manufacturer)

def on_create_project_pressed():
    # Get data from UI
    name = ...
    address = ...
    # Create project
    my_extension.create_project(name, address)

# Initialize Extension
ui = DeclarativeUI()
my_extension = OmniBIMExtension(ui)

# Connect UI signals to callbacks
ui.get_widget('create_element_button').clicked.connect(on_create_element_pressed)
ui.get_widget('create_project_button').clicked.connect(on_create_project_pressed)

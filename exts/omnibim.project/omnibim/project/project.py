from omni.ui import Window, Model, StringField, Button


class ProjectModel(Model):
    def __init__(self):
        super().__init__()
        self.name = "Default Project Name"
        self.address = "Default Address"
        

def edit_project_parameters():
    # This function will be called when the button is clicked
    # Create a window with fields to edit the name and address
    with Window("Edit Project Parameters", width=300, height=100) as win:
        with win.frame:
            with win.vertical:
                # Create a string field bound to the project name
                StringField("Name", model=Model().bind("name", project_model))
                # Create a string field bound to the project address
                StringField("Address", model=Model().bind("address", project_model))


# Create the main UI with a button to edit project parameters
with Window("Main UI", width=300, height=100) as main_win:
    with main_win.frame:
        with main_win.vertical:
            Button("Edit Project", clicked_fn=edit_project_parameters)

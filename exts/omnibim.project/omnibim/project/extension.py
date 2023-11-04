import omni.ext
import omni.ui as ui
import omni.kit.commands


# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[omnibim.project] some_public_function was called with x: ", x)
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class OmnibimProjectExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[omnibim.project] omnibim project startup")

        self._count = 0

        self._window = ui.Window("OmniBIM", width=300, height=300)
        with self._window.frame:
            with ui.VStack():
                label = ui.Label("")


                def on_click():
                    print("Creating cube!")
                    omni.kit.commands.execute('CreatePrimWithDefaultXform',
                        prim_type='Cube',
                        attributes={'size': 100.0, 'extent': [(-50.0, -50.0, -50.0), (50.0, 50.0, 50.0)]})


                def on_reset():
                    self._count = 0
                    label.text = "empty"

                on_reset()

                with ui.HStack():
                    ui.Button("Edit Project", clicked_fn=on_click)
                    ui.Button("Create Element", clicked_fn=on_reset)

    def on_shutdown(self):
        print("[omnibim.project] omnibim project shutdown")

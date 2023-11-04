import omni.ext
import omni.ui as ui


# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print(f"[omni.hello.world] some_public_function was called with {x}")
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class MyExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[omni.hello.world] MyExtension startup")

        self._count = 0

        self._window = ui.Window("My Window", width=300, height=800)
        with self._window.frame:
            with ui.VStack():
                
                IMAGE = "C:/repos/omnibim/exts/omni.hello.world/data/icon_new.png"
                ui.Image(IMAGE, width=64, height=64)

                label = ui.Label("", height=50)

                def add_click():
                    self._count += 1
                    label.text = f"count: {self._count}"
                
                def sub_click():
                    self._count -= 1
                    label.text = f"count: {self._count}"

                def on_click10():
                    self._count += 10
                    label.text = f"count: {self._count}"

                def on_reset():
                    self._count = 0
                    label.text = f"count: {self._count}"

                on_reset()
            
                with ui.HStack(height=50):
                    ui.Button("+", clicked_fn=add_click)
                    ui.Button("-", clicked_fn=sub_click)
                    ui.Button("Reset", clicked_fn=on_reset)
                
                # ------------------------

                ui.Label("SPAWN", height=50)
                with ui.VStack(height=100):
                    ui.Button("One")
                    ui.Button("Two")
                    ui.Button("Three")

                # ------------------------
                
                ui.Label("TRANSFORM", height=50)


                def slider_row(label, slider_width, slider_gap):
                    with ui.HStack(height=30):
                        ui.Label(f"{label}")
                        # x
                        ui.FloatDrag(width=slider_width)
                        ui.Label("", width=slider_gap)
                        # y
                        ui.FloatDrag(width=slider_width)
                        ui.Label("", width=slider_gap)
                        # z
                        ui.FloatDrag(width=slider_width)
                        ui.Label("", width=slider_gap)
                
                slider_width = 60
                slider_gap = 5

                slider_row("Translate", slider_width, slider_gap)
                slider_row("Rotate", slider_width, slider_gap)
                slider_row("Scale", slider_width, slider_gap)
            
                # ------------------------

                ui.Label("ELEMENT NAV", height=50)
                class Item(ui.AbstractItem):
                    def __init__(self, text, name, d=5):
                        super().__init__()
                        self.name_model = ui.SimpleStringModel(text)
                        self.children = [Item(f"Child {name}{i}", name, d - 1) for i in range(d)]

                class Model(ui.AbstractItemModel):
                    def __init__(self, name):
                        super().__init__()
                        self._children = [Item(f"Model {name}", name)]

                    def get_item_children(self, item):
                        return item.children if item else self._children

                    def get_item_value_model_count(self, item):
                        return 1

                    def get_item_value_model(self, item, column_id):
                        return item.name_model

                class NestedItem(ui.AbstractItem):
                    def __init__(self, source_item, source_model):
                        super().__init__()
                        self.source = source_item
                        self.model = source_model
                        self.children = None

                class NestedModel(ui.AbstractItemModel):
                    def __init__(self):
                        super().__init__()
                        models = [Model("A"), Model("B"), Model("C")]
                        self.children = [
                            NestedItem(i, m) for m in models for i in m.get_item_children(None)]

                    def get_item_children(self, item):
                        if item is None:
                            return self.children

                        if item.children is None:
                            m = item.model
                            item.children = [
                                NestedItem(i, m) for i in m.get_item_children(item.source)]

                        return item.children

                    def get_item_value_model_count(self, item):
                        return 1

                    def get_item_value_model(self, item, column_id):
                        return item.model.get_item_value_model(item.source, column_id)

                with ui.ScrollingFrame(
                    height=200,
                    horizontal_scrollbar_policy=ui.ScrollBarPolicy.SCROLLBAR_ALWAYS_OFF,
                    vertical_scrollbar_policy=ui.ScrollBarPolicy.SCROLLBAR_ALWAYS_ON,
                    style_type_name_override="TreeView",
                ):
                    self._model = NestedModel()
                    ui.TreeView(self._model, root_visible=False, style={"margin": 0.5})

                
                    

    def on_shutdown(self):
        print("[omni.hello.world] MyExtension shutdown")

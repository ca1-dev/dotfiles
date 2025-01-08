from .floatingwindow import FloatingWindow
from ignis.app import IgnisApp
from ignis.widgets import Widget

app = IgnisApp.get_default()


class ControlCenter(FloatingWindow):
    def __init__(self, widgets: list[Widget] = [], css_classes: list[str] = [], **kwargs) -> None:
        namespace = "ignis_CONTROL_CENTER"

        super().__init__(
            monitor=0,
            namespace=namespace,
            child=[
                Widget.Box(
                    vertical=True,
                    vexpand=True,
                    child=widgets,
                    css_classes=css_classes + ["control-center"],
                )
            ],
            **kwargs
        )

        self.clickOffAreaRight.set_width(0)
        self.clickOffAreaBottom.set_height(0)

        self.content.vexpand = True

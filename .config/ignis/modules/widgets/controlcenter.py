from .floatingwindow import FloatingWindow

import ignis


class ControlCenter(FloatingWindow):
    def __init__(self, widgets=[], css_classes=[], **kwargs) -> None:
        namespace = "ignis_CONTROL_CENTER"

        super().__init__(
            monitor=0,
            namespace=namespace,
            child=[
                ignis.widgets.Box(
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

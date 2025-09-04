from ignis import utils, widgets
from modules import globals
from modules.widgets import ClickOffArea


class FloatingWindow(widgets.Window):
    def __init__(self, monitor: int = 0, namespace: str = "", child=widgets.Box(), **kwargs) -> None:

        self.clickOffAreaLeft = ClickOffArea(namespace=namespace)
        self.clickOffAreaRight = ClickOffArea(namespace=namespace)
        self.clickOffAreaTop = ClickOffArea(namespace=namespace, height=0,)
        self.clickOffAreaBottom = ClickOffArea(namespace=namespace)

        self.content = widgets.Box(
            vertical=True,
            child=child,
            css_classes=["floating-window"],
        )

        box = [
            self.clickOffAreaLeft,
            widgets.Box(
                vertical=True,
                child=[
                    self.clickOffAreaTop,
                    self.content,
                    self.clickOffAreaBottom,
                ]
            ),
            widgets.EventBox(),
            self.clickOffAreaRight,
        ]

        super().__init__(
            monitor=monitor,
            namespace=namespace,
            anchor=["top", "right", "bottom", "left"],
            layer="top",
            kb_mode="on_demand",
            visible=False,
            popup=True,
            child=widgets.Box(child=box),
            **kwargs,
        )

        globals.currentMenu.connect(
            "notify::value", lambda menu, _: self.hide_if_other_active(
                menu.value
            )
        )

    def show(self) -> None:
        globals.currentMenu.value = self.namespace
        self.visible = True

    def toggle(self) -> None:
        if not self.visible:
            self.show()
        else:
            self.hide()

    def hide_if_other_active(self, namespace: str) -> None:
        if namespace != self.namespace:
            self.visible = False

    def set_position_x(self, middle: int) -> None:
        monitorWidth = utils.get_monitor(self.monitor).get_geometry().width
        size = self.content.get_preferred_size().natural_size
        width = size.width

        if middle + width / 2 > monitorWidth:
            self.clickOffAreaLeft.set_width(monitorWidth - width)
        elif middle - width / 2 < 0:
            self.clickOffAreaLeft.set_width(0)
        else:
            self.clickOffAreaLeft.set_width(middle - width / 2)

    def set_position_y(self, middle: int) -> None:
        monitorHeight = utils.get_monitor(self.monitor).get_geometry().height
        size = self.content.get_preferred_size().natural_size
        height = size.height

        if middle + height / 2 > monitorHeight:
            self.clickOffAreaTop.set_height(monitorHeight - height)
        elif middle - height / 2 < 0:
            self.clickOffAreaTop.set_height(0)
        else:
            self.clickOffAreaTop.set_height(middle - height / 2)

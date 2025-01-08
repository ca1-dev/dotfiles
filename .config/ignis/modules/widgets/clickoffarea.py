from ignis.app import IgnisApp
from ignis.widgets import Widget

app = IgnisApp.get_default()


class ClickOffArea(Widget.EventBox):
    def __init__(self, namespace: str = "", width: bool = False, height: bool = False, **kwargs) -> None:
        super().__init__(**kwargs)
        self.on_click = lambda _: app.close_window(namespace)

        self.set_width(width)
        self.set_height(height)

    def set_width(self, width: int) -> None:
        if width is not False:
            self.width_request = width
            self.hexpand = False
        else:
            self.hexpand = True

    def set_height(self, height: int) -> None:
        if height is not False:
            self.height_request = height
            self.vexpand = False
        else:
            self.vexpand = True

from ignis.app import IgnisApp
from ignis.widgets import Widget

app = IgnisApp.get_default()


class StatusPill(Widget.Button):
    def __init__(self, monitor: int = 0, widgets: list[Widget] = [], css_classes: list[str] = [], **kwargs):
        for w in widgets:
            w.add_css_class("status-pill-widget")

        self.monitor = monitor
        self.window: Widget.Window = app.get_window("ignis_CONTROL_CENTER")

        super().__init__(
            child=Widget.Box(child=widgets),
            css_classes=css_classes + ["bar-widget", "bar-status-pill"],
            **kwargs,
        )

    def on_click(self, _) -> None:
        if self.window.monitor == self.monitor:
            self.window.toggle()
        else:
            self.window.set_monitor(self.monitor)
            self.window.show()

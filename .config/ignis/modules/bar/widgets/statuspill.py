from ignis.window_manager import WindowManager

import ignis

window_manager = WindowManager.get_default()


class StatusPill(ignis.widgets.Button):
    def __init__(self, monitor: int = 0, widgets=[], css_classes: list[str] = [], **kwargs):
        for w in widgets:
            w.add_css_class("status-pill-widget")

        self.monitor = monitor
        self.window = window_manager.get_window("ignis_CONTROL_CENTER")

        super().__init__(
            child=ignis.widgets.Box(child=widgets),
            css_classes=css_classes + ["bar-widget", "bar-status-pill"],
            **kwargs,
        )

    def on_click(self, _) -> None:
        if self.window.monitor == self.monitor:
            self.window.toggle()
        else:
            self.window.set_monitor(self.monitor)
            self.window.show()

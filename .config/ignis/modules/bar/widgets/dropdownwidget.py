from gi.repository import Graphene
from ignis.widgets import Widget
from modules.widgets import FloatingWindow


class DropdownWidget(Widget.Button):
    def __init__(self, namespace: str = "", child: Widget = Widget.Box(), icon: Widget.Icon = Widget.Icon(), monitor: int = 0, **kwargs) -> None:
        super().__init__(child=icon, **kwargs)
        self.dropdown = FloatingWindow(
            monitor=monitor, namespace=namespace, child=child
        )

    def on_click(self, _) -> None:
        # this assumes the parent window touches the left of the screen
        parentWindow = self.get_root()
        [success, topLeft] = self.compute_point(parentWindow,
                                                Graphene.Point(0, 0))
        middle = topLeft.x + self.get_width() / 2
        self.dropdown.set_position_x(middle)

        self.dropdown.toggle()

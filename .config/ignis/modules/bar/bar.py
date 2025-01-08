from ignis.widgets import Widget


def Bar(monitor: int = 0, left: list[Widget] = [], center: list[Widget] = [], right: list[Widget] = [], css_classes: list[str] = [], **kwargs) -> Widget.Window:
    return Widget.Window(
        anchor=["left", "top", "right"],
        exclusivity="exclusive",
        monitor=monitor,
        namespace=f"ignis_BAR_{monitor}",
        layer="bottom",
        kb_mode="none",
        child=Widget.CenterBox(
            start_widget=Widget.Box(child=left),
            center_widget=Widget.Box(child=center),
            end_widget=Widget.Box(child=right),
            css_classes=css_classes + ["bar"],
        ),
        **kwargs,
    )

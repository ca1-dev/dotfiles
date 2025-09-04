from ignis import widgets


def Bar(monitor: int = 0, left=[], center=[], right=[], css_classes: list[str] = [], **kwargs) -> widgets.Window:
    return widgets.Window(
        anchor=["left", "top", "right"],
        exclusivity="exclusive",
        monitor=monitor,
        namespace=f"ignis_BAR_{monitor}",
        layer="bottom",
        kb_mode="none",
        child=widgets.CenterBox(
            start_widget=widgets.Box(child=left),
            center_widget=widgets.Box(child=center),
            end_widget=widgets.Box(child=right),
            css_classes=css_classes + ["bar"],
        ),
        **kwargs,
    )

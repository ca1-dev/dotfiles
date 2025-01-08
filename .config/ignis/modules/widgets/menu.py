from ignis.widgets import Widget


def MenuHeader(child: list[Widget] = [], css_classes: list[str] = [], **kwargs) -> Widget.Box:
    return Widget.Box(
        css_classes=css_classes + ["menu-header"],
        child=child,
        **kwargs,
    )


def MenuHeaderSeparator(css_classes: list[str] = [], **kwargs) -> Widget.Box:
    return Widget.Box(
        css_classes=css_classes + ["menu-header-separator"],
        **kwargs
    )


def MenuSeparator(css_classes: list[str] = [], **kwargs) -> Widget.Box:
    return Widget.Box(
        css_classes=css_classes + ["menu-separator"],
        **kwargs
    )

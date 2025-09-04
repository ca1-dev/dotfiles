from ignis import widgets


def MenuHeader(child=[], css_classes: list[str] = [], **kwargs) -> widgets.Box:
    return widgets.Box(
        css_classes=css_classes + ["menu-header"],
        child=child,
        **kwargs,
    )


def MenuHeaderSeparator(css_classes: list[str] = [], **kwargs) -> widgets.Box:
    return widgets.Box(
        css_classes=css_classes + ["menu-header-separator"],
        **kwargs
    )


def MenuSeparator(css_classes: list[str] = [], **kwargs) -> widgets.Box:
    return widgets.Box(
        css_classes=css_classes + ["menu-separator"],
        **kwargs
    )

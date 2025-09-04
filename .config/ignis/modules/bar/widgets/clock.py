from datetime import datetime
from ignis import utils, widgets


def Clock(format: str = "%H:%M", css_classes: list[str] = [], **kwargs) -> widgets.Label:
    return widgets.Label(
        label=utils.Poll(
            1000,
            lambda _: datetime.now().strftime(format)).bind("output"),
        css_classes=css_classes + ["bar-widget", "bar-clock"],
        **kwargs,
    )


def StatusPillClock(format: str = "%H:%M", **kwargs) -> widgets.Label:
    return widgets.Label(
        label=utils.Poll(
            1000,
            lambda _: datetime.now().strftime(format)).bind("output"),
        **kwargs,
    )

from datetime import datetime
from ignis.utils import Utils
from ignis.widgets import Widget


def Clock(format: str = "%H:%M", css_classes: list[str] = [], **kwargs) -> Widget.Label:
    return Widget.Label(
        label=Utils.Poll(
            1000,
            lambda _: datetime.now().strftime(format)).bind("output"),
        css_classes=css_classes + ["bar-widget", "bar-clock"],
        **kwargs,
    )


def StatusPillClock(format: str = "%H:%M", **kwargs) -> Widget.Label:
    return Widget.Label(
        label=Utils.Poll(
            1000,
            lambda _: datetime.now().strftime(format)).bind("output"),
        **kwargs,
    )

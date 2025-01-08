from .dropdownwidget import DropdownWidget
from icons import NotificationsIcon
from modules.widgets import NotificationCenter


class NotificationWidget(DropdownWidget):
    nextId = 0

    def __init__(self, monitor: int = 0, css_classes: list[str] = [], **kwargs) -> None:
        namespace = f"ignis_NOTIFICATION_DROPDOWN_{
            monitor}_{NotificationWidget.nextId}"

        super().__init__(
            namespace=namespace,
            monitor=monitor,
            icon=NotificationsIcon(),
            child=[
                NotificationCenter(
                    css_classes=["notification-dropdown"],
                ),
            ],
            css_classes=css_classes + [
                "bar-widget",
                "bar-widget-button",
                "bar-notifications"
            ],
            **kwargs,
        )

        NotificationWidget.nextId += 1

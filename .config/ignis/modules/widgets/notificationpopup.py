from .notificationcard import NotificationCard
from ignis.services.notifications import Notification, NotificationService
from ignis.widgets import Widget

notifications = NotificationService.get_default()


class NotificationPopup(Widget.Window):
    def __init__(self, monitor: int = 0, **kwargs) -> None:
        super().__init__(
            anchor=["right", "top"],
            monitor=monitor,
            namespace=f"ignis_NOTIFICATION_POPUP_{monitor}",
            layer="top",
            child=Widget.Box(
                vertical=True,
                valign="start",
                css_classes=["notification-popup"],
            ),
            visible=False,
            **kwargs,
        )

        notifications.connect(
            "new_popup", lambda _, notification: self.add(notification)
        )

        notifications.connect(
            "notify::popups",
            lambda _, __:
                self.set_visible(False)
                if len(notifications.popups) == 0 else
                ()
        )

    def add(self, notification: Notification) -> None:
        self.child.prepend(
            NotificationCard(notification, closeOn="dismissed")
        )

        self.set_visible(True)

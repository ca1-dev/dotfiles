from gi.repository import GLib
from icons import icons
from ignis.options import options
from ignis.services.notifications import Notification, NotificationService
from ignis.utils import Utils
from ignis.widgets import Widget
from modules.widgets import MenuHeader, MenuHeaderSeparator, MenuSeparator, NotificationCard

notifications = NotificationService.get_default()


class NotificationList(Widget.Box):
    def __init__(self, css_classes: list[str] = [], **kwargs) -> None:
        loading_notifications_label = Widget.Label(
            valign="center",
            vexpand=True,
            label="Loading notifications...",
            css_classes=["notification-center-info-label"],
        )

        super().__init__(
            vertical=True,
            vexpand=True,
            child=[loading_notifications_label],
            setup=lambda self: notifications.connect(
                "notified",
                lambda _, notification: self.on_notified(notification),
            ),
            css_classes=css_classes + ["notification-center-info-label"],
            **kwargs,
        )

        Utils.ThreadTask(
            self.load_notifications,
            lambda result: self.set_child(result),
        ).run()

    def on_notified(self, notification: Notification) -> None:
        self.prepend(NotificationCard(notification))

    def load_notifications(self) -> None:
        widgets = []
        for i in notifications.notifications:
            GLib.idle_add(lambda i=i: widgets.append(NotificationCard(i)))

        widgets.append(
            Widget.Label(
                valign="center",
                vexpand=True,
                visible=notifications.bind(
                    "notifications",
                    lambda value: len(value) == 0,
                ),
                label="No notifications",
            )
        )

        return widgets


def NotificationCenter(css_classes: list[str] = [], **kwargs) -> Widget.Box:
    notificationCount = Widget.Label(
        label=notifications.bind(
            "notifications",
            lambda value: str(len(value)),
        ),
    )

    header = Widget.Label(
        label=notifications.bind(
            "notifications",
            lambda notifications:
            "Notification"
            if len(notifications) == 1
            else "Notifications"
        ),
    )

    dndButton = Widget.Button(
        child=Widget.Icon(
            image=options.notifications.bind(
                "dnd",
                lambda dndEnabled:
                    icons["notifications"]["tray"]["empty"]
                    if dndEnabled else
                    icons["notifications"]["tray"]["dnd"]
            )
        ),
        on_click=lambda _:
            options.notifications.set_dnd(not options.notifications.dnd),
        css_classes=["notification-dnd"],
    )

    clearAllButton = Widget.Button(
        child=Widget.Label(label="Clear all"),
        on_click=lambda _: notifications.clear_all(),
        css_classes=["notification-clear-all"],
    )

    return Widget.Box(
        vertical=True,
        vexpand=True,
        child=[
            MenuHeader(
                child=[
                    notificationCount,
                    MenuHeaderSeparator(),
                    header,
                    MenuHeaderSeparator(),
                    Widget.Box(
                        child=[
                            dndButton,
                            MenuHeaderSeparator(),
                            clearAllButton
                        ],
                        hexpand=True,
                        halign="end"
                    )
                ],
            ),
            MenuSeparator(),
            Widget.Scroll(
                child=NotificationList(),
                vexpand=True,
            ),
        ],
        css_classes=css_classes + ["notification-center"],
        **kwargs,
    )

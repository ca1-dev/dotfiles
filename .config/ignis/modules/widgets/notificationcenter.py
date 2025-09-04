from gi.repository import GLib
from icons import icons
from ignis import utils, widgets
from ignis.options import options
from ignis.services.notifications import Notification, NotificationService
from modules.widgets import MenuHeader, MenuHeaderSeparator, MenuSeparator, NotificationCard

notifications = NotificationService.get_default()


class NotificationList(widgets.Box):
    def __init__(self, css_classes: list[str] = [], **kwargs) -> None:
        loading_notifications_label = widgets.Label(
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

        utils.ThreadTask(
            self.load_notifications,
            lambda result: self.set_child(result),
        ).run()

    def on_notified(self, notification: Notification) -> None:
        self.prepend(NotificationCard(notification))

    def load_notifications(self) -> None:
        notificationWidgets = []
        for i in notifications.notifications:
            GLib.idle_add(lambda i=i: notificationWidgets.append(
                NotificationCard(i)))

        notificationWidgets.append(
            widgets.Label(
                valign="center",
                vexpand=True,
                visible=notifications.bind(
                    "notifications",
                    lambda value: len(value) == 0,
                ),
                label="No notifications",
            )
        )

        return notificationWidgets


def NotificationCenter(css_classes: list[str] = [], **kwargs) -> widgets.Box:
    notificationCount = widgets.Label(
        label=notifications.bind(
            "notifications",
            lambda value: str(len(value)),
        ),
    )

    header = widgets.Label(
        label=notifications.bind(
            "notifications",
            lambda notifications:
            "Notification"
            if len(notifications) == 1
            else "Notifications"
        ),
    )

    dndButton = widgets.Button(
        child=widgets.Icon(
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

    clearAllButton = widgets.Button(
        child=widgets.Label(label="Clear all"),
        on_click=lambda _: notifications.clear_all(),
        css_classes=["notification-clear-all"],
    )

    return widgets.Box(
        vertical=True,
        vexpand=True,
        child=[
            MenuHeader(
                child=[
                    notificationCount,
                    MenuHeaderSeparator(),
                    header,
                    MenuHeaderSeparator(),
                    widgets.Box(
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
            widgets.Scroll(
                child=NotificationList(),
                vexpand=True,
            ),
        ],
        css_classes=css_classes + ["notification-center"],
        **kwargs,
    )

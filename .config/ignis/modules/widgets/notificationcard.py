from icons import icons
from ignis.services.notifications import Notification
from ignis.widgets import Widget
from typing import Literal


def NotificationCard(notification: Notification, closeOn: Literal["closed", "dismissed"] = "closed", css_classes: list[str] = [], **kwargs) -> Widget.Box:
    notificationIcon = Widget.Icon(
        image=notification.icon
        if notification.icon
        else icons["notifications"]["card"]["placeholder"],
        pixel_size=48,
        halign="start",
        valign="start",
    )

    notificationContent = Widget.Box(
        vertical=True,
        child=[
            Widget.Label(
                ellipsize="end",
                halign="start",
                visible=notification.summary != "",
                label=notification.summary,
            ),
            Widget.Label(
                ellipsize="end",
                halign="start",
                visible=notification.body != "",
                label=notification.body,
                css_classes=["notification-body"]
            ),
        ],
        css_classes=["notification-content"],
    )

    dismissButton = Widget.Button(
        halign="end",
        valign="start",
        hexpand=True,
        child=Widget.Icon(
            image=icons["notifications"]["card"]["dismiss"],
            pixel_size=20
        ),
        on_click=lambda _: notification.close(),
        css_classes=["notification-close"],
    )

    actionButtons = Widget.Box(
        homogeneous=True,
        spacing=10,
        child=[
            Widget.Button(
                child=Widget.Label(label=action.label),
                on_click=lambda _: action.invoke(),
                css_classes=["notification-action"],
            )
            for action in notification.actions
        ],
        css_classes=["notification-actions"],
    )

    return Widget.Box(
        vertical=True,
        hexpand=True,
        child=[
            Widget.Box(
                child=[
                    notificationIcon,
                    notificationContent,
                    dismissButton,
                ],
            ),
            actionButtons,
        ],
        setup=lambda self:
            notification.connect(closeOn, lambda _: self.unparent()),
        css_classes=css_classes + ["notification-card"],
        **kwargs,
    )

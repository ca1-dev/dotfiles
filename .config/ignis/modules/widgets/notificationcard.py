from icons import icons
from ignis import widgets
from ignis.services.notifications import Notification
from typing import Literal


def NotificationCard(notification: Notification, closeOn: Literal["closed", "dismissed"] = "closed", css_classes: list[str] = [], **kwargs) -> widgets.Box:
    notificationIcon = widgets.Icon(
        image=notification.icon
        if notification.icon
        else icons["notifications"]["card"]["placeholder"],
        pixel_size=48,
        halign="start",
        valign="start",
    )

    notificationContent = widgets.Box(
        vertical=True,
        child=[
            widgets.Label(
                ellipsize="end",
                halign="start",
                visible=notification.summary != "",
                label=notification.summary,
            ),
            widgets.Label(
                ellipsize="end",
                halign="start",
                visible=notification.body != "",
                label=notification.body,
                css_classes=["notification-body"]
            ),
        ],
        css_classes=["notification-content"],
    )

    dismissButton = widgets.Button(
        halign="end",
        valign="start",
        hexpand=True,
        child=widgets.Icon(
            image=icons["notifications"]["card"]["dismiss"],
            pixel_size=20
        ),
        on_click=lambda _: notification.close(),
        css_classes=["notification-close"],
    )

    actionButtons = widgets.Box(
        homogeneous=True,
        spacing=10,
        child=[
            widgets.Button(
                child=widgets.Label(label=action.label),
                on_click=lambda _: action.invoke(),
                css_classes=["notification-action"],
            )
            for action in notification.actions
        ],
        css_classes=["notification-actions"],
    )

    return widgets.Box(
        vertical=True,
        hexpand=True,
        child=[
            widgets.Box(
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

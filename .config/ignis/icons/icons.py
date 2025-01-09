from ignis.options import options
from ignis.services.audio import AudioService
from ignis.services.notifications import NotificationService
from ignis.widgets import Widget
import os.path

audio = AudioService.get_default()
notifications = NotificationService.get_default()


def assetPath(s: str) -> str:
    return os.path.dirname(__file__) + "/svg/" + s + ".svg"


icons = {
    "audio": {
        "speaker": {
            "muted": assetPath("material-volume-off-symbolic"),
            "low": assetPath("material-volume-down-symbolic"),
            "high": assetPath("material-volume-up-symbolic"),
            "menu_icon": assetPath("material-volume-up-symbolic"),
        },
        "microphone": {
            "muted": assetPath("material-mic-off-symbolic"),
            "unmuted": assetPath("material-mic-symbolic"),
            "menu_icon": assetPath("material-mic-symbolic"),
        },
    },
    "notifications": {
        "tray": {
            "nonEmpty": assetPath("material-notifications-unread-symbolic"),
            "empty": assetPath("material-notifications-symbolic"),
            "dnd": assetPath("material-notifications-off-symbolic")
        },
        "card": {
            "placeholder": assetPath("my-nix-snowflake-symbolic"),
            "dismiss": assetPath("material-close-symbolic"),
        },
    },
}


def speaker_icon_image(_) -> str:
    if audio.speaker.is_muted:
        return icons["audio"]["speaker"]["muted"]

    volume = audio.speaker.volume
    if not volume or volume < 50:
        return icons["audio"]["speaker"]["low"]
    else:
        return icons["audio"]["speaker"]["high"]


def set_microphone_icon(_) -> str:
    if audio.microphone.is_muted:
        return icons["audio"]["microphone"]["muted"]

    return icons["audio"]["microphone"]["unmuted"]


def AudioDeviceIcon(type) -> Widget.Icon:
    if type == "speaker":
        return Widget.Icon(
            image=audio.speaker.bind("icon_name", speaker_icon_image)
        )

    if type == "microphone":
        return Widget.Icon(
            image=audio.microphone.bind("icon_name", set_microphone_icon)
        )


def NotificationsIcon() -> Widget.Box:
    dndOn = Widget.Icon(
        image=icons["notifications"]["tray"]["dnd"],
        visible=options.notifications.bind("dnd"),
    )
    dndOff = Widget.Icon(
        image=notifications.bind(
            "notifications",
            lambda notifications:
                icons["notifications"]["tray"]["nonEmpty"]
                if len(notifications) > 0 else
                icons["notifications"]["tray"]["empty"]
        ),
        visible=options.notifications.bind(
            "dnd",
            lambda dndEnabled: not dndEnabled,
        ),
    )
    return Widget.Box(
        child=[
            dndOn,
            dndOff,
        ]
    )

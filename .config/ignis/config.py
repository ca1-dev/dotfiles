from icons import AudioDeviceIcon, NotificationsIcon
from ignis.app import IgnisApp
from ignis.widgets import Widget
from modules import Bar
from modules.bar.widgets import Clock, NotificationWidget, StatusPill, StatusPillClock, Tray, VolumeWidget, Workspaces
from modules.widgets import ControlCenter, DeviceMenu, MenuHeader, MenuSeparator, NotificationCenter, NotificationPopup, VolumeSlider

import os.path

app = IgnisApp.get_default()

ControlCenter(
    widgets=[
        MenuHeader(child=[Widget.Label(label="Volume")]),
        VolumeSlider("speaker"),
        VolumeSlider("microphone"),
        MenuSeparator(),
        DeviceMenu("speaker"),
        MenuSeparator(),
        DeviceMenu("microphone"),
        MenuSeparator(),
        NotificationCenter(),
    ]
)

Bar(
    0,
    left=[Workspaces()],
    right=[
        Tray(),
        StatusPill(
            monitor=0,
            widgets=[
                AudioDeviceIcon("speaker"),
                NotificationsIcon(),
                StatusPillClock("%a %d/%m %H:%M"),
            ]
        ),
    ],
    # css_classes=["floating"],
)

NotificationPopup(0)


app.apply_css(
    os.path.dirname(__file__) + "/scss/themes/" + os.getenv("THEME") + ".scss"
)

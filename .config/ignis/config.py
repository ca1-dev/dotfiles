from icons import AudioDeviceIcon, NotificationsIcon
from ignis import widgets, utils
from ignis.css_manager import CssManager, CssInfoPath
from modules import Bar
from modules.bar.widgets import Clock, NotificationWidget, StatusPill, StatusPillClock, Tray, VolumeWidget, Workspaces
from modules.widgets import ControlCenter, DeviceMenu, MenuHeader, MenuSeparator, NotificationCenter, NotificationPopup, VolumeSlider

import os.path

css_manager = CssManager.get_default()

ControlCenter(
    widgets=[
        MenuHeader(child=[widgets.Label(label="Volume")]),
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


css_manager.apply_css(
    CssInfoPath(
        name="main",
        path=os.path.dirname(__file__) + "/scss/themes/" +
        os.getenv("THEME") + ".scss",
        compiler_function=lambda path: utils.sass_compile(path=path),
    )
)

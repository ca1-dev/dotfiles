from .dropdownwidget import DropdownWidget
from icons import AudioDeviceIcon
from ignis import widgets
from modules.widgets import DeviceMenu, MenuHeader, MenuSeparator, VolumeSlider


class VolumeWidget(DropdownWidget):
    nextId = 0

    def __init__(self, monitor: int = 0, css_classes: list[str] = [], **kwargs) -> None:
        namespace = f"ignis_VOLUME_DROPDOWN_{monitor}_{VolumeWidget.nextId}"

        super().__init__(
            namespace=namespace,
            monitor=monitor,
            icon=AudioDeviceIcon("speaker"),
            child=[
                MenuHeader(child=[widgets.Label(label="Volume")]),
                VolumeSlider("speaker"),
                VolumeSlider("microphone"),
                MenuSeparator(),
                DeviceMenu("speaker"),
                MenuSeparator(),
                DeviceMenu("microphone"),
            ],
            css_classes=css_classes + ["bar-widget",
                                       "bar-widget-button", "bar-volume"],
            **kwargs,
        )

        VolumeWidget.nextId += 1

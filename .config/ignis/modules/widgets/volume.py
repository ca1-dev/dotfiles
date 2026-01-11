from icons import icons, AudioDeviceIcon
from ignis import widgets
from ignis.services.audio import AudioService, Stream
from modules.widgets import MenuHeader, MenuHeaderSeparator
from typing import Literal

audio = AudioService.get_default()

MENU_TITLES = {
    "speaker": "Speakers",
    "microphone": "Microphones",
}


def DeviceItem(stream: Stream, streamType: Literal["speaker", "microphone"], css_classes: list[str] = [], **kwargs) -> widgets.Button:
    icon = widgets.Icon(image=icons["audio"][streamType]["menu_icon"])

    deviceName = widgets.Label(
        ellipsize="end",
        max_width_chars=30,
        halign="start",
        label=stream.description,
        css_classes=["audio-device-entry-label"],
    )

    return widgets.Button(
        hexpand=True,
        child=widgets.Box(
            child=[
                icon,
                deviceName,
            ]
        ),
        setup=lambda self: stream.connect(
            "removed", lambda _: self.unparent()
        ),
        on_click=lambda _: setattr(audio, streamType, stream),
        css_classes=stream.bind(
            "is_default",
            lambda is_default:
                css_classes + ["audio-device-entry", "active"]
                if is_default else
                css_classes + ["audio-device-entry"],
        ),
        **kwargs,
    )


def VolumeSlider(streamType: Literal["speaker", "microphone"] = "speaker", css_classes: list[str] = [], **kwargs) -> widgets.Box:
    stream = getattr(audio, streamType)

    icon = widgets.Button(
        child=AudioDeviceIcon(streamType),
        on_click=lambda _: stream.set_is_muted(not stream.is_muted),
        css_classes=["slider-icon"],
    )

    scale = widgets.Scale(
        value=stream.bind("volume"),
        hexpand=True,
        sensitive=stream.bind("is_muted", lambda is_muted: not is_muted),
        on_change=lambda volume: stream.set_volume(volume.value),
        css_classes=["slider"],
    )

    return widgets.Box(
        child=[icon, scale],
        css_classes=css_classes + ["slider-container"],
        **kwargs,
    )


def DeviceMenu(streamType: Literal["speaker", "microphone"] = "speaker", css_classes: list[str] = [], **kwargs) -> widgets.Box:
    header = MenuHeader(child=[
        widgets.Icon(image=icons["audio"][streamType]["menu_icon"]),
        MenuHeaderSeparator(),
        widgets.Label(
            label=MENU_TITLES[streamType],
            halign="start",
        ),
    ])

    content = widgets.Box(
        vertical=True,
        setup=lambda self: audio.connect(
            f"{streamType}-added",
            lambda _, stream: self.append(
                DeviceItem(stream, streamType)),
        ),
    )

    return widgets.Box(
        name=f"volume-{streamType}",
        vertical=True,
        child=[header, content],
        css_classes=css_classes + ["audio-device-list"],
        **kwargs,
    )

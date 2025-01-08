from ignis.services.system_tray import SystemTrayItem, SystemTrayService
from ignis.widgets import Widget
from modules import globals

system_tray = SystemTrayService.get_default()


def TrayItem(item: SystemTrayItem, css_classes: list[str] = [], **kwargs) -> Widget.Button:
    if item.menu:
        menu = item.menu

    def on_click(_) -> None:
        globals.currentMenu.value = ""
        item.activate()

    def on_right_click(_) -> None:
        globals.currentMenu.value = ""
        menu.popup()

    return Widget.Button(
        tooltip_text=item.bind("tooltip"),
        child=Widget.Box(
            child=[
                Widget.Icon(image=item.bind("icon")),
                menu,
            ]
        ),
        on_click=on_click,
        on_right_click=on_right_click,
        setup=lambda self: item.connect("removed", lambda _: self.unparent()),
        css_classes=css_classes + ["bar-widget", "bar-widget-button"],
        **kwargs,
    )


def Tray(**kwargs) -> Widget.Box:
    return Widget.Box(
        setup=lambda self: system_tray.connect(
            "added", lambda _, item: self.append(TrayItem(item))
        ),
        **kwargs,
    )

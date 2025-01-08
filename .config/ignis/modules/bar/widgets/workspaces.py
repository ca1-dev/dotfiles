from ignis.services.hyprland import HyprlandService
from ignis.widgets import Widget
from modules import globals

hyprland = HyprlandService.get_default()


class WorkspaceButton(Widget.Button):
    def __init__(self, workspace: dict, css_classes: list[str] = [], **kwargs) -> None:
        self.workspace = workspace
        self.workspace_id = workspace["id"]

        self.icon = Widget.Box(
            css_classes=hyprland.bind(
                "active_window",
                lambda _:
                    ["bar-workspace-button-icon", "non-empty"]
                    if self.workspace["windows"] > 0 else
                    ["bar-workspace-button-inner", "empty"]
            ),
        )

        super().__init__(
            halign="start",
            valign="center",
            child=self.icon,
            css_classes=hyprland.bind(
                "workspaces",
                lambda _:
                    css_classes + ["active", "bar-workspace-button"]
                    if hyprland.active_workspace["id"] == self.workspace_id
                    else css_classes + ["inactive", "bar-workspace-button"]
            ),
            **kwargs,
        )

    def on_click(self, _) -> None:
        globals.currentMenu.value = ""
        hyprland.switch_to_workspace(self.workspace_id)


def workspace_next() -> None:
    current = hyprland.active_workspace["id"]
    target = current + 1
    if target != 10:
        hyprland.switch_to_workspace(target)


def workspace_prev() -> None:
    hyprland.switch_to_workspace(hyprland.active_workspace["id"] - 1)


def Workspaces(css_classes: list[str] = [], **kwargs) -> Widget.EventBox:
    if hyprland.is_available:
        box = Widget.EventBox(
            on_scroll_up=lambda _: workspace_next(),
            on_scroll_down=lambda _: workspace_prev(),
            child=hyprland.bind(
                "workspaces",
                transform=lambda value: [
                    WorkspaceButton(i) for i in value
                ],
            ),
            css_classes=css_classes + ["bar-widget", "bar-workspaces"],
            **kwargs,
        )
    else:
        box = Widget.EventBox()
    return box

from ignis import widgets
from ignis.services.hyprland import HyprlandService
from modules import globals

hyprland = HyprlandService.get_default()


class WorkspaceButton(widgets.Button):
    def __init__(self, workspace: dict, css_classes: list[str] = [], **kwargs) -> None:
        self.id = workspace.id

        self.icon = widgets.Box(
            css_classes=hyprland.bind_many(
                ["windows", "active_window"],
                transform=lambda *_: ["bar-workspace-button-inner", "non-empty"] if len(
                    hyprland.get_windows_on_workspace(self.id)) > 0 else ["bar-workspace-button-inner", "empty"]
            )
        )

        super().__init__(
            halign="start",
            valign="center",
            child=self.icon,
            css_classes=hyprland.bind_many(
                ["active_workspace"],
                transform=lambda *_: css_classes +
                ["active", "bar-workspace-button"] if hyprland.active_workspace.id == self.id else css_classes +
                ["inactive", "bar-workspace-button"]
            ),
            **kwargs,
        )

    def on_click(self, _) -> None:
        globals.currentMenu.value = ""
        hyprland.switch_to_workspace(self.id)


def workspace_next() -> None:
    current = hyprland.active_workspace.id
    target = current + 1
    if target != 10:
        hyprland.switch_to_workspace(target)


def workspace_prev() -> None:
    hyprland.switch_to_workspace(hyprland.active_workspace.id - 1)


def Workspaces(css_classes: list[str] = [], **kwargs) -> widgets.EventBox:
    if hyprland.is_available:
        box = widgets.EventBox(
            on_scroll_up=lambda _: workspace_next(),
            on_scroll_down=lambda _: workspace_prev(),

            child=hyprland.bind(
                "workspaces",
                transform=lambda workspaces: [
                    WorkspaceButton(i) for i in workspaces
                ]
            ),
            css_classes=css_classes + ["bar-widget", "bar-workspaces"],
            **kwargs,
        )
    else:
        box = widgets.EventBox()
    return box

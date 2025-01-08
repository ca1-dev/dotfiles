local wezterm = require('wezterm')

-- keybinds
local act = wezterm.action
local keys = {
    -- navigation
    { key = 'h',  mods = 'ALT',          action = act.ActivatePaneDirection('Left'), },
    { key = 'j',  mods = 'ALT',          action = act.ActivatePaneDirection('Down'), },
    { key = 'k',  mods = 'ALT',          action = act.ActivatePaneDirection('Up'), },
    { key = 'l',  mods = 'ALT',          action = act.ActivatePaneDirection('Right'), },
    { key = 'h',  mods = 'ALT|SHIFT',    action = act.ActivateTabRelative(-1), },
    { key = 'l',  mods = 'ALT|SHIFT',    action = act.ActivateTabRelative(1), },
    { key = 'n',  mods = 'ALT',          action = act.SwitchWorkspaceRelative(1), },
    { key = 'p',  mods = 'ALT',          action = act.SwitchWorkspaceRelative(-1), },

    -- resize panes
    { key = 'h',  mods = 'ALT|CTRL',     action = act.AdjustPaneSize({ 'Left', 5, }), },
    { key = 'j',  mods = 'ALT|CTRL',     action = act.AdjustPaneSize({ 'Down', 5, }), },
    { key = 'k',  mods = 'ALT|CTRL',     action = act.AdjustPaneSize({ 'Up', 5, }), },
    { key = 'l',  mods = 'ALT|CTRL',     action = act.AdjustPaneSize({ 'Right', 5, }), },

    -- move tabs
    { key = '<',  mods = 'ALT|SHIFT',    action = act.MoveTabRelative(-1), },
    { key = '>',  mods = 'ALT|SHIFT',    action = act.MoveTabRelative(1), },

    -- new panes/tabs
    { key = '\'', mods = 'ALT',          action = wezterm.action.SplitPane({ direction = 'Right', }), },
    { key = '"',  mods = 'ALT|SHIFT',    action = wezterm.action.SplitPane({ direction = 'Right', top_level = true, }), },
    { key = '-',  mods = 'ALT',          action = wezterm.action.SplitPane({ direction = 'Down', }), },
    { key = '_',  mods = 'ALT|SHIFT',    action = wezterm.action.SplitPane({ direction = 'Down', top_level = true, }), },
    { key = 'c',  mods = 'LEADER',       action = act.SpawnTab('CurrentPaneDomain'), },

    -- copy mode
    { key = '[',  mods = 'LEADER',       action = act.ActivateCopyMode, },

    -- other tmux stuff
    { key = 'x',  mods = 'LEADER',       action = wezterm.action.CloseCurrentPane({ confirm = true, }), },
    { key = 'q',  mods = 'LEADER',       action = wezterm.action.CloseCurrentTab({ confirm = true, }), },
    { key = 'y',  mods = 'CTRL|SHIFT',   action = act.SwitchToWorkspace({ name = '4', }), },
    { key = ':',  mods = 'LEADER|SHIFT', action = act.ActivateCommandPalette, },

    -- workspaces
    { key = 's',  mods = 'LEADER',       action = act.ShowLauncherArgs({ flags = 'WORKSPACES', }), },
    {
        key = 'n',
        mods = 'LEADER',
        action = act.PromptInputLine {
            action = wezterm.action_callback(function(window, pane, line)
                if line then
                    window:perform_action(act.SwitchToWorkspace {
                            name = line,
                        },
                        pane
                    )
                end
            end),
        },
    },

}

return function(config)
    -- domains
    config.unix_domains = {
        {
            name = 'unix',
        },
    }
    config.default_domain = 'unix'

    -- tab bar
    config.enable_tab_bar = true
    config.tab_bar_at_bottom = true
    config.use_fancy_tab_bar = false
    config.tab_max_width = 25
    config.window_padding.bottom = 0

    wezterm.on('update-right-status', function(window, pane)
        local workspace_count = #wezterm.mux.get_workspace_names()
        window:set_right_status(wezterm.format { {
            Text = string.format('[%s] (%d workspace%s)',
                wezterm.mux.get_active_workspace(),
                workspace_count,
                workspace_count > 1 and 's' or ''),
        }, })
    end)

    wezterm.on(
        'format-tab-title',
        function(tab, tabs, panes, config, hover, max_width)
            local title = tab.tab_title

            if not title or #title == 0 then
                title = tab.active_pane.title
            end

            title = string.sub(title, 1, config.tab_max_width - 3)

            return {
                { Text = ' ' .. title .. ' ', },
                { Foreground = { AnsiColor = 'White', }, },
                { Background = { Color = 'rgba(0, 0, 0, 0)', }, },
                { Attribute = { Intensity = 'Half', }, },
                { Text = '|', },
            }
        end
    )

    config.inactive_pane_hsb = {
        saturation = 1,
        brightness = 1,
    }

    for _, v in pairs(keys) do
        table.insert(config.keys, v)
    end
end

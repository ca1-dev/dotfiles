local wezterm = require('wezterm')
local multiplexing = require('multiplexing')

local env_theme = os.getenv('THEME')
local theme
local theme_file = io.open(os.getenv('HOME') .. '/.config/wezterm/themes/' .. (env_theme or '') .. '.lua', 'r')
if theme_file then
    io.close(theme_file)
    theme = require('themes.' .. env_theme)
else
    theme = require('themes.tokyonight')
end

local config = wezterm.config_builder()

-- general options
config.audible_bell = 'Disabled'
config.check_for_updates = false

-- visual
theme(config)
config.animation_fps = 120
config.font = wezterm.font('FiraCode Nerd Font Mono', { weight = 500, })
config.font_size = 12.0
config.adjust_window_size_when_changing_font_size = false
config.bold_brightens_ansi_colors = false
config.default_cursor_style = 'SteadyUnderline'
config.cursor_thickness = '1pt'
config.enable_tab_bar = false
config.window_decorations = 'RESIZE'
config.window_padding = {
    left = 10,
    right = 10,
    top = 10,
    bottom = 10,
}

-- keybinds
config.disable_default_key_bindings = true
local act = wezterm.action
config.leader = { key = 'Space', mods = 'CTRL', }
config.keys = {
    { key = '+', mods = 'SHIFT|CTRL', action = act.IncreaseFontSize, },
    { key = '-', mods = 'SHIFT|CTRL', action = act.DecreaseFontSize, },
    { key = '0', mods = 'SHIFT|CTRL', action = act.ResetFontSize, },

    { key = 'c', mods = 'SHIFT|CTRL', action = act.CopyTo('Clipboard'), },
    { key = 'c', mods = 'SUPER',      action = act.CopyTo('Clipboard'), },
    { key = 'v', mods = 'SHIFT|CTRL', action = act.PasteFrom('Clipboard'), },
    { key = 'v', mods = 'SUPER',      action = act.PasteFrom('Clipboard'), },

    { key = 'l', mods = 'SHIFT|CTRL', action = act.ShowDebugOverlay, },
    { key = 'p', mods = 'SHIFT|CTRL', action = act.ActivateCommandPalette, },
    { key = 'r', mods = 'SHIFT|CTRL', action = act.ReloadConfiguration, },
    { key = 'n', mods = 'SUPER',      action = act.SpawnWindow, },
}

-- fix things on wayland
config.enable_wayland = false
config.front_end = 'WebGpu'
config.webgpu_power_preference = 'HighPerformance'

multiplexing(config)

return config

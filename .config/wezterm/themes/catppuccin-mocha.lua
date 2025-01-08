return function(config)
    config.color_scheme = 'Catppuccin Mocha'

    config.window_background_opacity = 1.0

    if not config.colors then config.colors = {} end
    config.colors.tab_bar = {
        background = 'rgba(0, 0, 0, 0)',

        active_tab = {
            bg_color = '#cba6f7',
            fg_color = '#181825',
            intensity = 'Bold',
        },

        inactive_tab = {
            bg_color = 'rgba(0, 0, 0, 0)',
            fg_color = '#cdd6f4',
        },

        inactive_tab_hover = {
            bg_color = 'rgba(0, 0, 0, 0)',
            fg_color = '#cba6f7',
        },

        new_tab = {
            bg_color = 'rgba(0, 0, 0, 0)',
            fg_color = '#cdd6f4',
        },

        new_tab_hover = {
            bg_color = 'rgba(0, 0, 0, 0)',
            fg_color = '#cba6f7',
        },
    }
end

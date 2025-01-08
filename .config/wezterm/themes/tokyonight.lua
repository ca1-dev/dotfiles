return function(config)
    config.color_scheme = 'Tokyo Night'

    config.window_background_opacity = 1.0

    if not config.colors then config.colors = {} end
    config.colors.tab_bar = {
        background = 'rgba(0, 0, 0, 0)',

        active_tab = {
            bg_color = '#7aa2f7',
            fg_color = '#16161e',
            intensity = 'Bold',
        },

        inactive_tab = {
            bg_color = 'rgba(0, 0, 0, 0)',
            fg_color = '#c0caf5',
        },

        inactive_tab_hover = {
            bg_color = 'rgba(0, 0, 0, 0)',
            fg_color = '#7aa2f7',
        },

        new_tab = {
            bg_color = 'rgba(0, 0, 0, 0)',
            fg_color = '#c0caf5',
        },

        new_tab_hover = {
            bg_color = 'rgba(0, 0, 0, 0)',
            fg_color = '#7aa2f7',
        },
    }
end

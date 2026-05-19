if status is-interactive
    # general options
    set fish_greeting ""

    # key bindings
    fish_vi_key_bindings
    bind --mode insert \cf forward-char

    # aliases
    alias la='ls -A'
    alias mv='mv -i'
    alias gs='git status'
    alias gl='git log --oneline --graph'
    alias dev='nix develop -c fish'
    alias nix-shell='nix-shell --command fish'
    alias todo='cat ~/todo.md'

    alias mutt0='ACCOUNT_NUMBER=0 neomutt'
    alias mutt1='ACCOUNT_NUMBER=1 neomutt'
    alias mutt2='ACCOUNT_NUMBER=2 neomutt'
    alias mutt3='ACCOUNT_NUMBER=3 neomutt'
    alias mutt4='ACCOUNT_NUMBER=4 neomutt'
    alias mutt5='ACCOUNT_NUMBER=5 neomutt'
    alias mutt6='ACCOUNT_NUMBER=6 neomutt'
    alias mutt7='ACCOUNT_NUMBER=7 neomutt'
    alias mutt8='ACCOUNT_NUMBER=8 neomutt'

    # environment variables
    fish_add_path "$HOME/.cargo/bin/" --path

    source ~/.config/fish/local.fish 2>/dev/null
    source '/etc/profiles/per-user/$USER/etc/profile.d/hm-session-vars.fish' 2>/dev/null
    source "$HOME/.nix-profile/etc/profile.d/hm-session-vars.fish" 2>/dev/null
    source "$HOME/.local/bin/env.fish"

    set EDITOR nvim

    # other
    type -q zoxide; and eval (zoxide init fish | source)

    # theme (default to tokyonight if invalid $THEME)
    set accent_primary blue
    set accent_secondary magenta
    set accent_tertiary magenta
    source ~/.config/fish/themes/$THEME.fish 2>/dev/null
end

function fish_title
    echo (status current-command) \((prompt_pwd)\)
end

# prompt stuff
function fish_prompt
    echo "$(set_color $accent_primary)$(prompt_pwd --full-length-dirs 99)$(vcs_info) $(set_color $accent_secondary)❯ "
end

function fish_mode_prompt
end

function newline --on-event fish_postexec
    echo
end

function vcs_info
    set -g __fish_git_prompt_showdirtystate 1
    set -g __fish_git_prompt_describe_style branch

    set -g __fish_git_prompt_char_stateseparator ' '
    set -g __fish_git_prompt_color $accent_tertiary

    set -g __fish_git_prompt_char_dirtystate '!'
    set -g __fish_git_prompt_char_stagedstate '+'

    set -g __fish_git_prompt_color_flags yellow
    set -g __fish_git_prompt_color_merging red

    set -g __fish_git_prompt_status_order dirtystate stagedstate

    set -l gitinfo (__fish_git_prompt '  %s')
    set -l gitinfo (string replace -r '\|\s*(REBASE(-\w+)?|MERGING|REVERTING)(.*)' " (\1\3$(set_color red))" $gitinfo)

    echo $gitinfo
end

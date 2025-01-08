# colours, set default if $THEME file not found
accent_primary=blue
accent_secondary=magenta
accent_tertiary=magenta
source ~/.config/zsh/themes/$THEME.zsh

# completion
autoload -Uz compinit && compinit
zstyle ':completion:*' matcher-list '' 'm:{[:lower:]}={[:upper:]}'
zstyle ':completion:*' menu select
zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}

# use vim keys to move through completion list
zmodload zsh/complist
bindkey -M menuselect 'h' vi-backward-char
bindkey -M menuselect 'k' vi-up-line-or-history
bindkey -M menuselect 'l' vi-forward-char
bindkey -M menuselect 'j' vi-down-line-or-history

# history
HISTFILE=~/.zsh_history
HISTSIZE=1000
SAVEHIST=$HISTSIZE
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_find_no_dups

# aliases
alias la='ls -A'
alias mv='mv -i'
alias gs='git status'
alias dev='nix develop -c zsh'
alias pfetch='PF_INFO="ascii title os shell wm editor palette" pfetch'

# general settings
unsetopt beep
bindkey -v
setopt autocd

# environment variables
export EDITOR='nvim'
path+=("$HOME/.cargo/bin/")
export PATH

# vcs_info
autoload -Uz add-zsh-hook vcs_info
add-zsh-hook precmd vcs_info
zstyle ':vcs_info:*' enable git
zstyle ':vcs_info:git*' check-for-changes true

zstyle ':vcs_info:*' formats '  %b%u%c'
zstyle ':vcs_info:*' actionformats 'hi'
zstyle ':vcs_info:*' stagedstr ' %F{yellow}+'
zstyle ':vcs_info:*' unstagedstr ' %F{yellow}!'

# prompt
setopt prompt_subst
export PS1='%F{$accent_primary}%~%F{$accent_tertiary}${vcs_info_msg_0_} %F{$accent_secondary}❯%F{white} '
_precmd_newline_between_prompts() $funcstack[1]() echo
add-zsh-hook precmd _precmd_newline_between_prompts

# window title
function xtitle () {
    builtin print -n -- "\e]0;$@\a"
}

# hook functions
function precmd () {
    xtitle "$(print -P zsh '(%~)'| sed -E 's:/://:g; s:(/[\.]*[^/])[^/]*/:\1:g; s://:/:g')"
}
function preexec () {
    xtitle "$1 $(print -P '(%~)' | sed -E 's:/://:g; s:(/[\.]*[^/])[^/]*/:\1:g; s://:/:g')"
}

# system-specific options file, home manager environment variables
source ~/.config/zsh/local.zsh 2> /dev/null
source '/etc/profiles/per-user/$USER/etc/profile.d/hm-session-vars.sh' 2> /dev/null
source "$HOME/.nix-profile/etc/profile.d/hm-session-vars.sh" 2> /dev/null
eval "$(zoxide init zsh 2> /dev/null)"

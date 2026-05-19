# completion
autoload -Uz compinit && compinit -d ~/.cache/zsh/zcompdump
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
HISTFILE=~/.cache/zsh/zsh_history
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
alias gl='git log --oneline --graph'
alias dev='nix develop -c zsh'
alias pfetch='PF_INFO="ascii title os shell wm editor palette" pfetch'
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

# general settings
unsetopt beep
bindkey -v
setopt autocd

bindkey -M vicmd 'K' history-beginning-search-backward
bindkey -M vicmd 'J' history-beginning-search-forward

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
zstyle ':vcs_info:*' actionformats '  %b%u%c %F{red}(%a %m)'
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

. "$HOME/.local/bin/env"

# colours, set default if $THEME file not found
accent_primary=blue
accent_secondary=magenta
accent_tertiary=magenta
source ~/.config/zsh/themes/$THEME.zsh 2> /dev/null


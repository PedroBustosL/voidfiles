# .bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias hc='herbstclient'
complete -F _herbstclient_complete -o nospace hc

source $HOME/.config/herbstluftwm/herbstclient-completion.bash
export PATH=$HOME/scripts:$PATH
PS1='[\u@\h \W]\$ '
setxkbmap latam

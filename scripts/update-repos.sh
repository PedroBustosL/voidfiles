#!/bin/bash

if [ -d $HOME/voidfiles ];
then
	cd $HOME/voidfiles || exit
	git pull > /tmp/git_pull.log &
else
	echo "No se encuentra directorio "$HOME/voidfiles" " > /tmp/git_pull.log
fi
if [ -d $HOME/soportetimundo ];
then
	cd $HOME/soportetimundo || exit 
	git pull > /tmp/git_pull.log &
else
	echo "No se encuentra directorio "$HOME/soportetimundo" " > /tmp/git_pull.log
fi

#!/bin/bash

if [[ -d $HOME/voidfiles ]];
then
	cd $HOME/voidfiles || git pull
elseif [[ -d $HOME/soportetimundo ]]
then
	cd $HOME/soportetimundo || git pull
else
	echo "No se encuentra directorio" > /tmp/git_pull.log

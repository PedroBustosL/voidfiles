#!/bin/bash

########## PKG MAGNAMENT ########
sudo xbps-install -Suv
PACKAGES=$HOME/voidfiles/pkgs.txt

for PKG in $PACKAGES
do
	sudo xpbs-install -y $PKG
done

########## CONFIG MAGNAMENT #############################
cp $HOME/voidfiles/herbswm/* $HOME/.config/herbstluftwm/
sudo cp $HOME/voidfiles/scripts/scratchpad /usr/local/bin/
sudo cmod +x /usr/local/bin/scratchpad


########## SETUP VOID PKGS ####################
mkdir $HOME/pkgs
https://github.com/void-linux/void-packages.git

########## SETUP LIGHTDM ################
cp $HOME/voidfiles/lightdm/* /etc/lightdm/
sed -i "s/PLACEHOLDER/$(whoami)/" /etc/lightdm/lightdm-mini-greeter.conf

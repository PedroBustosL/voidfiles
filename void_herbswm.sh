#!/bin/bash

########## PKG MAGNAMENT ########
sudo xbps-install -Suv
PACKAGES=$(cat $HOME/voidfiles/pkgs.txt)

for PKG in $PACKAGES
do
	sudo xbps-install -y $PKG
done

########## START SERVICES #############
sudo ln -s /etc/sv/lightdm /var/service
sudo ln -s /etc/sv/elogind /var/service
sudo ln -s /etc/sv/dbus /var/service
sudo sv up lightdm
sudo sv up elogind 
sudo sv up dbus 

########## CONFIG MAGNAMENT #############################
mkdir .config .config/herbstluftwm
cp -r $HOME/voidfiles/herbswm/* $HOME/.config/herbstluftwm/
sudo cp $HOME/voidfiles/scripts/scratchpad /usr/local/bin/
sudo chmod +x /usr/local/bin/scratchpad
cp $HOME/voidfiles/bashrc/.bashrc $HOME/.bashrc
source $HOME/.bashrc


########## SETUP VOID PKGS ####################
mkdir $HOME/pkgs
git clone https://github.com/void-linux/void-packages.git $HOME/pkgs

########## SETUP LIGHTDM ####################################################
sudo cp $HOME/voidfiles/lightdm/* /etc/lightdm/
sudo sed -i "s/PLACEHOLDER/$(whoami)/" /etc/lightdm/lightdm-mini-greeter.conf

########## CUSTOM SCRIPTS ####### 
mkdir $HOME/scripts
cp $HOME/voidfiles/scripts/* $HOME/scripts

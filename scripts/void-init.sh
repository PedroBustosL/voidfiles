#!/usr/bin/env bash

cd $HOME
sudo xbps-install -Suvy

sudo xbps-install -vy void-repo-nonfree curl wget xz unzip zip gptfdisk xtools mtools mlocate ntfs-3g fuse-exfat bash-completion linux-headers gtksourceview4 ffmpeg mesa-vdpau mesa-vaapi
sudo xbps-install -vy autoconf automake bison m4 make libtool flex meson ninja optipng sassc zig base-devel pam-devel libxcb-devel

sudo xbps-install -vy xorg i3
git clone https://codeberg.org/AnErrupTion/ly.gitcd ly
zig build
zig build installrunit
sudo unlink /var/service/agetty-tty2
sudo ln -s /etc/sv/ly /var/service/
cd $HOME

sudo xbps-install -vy xdg-desktop-portal xdg-desktop-portal-gtk xdg-user-dirs xdg-user-dirs-gtk xdg-utils

sudo xbps-install -vy dbus elogind

sudo ln -s /etc/sv/dbus /var/service/
sudo ln -s /etc/sv/elogind /var/service/

sudo xbps-install -vy NetworkManager
sudo unlink /var/service/dhcpcd
sudo ln -s /etc/sv/NetworkManager /var/service/

sudo xbps-install -vy pipewire wireplumber
sudo mkdir -p /etc/pipewire/pipewire.conf.d
sudo ln -s /usr/share/examples/wireplumber/10-wireplumber.conf /etc/pipewire/pipewire.conf.d/
sudo ln -s /usr/share/examples/pipewire/20-pipewire-pulse.conf /etc/pipewire/pipewire.conf.d/

sudo xbps-install -vy tlp tlp-rdw powertop
sudo ln -sv /etc/sv/tlp /var/service

sudo xbps-install -vy librewolf mpv

sudo xbps-install -vy socklog-void
sudo ln -s /etc/sv/socklog-unix /var/service/
sudo ln -s /etc/sv/nanoklogd /var/service/

git clone https://github.com/madand/runit-services
cd runit-services
sudo mv psd /etc/sv/
sudo ln -s /etc/sv/psd /var/service/
sudo chmod +x etc/sv/psd/*

git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install

sudo xbps-install -S zoxide ripgrep dust flatpak thunar
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

sudo xbps-install -vy intel-ucode 
linuxKernel=$(xbps-query -l | grep linux- | awk 'NR==1 {print $2}')
sudo xbps-reconfigure -f $linuxKernel



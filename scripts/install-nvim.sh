#!/usr/bin/env bash

git clone --depth 1 https://github.com/neovim/neovim.git ~/neovim
cd neovim
make CMAKE_BUILD_TYPE=RelWithDebInfo
sudo make install

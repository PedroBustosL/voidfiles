# Touchpad en gnome

- Copiar archivo 40-libinput.conf a /etc/X11/xorg.conf.d/

# Agregar Nvidia a kernel void

## Kernel

- editar /etc/default/grub y agregar nvidia-drm,modeset=1 al parametro GRUB_CMDLINE_LINUX_DEFAULT
- sudo update-grub

## Dracut

- nuevo archivo /etc/dracut.conf.d/nvidia.conf
- incluir addd_dicers+="nvidia nvidia-drm nvidia-modeset nvidia-uvm"
- sudo dracut -f

## Gnome

- crear carpeta (si no existe) /etc/udev/rules.d/
- enviar a null la regla que bota wayland en nvidia sudo ln -s /dev/null /etc/udev/rules.d/61-gdm.rules

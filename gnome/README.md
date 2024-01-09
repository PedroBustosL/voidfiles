# Touchpad en gnome

- Copiar archivo 40-libinput.conf a /etc/X11/xorg.conf.d/

# Agregar Nvidia a kernel void

## Kernel

- edditar /etc/default/grub y agregar nvidia-drm,modeset=1 al parametro GRUB_CMDLINE_LINUX_DEFAULT
- sudo update-grub

## Dracut

- nuevo archivo /etc/dracut.conf.d/nvidia.conf
- incluir addd_dicers+="nvidia nvidia-drm nvidia-modeset nvidia-uvm"
- sudo dracut -f

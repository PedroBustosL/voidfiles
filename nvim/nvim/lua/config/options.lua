-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here

if jit.os == "Windows" then
  vim.o.shell = "pwsh.exe"
  vim.o.shellxquote = ""
  vim.o.shellcmdflag = "-NoLogo -NoProfile -ExecutionPolicy RemoteSigned -Command "
  vim.o.shellquote = ""
  vim.o.shellpipe = "| Out-File -Encoding UTF8 %s"
  vim.o.shellredir = "| Out-File -Encoding UTF8 %s"

  vim.api.nvim_create_user_command(
    "Exec",
    "set splitbelow | new | set ft=ps1 | read !pwsh.exe #",
    { desc = "Execute current ps1 file" }
  )
end
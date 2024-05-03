return {
--   -- Treesitter is a new parser generator tool that we can
--   -- use in Neovim to power faster and more accurate
--   -- syntax highlighting.
--
--   -- Show context of the current function
--   {
--     "nvim-treesitter/nvim-treesitter-context",
--     event = "LazyFile",
--     enabled = true,
--     opts = { mode = "cursor", max_lines = 3 },
--     keys = {
--       {
--         "<leader>ut",
--         function()
--           local Util = require("lazyvim.util")
--           local tsc = require("treesitter-context")
--           tsc.toggle()
--           if Util.inject.get_upvalue(tsc.toggle, "enabled") then
--             Util.info("Enabled Treesitter Context", { title = "Option" })
--           else
--             Util.warn("Disabled Treesitter Context", { title = "Option" })
--           end
--         end,
--         desc = "Toggle Treesitter Context",
--       },
--     },
--   },
--
--   -- Automatically add closing tags for HTML and JSX
--   {
--     "windwp/nvim-ts-autotag",
--     event = "LazyFile",
--     opts = {},
--   },
}
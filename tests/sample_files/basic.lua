local M = {}

M.foo = "Hello, world"

some_num = 1
M.another_num = 2

M.some_table = { "a", "b", "c" }

function M.add(a, b)
    return a + b
end

return M

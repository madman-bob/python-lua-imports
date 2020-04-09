# lua_imports

Import Lua modules directly from within Python.

## Basic Usage

Once `lua_imports.lua_importer` has been registered, write an `import` statement in your Python code, referring to your Lua module.

### Example

`foo.lua`

```lua
return {
    say_hello = function(person)
        print("Hello, " .. person)
    end
}
```

`bar.py`

```python
import foo

foo.say_hello("World")
```

## Registration

`lua_importer` may be registered within Python code:

```python
from lua_imports import lua_importer

lua_importer.register()
```

(Note that this must come *before* any Lua imports)

Alternatively, to register `lua_importer` environment-wide, create a `lua-imports.pth` file in your environment's `site-packages` folder with the following contents:

```pth
import lua_imports; lua_imports.lua_importer.register()
```

## Caveats

This module wraps [Lupa](https://github.com/scoder/lupa), and so comes with all the same caveats about Lua vs. Python data types.
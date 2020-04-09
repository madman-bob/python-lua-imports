from dataclasses import dataclass

from custom_imports import FileModuleExtensionFinder, Importer, SimpleLoader
from lupa import LuaRuntime
from more_properties import cached_static_property

__all__ = ["lua_importer"]


@dataclass(frozen=True)
class LuaModuleFinder(FileModuleExtensionFinder):
    extension: str = "lua"

    def find_module_locator(self, fullname, path, target):
        path = super().find_module_locator(fullname, path, target)

        if path is not None:
            return fullname


@dataclass
class LuaModule:
    runtime = cached_static_property(LuaRuntime)

    lua_module: object = None

    def load_module(self, module_name):
        self.lua_module = self.runtime.require(module_name)

    def __getattr__(self, item):
        return getattr(self.lua_module, item)


lua_importer = Importer(
    finder=LuaModuleFinder(),
    loader=SimpleLoader(module_type=LuaModule, load_module=LuaModule.load_module),
)

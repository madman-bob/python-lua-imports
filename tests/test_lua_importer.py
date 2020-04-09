from unittest import TestCase


class TestLuaImporter(TestCase):
    def test_lua_importer_basic(self):
        from tests.sample_files import basic

        self.assertEqual("Hello, world", basic.foo)
        self.assertEqual(None, basic.some_num)
        self.assertEqual(2, basic.another_num)

        self.assertEqual(["a", "b", "c"], list(basic.some_table.values()))

        self.assertEqual(3, basic.add(1, 2))

    def test_lua_importer_internal_imports(self):
        from tests.sample_files import internal_imports

        self.assertEqual(3, internal_imports.result)

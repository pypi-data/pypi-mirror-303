import unittest
from source_translator import SourceCode


class TestCase(unittest.TestCase):
    def assert_code(self, py, translated, translator=None):
        if translator is None:
            translator = self.translator

        out = translator.convert(SourceCode(py))
        self.assertEqual(out, translated)

    def assert_expression(self, py, translated, translator=None):
        if translator is None:
            translator = self.translator

        out = translator.expression_to_string(SourceCode(py).ast.body[0].value, False)
        self.assertEqual(out, translated)

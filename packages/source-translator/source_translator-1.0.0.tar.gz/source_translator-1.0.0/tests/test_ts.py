from .test_base import TestCase
from inspect import cleandoc
from source_translator.langs.ts import TypeScriptTranslator
from source_translator import c_like


class TestTs(TestCase):
    translator = TypeScriptTranslator(True, c_like.AllmanStyle())

    def test_literals(self):
        self.assert_expression("1", "1")
        self.assert_expression("1.5", "1.5")
        self.assert_expression("True", "true")
        self.assert_expression("False", "false")
        self.assert_expression("None", "null")
        self.assert_expression('"Hello"', '"Hello"')
        self.assert_expression('"Hello\\nWorld"', '"Hello\\nWorld"')

    def test_binop(self):
        self.assert_expression("1 + 2", "1 + 2")
        self.assert_expression("1 // 2", "1 / 2")
        self.assert_expression("1 or 2", "1 || 2")

    def test_comp(self):
        self.assert_expression("1 < 2", "1 < 2")
        self.assert_expression("1 < x < 2", "(1 < x && x < 2)")

    def test_precendence(self):
        self.assert_expression("1 + 2 * 3", "1 + 2 * 3")
        self.assert_expression("(1 + 2) * 3", "(1 + 2) * 3")

    def test_func_call(self):
        self.assert_expression("foo()", "foo()")
        self.assert_expression("foo(bar)", "foo(bar)")
        self.assert_expression("foo(1, 2)", "foo(1, 2)")
        self.assert_expression("foo(*bar)", "foo(...bar)")
        self.assert_expression("Foo()", "new Foo()")

    def test_attr(self):
        self.assert_expression("foo.bar.baz", "foo.bar.baz")
        self.assert_expression("math.cos", "Math.cos")
        self.assert_expression("math.pi", "Math.PI")

    def test_subscript(self):
        self.assert_expression("arr[1]", "arr[1]")
        self.assert_expression("arr[1:2]", "arr.slice(1, 2)")
        self.assert_expression("arr[1:2:3]", "arr.slice(1, 2, 3)")
        self.assert_expression("arr[1::3]", "arr.slice(1, undefined, 3)")
        self.assert_expression("arr[:2:3]", "arr.slice(undefined, 2, 3)")

    def test_expr_statement(self):
        self.assert_code("foo()", "foo();\n")

    def test_assign(self):
        self.assert_code("x = 1", "x = 1;\n")
        self.assert_code("x = y = 1", "x = y = 1;\n")
        self.assert_code("x += 1", "x += 1;\n")

    def test_expr_if(self):
        self.assert_expression("1 if 2 else 3", "2 ? 1 : 3")

    def test_if(self):
        self.assert_code(cleandoc("""
            if True:
                foo()
        """), cleandoc("""
            if ( true )
            {
                foo();
            }
        """) + "\n")
        self.assert_code(cleandoc("""
            if True:
                foo()
            else:
                bar()
        """), cleandoc("""
            if ( true )
            {
                foo();
            }
            else
            {
                bar();
            }
        """) + "\n")
        self.assert_code(cleandoc("""
            if 1:
                foo()
            elif 2:
                bar()
            else:
                baz()
        """), cleandoc("""
            if ( 1 )
            {
                foo();
            }
            else if ( 2 )
            {
                bar();
            }
            else
            {
                baz();
            }
        """) + "\n")

    def test_simple_branch(self):
        self.assert_code("break", "break;\n")
        self.assert_code("continue", "continue;\n")

    def test_return(self):
        self.assert_code("return", "return;\n")
        self.assert_code("return 5", "return 5;\n")

    def test_while(self):
        self.assert_code(cleandoc("""
            while True:
                foo()
        """), cleandoc("""
            while ( true )
            {
                foo();
            }
        """) + "\n")

    def test_switch(self):
        self.assert_code(cleandoc("""
            match x:
                case 1:
                    foo()
                case _:
                    bar()
        """), cleandoc("""
            switch ( x )
            {
                case 1:
                    foo();
                    break;
                default:
                    bar();
                    break;
            }
        """) + "\n")

    def test_func(self):
        self.assert_code(cleandoc("""
            def foo():
                print()
        """), cleandoc("""
            function foo()
            {
                print();
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            def foo(bar: int):
                print(bar)
        """), cleandoc("""
            function foo(bar: number)
            {
                print(bar);
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            def foo(bar):
                print(bar)
        """), cleandoc("""
            function foo(bar)
            {
                print(bar);
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            def foo(bar: int, baz: float = 2):
                print(bar)
        """), cleandoc("""
            function foo(bar: number, baz: number = 2)
            {
                print(bar);
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            def foo(bar: int) -> int:
                print(bar)
        """), cleandoc("""
            function foo(bar: number): number
            {
                print(bar);
            }
        """) + "\n")

    def test_declare(self):
        self.assert_code("x: int", "let x: number;\n")
        self.assert_code("x: int = 2", "let x: number = 2;\n")

    def test_class(self):
        self.assert_code(cleandoc("""
            class Foo:
                def foo():
                    return
        """), cleandoc("""
            class Foo
            {
                foo()
                {
                    return;
                }
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            class Foo:
                def foo(self):
                    return self
        """), cleandoc("""
            class Foo
            {
                foo()
                {
                    return this;
                }
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            class Foo:
                def foo(self, a: int):
                    return self
        """), cleandoc("""
            class Foo
            {
                foo(a: number)
                {
                    return this;
                }
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            class Foo:
                def __init__(self, a: int):
                    self.a = a
        """), cleandoc("""
            class Foo
            {
                constructor(a: number)
                {
                    this.a = a;
                }
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            class Foo:
                def __str__(self) -> str:
                    return ""
        """), cleandoc("""
            class Foo
            {
                toString(): string
                {
                    return "";
                }
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            class Foo:
                x: number = 1
                y: number
        """), cleandoc("""
            class Foo
            {
                static x: number = 1;
                static y: number;
            }
        """) + "\n")

    def test_property(self):
        self.assert_code(cleandoc("""
            class Foo:
                @property
                def foo():
                    return 2
        """), cleandoc("""
            class Foo
            {
                get foo()
                {
                    return 2;
                }
            }
        """) + "\n")

    def test_foreach(self):
        self.assert_code(cleandoc("""
            for i in a:
                print(i)
        """), cleandoc("""
            for ( let i of a )
            {
                print(i);
            }
        """) + "\n")

    def test_for_iter(self):
        self.assert_code(cleandoc("""
            for i in range(10):
                print(i)
        """), cleandoc("""
            for ( let i: number = 0; i < 10; i++ )
            {
                print(i);
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            for i in range(1, 10):
                print(i)
        """), cleandoc("""
            for ( let i: number = 1; i < 10; i++ )
            {
                print(i);
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            for i in range(1, 10, 2):
                print(i)
        """), cleandoc("""
            for ( let i: number = 1; i < 10; i += 2 )
            {
                print(i);
            }
        """) + "\n")

    def test_type_alias(self):
        self.assert_code("type Vector = list[float]", "type Vector = Array[number];\n")

    def test_type_names(self):
        self.assert_expression("int", "Number")
        self.assert_expression("float", "Number")
        self.assert_expression("str", "String")
        self.assert_expression("dict", "Map")
        self.assert_expression("set", "Set")
        self.assert_expression("list", "Array")
        self.assert_expression("tuple", "Array")
        self.assert_expression("my_var", "myVar")
        self.assert_expression("max", "Math.max")

    def test_container_literals(self):
        self.assert_expression("[1, 2, 3]", "[1, 2, 3]")
        self.assert_expression("(1, 2, 3)", "[1, 2, 3]")
        self.assert_expression("{1, 2, 3}", "new Set([1, 2, 3])")
        self.assert_expression("{1: 2, 3: 4}", "{1: 2, 3: 4}")

    def test_delete(self):
        self.assert_code("del foo", "delete foo;\n")

    def test_names(self):
        self.assert_expression("foo", "foo")
        self.assert_expression("is_", "is")
        self.assert_expression("this", "this_")

    def test_async(self):
        self.assert_code(cleandoc("""
            async def foo():
                await print()
        """), cleandoc("""
            async function foo()
            {
                await print();
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            async for i in x:
                pass
        """), cleandoc("""
            for await ( let i of x )
            {
            }
        """) + "\n")

    def test_import(self):
        self.assert_code("import foo", "import * as foo from 'foo';\n")
        self.assert_code("import foo, bar", "import * as foo from 'foo';\nimport * as bar from 'bar';\n")
        self.assert_code("import foo as bar", "import * as bar from 'foo';\n")
        self.assert_code("from foo import bar", "import bar from 'foo';\n")
        self.assert_code("from foo import bar as baz", "import {bar as baz} from 'foo';\n")
        self.assert_code("from foo import foo, bar", "import {foo, bar} from 'foo';\n")

    def test_plain_js(self):
        translator = TypeScriptTranslator(False, c_like.AllmanStyle())
        self.assert_code(cleandoc("""
            def foo(a: int) -> int:
                b: int = a
        """), cleandoc("""
            function foo(a)
            {
                let b = a;
            }
        """) + "\n", translator)

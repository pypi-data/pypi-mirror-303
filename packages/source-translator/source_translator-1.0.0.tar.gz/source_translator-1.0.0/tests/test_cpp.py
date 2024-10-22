from .test_base import TestCase
from inspect import cleandoc
from source_translator.langs.cpp import CppTranslator
from source_translator import c_like


class TestCpp(TestCase):
    translator = CppTranslator()

    def test_literals(self):
        self.assert_expression("1", "1")
        self.assert_expression("1.5", "1.5")
        self.assert_expression("True", "true")
        self.assert_expression("False", "false")
        self.assert_expression("None", "nullptr")
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

    def test_attr(self):
        self.assert_expression("foo.bar.baz", "foo.bar.baz")
        self.assert_expression("math.cos", "std::cos")
        self.assert_expression("math.pi", "std::numbers::pi")

    def test_subscript(self):
        self.assert_expression("arr[1]", "arr[1]")

    def test_expr_statement(self):
        self.assert_code("foo()", "foo();\n")

    def test_assign(self):
        self.assert_code("x = 1", "x = 1;\n")
        self.assert_code("x = y = 1", "x = y = 1;\n")
        self.assert_code("x += 1", "x += 1;\n")

    def test_expr_if(self):
        self.assert_expression("1 if 2 else 3", "2 ? 1 : 3")

    def test_style_newlines(self):
        self.assert_code(cleandoc("""
            if True:

                foo()

            else:

                bar()
        """), cleandoc("""
            if ( true ) {

                foo();

            } else {

                bar();
            }
        """) + "\n", CppTranslator(c_like.KandRStyle()))

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
        """) + "\n", CppTranslator(c_like.AllmanStyle()))

    def test_style(self):
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
        """) + "\n", CppTranslator(c_like.AllmanStyle()))

        self.assert_code(cleandoc("""
            if True:
                foo()
            else:
                bar()
        """), cleandoc("""
            if ( true ) {
                foo();
            } else {
                bar();
            }
        """) + "\n", CppTranslator(c_like.KandRStyle()))

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
        """) + "\n", CppTranslator(c_like.WhitesmithsStyle()))

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
        """) + "\n", CppTranslator(c_like.GnuStyle()))

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
            void foo()
            {
                print();
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            def foo(bar: int):
                print(bar)
        """), cleandoc("""
            void foo(int bar)
            {
                print(bar);
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            def foo(bar: int, baz: float = 2):
                print(bar)
        """), cleandoc("""
            void foo(int bar, float baz = 2)
            {
                print(bar);
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            def foo(bar: int) -> int:
                print(bar)
        """), cleandoc("""
            int foo(int bar)
            {
                print(bar);
            }
        """) + "\n")

    def test_declare(self):
        self.assert_code("x: int", "int x;\n")
        self.assert_code("x: int = 2", "int x = 2;\n")
        self.assert_code("x: int = int(2)", "int x = 2;\n")
        self.assert_code("x: Foo = Foo(2)", "Foo x(2);\n")

    def test_class(self):
        self.assert_code(cleandoc("""
            class Foo:
                def foo():
                    return
        """), cleandoc("""
            class Foo
            {
                void foo()
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
                void foo()
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
                void foo(int a)
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
                Foo(int a)
                {
                    this->a = a;
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
                operator std::string() const
                {
                    return "";
                }
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            class Foo:
                x: int = 1
                y: int
        """), cleandoc("""
            class Foo
            {
                static int x;
                static int y;
            }
        """) + "\n")

    def test_foreach(self):
        self.assert_code(cleandoc("""
            for i in a:
                print(i)
        """), cleandoc("""
            for ( const auto& i : a )
            {
                print(i);
            }
        """) + "\n")

    def test_for_iter(self):
        self.assert_code(cleandoc("""
            for i in range(10):
                print(i)
        """), cleandoc("""
            for ( int i = 0; i < 10; i++ )
            {
                print(i);
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            for i in range(1, 10):
                print(i)
        """), cleandoc("""
            for ( int i = 1; i < 10; i++ )
            {
                print(i);
            }
        """) + "\n")

        self.assert_code(cleandoc("""
            for i in range(1, 10, 2):
                print(i)
        """), cleandoc("""
            for ( int i = 1; i < 10; i += 2 )
            {
                print(i);
            }
        """) + "\n")

    def test_type_alias(self):
        self.assert_code("type Vector = list[float]", "using Vector = std::vector<float>;\n")

    def test_type_names(self):
        self.assert_expression("int", "int")
        self.assert_expression("float", "float")
        self.assert_expression("str", "std::string")
        self.assert_expression("dict", "std::unordered_map")
        self.assert_expression("set", "std::set")
        self.assert_expression("list", "std::vector")
        self.assert_expression("tuple", "std::tuple")

    def test_container_literals(self):
        self.assert_expression("[1, 2, 3]", "{1, 2, 3}")
        self.assert_expression("(1, 2, 3)", "{1, 2, 3}")
        self.assert_expression("{1, 2, 3}", "{1, 2, 3}")
        self.assert_expression("{1: 2, 3: 4}", "{{1, 2}, {3, 4}}")

    def test_delete(self):
        self.assert_code("del foo", "delete foo;\n")

    def test_names(self):
        self.assert_expression("foo", "foo")
        self.assert_expression("is_", "is")
        self.assert_expression("this", "this_")

    def test_line_commens(self):
        self.assert_code(cleandoc("""
            # a
            if True:
                # b
                foo()
            # c
            else:
                # d
                bar()
        """), cleandoc("""
            // a
            if ( true )
            {
                // b
                foo();
            }
            // c
            else
            {
                // d
                bar();
            }
        """) + "\n")

    def test_multiline_comments(self):
        self.assert_code(cleandoc("""
            'comment'

            '''
            This is
            a
            comment
            '''
            ''
            foo()
            bar() # comment?
        """), cleandoc("""
            // comment

            /*
            This is
            a
            comment
            */

            foo();
            bar(); // comment?
        """) + "\n")

    def test_docs_comment(self):
        self.assert_code(cleandoc("""
            def foo():
                '''
                This is
                a
                comment
                '''
                return
        """), cleandoc("""
            /**
             * This is
             * a
             * comment
             */
            void foo()
            {
                return;
            }
        """) + "\n")

    def test_pass(self):
        self.assert_code(cleandoc("""
            def foo():
                pass
        """), cleandoc("""
            void foo()
            {
            }
        """) + "\n")

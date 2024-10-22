import json
from .python_source import IndentationStyle, AstTranslator, IndentationManager, build_precedence_map


class AllmanStyle(IndentationStyle):
    def __init__(self, offset=0, *a, **kw):
        super().__init__(*a, **kw)
        self.offset = offset

    def begin_block(self, translator: AstTranslator, header: str):
        translator.push_code(header)
        translator.push_code("{", False, self.offset)
        translator.comments.skip_newline()

    def mid_block(self, translator: AstTranslator, header: str):
        translator.comments.skip_newline()
        translator.push_code("}", False, self.offset)
        translator.comments.skip_newline()
        translator.push_code(header, True)
        translator.push_code("{", False, self.offset)
        translator.comments.skip_newline()

    def end_block(self, translator: AstTranslator):
        translator.push_code("}", True, self.offset)


class KandRStyle(IndentationStyle):
    def begin_block(self, translator: AstTranslator, header: str):
        translator.push_code(header + " {")

    def mid_block(self, translator: AstTranslator, header: str):
        translator.push_code("} " + header + " {")

    def end_block(self, translator: AstTranslator):
        translator.push_code("}")


class WhitesmithsStyle(AllmanStyle):
    def __init__(self, *a, **kw):
        super().__init__(1, *a, **kw)


class GnuStyle(AllmanStyle):
    def __init__(self, *a, **kw):
        super().__init__(0.5, *a, **kw)


class CLike(AstTranslator):
    ops = {
        "Eq": "==",
        "NotEq": "!=",
        "Lt": "<",
        "LtE": "<=",
        "Gt": ">",
        "GtE": ">=",
        "Is": "==",
        "IsNot": "!=",
        "In": " <in>",
        "NotIn": "<not in>",
        "Add": "+",
        "Sub": "-",
        "Mult": "*",
        "MatMult": "*",
        "Div": "/",
        "Mod": "%",
        "LShift": "<<",
        "RShift": ">>",
        "BitOr": "|",
        "BitXor": "^",
        "BitAnd": "&",
        "FloorDiv": "/",
        "Pow": "**",
        "Invert": "~",
        "Not": "!",
        "UAdd": "+",
        "USub": "-",
        "And": "&&",
        "Or": "||",
    }
    operator_precedence = build_precedence_map(
        ["::"],
        [".", "->", "++", "--", "?."],
        [".*", "->*"],
        ["***"],
        ["*", "/", "%"],
        ["+", "-"],
        ["<<", ">>", ">>>"],
        ["<=>"],
        ["<", "<=", ">", ">="],
        ["==", "!=", "===", "!=="],
        ["&"],
        ["^"],
        ["|"],
        ["&&"],
        ["||", "??"],
        ["=", "if", "=>", "..."],
        [","],
    )
    keywords = []

    def __init__(self, indent_style=AllmanStyle()):
        super().__init__(indent_style)

    def begin_block(self, header):
        self.indent_style.begin_block(self, header)

    def mid_block(self, header):
        self.indent_style.mid_block(self, header)

    def styled_name(self, id):
        id = id.strip("_")
        if id in self.keywords:
            return id + "_"
        return id

    def begin_class(self, obj):
        self.begin_block("class %s" % obj)

    def end_block(self):
        self.indent_style.end_block(self)

    def assign(self, targets, value):
        code = " = ".join(targets)
        code += " = %s;" % value
        self.push_code(code)

    def assign_op(self, target, op, value):
        self.push_code("%s %s= %s;" % (target, op, value))

    def begin_if(self, expr):
        self.begin_block("if ( %s )" % expr)

    def begin_elif(self, expr):
        self.mid_block("else if ( %s )" % expr)

    def begin_else(self):
        self.mid_block("else")

    def begin_while(self, cond):
        self.begin_block("while ( %s )" % cond)

    def basic_statement(self, statement):
        self.push_code(statement + ";")

    def return_statement(self, value):
        if value is None:
            self.push_code("return;")
        else:
            self.push_code("return %s;" % value)

    def begin_switch(self, expr):
        self.begin_block("switch ( %s )" % expr)

    def begin_switch_case(self, pattern):
        if pattern is None:
            self.push_code("default:")
        else:
            self.push_code("case %s:" % pattern)

    def end_switch_case(self):
        self.push_code("break;")

    def expr_func(self, name, args):
        code = name
        code += "("
        code += ", ".join(args)
        code += ")"
        return code

    def expr_attribute(self, object, member):
        return "%s.%s" % (object, self.styled_name(member))

    def expr_compare(self, value, annotation):
        all = []
        left = self.expression_to_string(value.left, annotation)
        for cmp, op in zip(value.comparators, value.ops):
            right = self.expression_to_string(cmp, annotation)
            all.append("%s %s %s" % (left, self.expression_to_string(op, annotation), right))
            left = right
        if len(all) == 1:
            return all[0]
        return "(%s)" % " && ".join(all)

    def expr_starred(self, value):
        return "...%s" % value

    def format_doc_comment(self, comment):
        self.push_code("/**")
        for line in comment:
            self.push_code(" * " + line)
        self.push_code(" */")

    def format_comment(self, value):
        if len(value) > 1:
            self.push_code("/*")
            for line in value:
                self.push_code(line)
            self.push_code("*/")
        elif value:
            self.push_code("// " + value[0])
        else:
            self.push_code("")

    def expression_statement(self, v):
        self.push_code(v + ";")

    def convert_line_comment(self, comment):
        return "// " + comment

    def expr_if(self, *args):
        return "%s ? %s : %s" % args

    def expr_subscript(self, value, index):
        return "%s[%s]" % (value, index)

    def function_body(self, decl, body):
        self.begin_block(decl)
        with IndentationManager(self, None):
            self.convert_ast(body)
        self.end_block()

    def convert_constant(self, value, annotation):
        return json.dumps(value)

    def convert_name(self, name, annotation):
        if self.class_name and name == "self":
            return "this"
        return self.styled_name(name)

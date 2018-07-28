import ast


terminal = {
    # Literals
    ast.Num,
    ast.Str,
    ast.Bytes,
    ast.NameConstant,
    ast.Ellipsis,

    # Variables
    ast.Name,
}


scoped = {
    # Comprehension
    ast.comprehension,

    # Control flow
    ast.If,
    ast.For,
    ast.While,
    ast.Try,
    ast.ExceptHandler,
    ast.With,

    # Function/Class definitions
    ast.FunctionDef,
    ast.Lambda,
    ast.ClassDef,

    # Async
    ast.AsyncFunctionDef,
    ast.AsyncFor,
    ast.AsyncWith,
}


color = {
    ast.Num: '456355',
    ast.Str: 'FCD16B',
    ast.FormattedValue: 'D3DDDC',
    ast.JoinedStr: 'C6B19D',

    ast.Bytes: '1DACE8',
    ast.List: '1C366B',
    ast.Tuple: 'F24D29',
    ast.Set: 'E5C4A1',
    ast.Dict: 'C4CFD0',

    ast.Ellipsis: 'AEA8A8',
    ast.NamedConstant: 'AEA8A8',

    ast.Name: 'CB9E23',
    ast.Starred: 'CB9E23',

    ast.UnaryOp: 'E6A2C5',
    ast.BinOp: 'D8A49B',
    ast.BoolOp: 'C7CEF6',
    ast.Compare: '7496D2',

    ast.Call: '957A6D',
    ast.keyword: '',
    ast.IfExp: '',
    ast.Attribute: '',

    ast.Subscript: 'AC6E49',
    ast.Index: 'AC6E49',
    ast.Slice: 'AC6E49',
    ast.ExtSlice: 'AC6E49',

    ast.ListComp: 'DBB165',
    ast.SetComp: 'DEB18B',
    ast.GeneratorExp: '2E604A',
    ast.DictComp: '27223C',
    ast.comprehension: 'D1362F',

    ast.Assign: '9A872D',
    ast.AnnAssign: '9A872D',
    ast.AugAssign: '9A872D',

    ast.Print: 'F5CDB6',
    ast.Raise: 'F5CDB6',
    ast.Assert: 'F5CDB6',
    ast.Delete: 'F5CDB6',
    ast.Pass: 'F5CDB6',

    ast.Import: 'F7B0AA',
    ast.ImportFrom: 'F7B0AA',
    ast.alias: 'F7B0AA',

    ast.If: 'FDDDA4',
    ast.For: '76A08A',
    ast.While: '76A08A',

    ast.Break: 'F5CDB6',
    ast.Continue: 'F5CDB6',

    ast.Try: 'B62A3D',
    ast.ExceptHandler: 'B62A3D',
    ast.With: 'EDCB64',
    ast.withitem: 'EDCB64',

    ast.FunctionDef: 'B5966D',
    ast.Lambda: 'DAECED',
    ast.arguments: 'CECD7B',
    ast.arg: 'CECD7B',

    ast.Return: 'F8DF4F',
    ast.Yield: 'F8DF4F',
    ast.YieldFrom: 'F8DF4F',
    ast.Global: 'F8DF4F',
    ast.Nonlocal: 'F8DF4F',

    ast.ClassDef: 'A35E60',

    ast.AsyncFunctionDef: 'CC8B3C',
    ast.Await: '541F12',
    ast.AsyncFor: 'E8D2B9',
    ast.AsyncWith: 'E8D2B9',
}


fields = {
    ast.Num: ['n'],
    ast.Str: ['s'],
    ast.FormattedValue: ['value'],
    ast.JoinedStr: ['values'],

    ast.Bytes: ['s'],
    ast.List: ['elts'],
    ast.Tuple: ['elts'],
    ast.Set: ['elts'],
    ast.Dict: ['keys'],

    ast.Ellipsis: [],

    ast.NamedConstant: ['value'],

    ast.Name: ['id'],
    ast.Starred: ['value'],

    ast.UnaryOp: ['op'],
    ast.BinOp: ['op'],
    ast.BoolOp: ['op'],
    ast.Compare: ['op'],

    ast.Call: ['func', 'args', 'keywords'],
    ast.keyword: ['arg', 'value'],
    ast.IfExp: ['test', 'body', 'orelse'],
    ast.Attribute: ['value', 'attr'],

    ast.Subscript: ['value'],
    ast.Index: ['value'],
    ast.Slice: ['lower', 'upper'],
    ast.ExtSlice: ['dims'],

    ast.ListComp: ['elt', 'generators'],
    ast.SetComp: ['elt', 'generators'],
    ast.GeneratorExp: ['elt', 'generators'],
    ast.DictComp: ['elt', 'generators'],
    ast.comprehension: ['target', 'iter', 'ifs'],

    ast.Assign: ['targets', 'value'],
    ast.AnnAssign: ['target', 'annotation'],
    ast.AugAssign: ['target', 'op', 'value'],

    ast.Print: ['values'],
    ast.Assert: ['test'],
    ast.Delete: ['targets'],

    ast.Import: ['names'],
    ast.ImportFrom: ['module', 'names'],
    ast.alias: ['name'],

    ast.If: ['test', 'body', 'orelse'],
    ast.For: ['target', 'iter', 'body', 'orelse'],
    ast.While: ['test', 'body', 'orelse'],

    ast.Try: ['body', 'handlers', 'orelse', 'finalbody'],
    ast.ExceptHandler: ['body'],
    ast.With: ['items', 'body'],
    ast.withitem: ['context_expr'],

    ast.FunctionDef: ['name', 'args', 'body', 'decorator_list'],
    ast.Lambda: ['args', 'body'],
    ast.arguments: ['args', 'kwonlyargs', 'vararg', 'kwarg', 'defaults', 'kw_defaults'],
    ast.arg: ['arg'],

    ast.Global: ['names'],
    ast.Nonlocal: ['names'],

    ast.ClassDef: ['name', 'bases', 'keywoards, body', 'decorator_list'],

    ast.AsyncFunctionDef: ['name', 'args', 'body', 'decorator_list'],
    ast.Await: ['value'],
    ast.AsyncFor: ['target', 'iter', 'body', 'orelse'],
    ast.AsyncWhile: ['test', 'body', 'orelse'],
}


optional_fields = {
    ast.FormattedValue: ['format_spec'],

    ast.Slice: ['step'],

    ast.AnnAssign: ['value'],

    ast.Print: ['dest'],
    ast.Raise: ['exc', 'cause'],
    ast.Assert: ['msg'],

    ast.alias: ['asname'],

    ast.ExceptHandler: ['type', 'name'],
    ast.withitem: ['optional_vars'],

    ast.FunctionDef: ['returns'],
    ast.arg: ['annotation'],

    ast.Return: ['value'],
    ast.Yield: ['value'],
    ast.YieldFrom: ['value'],
}


def descend(node):
    pass

import pytest


@pytest.fixture(params=[
    ('40', ['40']),
    ('[40]', '[ 40 ]'.split()),
    ('[true, false, null]', '[ true , false , null ]'.split()),
    ('{"foo": "bar"}', '{ "foo" : "bar" }'.split()),
])
def good(request):
    return request.param


@pytest.fixture(params=['{True, False}', "'hello!'"])
def bad(request):
    return request.param


@pytest.fixture
def lexer():
    import lexer
    try:
        return lexer.lexer
    except AttributeError:
        msg = 'você não pode modificar o nome da função lexer() no módulo lexer!'
        raise RuntimeError(msg)


class TestJSONLexer:
    @pytest.fixture(params=[
        ('40', 'number'),
        ('"hello"', 'string'),
        ('true', 'constant'),
        ('false', 'constant'),
        ('null', 'constant'),
        ('[', 'lbrack'),
        (']', 'rbrack'),
        ('{', 'lbrace'),
        ('}', 'rbrace'),
        (',', 'comma'),
        (':', 'colon'),
    ])
    def tok_type(self, request):
        return request.param

    def test_lexer_do_not_raise_errors(self, lexer):
        lexer('42')

    def test_basic_tokens(self, tok_type, lexer):
        src, tk_type = tok_type
        tok = lexer(src)[0]
        assert tok.type == tk_type
        assert tok.value == src

    def test_good_example(self, good, lexer):
        src, expected = good
        tokens = [tk.value for tk in lexer(src)]
        assert tokens == expected

    def test_bad_example(self, bad, lexer):
        with pytest.raises(SyntaxError):
            lexer(bad)
        
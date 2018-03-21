from lexer import Token
from test_basic import *


class TestJSONLexerAll:
    @pytest.fixture(params=[
        r'"\u01aF"', r'"\n\f"', r'"hello \"world\"!"', '-42', '0.42', '6.62e-34',
        '2.99e8', '2.99e+8',
    ])
    def good(self, request):
        return (request.param, [request.param])

    @pytest.fixture(params=['"foo\\a"', "foo\\uafgh", "foo\\uFF", '+42'])
    def bad(self, request):
        return request.param

    test_good_example = TestJSONLexer.test_good_example
    test_bad_example = TestJSONLexer.test_bad_example

    def test_octal_parse_as_multiple_ints(self, lexer):
        assert lexer('01') == [Token('0', 'number'), Token('1', 'number')]

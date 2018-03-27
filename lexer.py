from collections import namedtuple
# from pprint import pprint
import re

# Classe que representa uma token com campos value e type
Token = namedtuple('Token', ['value', 'type'])

re_number = r'(?P<number>\-?(0|[1-9]([0-9]*))(\.\d+)?([eE][+-]?\d+)?)'
re_space = r'(?P<space>\s+)'
re_left_key = r'(?P<lbrace>\{)'
re_right_key = r'(?P<rbrace>\})'
re_left_bracket = r'(?P<lbrack>\[)'
re_right_bracket = r'(?P<rbrack>\])'
re_comma = r'(?P<comma>\,)'
re_colon = r'(?P<colon>\:)'
re_constant = r'(?P<constant>(true|false|null))'
re_string = r'(?P<string>\"([^\\"]|\\(\"|\\|\/|b|f|n|r|t)|\\u[0-9a-fA-F]{4})*\")'
re_object = r'(?P<object>\{(?:(s*(?P=string)\s*:((?P=string)|(?P=number)|(?P=constant)))(?: , (s*(?P=string)\s*:((?P=string)|(?P=number)|(?P=constant))))*)?\})'
re_array = r'(?P<array>\[(?:((?P=string)|(?P=number)|(?P=constant))(?:,((?P=string)|(?P=number)|(?P=constant))))\])'

re_list = [
    re_number,
    re_space,
    re_left_key,
    re_right_key,
    re_left_bracket,
    re_right_bracket,
    re_comma,
    re_colon,
    re_constant,
    re_string,
    re_object,
    re_array,

]

re_full = '|'.join(re_list)
re_compiled = re.compile(re_full)

def lexer(src: str) -> list:
    """
    Lê uma string de código fonte JSON e retorna a lista de Tokens
    correspondente.

    Em caso de erros, levanta uma exceção do tipo SyntaxError.
    """

    tokens = []
    last_char = 0
    for m in re_compiled.finditer(src):
        i, j = m.span()

        if i > last_char:
            raise SyntaxError('invalid token: %r' % src[last_char:i])

        last_char = j

        tk_type = m.lastgroup
        tk_value = src[i:j]

        if tk_type != 'space':
            token = Token(tk_value, tk_type)
            tokens.append(token)

    if last_char != len(src):
        raise SyntaxError('invalid token: %r' % src[last_char:])

    return tokens

# pprint(lexer(input('Expr: ')))

from collections import namedtuple
import re

# Classe que representa uma token com campos value e type
Token = namedtuple('Token', ['value', 'type'])

re_number = r'(?P<NUMBER>\-?\d+(\.\d+)?([eE][+-]\d+)?)'  
re_operator = r'(?P<OPERATOR>[-+*/])'
re_space = r'(?P<SPACE>\s+)'

re_list = [
    re_number,
    re_operator,
    re_space
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

    

    return [Token('hello', 'string')]

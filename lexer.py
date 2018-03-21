from collections import namedtuple
import re

# Classe que representa uma token com campos value e type
Token = namedtuple('Token', ['value', 'type'])


def lexer(src: str) -> list:
    """
    Lê uma string de código fonte JSON e retorna a lista de Tokens 
    correspondente.

    Em caso de erros, levanta uma exceção do tipo SyntaxError.
    """

    return [Token('hello', 'string')]

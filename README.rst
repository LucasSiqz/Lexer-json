Lexer do JSON
=============

Implementar utilizando **apenas** as bibliotecas nativas do Python (ex.: módulo re)
um lexer para o formato JSON  (http://json.org/)

O seu lexer deve incluir uma função ``lexer(src: str) -> list`` que retorna uma
lista de tokens a partir de uma string de código fonte JSON. Cada token deve
ter pelo menos dois campos: ``token.value``, que contêm o valor da mesma como
string e ``token.type`` que identifica o tipo de token (number, string, boolean,
etc).


Data de entrega: 27/03/2018
Grupo: 1 ou 2 pessoas
Nota:
  Baseada em testes unitários

    - Passou em test_basic.py: 50%
    - Passou em test_full.py: 75%
    - Passou na suite de teste completa no computador do professor: 100%

  A nota pode ser revista e anulada pela presença de plágio.


Rodando os testes
-----------------

Você deve ter o Pytest para Python 3 instalado na sua máquina (``pip3 install pytest --user``).
Para rodar os testes, simplesmente execute ``pytest --maxfail=2``. 
Se quiser rodar apenas os testes básicos, execute ``pytest --maxfail=2 test_basic.py``
 
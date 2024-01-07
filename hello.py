#!/usr/bin/env python3

# a linha acima garante que variáveis de ambiente estarão disponíveis ao 
# programa executado pelo interpretador

"""Multi Language Hello World.

Dependent of language set in env variable, the program shows correspondent
message.

Observation:
    LANG variable must be set:
        (for example) export LANG=pt-br

Execution:
    python3 hello.py
    or
    ./hello.py
"""

# metadados
# muito utilizado por sistemas de deploy, mas em geral ignorados pelo
# interpretador
__version__ = "0.0.1"
__author__ = "Iury Santos"
__license__ = "Unlicensed"

import os #importa biblioteca padrão (mas que não é builtin)

# Dunder -> double underline. Linha 20 acima seria chamada de Dunder Version
# por exemplo.

"""
Python não tem uma função main que sempre é chamada quando um programa é
executado. Todos os comandos do script são rodados em sequência. Para lidar
com isso, existe uma convenção de checar o dunder name para o valor __main__
e executar o script se o retorno for verdadeiro.
Exemplo:
if __name__ == "__main__":
    print("Hello, World!")
"""

# atribui à variável current_language uma fatia([:5] de 0 ao 5 caractere,
# exclusive) da variável LANG que foi carregada no início do programa. Caso
# não consiga ler, assume que o valor padrão dela é "en_US".
current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"

print(msg)

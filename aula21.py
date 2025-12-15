"""
or -> Desde que haja uma expressão verdadeira, o resultado sempre será = True
"""

entrada = input('[E]ntrar - [S]air: ')
senha_digitada = input("Senha: ")

senha_permitida = '123'

if entrada == 'E' or entrada == 'e' and senha_permitida == senha_digitada:
    print("Entrar")
else:
    print("Sair")
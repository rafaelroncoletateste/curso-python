"""
and -> As duas ou mais expressões devem ser verdadeiras para o resultado ser = True
0 0.0 '' False -> False
"""
entrada = input('[E]ntrar - [S]air: ')
senha_digitada = input("Senha: ")

senha_permitida = '123'

if entrada == 'E' and senha_permitida == senha_digitada:
    print("Entrar")
else:
    print("Sair")

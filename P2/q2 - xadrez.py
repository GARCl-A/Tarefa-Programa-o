import re

def verifica_input(entrada):
    padrao = re.compile('[a-h][1-8] [a-h][1-8]')
    if (bool(padrao.match(entrada))):
        inicial = entrada[0:2]
        final = entrada[3:]

        return movimento_valido(inicial,final)
    else:
        return 'Input Inválido'

def movimento_valido(inicial,final):
    #Tabuleiro vai de A-H e de 1-8
    lista_letras = ['a','b','c','d','e','f','g','h']
    lista_numeros = [1,2,3,4,5,6,7,8]
    ili = lista_letras.index(inicial[0]) #index_letra_inicial
    ini = int(inicial[1]) - 1
    try:
        mov1 = f'{lista_letras[ili + 1]}{lista_numeros[ini + 2]}'
    except:
        mov1 = None
    try:
        mov2 = f'{lista_letras[ili + 1]}{lista_numeros[ini - 2]}'
    except:
        mov2 = None
    try:
        mov3 = f'{lista_letras[ili + 2]}{lista_numeros[ini + 1]}'
    except:
        mov3 = None
    try:
        mov4 = f'{lista_letras[ili + 2]}{lista_numeros[ini - 1]}'
    except:
        mov4 = None
    try:
        mov5 = f'{lista_letras[ili - 1]}{lista_numeros[ini + 2]}'
    except:
        mov5 = None
    try:
        mov6 = f'{lista_letras[ili - 1]}{lista_numeros[ini - 2]}'
    except:
        mov6 = None
    try:
        mov7 = f'{lista_letras[ili - 2]}{lista_numeros[ini + 1]}'
    except:
        mov7 = None
    try:
        mov8 = f'{lista_letras[ili - 2]}{lista_numeros[ini - 1]}'
    except:
        mov8 = None

    movimentos_possiveis = [mov1,mov2,mov3,mov4,mov5,mov6,mov7,mov8]
    if final in movimentos_possiveis:
        return 'MOVIMENTO VÁLIDO'
    else:
        return 'MOVIMENTO INVÁLIDO'

entrada = False
print('Formato: (d4 c2)')
while (entrada != 'f'):
    entrada = input('Insira o movimento: ')    
    if entrada != 'f': #Evita a exibição de mais um ciclo de inputs caso o usuário encerre
        valido = verifica_input(entrada)
        print(valido)
numeros = []
frequencias = []

entrada = None
while entrada != 'f':
    entrada = input('Insira um número inteiro: ')
    if entrada != 'f':
        try:
            entrada = int(entrada)
            if entrada not in numeros:
                numeros.append(entrada)
                frequencias.append(1)
            else:
                index = numeros.index(entrada)
                frequencias[index] += 1
        except:
            continue

contador = 0
for numero in numeros:
    if frequencias[contador] > 1:
        print(f'O número {numero} apareceu {frequencias[contador]} vezes')
    else:
        print(f'O número {numero} apareceu 1 vez')
    contador += 1
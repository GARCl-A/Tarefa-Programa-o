import re

#A ordem da tupla é 100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.01
notas_moedas = [0,0,0,0,0,0,0,0,0,0,0,0]
valores_possiveis = [100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.01]
formato = re.compile('[0-9]*\.[0-9][0-9]')
entrada = input('Insira o valor (rrr.cc): ')

if not formato.match(entrada):
    print('Input Inválido')
else:
    entrada = float(entrada)
    contador = 0
    atual = valores_possiveis[0]

    while entrada > 0.01:
        if entrada > atual:
            quantidade = int(entrada/atual)
            entrada -= (quantidade * atual) 
            notas_moedas[contador] = quantidade
        contador += 1
        if contador <= 11:
            atual = valores_possiveis[contador]


    print(
    f'''
NOTAS:
{notas_moedas[0]} nota(s) de R$ 100.00
{notas_moedas[1]} nota(s) de R$ 50.00
{notas_moedas[2]} nota(s) de R$ 20.00
{notas_moedas[3]} nota(s) de R$ 10.00
{notas_moedas[4]} nota(s) de R$ 5.00
{notas_moedas[5]} nota(s) de R$ 2.00

MOEDAS:
{notas_moedas[6]} moeda(s) de R$ 1.00
{notas_moedas[7]} moeda(s) de R$ 0.50
{notas_moedas[8]} moeda(s) de R$ 0.25
{notas_moedas[9]} moeda(s) de R$ 0.10
{notas_moedas[10]} moeda(s) de R$ 0.05
{notas_moedas[11]} moeda(s) de R$ 0.01
    '''
    )
#Converte para graus a partir de uma constante
def hora_graus(hora,minuto):
    grauh = hora * 30
    if grauh >= 360:
        grauh -= 360
    graum = minuto * 6

    return grauh,graum

#Separa hora de minutos
def extrai_hora(horastr):
    horas = horastr[0:2]
    minutos = horastr[3:]

    return valida_hora(horas,minutos)


def valida_hora(horas,minutos):
    #verifica se os valroes são numericos
    try:
        horas = int(horas)
        minutos = int(minutos)
    except:
        return 'Input Inválido'

    #Verifica se os valores estão nos limites certos
    if (int(horas) > 23 or int(minutos) > 59):
        return 'Input Inválido'
    else:
        return hora_graus(horas, minutos)

def retorna_angulo(grauh,graum):
    ang1 = abs(grauh - graum)
    ang2 = abs(graum - grauh)

    if ang1 < ang2:
        return ang1
    else:
        return ang2

entrada = True
while (entrada != 'f'):
    entrada = input('Insira a hora[hh:mm]: ')
    valores = extrai_hora(entrada)    
    if entrada != 'f': #Evita a exibição de mais um ciclo de inputs caso o usuário encerre
        if len(valores) == 2:
            angulo = retorna_angulo(valores[0], valores[1])
            print(f'O menor ângulo é de {angulo}°')
        else:
            print(valores)


    

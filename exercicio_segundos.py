#dias, horas, minutos e segundos

dias = int(input('Vamos calcular uma quande quantidade de tempo em segundos. Qual é a quantidade de dias?'))
hora = int(input('E qual a quantidade de horas?'))
min = int(input('Quantos minutos?'))
sec = int(input('E quantos segundos?'))
media = (dias*24*60*60)+(hora*60*60)+(min*60)+sec
print()
print('O resultado é {}s.' .format(media))


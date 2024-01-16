# inputs -> km percorridos, dias de aluguel. Calcular preço a pagar, sendo 60 por dia e 0,15 por km

km = float(input('Digite a quantidade de kilômetros percorridos: '))
dias = float(input('Digite a quantidade de dias de aluguel: '))

custo = km * 0.15 + dias * 60
print('\n'+'O custo referente ao aluguel do veículo é: R${:.2f}' .format(custo))


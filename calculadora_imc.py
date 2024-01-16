# insira seu peso e altura. O seu IMC é x
peso = float(input('Digite o seu peso: '))
altura = int(input('Agora digite sua altura em centímetros: '))
print('\n')
('Peso = {}kg. Altura = {}cm.'.format(peso, altura))
imc = peso / ((altura / 100) * (altura / 100))
print('Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 24.9:
    print('Seu peso está dentro da faixa saudável.')
elif 25 <= imc < 29.9:
    print('Você está com sobrepeso.')
else:
    print('Você está obeso. Recomendamos consultar um profissional de saúde.')

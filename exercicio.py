# exercicio média

nome = input('Qual é o seu nome?')
p1 = float(input('{}, me fale qual foi sua nota na avaliação escrita.' .format(nome)))
print('Ok, sua primeira nota foi {}.'.format(p1))
p2 = float(input('E qual foi sua nota no trabalho em grupo?'))
print('Perfeito! Eu não esperava que você tirasse menos que {}'.format(p2))

media = (p1 + p2) / 2
print()
print('{}, então, sua média final na disciplina foi {:.1f}! Parabéns!'.format(nome,media))

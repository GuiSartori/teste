s1 = 'Gui'
print(s1+' Sartori')

#nome é uma pessoa do gênero genero e tem n anos

nome = input('Qual é o seu nome?')
gender = input('E qual é o seu gênero?')
age = input('Quantos anos você tem?')
print('{} é uma pessoa do gênero {} e tem {} anos.' .format(nome,gender,age))
print (nome+gender[:4]+age)
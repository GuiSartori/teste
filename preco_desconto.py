
preco = float(input('Qual é o preço do produto?'))
desc = float(input('E qual é o desconto a ser aplicado?'))
valordesc = desc/100*preco
valorcomdesc = preco-valordesc
print('Desconto: R${:.2f}' .format(valordesc))
print('O preço com desconto é R${:.2f}' .format(valorcomdesc))



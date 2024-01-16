celsius = int(input('Qual é a temperatura em graus Celsius?'))
fahr = 9*celsius/5+32
print ('{}ºC equivalem a {}ºF.' .format(celsius, fahr))
print ('%.0fºC equivalem a %.1fºF.' %(celsius,fahr))
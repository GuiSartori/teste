#Bhaskara -> (-b±√Δ)/2a
#Δ=b²-4ac

a = float(input('Digite o valor de "a": '))
b = float(input('Digite o valor de "b": '))
c = float(input('Digite o valor de "c": '))
delta = b**2-4*a*c
x1 = (-b+delta**(1/2))/(2*a)
x2 = (-b-delta**(1/2))/(2*a)


print ('Δ = {}' .format(delta))
print ('x1 = {}' .format(x1))
print ('x2 = {}' .format(x2))


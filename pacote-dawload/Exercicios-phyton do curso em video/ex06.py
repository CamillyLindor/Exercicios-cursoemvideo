#algoritmo que le um numero e mostra o seu dobro, triplo e a raiz quadrada
import math
n = int(input('digite um numero:'))
m = n*2
m2 = n*3
r = math.sqrt(n)
print('o dobro do valor é {}, o triplo {}, e a raiz é {}' .format(m, m2, r))
#programa que le um numero e mostre na tela seu sucessor e seu antecessor
n = int(input('digite um numero:'))
a = n-1
s = n+1
print('o antecessor desse valor é {} e o sucessor {}' .format(a, s))

#nao precisaria criar variaveis se no format eu adicionace dentro do parenteses((n-1), (n+1)))
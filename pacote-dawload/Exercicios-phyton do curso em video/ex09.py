# programa que leia um numero inteiro qualquer e mostre toda sua tabuada
n = int(input('digite um  numero:'))
for i in range(11):
    t = i*n
    print('a tabuada desse valor é {}' .format(t))
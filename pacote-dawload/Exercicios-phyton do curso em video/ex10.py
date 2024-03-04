#crie um programa que leia quanto a pessoa tem de dinheiro e mostre quantos dolares ela pode comprar
c = float(input('quanto voce tem de dinhero?'))
dolar = c/4.98
print('com R${:.2f}, voce consegue comprar US${:.2f} '.format(c, dolar))
#programa que le a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessaria para pinta-la
#sabendo que cada 2l de tinta, pinta uma area de 2m ao quadrado

largura = float(input('qual é a largira dessa parede?'))
altura = float(input('qual é a altura dessa parede?'))
area = largura*altura
tinta =  area/2

print('sua parede tem a dimensão de {}X{} e sua area é de {}' .format(largura, altura, area))
print('para pintar essa parede, voce precisara de {}L de tinta' .format(tinta))
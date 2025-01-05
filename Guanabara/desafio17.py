import math
cateto_o = int(input('Digite o valor do cateto oposto: '))
cateto_a = int(input('Digite o valor do cateto adjascente: '))
hip = math.sqrt((cateto_o**2)+(cateto_a**2))
print(f'A hipotenusa é {hip}')
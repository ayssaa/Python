dias = int(input('Por quantos dias você ficou com o carro? '))
km = float(input('Por quantos KM você rodou com o carro? '))
print(f'O total a pagar é de R${(60*dias)+(0.15*km):.2f}')
print('=====CONVERSOR=====')
medida1 = str(input('Medida de origem: '))
medida2 = str(input('Medida convertida: '))
temp1 = float(input('Valor da temperatura: '))
if medida1 == 'C':
    if medida2 == 'F':
        temp2 = (1.8*temp1)+32
    elif medida2 == 'K':
        temp2 = temp1+273
elif medida1 == 'F':
    if medida2 == 'K':
        temp2 = ((temp1-32)/1.8)+273
    elif medida2 == 'C':
        temp2 = (temp1-32)/1.8
elif medida1 == 'K':
    if medida2 == 'C':
        temp2 = temp1-273
    elif medida2 == 'F':
        temp2 = ((temp1-273)*1.8)+32
print('...CONVERTENDO...')
print(f'{temp1} em {medida1} equivale a {temp2:.2f} {medida2}')
print("====DESAFIO 04====")
seq = input('Digite qualquer coisa! ')
print('você digitou', seq, 'que é do tipo', type(seq))
print('====CHECKLIST====')
checando = [seq.isalnum(), seq.isalpha(), seq.isdecimal(), seq.isdigit(), seq.isnumeric(), seq.isspace(), seq.islower(), seq.isupper(), seq.istitle()]
checado = ""
for i in checando:
    if i == True:
        checado += 'O'
    else:
        checado += 'X'
print('é alfa-numérico?', checado[0])
print('é alfabético?', checado[1])
print('é um número decimal?', checado[2])
print('é um dígito?', checado[3])
print('é numérico?', checado[4])
print('é um espaço?', checado[5])
print('está todo minúsculo?', checado[6])
print('está todo maiúsculo?', checado[7])
print('é um título?', checado[8])
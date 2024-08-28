import math
angulo = float(input('Digite um ângulo qualquer: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print(f'O seno de {angulo} vale {seno :.2f} O cosseno de {angulo} vale {cosseno :.2f} A tangente de {angulo} vale {tang:.2f}')
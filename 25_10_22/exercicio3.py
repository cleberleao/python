# Crie um programa para receber dois números e realizar todasoperações matemáticas e
# ao final mostrar todos os resultados,incluindo resto da divisão e exponencial.

nun1 = int(input("Digite o primeiro numero inteiro: "))
nun2 = int(input("Digite o segundo numero inteiro: "))

soma = nun1+nun2
mult = nun1*nun2
div = nun1/nun2
sub = nun1-nun2
resto = nun1%nun2
potencia = nun1**nun2

print("O resultado da soma é: " + str(soma))
print("O resultado da multiplicação é: " + str(mult))
print("O resultado da divisão é: " + str(div))
print("O resultado da subitração é: " + str(sub))
print("O resultado da resto da divisão é: " + str(resto))
print("O resultado da resto da potencia de n1 por n2 é: " + str(potencia))

# Crie um programa com uma função para multiplicar dois números e
# o algoritmo mostrar o resultado. Comando para criar uma função é:

def multiplica(n1, n2):
    result = n1 * n2
    return result

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
print("O resultado da multiplicação é: ", round(multiplica(n1, n2), 2))

# STEPHANIE
# código para fazer uma tabuada de 1 a 10 de um número que o usuário quizer

# Declarando a variável que é pedida pelo usuário no int input
numero = int(input("Escolha um número para a tabudada: "))

# Aqui o for ajuda com o loop de 1 a 10 para fazer tabuada de 1 a 10 com o número que o usuário quis
for tab in range (1,11):
    print(f"{tab} x {numero} = {tab * numero}")

#STEPHANIE

#declarando soma
soma = 0

#Somando somente números pares entre 1 a 50 
for numero in range (1,51):
    if numero % 2 == 0:
      soma += numero

print(f"Soma de todos os números pares entre 1 a 50: {soma}")
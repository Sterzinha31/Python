# variaveis
dias_locados = int(input("Dias alugados: "))
km_percorridos = float(input("Quantos km foram pecorridos? "))

#calculo do preço total
total = (dias_locados*60)+(km_percorridos*0.15)
print(f"O valor total a pagar é R${total:.2f}")
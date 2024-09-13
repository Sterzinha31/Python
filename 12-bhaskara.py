import math

# Solicite  os coeficientes A,B,C ao usuário 
A = float(input("Digite o coeficiente A: "))
B = float(input("Digite o coeficiente B: "))
C = float(input("Digite o coeficiente C: "))

# Verificar se A é difierente de  zero, já que A = 0 torna a equação de 1ºgrau
if A == 0:
    print("O valor de A deve ser diferente de 0 para que seja uma equação do 2º grau.")
else:
    # Calcula o discriminante (delta)
    delta = B**2 - 4 * A * C

    # Verifica o valor de delta
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        # Calcula a única reaíz real
        raiz_unica = -B / (2 * A)
        print(f"Equação possui uma única raíz real: {raiz_unica: .2f}")
    else:
        #calcula as duas raízes reais
        raiz1 = (-B + math .sqrt(delta))  /  (2 * A)
        raiz2 = (-B + math .sqrt(delta))  /  (2 * A)
        print(f"A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}")

print("Seja bem vindo(a) a balada do Dudu!")

idade = int(input("Me informe sua idade: "))

if idade >= 18 :
    print("Você está liberado(a)!! PODE ENTRAR :)")
          
elif idade >= 16 and idade <= 17 :
    autorizacao = input("Você tem autorização dos pais?(S/N):  ")

    if autorizacao == 'S':
        print("Você está liberado(a)!! PODE ENTRAR :)")

    elif autorizacao == 'N':
        print("VOCÊ NÃO PODE ENTRAR!")

elif idade <= 16:
 print ("VOCÊ NÃO PODE ENTRAR!")
    


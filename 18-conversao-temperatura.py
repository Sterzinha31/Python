def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def menu():
    print("\n-Menu de conversão de temperaturas-")
    print("1. Converter celsius para fahrenheit")
    print("2. Converter celsius para kelvin")
    print("3. Converter fahrenheit para celsius")
    print("4. Converter fahrenheit para kelvin")
    print("5. Converter kelvin para celsius")
    print("6. Converter kelvin para fahrenheit")
    print("0. Sair")

while True:
    menu()
    opcao = input("Selecione a conversão desejada (Clique 0 para sair): ")

    if opcao == '0':
        print("programa encerrado! :)")
        break
    elif opcao == '1':
        celsius = float(input("digite a temperatura em celsius: "))
        print(f"{celsius}°C é igual a {celsius_para_fahrenheit(celsius):.2f}°F")
    elif opcao == '2':
        celsius = float(input("digite a temperatura em celsius: "))
        print(f"{celsius}°C é igual a {celsius_para_kelvin(celsius):.2f}K")
    elif opcao == '3':
        fahrenheit = float(input("digite a temperatura em fahrenheit: "))
        print(f"{fahrenheit}°F é igual a {fahrenheit_para_celsius(fahrenheit):.2f}°C")
    elif opcao == '4':
        fahrenheit = float(input("digite a temperatura em fahrenheit: "))
        print(f"{fahrenheit}°F é igual a {fahrenheit_para_kelvin(fahrenheit):.2f}K")
    elif opcao == '5':
        kelvin = float(input("digite a temperatura em kelvin: "))
        print(f"{kelvin}K é igual a {kelvin_para_celsius(kelvin):.2f}°C")
    elif opcao == '6':
        kelvin = float(input("digite a temperatura em kelvin: "))
        print(f"{kelvin}K é igual a {kelvin_para_fahrenheit(kelvin):.2f}°F")
    else:
        print("opção inválida... tente novamente! :/ ")

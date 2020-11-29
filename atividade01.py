def leiaInt():
    
    try:
        numero = int(input("Digite um número: "))
    except:
        numero = 0

    return numero


print(leiaInt())
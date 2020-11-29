def leiaInt():
    
    try:
        numero = int(input("Digite um número: "))
    except:
        numero = 0

    return numero

def leiaFloat():
    
    try:
        numero = float(input("Digite um número: "))
    except:
        numero = 0

    return numero

print(leiaInt())
print(leiaFloat())
numero = int(input("Digite um número inteiro: "))

if numero <= 0:
    print("Número inválido!")
else:
    i = 2
    while numero > 0:
        j = 2
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
                break
            j += 1
        if primo:
            print(i)
            numero = numero - 1
        i = i + 1
        
#ejercicio_2

def primo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            print("El numero", n, "no es primo, es divisor")
            return False
    print("El numero", n, "es primo")
    return True

def lista():
    primos = []
    for dividiendo in range (2, 1000):
        for divisor in range (2, dividiendo):
            if dividiendo % divisor == 0:
                break

        else:
            primos.append(dividiendo)
    print(primos)


if __name__ =="__main__":
    primo(799)
    lista()
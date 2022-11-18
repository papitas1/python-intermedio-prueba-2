#ejercicio_3


from functools import reduce


def Datos():

    print("Ingrese el primer numero de la lista que desee crear")
    Uno = int(input())

    print("Ingrese el segundo numero de la lista que desee crear")
    Dos = int(input())

    print("Ingrese el tercer numero de la lista que desee crear")
    Tres = int(input())

    print("Ingrese el cuarto numero de la lista que desee crear")
    Cuatro = int(input())

    print("Ingrese el quinto numero de la lista que desee crear")
    Cinco = int(input())

    print("Ingrese el sexto numero de la lista que desee crear")
    Seis = int(input())

    Lista = (Uno, Dos, Tres, Cuatro, Cinco, Seis)

    Suma = reduce(lambda a, b, c, d, e, f : a+b+c+d+e+f , Lista)
    print("Suma:", Suma)

    Resta = reduce(lambda a, b, c, d, e, f : a-b-c-d-e-f , Lista)
    print("Resta", Resta)

    Multiplicacion = reduce(lambda a, b, c, d, e, f : a*b*c*d*e*f , Lista)
    print("Multiplicacion", Multiplicacion)

    Division = reduce(lambda a, b, c, d, e, f : (((((a/b)/c)/d)/e)/f) , Lista)
    print("Division", Division)

    Exponente = reduce(lambda a, b, c, d, e, f : (((((a**b)**c)**d)**e)**f) , Lista)
    print("Exponente", Exponente)

    Raiz_Cuadrada = reduce(lambda a, b, c, d, e, f : (((((a**(1/b))**(1/c))**(1/d))**(1/e))**(1/f)) , Lista)
    print("Raiz cuadrada", Raiz_Cuadrada)

if __name__=="__main__":
    Datos()
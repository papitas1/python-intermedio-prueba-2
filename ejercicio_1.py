#ejercicio_1

def Promedios():
    print("Ingrese las notas del primer estudiante en el siquiente orden: Historia, Lenguaje, MAtematicas, Fisica, Quimica y Biologia")
    Historia_1 = int(input())
    Lenguaje_1 = int(input())
    Matematicas_1 = int(input())
    Fisica_1 = int(input())
    Quimica_1 = int(input())
    Biologia_1 = int(input())
    Notas_1 = (Historia_1, Lenguaje_1, Matematicas_1, Fisica_1, Quimica_1, Biologia_1)

    print("Ingrese las notas del segundo estudiante en el siquiente orden: Historia, Lenguaje, MAtematicas, Fisica, Quimica y Biologia")
    Historia_2 = int(input())
    Lenguaje_2 = int(input())
    Matematicas_2 = int(input())
    Fisica_2 = int(input())
    Quimica_2 = int(input())
    Biologia_2 = int(input())
    Notas_2 = (Historia_2, Lenguaje_2, Matematicas_2, Fisica_2, Quimica_2, Biologia_2)

    print("Ingrese las notas del tercer estudiante en el siquiente orden: Historia, Lenguaje, MAtematicas, Fisica, Quimica y Biologia")
    Historia_3 = int(input())
    Lenguaje_3 = int(input())
    Matematicas_3 = int(input())
    Fisica_3 = int(input())
    Quimica_3 = int(input())
    Biologia_3 = int(input())
    Notas_3 = (Historia_3, Lenguaje_3, Matematicas_3, Fisica_3, Quimica_3, Biologia_3)

    Resultado = map(lambda x, y, z : ((x + y + z)/3), Notas_1, Notas_2, Notas_3)
    print(list(Resultado))

if __name__ == "__main__":
    Promedios()
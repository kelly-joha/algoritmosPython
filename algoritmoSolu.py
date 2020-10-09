# 1) Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un
# algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al
# final las dos variables (recuerda la asignación).
import math

while True:
    try:
        A = int (input("ingrese el primer numero para la variable A: "))
        B = int (input("ingrese el primer numero para la variable B: "))
        C = A
        A = B
        B = C
        print ("la variable A es ", A)
        print ("la variable B es ", B)
        break
    except ValueError:
        print ("por favor ingrese un numero")


# 2) Algoritmo que lea dos números, calculando y escribiendo el valor de su suma, resta,
# producto y división.


while True:
    try:
        num1 = int (input ("ingrese el primer numero "))
        num2 = int (input ("ingrese el segundo numero "))
        suma = num1 + num2
        resta = num1 - num2
        producto = num1 * num2
        if B <= 0:
            división = 0
        else:
            division = num1 / num2
        print ("la suma es de ", suma)
        print (" la resta es de ", resta)
        print (" el producto es de ", producto)
        print (" la division es de ", division)
        break
    except ValueError:
        print ("por favor ingrese un numero")


# 3) Algoritmo que lea dos números y nos diga cual de ellos es mayor o bien si son
# iguales (recuerda usar la estructura condicional SI)

while True:
    try:
        A = int (input ("ingrese el primer numero "))
        B = int (input ("ingrese el segundo numero "))
        if A < B:
            print ("el primer numero es menor que el segundo ingresado")
        elif A > B:
             print ("el primer numero es mayor que el segundo ingresado")
        else:
            print ("los numeros son iguales")
        break
    except ValueError:
        print ("por favor ingrese un numero")


# 4) Algoritmo que lea tres números distintos y nos diga cual de ellos es el mayor
# (recuerda usar la estructura condicional Si y los operadores lógicos).

while True:
    try:
        A = int (input ("ingrese el primer numero "))
        B = int (input ("ingrese el segundo numero "))
        c = int (input ("ingrese el tercer numero "))
        if A > B and B > C:
            print ("el primer numero es mayor")
        elif B > A and B > C:
             print ("el segundo numero es mayor")
        elif C > A and C > B:
            print ("el tercer numero es mayor")
        else:
            print("todos los numeros son iguales")
        break
    except ValueError:
        print ("por favor ingrese un numero")


# 5) Diseñar un algoritmo que pida por teclado tres números; si el primero es negativo,
# debe imprimir el producto de los tres y si no lo es, imprimirá la suma.

while True:
    try:
        A = int (input ("ingrese el primer numero "))
        B = int (input ("ingrese el segundo numero "))
        c = int (input ("ingrese el tercer numero "))

        if A < 0:
            producto = A * B * C
            print ("el producto de los valores ingresados es ", producto)
        else:
            producto = A + B + C
            print ("la suma de los valores ingresados es ", producto)
        break
    except ValueError:
        print ("por favor ingrese un numero")

  

# 6) Realizar un algoritmo que lea un número por teclado. En caso de que ese número
# sea 0 o menor que 0, se saldrá del programa imprimiendo antes un mensaje de error.
# Si es mayor que 0, se deberá calcular su cuadrado y la raiz cuadrada del mismo,
# visualizando el numero que ha tecleado el usuario y su resultado (“Del numero X, su
# potencia es X y su raiz X” ). Para calcular la raiz cuadrada se puede usar la función
# interna RAIZ(X) o con una potencia de 0,5.

while True:
    try:
        A = int (input ("ingrese un numero ")
        if A <= 0:
            print ("error")
        else:
            B = A ** 2
            C = math.sqrt(A)
            print ("del numero ingresado", A, "su pontencia es ", B "y su raiz es ", C)
        break
    except ValueError:
        print ("por favor ingrese un numero")


# 7) Un colegio desea saber qué porcentaje de niños y qué porcentaje de niñas hay en el
# curso actual. Diseñar un algoritmo para este propósito (recuerda que para calcular el
# porcentaje puedes hacer una regla de 3).

while True:
    try:
        nino = int (input ("ingrese un numero de niños")
        nina = int (input ("ingrese un numero de niños")
        total = nino + nina
        if total > 0:
            pornino = (nino/total) * 100
            pornina = (nino/total) * 100
            print ("el porcentaje de niños es ", pornino, "el porcentaje de niñas es ", pornina)
        else:
            pornino = 0
            pornina = 0
            print ("no se puede hacer promedio de niños la cantidad es cero")
        break
    except ValueError:
        print ("por favor ingrese un numero")


# 8) Una tienda ofrece un descuento del 15% sobre el total de la compra durante el mes
# de octubre. Dado un mes y un importe, calcular cuál es la cantidad que se debe cobrar
# al cliente.

texmeses = texMeses = """
Por favor emplee la siguiente convención para definir cada mes:
        Enero => 1                     Julio => 7
        Febrero => 2                   Agosto => 8
        Marzo => 3                     Septiembre => 9
        Abril => 4                     Octubre => 10
        Mayo => 5                      Noviembre => 11
        Junio => 6                     Diciembre => 12
"""

while True:
    try:
        print(texMeses)
        mes = int(input("Ingrese el mes del importe  "))
        importe = int(input("ingrese el valor del importe "))  
        descuento = int((importe * 15)/100)
        totaldescuento = importe - descuento
        if mes > 12 and mes < 1:
            print ("el mes debe estar entre 1 y 12")
        elif mes == 10:
            print (" el valor a cobrar es ", totaldescuento)
        else:
            print (" el valor a cobrar es ", importe)     
        break
    except ValueError:
        print("Por favor ingrese solo números")



# 9) Realizar un algoritmo que dado un número entero, visualice en pantalla si es par o impar. En el caso de ser 0, debe visualizar “el número no es par ni impar” (para que un numero sea par, se debe dividir entre dos y que su resto sea 0)


NumEnt = int(input("Escriba un número: "))
if NumEnt == 0:
    print(f"{NumEnt} el número no es par, ni impar")
elif NumEnt % 2 == 0:
    print(f"{NumEnt} es par")
else:
    print(f"{NumEnt} es impar")

# 10) Modificar el algoritmo anterior, de forma que si se teclea un cero, se vuelva a pedir el número por teclado (así hasta que se teclee un número mayor que cero) (recuerda la estructura mientras).

NumEnt = int(input("Escriba un número mayor a 0: "))
while NumEnt == 0:
    print("¡El número debe ser mayor a 0! Inténte de nuevo")
    NumEnt = int(input("Escriba un número mayor a 0: "))
    if NumEnt % 2 == 0:
        print(f"{NumEnt} es par")
    else:
        print(f"{NumEnt} es impar")


# 11) Algoritmo que nos diga si una persona puede acceder a cursar un ciclo formativo
# de grado superior o no. Para acceder a un grado superior, si se tiene un titulo de
# bachiller, en caso de no tenerlo, se puede acceder si hemos superado una prueba de
# acceso.




# 12) Desarrollar un algoritmo que nos calcule el cuadrado de los 9 primeros números naturales (recuerda la estructura desde-hasta)

for num in range (1, 9 + 1):
    print(f"Ahora num vale {num} y su cuadrado {num ** 2}")
print("Fin")

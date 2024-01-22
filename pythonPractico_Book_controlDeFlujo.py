# PYTHON PRACTICO - TEMA CONTROL DE FLUJO.

"""
Se explica las diferentes instrucciónes de bifurcación que existen en la programación, Independientemente de
el tipo de bifurcación que se use, se debe especificar la condicioon a evaluar y agrupar el conjunto de instrucciones que forman
cada camino posible a tomar, indicando el inicio y el final.
"""

# OPERADORES RELACIONALES.

"""
Son operadores que permiten comparar dos elementos, en caso de que la comparación sea cierta la operación devolvera True o False en caso
de no ser cierta los siguientes son los operadores disponibles en Python.

Menor que : < ¿ el primer elemento es menor que el segundo?

Mayor que : > ¿ el primer elemento es mayor que el segundo?

Menor o igual que : <= ¿el primer elemento es menor o igual que el segundo?

Mayor o igual que : >= ¿el primer elemento es mayor o igual que el segundo?

Igual que : == ¿el primer elemento es igual que el segundo?

Distinto que : != ¿el primer elemento es distinto que el segundo?

Ejemplo:    4<6  .................true
            3>6 ..................false
            5<=5 .................true
            7>= 4 ................true
            3==3 .................true
            1!=1 = ...............false
            
"""

# BLOQUES DE IDENTACIÓN

"""
Es importante comprender los conseptos de bloque de código e identación.

Los bloques de código fuente son un conjunto de sentencias que estan delimitadas por un inicio y un fin. La forma de delimintar los bloques
depende de cada lenguaje de programación.

La identación o tabulación, es una forma de mejorar la legibilidad del código, mediante el desplazamiento de las sentencias hacia la derecha,
mediante espacios en blanco o tabuladores separandola del margen izquierdo, a diferencia de otros lenguajes, en Python la identación tiene
significado, es obligatoria y hace parte de la sintaxis del lenguaje.

Ejemplo:

Bloque 1
    Bloque 2
        Bloque 3
    Bloque 2 (Continuación)
        bloque 4
            bloque 5
        Bloque 4 (continuación)
    Bloque 2 (continuación)
Bloque 1 (continuación)

"""

# IF \ ELIF \ ELSE

"""
If forma parte de un conjunto de sentencias encargadas de bifurcar la ejecución del código fuente, dependiendo de una serie de
condiciones. por lo tanto, la sentencia if permite tomar decisiones, evaluará una condicion de una operación lógica y dependiendo
del resultado ejecutará un codigo fuente u otro.

Comandos if :

if : Permite generar un bloque que se ejecuta si se cumple la condición de entrada que se dió.

elif : Permite generar un camino alternativo con una condición de entrada.

else : Permite generar un camino alternativo siempre que no se hayan las condiciones posibles de if y elif.

Tambien es posible incluir ifs dentro de otros ifs, siendo estos ifs anidados.


"""
# EJERCICIO 1, IF

print("EJERCICIO 1 IF")

print("-------------------------------------------------------------------")

numero = int(input("Escriba un númerodel 1 al 1000 : "))
if numero < 400:
    print("El numero es menor que 400")
print("Ha escrito el numero " + str(numero))

print("-------------------------------------------------------------------")

# EJERCICIO 2, USO DEL OPERADOR OR PARA COMPROBAR SI UNA CADENA TERMINA EN VOCAL.

print("COMPROBAR SI UNA CADENA DE TEXTO TERMINA EN VOCAL CON IF Y EL OPERADOR OR ")

print("-------------------------------------------------------------------")

cadena = input("Introduzca una cadena de texto: ")
if cadena.endswith("a") or cadena.endswith("e") or cadena.endswith("i") or cadena.endswith("o") or cadena.endswith("u"):
    print('La cadena de texto acaba en vocal ')
print("Ha escrito : " + cadena )

print("-------------------------------------------------------------------")

# EJERCICIO 3 , USO DE LA SENTENCIA ELSE
print('USO DE LA SENTENCIA ELSE')

print("-------------------------------------------------------------------")

numero = int(input("Escriba un númerodel 1 al 1000 : "))
if numero < 400:
    print("El numero es menor que 400")
else:
    print("El numero que ha escrito es mayor o igual a 400")
print("Ha escrito el numero : " + str(numero))

print("-------------------------------------------------------------------")


# EJERCICIO 4 , USO DE IF Y ELSE ANIDADAS. INDTRODUCIR DOS NUMEROS Y REALIZAR UNA SUMA DE ELLOS. EL RESULTADO SE USA PARA EVALUAR
# DIFERENTES IFS E IMPRIMIR MENSAJE POR PANTALLA.

print(" USO DE IF Y ELSE ANIDADOS")

print("-------------------------------------------------------------------")

sumando1 = int(input("Escriba el primer sumando .  "))
sumando2 = int(input("Escriba el segundo sumando : "))
resultado = sumando1 + sumando2

print('El resultado de la sima es : ', str(resultado))
if resultado%2 == 0:
    if resultado >= 1000:
        print("El resultado de la suma es par y mayor o igual que 1000")
    else:
        print("El resultado de la suma es par y menor o igual que 1000")
else :
    if resultado >= 1000:
        print("El resultado de la suma es impar y mayor o igual que 1000")
    else :
        print("El resultado de la suma es impar y menor o igual que 1000")

print("-------------------------------------------------------------------")

# EJERCICIO 5 , MANEJO DE LA SENTENCIA ELIF
"""
 elif permite introducir un camino alternativo al anterior if pero con una condición. Esto lo diferencia de else.Mediante la sentencia
 elif se puede crear caminos alternativos infinitos dependiendo del cumplimiento de la condicion de entrada y un camino que se tomará en caso
 de que no se cumpla ninguna de las condiciones de entrada a los caminos previos. 
"""
print(' USO DE LA SENTENCIA ELIF ')

numero1 = int(input("Escriba el primer número : "))
numero2 = int(input("Escriba el segundo numero : "))

if numero1 == numero2:
    print("Ambos numeros son iguales")
elif numero1 > numero2:
    print("Numero 1 es mayor que numero2")
else:
    print('El primer número es menor que el segundo')
        


























































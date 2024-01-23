# PYTHON PRACTICO - BUCLES

"""
En programación se puede definir un bucle como la repetición de la ejecución de
un conjunto de instrucciones, donde a cada repetición se le llama iteración.

Hay diferentes tipos de bucles, se debe tener muy claro cuando usar uno u otro
ya que esta recomendado el uso de cada uno en diferentes contextos, que varia
dependiendo del tipo de condición de parada de ejecución del bucle que se necesite.

En otras palabras se utilizara un bucle u otro dependiendo de la forma en la que
se necesite indicarle el numero de iteraciones a realizar.

Para el uso de los bucles se debe indicar el punto de inicio, el punto final y el
numero de iteraciones que van a realizarse, y aunque para cada tipo de bucle se
especifica de una forma distinta todos tienen estos elementos en comun.

    * Punto de inicio del bucle.
    * Punto de fin del bucle.
    * Número de iteraciones.
    * Bloque de intrucciones a ejecutar.
"""

# BUBLE FOR

"""
Esta recomendado para contextos en los que se sabe el numero de iteraciones
exactas que se van a dar en ejecución, o sea, es un bucle que busca ejecutar
un conjunto de instrucciones de forma repetitiva hasta llegar al numero maximo
de iteraciones definidas.

Los bucles for se ejecutan en Python sobre elementos iterables como listas, tuplas
cadenas de texto o diccionarios. El numero de iteraciones que se ejecutarán depende
de el numero de elementos de los que se compone el elemento iterable.

La sintaxis de los bucles for es la siguiente.

        for Variable in ColeccionIterable:
            bloqueInstrucciones

for  : Indicador del comienzo del bucle

Variable : variable que almacena el elemento sobre el que se esta iterando.

ColeccionIterable : Elemento sobre el que se ejecuta el bucle.

BloqueInstrucciones : conjunto de instrucciones que se ejecutarán en cada iteración.
"""
# EJERCICIO 1 , RECORRER LISTA USANDO BUCLE FOR Y MOSTRANDO LOS ELEMENTOS EN PANTALLA.
print('------------------------------------------------------------------------------')

print (" RECORRER LISTA USANDO BUCLE FOR , IMPRIMIR ELEMENTOS EN PANTALLA")

print('------------------------------------------------------------------------------')

lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r",]

for item in lista :
    print("Esta el la letra :" , item) # imprimira el print por cada letra de la lista

print('------------------------------------------------------------------------------')

# EJERCICIO 2 , MOSTRAR LA LISTA ANTERIOR UN NUMERO DE VECES DETERMINADAS POR OTRO BUCLE FOR.

"""
Esto se conoce como bucle for anidado, consiste en la utilizacion de bucles como parte del bloque de instrucciones
de otros bucles, el bucle que se encuentra dentro de otro bucle se conoce como bucle internoo interior, y el que contiene
otros bucles externoo o exterior.
"""
print('------------------------------------------------------------------------------')

listaLetras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r",]

listaIteraciones = [1,2,3,4,5]

for item in listaIteraciones :
    print("Iteración número :" + str(item))

    for letra in listaLetras :
        print(letra , end = " ")
    print ("\n")

print('------------------------------------------------------------------------------')


# EJERCICIO 3 , UITILIZACIÓN DE UNA LISTA CON ELEMENTOS DISTINTOS , PARA ITERAR CON FOR.

print('------------------------------------------------------------------------------')

print (" USAR UNA LISTA COMPUESTA POR ELEMENTOS DE TIPOS DIFERENTES PARA ITERAR CON FOR ")

print('------------------------------------------------------------------------------')

lista = [ 88, "Silla" , ["Hola", "Mundo"], "Perrito", "Gatito", 35 ]

for item in lista :
    print (item)


print('------------------------------------------------------------------------------')

# EJERCICIO 4 , APRENDER INSTRUCCIÓN QUE PERMITE OBTENER LISTA SECUENCIAL DE ELEMENTOS ENTEROS, EMPEZANDO EN 0 HASTA EL VALOR INDICADO.
# ES LA SENTENCIA range.

"""
El ejercicio consiste en dos bucles for anidados que recorreran 2 listas devueltas por la sentencias range, mostrando
el valor de ambas listas. El bucle interno se ejecuta tantas veces como iteraciones tenga el bucle externo, en este caso el
bucle interno se ejecutará completamente un total de cinco veces.
"""
print('------------------------------------------------------------------------------')

print (" USO DE LA SENTENCIA range EN BUCLES")

print('------------------------------------------------------------------------------')


for item in range(5):
    for item2 in range(3):
        print("Iteración " + str(item) + "," + str(item2))


"""
utiliza dos bucles for anidados para imprimir una cadena de texto que contiene las iteraciones de los bucles.
El primer bucle for itera sobre un rango de números del 0 al 4, mientras que el segundo bucle for itera sobre un rango
de números del 0 al 2. En cada iteración del segundo bucle for, se imprime una cadena de texto que contiene los valores de
las variables item y item2.
"""

# ****************************************************************************************************************************

# TEMA BUCLES - SUBTEMA BUCLE WHILE.

print('------------------------------------------------------------------------------')

"""
Este bucle esta recomendado para contextos en los que no se sabe exactamente el número de iteraciones que se tiene que ejecutar.
pero se sabe que hay que ejecutar iteraciones hasta que deje de cumplir una condición.

Los bucles while tienen la siguiente sintaxis.

        while Condicion :
            BloqueInstrucciones

while : indicador de comienzo del bucle

Condición : condición que debe cumplirse para que se siga ejecuntando la iteración.

BloqueInstrucciones : conjunto de instrucciones que se ejecutarán en cada iteración.


    Posibles problemas en el uso de while.

    * Bloques que no se ejecutarán nunnca : Se debe poner atención a la inicialización de las variables de control del bucle, para asegurarse de
      que la condición es True , si desde el principio la condición es false el bucle jamas se ejecutara.

    * Bucles infinitos : Se debe prestar atención a la modificación de los valores de las variables de control del bucle dentro del bucle, ya que
      si estos valores no se ven afectados nunca , el bucle jamas parará de ejecutarse.

      --------------------------------------------------------------------------------------------------------------------------------

      variableDeControl = 0       .................................> Esta es la variable de control y esta fuera del bucle while.

      while varialbleDeControl < 10 :
          print (variableDeControl , end = " ")
          variableDeControl = variableDeControl +1 
"""
# EJERCICIO 1 , MOSTRAR VALOR DE VARIABLE DE CONTROL.

print('------------------------------------------------------------------------------')

print (" EJERCICIO 1 MOSTRAR VALOR DE LA VARIABLE DE CONTROL - BUCLE WHILE")

i = 0

while i< 10:
    print(i,end=" ")
    i = i +1
print('------------------------------------------------------------------------------')

# EJERCICIO 2, USAR UNA VARIABLE DE CONTROL DIFERENTE DE UN NUMERO ENTERO.

print(" USAR UNA VARIABLE DE OONTROL DIFERENTES A UN NUMERO ENTERO")

pedirNumero = True
while pedirNumero :
    valor = int(input("Introduce un numero entero inferior a 10 : "))
    if valor <10:
        pedirNumero = False
print("Fin : Ha introducido un valor inferior a 10 ")

print('------------------------------------------------------------------------------')

"""
Al igual que con los bucles for , se pueden usar bucles while anidados, se debe tener en cuenta algo muy importante
y es que en cada iteración del bucle exterior , se debe inicializar la variable de control del bucle interior.
"""

print('------------------------------------------------------------------------------')

# EJERCICIO 3, BUCLES WHILE ANIDADOS.
print("BUCLES WHILE ANIDADOS")

item1 = 0

while item1 < 5 :
    item2 = 0
    while item2 <3:
        print("Iteración " + str(item1) + "," + str(item2))
        item2 = item2 + 1
    item1 = item1 + 1

print('------------------------------------------------------------------------------')

# EJERCICIO 4 , ANIDAR BUCLE FOR Y BUCLE WHILE

print("ANIDAR BULCE FOR Y BUCLE WHILE")

for item1 in range(5):
    item2 = 0
    while item2 < 3:

        print("Iteración " + str(item1) + "," + str(item2))
        item2 = item2 + 1

print('------------------------------------------------------------------------------')
        









































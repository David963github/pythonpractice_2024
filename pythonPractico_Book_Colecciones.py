# PYTHON PRACTICO  TEMA TIPO DE DATOS *** SUBTEMA LISTAS TUPLAS Y DICCIONARIOS

"""
En Python, tenemos tres posibles colecciones:

* Listas

* Tuplas

* Diccionarios

Listas : Son un conjunto ordenado de elementos, que puede contener datos de cualquier tipo. Una caracteristica muy importante de las listas es que
pueden contener elementos de diferentes tipos, puede estar compuesta por cadenas de texto, numeros enteros, y por otras listas.

Se representan por una serie de elementos separados por comas, y delimitados entre corchetes [] Ej: [ 56, "Python", "Valeria", 345,99]

Los elementos en las listas ocupan posiciones concretas, mediante las cuales se puede acceder directamente a cada elemento, se debe recordar que los elementos
empiezan desde la pocicion cero 0.

"""

# EJERCICIOS , estan divididos en dos partes, primero la manipulación de las listas y el segundo aprendizaje de los metodos propios de listas.

# MANIPULACIÓN.

print("****************************************************************")
print("Definición de una lista con diferentes tipos de datos, imprimir en pantalla la lista entera y partes de la misma")

lista = ["Python", "RA-MA", 2019,"Libro",3]
print(lista)
print(lista [0])
print(lista [1])
print(lista [2])
print(lista [3])
print(lista [4])

print("****************************************************************")
print("USO DE LA FUNCION len() y CONCATENACIÓN DE LISTAS")

# Segundo ejercicio, operador + para unir listas. listaConcatenada = lista1 + lista2

# Uso de la función len() que indica el numero de elementos que componen la lista. NumeroElementos = len(lista)

lista1 = ["Camiseta", "Pantalón", "Zapatillas"]
lista2 = ["Abrigo", "Jersey", "Sudadera", "Calcetiles"]

print("Numero de elementos de lista1: ", len(lista1))
print("lista1 :", lista1)
print("Numero de elementos de lista2:", len(lista2))
print("lista2 :", lista2)
listaconcatenada = lista1 + lista2
print("Numero de elementos lista concatenada: ", len(listaconcatenada))
print("Lista concatenada", listaconcatenada)

# Ejercicio 3, añadir elementos a las listas de diferente forma,

print("****************************************************************")
print("AÑADIR ELEMENTOS A LAS LISTAS")
print("****************************************************************")

lista = ["Camiseta", "Pantlona", "Zapatillas"]
print(lista)
lista = lista + ["Abrigo"]
print(lista)
lista = lista + ["Yersey", "Sudadera"]
print(lista)
lista = lista + ["Calcetiles"] + ["Bufanda"]
print(lista)
print("****************************************************************")
# Ejercicio 4, modificar y eliminar elementos de una lista.  para modificar => Lista[posición] = NuevoValor
# Para eliminar => instrucción [del]  del Lista [posición]

print("MODIFICAR Y ELIMINAR ELEMENTOS DE UNA LISTA")

lista = ["Camiseta", "Pantalón", "Zapatillas"]
print(lista)
lista [1] = "Cazadora"
print(lista)
del lista [0]
print (lista)

print("****************************************************************")

# Ejercicio 5, operador * , permite concatenar listas con si mismas un numero finito de veces. ListaConcatenada = Lista * NúmeroEntero

print("  OPERADOR * CONCATENAR LISTAS")

print("****************************************************************")

lista = ["Camiseta", "Pantalón", "Zapatillas"]
print (lista)
listaConcatenada = lista * 3
print(listaConcatenada)

print("****************************************************************")

# Ejercicio 6, listas como elementos de una lista , acceso a elementos de listas dentro de otras listas.

print("LISTAS COMO ELEMENTOS DE UNA LISTA")

lista = ["Camiseta", ['Calcetines', 'Cazadora'], "Zapatillas"]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[1][0])
print(lista[1][1])

print("****************************************************************")

# Ejercicio 7, Extraer una porción de una lista, en una nueva lista. Lista[n:m]

print(" EXTRACCIÓN DE FRAGMENTO DE UNA LISTA EN UNA LISTA NUEVA")

# NOTA: TENER EN CUENTA QUE n siempre deve ser menor que m , si no se especifica n sera 0 por defecto, si no se especifica m sera el tamaño de la lista menos uno.

lista = [1,2,3,4,5,6,7,8,9]
print(lista)
lista1 = lista[3:7]
print(lista1)
lista2 = lista[:5] # aqui no se esta especificando n 
print(lista2)
lista3 = lista [6:] # aqui no se esta especificando m
print(lista3)

# MÉTODOS PROPIOS DE PYTHON PARA LISTAS.

print("****************************************************************")

print(" MÉTODOS PROPIOS DE PYTHON PARA LISTAS")

print("****************************************************************")

"""
Permite manipular listas realizando operaciones complejas de manera sencilla.

La gran mayoria de estos métodos se escriben con la siguiente estructura, lista.NombreFuncion(Parámetros)


Las funciones de listas en Python son las siguientes:

append :añade el elemento pasado como parámetro a la lista.
        Valor devuelto : lista modificada con el elemento añadido.
        Parámetros : elemento de cualquier tipo de dato

insert : Añade un elemento pasado como parametro a la lista en la posición indicada tambien en el parámetro. el elemento que ocupe esa posicion y
los de posiciones superiores seran desplazados hacia la derecha dentro de la lista.

        Valor devuelto : Lista modificada con el elemento añadido
        Parámetros : Recibe 2 parámetros, el primero indica la posicion en la que se insertará el elemento dentro de la lista y el segundo el elemento a insertar.

remove : Elimina la primera ocurrencia empezando por la izquierda de la lista del elemento indicado como parámetro. En caso de no encontrar el elemento se lanza un error.

        Valor devuelto : Lista modificada con el elemento eliminado o error. dependiendo de si el elemento es encontrado o no.

reverse : Invierte el orden de la lista.

        Valor devuelto : lista modificada
        parámetros : no tiene.

sort : Ordena una lista si es posible. por defecto la ordenacion es ascendente, para ordenación descendente, se debe indicar por parametro.

        Valor devuelto : Lista modificada
        parámetros : Tiene un parámetro que es opcional, (reverse = true )para indicar ordenación descendente.

pop : Sive para eliminar un elemento de la lista, devuelve como resultado de la operación.

        Valor devuelto : lista modificada
        Parámetros : Tiene uno opcional, para indicar el elemento a eliminar, en caso de no especificar, la función se ejecuta en el ultimo elemento de la lista.

extended : Añadir elementos a una lista, se diferencia del metodo apend en que , append añade la lista como elemento de lista, estended añade los elementos de la
lista a la lista, obteniendo como resultado una lista con los elementos de ambas.

        Valor devuelto  : lista modificada
        Parámetros : lista que se quiere añadir a la lista.

count : Numero de veces que aparece un elemento indicado como parámetro de la lista.

        Valor devuelto : numero de ocurrencias del elemento
        Parámetros : elemento del que se quiere saber el numero de veces que aparaese en la lista.

index : Este devuelve la posición de la primera ocurrencia de izquierda a derecha en la lista del elemento pasado como parámetro.

        Valor devuelto : posición que ocupa el elemento dentro de la lista
        Parámetros : tiene 3 parámetros, el primero es obligatorio, y es el elemento a buscar, el segundo es opcional y se utiliza ipara indicar en que posicion empezar a buscar
        y por ultimo, el tercer parámetro es opcional y se usa para indicar en que posición finalizar la busqueda.

clear : Elimina todos los elementos de la lista.

        Valor devuelto : Lista vacia
        Parámetros: no tiene.


"""

lista = [45,32,3,78]
print("Lista original you know : ", lista)
lista.append(995)
lista.append(7)
print("Lista despues de append:", lista)
lista.sort()
print("Lista ordenada :", lista)
lista.reverse()
print("Lista al revez : ", lista)

listaextend = [1,5,87,45]
lista.extend(listaextend)
print("Lista despues de extend", lista)
lista.sort(reverse = True)
print("Lista ordenada al revez :", lista)
print("Numero de elementos 45 : ",lista.count(45))
lista.insert(4,111)
print("Lista despues de insert:",lista)
lista.remove(45)
print("Lista despues de remove :", lista)
print("Posición del elemento 111 :", lista.index(111))
lista.pop()
print("Lista despues de pop : ", lista )
lista.clear()
print("Lista despues de clear : ", lista)
      
print("**************************************************")

# TUPLAS

print("TUPLAS")

"""
Son un conjunto o set de datos ordenado e inmutable, a diferencia de las listas, en la tuplas no se puede modificar los elementos, pueden contener
elementos de diferentes tipos de datos, la sintaxis de las tuplas es : una serie de elementos delimitados entre parentesis y separados por comas.

("Casa", "2" , 345 , "Kiara", 99)

"""
# Ejercicio , definir una tupla y acceder a sus elementos.

print(" DEFINIR TUPLA - ACCEDER A SUS ELEMENTOS")

print("***************************************************")

tupla = ("Casa", "2" , 345 , "Kiara", 99)
print("Elementos de la tupla : ", tupla)
print("Elemento en la posición [0]" , tupla [0])
print("Elemento en la posición [1]" , tupla [1])
print("Elemento en la posición [2]" , tupla [2])
print("Elemento en la posición [3]" , tupla [3])
print("Elemento en la posición [4]" , tupla [4])

"""
Al igual que las listas, las tuplas tienen sus propios metodos , los cuales son los siguientes:

count : Cuenta el numero de veces que se encuentra el elemento indicado como parámetro dentro de la tupla

        Valor devuelto : Numero de ocurrencias del elemento
        Parámetros : Elemento del que se quiere saber el numero de veces que aparece en la tupla

index : Devuelve la posición de la primera aparición del elemento empezando de izquierda a derecha, en la tupla.

        Valor devuelto : Posición del elemento dentro de la tupla.
        Parámetros : 3 el primero es obligatorio, es el elemento a buscar, el segundo opcional , se usa para indicar en que posición empezar la busqueda,
        y el tercero opcional para indicar en que posición termina la busqueda.


"""

# Ejercicio 2, uso de las funciones count e index de las tuplas en Python.

print("---------------------------------------------------------------------")

print("USO DE COUNT E INDEX EN TUPLAS")


tupla = ("Casa", "2" , 345 , "Kiara", 99)
print("Elementos de la tupla : ", tupla)
print("Número de elementos 99", tupla.count(99))
print("Posición que ocupa el elemento Kiara : ", tupla.index("Kiara"))

"""
En las tuplas, tambien se puede extraer porciones de estas en otras nuevas, para extraer un fragmento de una tupla en otra nueva se usa la sintaxis :

Tupla[n:m]

n indice o posición de inicio de la nueva tupla
m posición final.

n siempre es menor que m
si no se especifica n sera 0 por defecto , si no se especifica m sera el tamaño de la lista menos uno.


"""

#Ejercicio 3, extracción de fragmento de tupla en una nueva tupla.


print("---------------------------------------------------------------------")

print(" EXTRACCIÓN DE FRAGMENTO DE TUPLA")

tupla = (1,2,3,4,5,6,7,8,9)
print(tupla)
print(tupla [4:9])
print(tupla [:3])
print(tupla [2:])


# Operador + con tuplas, permite realizar uniones de tuplas. TuplaConcatenada = Tupla1 + Tupla 2
# Conocer el numero de elementos que componen una tupla . NumeroElementos = len(Tupla)

print("---------------------------------------------------------------------")
print(" CONCATENAR TUPLAS - NUMERO DE ELEMENTOS DE LA TUPLA")

tupla1 = (29, "Televisor", 8763)
tupla2 = (1,2,3,"Videogame")
print("Numero de elementos de la tupla1 : ",len(tupla1))
print("Tupla1 : ",tupla1)
print("Número de elementos de la tupla2 : ",len(tupla2))
print("Tupla2 : ",tupla2)
tuplaConcatenada = tupla1 + tupla2
print("Número de elementos de tuplaConcatenada : ", len(tuplaConcatenada))
print("tuplaConcatenada : ", tuplaConcatenada)
print("---------------------------------------------------------------------")

# Ejercicio 4, Operador * , permite concatenar un número de veces finito una tupla con si misma. TuplaResultante = Tupla * NúmeroEntero

print(" OPERADOR * , CONCATENAR TUPLA CON SI MISMA")

tupla = (1,2,3,4,5,6,7,8,9,0)
print(tupla)
tuplaResultante = tupla * 4
print(tuplaResultante)

print("---------------------------------------------------------------------")

# DICCIONARIOS

print("DICCIONARIOS EN PYTHON")

"""
Son un conjunto de datos ordenado cuyos indices no son númericos sino identificadores, pueden contener datos de cualquier tipo. los elementos de
un diccionario en Python, estan compuestos por clave y valor, con la caracteristica de que las claves no pueden repetirse.

Se delimitan entre llaves {} , con cada elemento separado por coma , y la clave separada del valor mediante dos puntos :
Ej. {"clave1:"valor1", "Clave2:"Valor2", "Clave3:Valor3"}

Las claves pueden ser de diferente tipo de datos, pero deben ser elementos inmutables, pueden ser

*cadenas de texto
*Números (enteros, reales, complejos)
*Booleanos
*Bytes
*Tupla

"""

# EJERCICIOS CON DICCIONARIOS, 1 : MANIPULACIÓN DE ELEMENTOS 2: USO DE MÉTODOS PROPIOS DE LOS DICCIONARIOS.
print("---------------------------------------------------------------------")
print(" MANUPULACIÓN DE ELEMENTOS DE DICCIONARIOS")

# EJERCICIO 1, CREAR DICCIONARIO, MOSTRAR ELEMENTOS, PARA ACCEDERA AL ELEMENTO SE UTILIZA LA CLAVE DEL ELEMENTO.

diasSemanaIngles = {"Lunes": "Monday",
                    "Martes":"Tuesday",
                    "Miercoles":"Wednesday",
                    "Jueves":"Thursday",
                    "Viernes":"Frayday"
                    }
print(diasSemanaIngles["Lunes"])
print(diasSemanaIngles["Miercoles"])
print(diasSemanaIngles["Viernes"])

print("********************************************************************")

# EJERCICIO 2, AÑADIR, MODIFICAR Y ELIMINAR ELEMENTOS DE UN DICCIONARIO

"""
Añadir : Diccionario [NuevaClave] = NuevoValor

Modificar : Diccionario [ClaveQueSeVaAModificar] = Nuevo valor

Eliminar : del Diccionario[ClaveAEliminar]

"""
print("AÑADIR, MODIFICAR Y ELIMINAR ELEMENTOS DE UN DICCIONARIO")

diasSemanaIngles = {"Lunes": "Monday",
                    "Martes":"Tuesday",
                    "Miercoles":"Wednesday",
                    "Jueves":"Thursday",
                    "Viernes":"Frayday"
                    }
print (diasSemanaIngles)
diasSemanaIngles ["Sábado"] = "Saturday"
print (diasSemanaIngles)
diasSemanaIngles ["Domingo"] = "Sunday"
print(diasSemanaIngles)
diasSemanaIngles ["Lunes"] = "MondayBORRAR"
print(diasSemanaIngles)
del diasSemanaIngles ["Lunes"]
print(diasSemanaIngles)


print("********************************************************************")

"""
En los diccionarios de Python, tambien es posible usar los métodos len, max y min, len devuelve el numero de elementos que conforman
el diccionario, max devuelve el elemento con el mayor valor del diccionario, min el elemento con menor valor.

max y min se son devueltos siempre que se puedan calcular dependiendo de los elementos que componen el diccionario.
"""

# EJERCICIO 3, 
print("********************************************************************")

print(" METODOS LEN , MAX , MIN ")


diasSemanaIngles = {"Lunes": "Monday",
                    "Martes":"Tuesday",
                    "Miercoles":"Wednesday",
                    "Jueves":"Thursday",
                    "Viernes":"Frayday"
                    }
print(diasSemanaIngles)
print("Número de elementos del diccionario : ", len(diasSemanaIngles))
print("Elemento mayor del dixionario : ", max(diasSemanaIngles))
print("Elemento menor del diccionario : ", min(diasSemanaIngles))

print("********************************************************************")

# MÉTODOS PROPIOS DICCIONARIOS

"""
Los tipos de datos diccionario en Python, tienen una serie de funciones que ayudan a manipularlos realizando complejas operaciones
de manera sencilla y con una sola instrucción, el formato comun es : Diccionario.NombreFuncion(Parámetros)

copy : realiza una copia exacta del diccionario en uno nuevo.

        Valor devuelto : diccionario copiado
        Parámetros : no tiene

pop : Obtiene el valor de la clave pasada como parámetro, y ademas elimina el elemento del diccionario.

        Valor devuelto : Valor del elemento o error en caso de no encontrar la clave.
        Parámetros : clave a buscar en el diccionario.

popitem : obtiene un elemento aleatorio del diccionario y lo elimina del mismo.

        Valor devuelto : elemento del diccionari, en caso de diccionario vacio retorna error.
        Parámetros : no tiene

get : obtiene el valor de la clave pasada como parametro.

        Valor devuelto : valor del elemento en caso de existir dicha clave, en caso de no existir devolvera 'None'
        existe la posibilidad de especificar mediante un segundo parámetro un valor diferente a 'None' como retorno
        Parámetros : 2 parametros, primero es obligatorio, es la clave del elemento a buscar, segundo es opcional y es
        el valor que se desea retornar en caso de no existir dicha clave.

update : Realiza una actualización del diccionario utilizando otro diccionario, aquellos elementos que se utilizen para actualizar el
principal sustituiran los existentes, y aquellos que no existen serán añadidos como nuevos elementos.

        Valor devuelto : Nuevo diccionario
        Parámetros : diccionario

setdefault : Intenta insertar un elemento (clarve y valor) en el diccionario. En caso de no existir dicho elemento, la funcion inserta y devuelve
el valor del elemento y en caso de existir, lo unico que hace es devolver el valor actual.

        Valor devuelto : diccionario resultante
        Parámetros : dos parámetros que son la clave y el valor. Es posible no especificar el valor y por defecto se insertará el valor None
        como valor del elemento.

clear : Elimina todos los elementos del diccionario.

        Valor devuelto : diccionario vacio
        Parámetros : no tiene

items : Devuelve un objeto iterable (que puede utilizarce en bucles.) compuesto por todos los elementos del diccionario

        Valor devuelto : Objeto iterable compuesto por todos los elementos del diccionario.
        Parámetros : no tiene.

keys : Devuelve un objeto iterable, compuesto por todas las claves del diccionario.

        Valor devuelto : Objeto iterable con todas las claves del diccionario.
        Parámetros : no tiene

values : Devuelve un objeto iterable con todos los valores del diccionario.

        Valor devuelto : objeto iterable con todos los valores del diccionario.
        Parámetros : no tiene.

"""

print("-------------------------------------------------------------------------------")

# EJERCICIO MÉTODOS PROPIOS DICCIONARIOS

print(" EJEMPLOS MÉTODOS PROPIOS DICCIONARIOS")
print("-------------------------------------------------------------------------------")


diasSemanaIngles = {"Lunes": "Monday",
                    "Martes":"Tuesday",
                    "Miercoles":"Wednesday",
                    "Jueves":"Thursday",
                    "Viernes":"Frayday"
                    }
print("Diccionario original : ", diasSemanaIngles)
diccionarioCopia = diasSemanaIngles.copy()
print("Diccionario copia : " , diccionarioCopia)
print("Valor del lunes (pop)", diasSemanaIngles.pop("Lunes"))
print("Diccionario despues de pop : ", diasSemanaIngles)
print("Elemento al azar con popitem : ", diasSemanaIngles.popitem())
print("Diccionario despues de popitem : ", diasSemanaIngles)
print("Valor de Martes (get) :", diasSemanaIngles.get("Martes"))
print("Valor del Lunes (get) (no existe):", diasSemanaIngles.get("Lunes"))
print("Valor del Lunes (get) (no existe):", diasSemanaIngles.get("Lunes","No existe"))
diasSemanaIngles.update({"Lunes":"MondayNuevo","Martes":"TuesdayNuevo"})
print("Diccionario despues de update :", diasSemanaIngles)
print("setdefault del Sábado : ", diasSemanaIngles.setdefault("Sábado","Saturday"))
print("Diccionario despues de setdefault (nuevo elemento):", diasSemanaIngles)
print("setdefault del Lunes : ", diasSemanaIngles.setdefault("Lunes","Lunes"))
print("Diccionario despues de setdefault (elemento existente): ", diasSemanaIngles)
print("Elemento iterable (items):", diasSemanaIngles.items())
print("Elemento iterable (claves):", diasSemanaIngles.keys())
print("Elemento iterable (valores):", diasSemanaIngles.values())
print("Diccionario despues del clear : ", diasSemanaIngles.clear())





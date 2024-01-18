# TEMA TIPOS DE DATOS // SUBTEMA CADENAS DE TEXTO.

"""
En Python, hay dos formas de definir cadenas de texto, usando comillas dobles "" o usando comillas sencillas ''.
las dos formas son validas y no tienen diferencia en el resultado
"""
print("CADENAS DE TEXTO")

cadena1 = "Hola soy una cadena con comillas dobles"
cadena2 = 'Hola soy una cadena con comillas sencillas'
print(cadena1)
print(cadena2)

"""
Las cadenas de texto estan compuestas por una secuencia de caracteres, estos son accecibles de forma unitaria dentro de la cadena. para acceder
a un caracter en concreto, se debe indicar la posición que ocupa dentro de la cadena de texto, las posiciones de los strings como tambien se conoce
a las cadenas de texto, empiesan desde la posición cero, [0]
"""
print("Ejercicio practico cadenas de texto Posición")

print("cadena de texto sera la palabra Python")

cadena = "Python"
print("Carácter posición 0:", cadena [0])
print("Carácter posición 1:", cadena [1])
print("Carácter posición 2:", cadena [2])
print("Carácter posición 3:", cadena [3])
print("Carácter posición 4:", cadena [4])
print("Carácter posición 5:", cadena [5])
print("*******************************")

# OPERADORES CON CADENAS
"""
En Python, las cadenas de caracteres, pueden utilizar los operadores de multiplicación y suma * + , este ultimo para concatenar cadenas y el
primero para multiplicarlas.
La concatenación permite unir varias cadenas de texto en una unica cadena resultante. la operación de multiplicar dara como resultado una cadena
libs
"""
print("Ejercicio practico")
print("")
print("")
print("////////////////////////////")


cadena1 = input("Introduzca la primera cadena: ")
cadena2 = input("Intrudusca la segunda cadena: ")
cadena3 = input("Introduzca la tercera cadena: ")
cadenasuma = cadena1 + " " + cadena2 + " " + cadena3
cadenamultiplicacion = (cadena2 + " ")*5
print("Carácter concatenada:",cadenasuma)
print("Carácter multiplicada:",cadenamultiplicacion)

"""
La operación de concatenación puede realizarse de manera simplificada, utilizando el operador "+=", para concatenar la cadena de texto a la
cadena que se esta asignando.
"""
cadena1 = input("Introduzca la primera cadena: ")
cadena2 = input("Intrudusca la segunda cadena: ")
cadena3 = input("Introduzca la tercera cadena: ")
cadenasuma = cadena1
cadenasuma += " "
cadenasuma += cadena2
cadenasuma += " "
cadenasuma += cadena3
print("Cadena concatenada : ",cadenasuma)

#Python ofrece un operador que permite comprobar si una caden contiene otra cadena o un caracter en concreto. es [ in ] ej: cadena1 in cadena2

print("Ejercicio practico operador in")
cadena1 = input("Introduzca la primera cadena: ")
cadena2 = input("Introduzca la segunda cadena: ")
print("¿ Está la segunda cadena contenida en la primera? ", cadena2 in cadena1)

#Caracteres especiales. se utiliza el caracter barra invertida [ alt + 92 windows ], \


print("Ejercicio practico unificar cadenas")

cadena1 = input("Introduzca la primera cadena: ")
cadena2 = input('Introduzca la segunda cadena: ')
cadena3 = input ('Introduzca la tercera cadena: ')
cadenaconsaltos = "\n\t" + cadena1 + "\n\t" + cadena2 + "\n\t" + cadena3
print("Cadena con saltos:", cadenaconsaltos)

# En Python, es posible ignorar caracteres especiales en los strings o cadenas, añadiendo " r " antes de la definición de la cadena

print(" Ejemplo ignorar caracteres especiales en cadenas de texto")
print("/////////////////////////////////////////////////////////")


cadena1 = input("Introduzca la primera cadena: ")
cadena2 = input('Introduzca la segunda cadena: ')
cadena3 = input ('Introduzca la tercera cadena: ')
cadenaconsaltos = r"\n\t" + cadena1 + r"\n\t" + cadena2 + r"\n\t" + cadena3
print("Cadena con saltos r:", cadenaconsaltos)



# FUNCIONES
"""
Las cadenas de texto en Python, poseen una serie de funciones que nos permiten manipularlas, realizando de forma sencilla, opéraciones
complejas, el formato es:

ValorDevuelto = CadenaTexto.NombreFuncion(Parametros)

ValorDevuelto: La ejecución de la función tendra un resultado.Este puede ser booleano, numero, otra cadena de texto o una lista
de elementos.

CadenaTexto : Es la cadena sobre la que se ejecutará la función.

NombreFunción : Nombre de la función que se quiere ejecutar.

Parámetros : No todas las funciones tienen parámetros para ejecutarse, esto depende de la función que se quiera ejecutar.

"""
#Las funciones de cadenas que brinda Python son:

"""
capitalize : Permite poner la primera letra o caracter de la cadena en mayuscula.
             valor devuelto: Cadena de texto modificada
             Parámetros: no tiene

title : Permite poner la primera letra de cada palabra de la cadena en mayuscuala, y el resto en minuscula.
        valor devuelto: Cadena de texto modificada
        Parámetros: no tiene.

upper: Permite poner en mayúsculas por completo la cadena de texto.
        Valor devuelto: Cadena modificada
        parámetros: no tiene

lower : Permite poner en minúsculas por completo la cadena de texto.
        valor devuelto: cadena modificada
        parámetros : no tiene

len : Sirve para saber el numero de caracteres que contiene la cadena de texto.
        valor devuelto : Entero que indica el numero de caracteres que conforman la cadena de texto
        parámetros : no tiene

count : permite saber el número de veces que aparece una cadena de texto dentro de otra.
        valor devuelto: Entero que indica el numero de apariciones.
        parámetros : no tiene.

isalnum : Permite comprobar si todos los caracteres de la cadena de texto son caracteres alfanumericos o no. Se debe tener en cuento que los
caracteres de punto y espacio en blanco no son caracteres alfanumericos.
        valor devuelto: Valor booleano que indica si todos los caracteres son alfanumericos o no.
        parámetros : no tiene

isalpha : Permite comprobar si todos los caracteres de una cadena de texto son alfabeticos. Se debe tener en cuenta que
          ni los numeros, los espacios en blanco o signos de puntuación son alfabeticos. unicamente las letras.

          valor devuelto : Valor booleano que indica si son o no son alfabeticos los caracteres de una cadena
          parámetros : no tiene.

isdigit : Permite comprobar si todos los caracteres de una cadena representan digitos.

        valor devuelto : booleano que indica si todos los caracteres son digitos o no.
        parámetros : no tiene

isnumeric : Comprobar si todos los caracteres de una cadena son caracteres con representación numérica.

        valor devuelto : booleano que indica si son todos los caracteres numericos o no.
        parámetros : no tiene


isdecimal : Permite comprobar si todos los caracteres de una cadena son caracteres con representacion decimal.

        valor devuelto : valor booleano.
        parámetros : no tiene

islower : Permite comprobar si todos los caracteres de una caden estan en minuscula o no.

        valor devuelto : booleano
        parametros : no tiene

isupper : Permite comprobar si todos los caracteres de una cadena estan en mayuscula.

        valor devuelto : booleano
        parámetros : no tiene

istitle : Permite comprobar si el primer caracter de todas las palabras es mayúscula y el resto minusculas.

        valor devuelto : booleano
        parámetros : no tiene

isprintable : Permite comprobar si todos los caracteres de una cadena son imprimibles o no.
        
        valor devuelto : booleano
        parámetros : no tiene

isspace : Permite comprobar si la cadena de texto esta compuesta exclusivamente por caracteres en blanco.

        valor devuelto : booleano
        parámetros : no tiene

istrip : Permite eliminar los caracteres en blanco al principio de la cadena.

        valor devuelto: cadena modificada
        parámetros : no tiene.

rstrip : Permite eliminar los caracteres en blanco al final de la cadena.

        valor devuelto: cadena modificada
        parámetros : no tiene

strip : Permite eliminar los carácteres en blanco al principio y al final de la cadena.

        valor devuelto: cadena modificada
        parámetros : no tiene

max : Permite conocer el caracter alfabético mayor de la cadena.

        valor devuelto: Caracter alfanumerico con mayor valor en la cadena.
        parametros: no tiene.

min : Permite conocer el caracter alfabético menor de la cadena.

        valor devuelto: Caracter alfanumerico con menor valor en la cadena.
        parametros: no tiene.

startswhith : Permite comprobar si una cadena de texto empieza por una cadena de texto concreta.

        Valor devuelto: Valor booleano que indica si empieza o no por esa cadena.
        Parámetros : Tiene un parámetro obligatorio que es la cadena que se quiere comprobar si es por la que
        empieza la otra cadena.

endwith: Permite comprobar si una cadena de texto termina por una cadena de texto concreta.

        Valor devuelto : booleano que indica si termina o no por esa cadena.
        parámetros : Cadena que se quiere comprobar.

replace : permite reemplazar una cadena de texto de la cadena por otra cadena.

        valor devuelto : cadena de texto modificada.
        parámetros : Tiene 2 parametros, el primero es la cadena que se quiere reemplazar, el segundo es
        la cadena que se usará para hacer el reeemplazo.

swapcase : Permite invertir las mayusculas y las minuscuals de la caeena de texto, es decir, las mayusculas pasaran a ser minusculas, y viseversa.

        valor devuelto : cadena de texto modificada
        parametros : no tiene

split : permite convertir una cadena de texto en una lista de elementos que se encuentra separado por un caracter concreto.

        valor devuelto : lista de elementos de tipo cadena de texto.
        parámetros : Tiene un parametro opcional que indica el caracter a utilizar para dividir la cadena de texto, en caso de
        no especificarse se usara el caracter espacio en blanco por defecto.

splitlines : Permite convertir la cadena de texto en una lista de elementos que se encuentra  separados por saltos de linea.

        valor devuelto : Lista de elementos tipo cadena de texto.
        parámetros : No tiene.

find : Permite encontrar una cadena de texto dentro de otra buscando de izquierda a derecha.

        valor devuelto : En caso de encontrar la cadena devolvera la posición dentro de la cadena en la que empieza la cadena buscada, en caso de no encontrarla,
        devolvera -1.
        parámetros : cadena a buscar.

rfind : Permite encontrar una cadena de texto dentro de otra buscando de derecha a izquierda.

        valor devuelto : en caso de encontrar la cadena devolverá la posición dentro de la cadena en la que empieza la cadena buscada, en caso
        de no encontrarla devolvera -1
        parámetros: cadena a buscar.

center : Permite centrar el texto de la cadena en una cadena de texto de longitud mayor, añadiendo espacios en blanco a la izquierda y derecha del mismo

        valor devuelto : cadena de texto modificada.
        parámetros : Tiene un parametro obligatorio, que es la longitud de la cadena de texto que queremos obtener y tiene un parametro
        opcional para indicar el carácter con el que  rellenar para llegar a esa longitud. si no se especifica el segundo parametro, lo realiza con
        espacios en blanco por defecto.

ljust : Permite ajustar una cadena de texto a la izquierda con una longitud indicada por parámetros y añadiendo tantos caracteres en blanco a la derecha
        como sea necesario para llegar a esa longitud.

        valor devuelto : cadena de texto modificada.
        parámetros : Tiene un parámetro obligatorio que es la longitud de la cadena de texto que queremos obtener, y un parámetro opcional que es el carácter
        con el que rellenar para llegar a esa longitud. Si no se especifica el carácter, lo realiza con espacios en blanco por defecto.

rjust : Permite ajustar una cadena de texto a la derecha con una longitud indicada por parámetros y añadiendo tantos caracteres en blanco a la izquierda
        como sea necesario para llegar a esa longitud.

        valor devuelto : cadena de texto modificada.
        parámetros : Tiene un parámetro obligatorio que es la longitud de la cadena de texto que queremos obtener, y un parámetro opcional que es el carácter
        con el que rellenar para llegar a esa longitud. Si no se especifica el carácter, lo realiza con espacios en blanco por defecto.

expandtabs : Permite sustituir los tabuladores que tienen la cadena de texto por espacios en blanco.

        Valor devuelto: cadena de texto modificada
        Parámetros : Tiene un parámetro opcional para indicar el número de espacios en blanco por los que sustituye cada tabulador, por defecto
        lo hace sustituyendo por cuatro espacios en blanco.

zfill : Permite crear una cadena de texto de longitud indicada por parámetros compuesta por ceros a la izquierda y a la derecha la cadena de texto.

        Valor devuelto : cadena de texto modificada.
        Parámetros : longitud de la cadena resultante.

      
"""

# EJERCICIOS PRACTICOS MÉTODOS STRING

print("****************************************************************")
print("")
print('Ejercicios practicos funciones con strings')
print("")
print("")

print('Realizar operaciones de conversión del texto y comprobaciones.')
print("")
print("")

cadena1 = input("Introduzca la primera cadena: ")
cadena2 = input ("Introduzca la segunda cadena: ")
cadena3 = input ("Introduzca la tercera cadena: ")
print("Longitud de la cadena 2 (len)", len(cadena2))
print("Cadena 3 todo a mayúsculas (upper):", cadena3.upper())
print("Cadena 3 todo a minúsculas (lower):", cadena3.lower())
print("Cadena2 cambia de mayúsculas a minúsculas y viceversa (swapcase):",cadena2.swapcase())
print("Cadena1 la primera a mayúsculas (capitalize): ", cadena1.capitalize())
print("cadena2 la primera de cada palabra a mayúscula (title): ", cadena2.title())
print("¿Cadena1 todo minúsculas? (islower):" , cadena1.islower())
print("¿Cadena3 todo mayúsculas? (isupper):" , cadena3.isupper())
print("¿Cadena2 todo caracter es imprimible? (isprintable): ", cadena2.isprintable())
print("¿Cadena3 todo caracteres alfanumericos? (isalnum): ", cadena3.isalnum())
print("¿Cadena1 todo caracteres alfabéticos? (isalpha): ", cadena1.isalpha())
print("¿Cadena3 la primera de cada palabra en mayúsculas y el resto en minusculas (istitle): ?", cadena3.istitle())
print("¿Cadena2 todos los caracteres son espacios en blanco? (isspace):", cadena2.isspace())
print("¿Cadena1 todo digitos? (isdigit):", cadena1.isdigit())
print("¿Cadena2 todo caracteres con representación numérica? (isnumeric):",cadena2.isnumeric())
print("¿Cadena3 todos los caracteres son numeros con representación decimal? (isdecimal): ", cadena3.isdecimal())
print("Caracter mas alto de la cadena1 (max):", max(cadena1))
print("Caracter mas bajo de la cadena3 (min):",min(cadena3))
print("")
print("")
print("//////////////////////////////////////////////////////////////")
print("Ejercicio practico, eliminar carácteres de espacios en  blanco de la cadena")

cadena = input("Introduzca una cadena con espacios en blanco al principio y al final: ")
print("Longitud de la cadena:", len(cadena))
cadenalstrip = cadena.lstrip()
print("Cadena (lstrip):",cadenalstrip,end = '.')
print("\nLongitud de la cadena (lstrip):",len(cadenalstrip))

cadenarstrip = cadena.rstrip()
print("cadena (rstrip):", cadenarstrip, end = '*')
print("\nLongitud cadena (rstrip): ", len(cadenarstrip))

cadenastrip = cadena.strip()
print("Cadema (strip): ", cadenastrip, end = '.')
print("\nLongitud de la cadena (strip):", len(cadenastrip))


print("")
print("")
print("*************************************************")
print("Ejercicio 3 comprobar si una cadena empieza y termina por otra y contar cuantas veces aparece dicha cadena en la cadena base")

cadena = input("Introduzca una cadena: ")
buscar = input("Introduzca una cadena para buscar: ")
print("¿Comienza la cadena por la cadena a buscar? (startwith): ",cadena.startswith(buscar))
print("¿Termina la cadena por la cadena a buscar ? (endswith): ", cadena.endswith(buscar))
print("¿Cuantas veces aparece la cadena a buscar en la cadena? (count): ", cadena.count(buscar))

print("")
print("")
print("********************************************************")
print("Ejercicio 4, realización de busqueda de izquierda a derecha y de derecha a izquierda de una cadena de texto en otra")
print("")

cadena = input("Introduzca una cadena: ")
buscar = input("Introduzca una cadena para buscar")
print("La cadena aparece en la pocición (find):", cadena.find(buscar))
print("La cadena aparece en la pocición (rfind):", cadena.rfind(buscar))
print("")
print("")
print("")
print("************************************************************")
print("Ejercicio 5, reemplazo de una cadena de texto base por otra cadena de texto")

cadena = input( "Introduzca una cadena: " )
reemplazar = input("Introduzca una subcadena de la anterior para reemplazar: ")
reemplazo = input("Introduzca la cadena por la que se reemplazara la anterior: ")
print("Cadena original: ", cadena)
print("Cadena nueva (replace): ", cadena.replace(reemplazar, reemplazo))

print("")
print("")
print("")
print("///////////////////////////////////////////////////////////////////////////")
print("Ejercicio 6, crear una lista de cadenas de texto a partir de las palabras que componen la cadena de texto.")

cadena = input("Introduzca una cadena con varias palabras: ")
print("Cadena dividida por espacios en blanco (split):", cadena.split())

#PORCIONES DE CADENAS
print("///////////////////////////////////////////////////////////////////////////")
print("PORCIONES DE CADENAS")
"""
Python ofrece la funcionalidad de extraer fragmentos de una cadena de texto, es decir, partiendo de una cadena de texto base nos ofrece
la posibilidad de extraer subcadenas para trabajar con estas.

Para extraer estas subcadenas se utiliza el opereador [n:m], donde n es la posicion del caracter inicial y m la posicion del caracter final. El operador
[n:m] permite omitir uno de los indices, en caso de omitir la n la subcadena empezará desde el principio de la cadena y en caso de omitir la m la subcadena
ira hasta el fnal de la cadena.
"""

cadena = "F.C. Barcelona, Atletico de Madrid, Real Madrid"
print("primer equipo(cadena[0:13]):", cadena [0:13])
print("Segundo equipo (cadena [15:33]):", cadena [15:33])
print("Tercer equipo cadena [35:46]:", cadena [35:46])
print("Desde el principio (cadena [:13]):", cadena [:13])
print("Desde el final (cadena [15:]):", cadena [15:])

#FORMATEO DE CADENAS
"""
Hasta el momento hemos construido cadnas concatenandolas, pero Python ofrece dos formas de crear cadenas que estan compuestas por varias
cadenas. La primera es utilizando un operador concreto para componer la cadena y la segunda es utilizando la función format.

OPERADOR %

La primera forma de componer cadenas es usando en operador % . El operador indica que dentro de la cadena base, se realizará la sustitucion
de ese operador por la cadena que se especifique. Al operador hay que indicarle el tipo de dato que lleva asociado, la siguiente tabla muestra
el valor que tendra que tener el operador en cada caso de tipo de dato.

%c ...............Un carácter
%s ...............Cadena de texto
%d ...............Numero entero
%f ...............Numero real
%o ...............Numero octal
%x ...............Numero hexadecimal

"""

print("///////////////////////////////////////////////////////////////////////////")
print(" Ejercicio construir una cadena sustituyendo los operadores por los valores enteros introducidos por el usuario y tambien por el resultado de la multiplicación")
print("")
multiplicando = int(input("Multiplicando: "))
multiplicador = int(input("Multiplicador: "))
print("El resultado de multiplicar %d por %d es %d" % (multiplicando, multiplicador, multiplicando*multiplicador))

print("------------------------------------------------------------------------------------------------------------")
# FORMAT format()

"""
La funcion format, devuelve una versión formateada de una cadena de caracteres, usando sustituciones desde argumentos args y kwargs.La forma de
especificar dentro de la cadena de texto base la posición qeu deben ocupar los argumentos se identifican con llaves {} dentro de la cadena y el numero
del argumento que sustituirá a las llaves.
"""
print("")
print("")
print(" Ejercicio utilizando format")

print('+++++++++++++++++++++++++++++++++++++++++++++++++++..')
multiplicando = int(input("Multiplicando: "))
multiplicador = int(input("Multiplicador: "))
print("El resultado de multiplicar {0} por {1} es {2}".format(multiplicando,multiplicador,multiplicando*multiplicador))





























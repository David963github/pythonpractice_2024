# PYTHON PRACTICO , TEMA : FUNCIONES.

"""
Una función es un bloque de codigo fuente que contiene un conjunto de instrucciones que realiza algo concreto y que puede ser utilizada
desde el codigo fuente que se escribe tantas veces como se necesite.

Las caracteristicas de las funciones son :

    * Tienen un nombre para ser identificadas.
    * Ejecutan una tarea concreta.
    * Pueden recibir parametros para su ejecucion
    * Puede devolver un resultado como resultado de su ejecución.

    Tanta los parametros como el resultado que devuelve una función, son opcionales, se puede encontrar funciones que no reciben
    datos o que no devuelven nada.

    Las funciones pertenecen a un tipo de programacion denominada programacion estructurada, y tiene estas ventajas:

        Modularización : permiten segmentar el codigo complejo en un conjunto de modulos, que hace que el código sea mas sencillo de
        leer, depurar y mantener.

        Reutilización : Permite reutilizar funciones en otros programas o modulos del mismo programa.

    La sintaxis de las funciones es :

            def NombreFuncion ( parámetros ):
                BloqueInstrucciones
                return ValorRetorno

    Para poder utilizar funciones en Python desde el codigo fuente se debe hacer de la siguiente manera :

            Variable = NombreFuncion (paramentros)

                Variable : Almacenará el valor que devuelve la funcion. Es opcional, ya que se suprime si la funcion no devuelve nada.

                NombreFuncion : Nombre de la funcion que se va a utilizar

                Parámetros : Parámetros de entreada que tiene la funcion , que se escriben separados por coma en caso de ser
                mas de uno. Es opcional, por lo que si la funcion no recibe parametros se suprimira.

        Cuando se trabaja con funciones se debe tener en cuenta los siguientes puntos :

            ° La definición de funciones suele hacerce al inicio del programa.
            ° La indentacion de la funcion y el bloque de instrucciones de adentro de la funcion siguen las mismas reglas
            que el resto de codigo.
            ° Cuidado con el nombre de las variables, ya que si hay nombres duplicados puede generar errores o resultados no
            esperados, por lo generar las variables de una funcion solo son validas dentro de la funcion.

            
"""

# EJERCICIO 1 , FUNCIÓN QUE MUESTRA UN MENSAJE EN PANTALLA, USARLA VARIAS VECES DESDE EL CODIGO FUENTE DEL PROGRAMA PRINCIPAL.

print("FUNCIÓN QUE MUSTRA UN MENSAJE EN PANTALLA")

print("--------------------------------------------------------")

def Hola():
    print("HOla")
print("Primera invocación :", end=" ")
Hola()#.........esta es la forma de invocar una función 
print("Segunda invocación : ")
Hola()

print("--------------------------------------------------------")

# EJERCICIO 2 SENTENCIA RETURN.

"""
Return permite devolver información como producto de la ejecución de esta.

"""
print("--------------------------------------------------------")

def Hola():
    return "Hola Python"

print("Primera invocación : "+ Hola())

print("Segunda invocación : "+ Hola())

print("--------------------------------------------------------")

# EJERCICIO 3 , USO DE PARÁMETROS EN LAS FUNCIONES.
"""
Mediante los parametros podemos pasarle datos a las funciones, para que realicen operaciones utilizando datos den entrada.

"""

# FUNCIÓN QUE COMPRUEBA SI UN NUMERO PASADO POR PARAMETRO ES PAR O IMPAR.

print("fUNCIÓN COMPROBAR SI UN NUMERO ES PAR O IMPAR ")

print("--------------------------------------------------------")

def EsParOImpar (param):
    if param%2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

numero = int(input("Introduce un numero : "))
EsParOImpar(numero)

print("--------------------------------------------------------")
            
# EJERCICIO 4, CREAR FUNCIÓN QUE MULTIPLIQUE DOS VALORES PASADOS COMO PARAMETRO Y RETORNE EL RESULTADO.

print("FUNCIÓN QUE MULTIPLICA DOS VALORES, Y RETORNA EL RESULTADO")
print("--------------------------------------------------------")

def Multiplicar (param1 , param2):
    return param1 * param2

multiplicando = int(input("Introduce el multiplicando : "))

multiplicador = int(input("Introduce el multiplicador : "))

resultado = Multiplicar (multiplicando , multiplicador)
print("El resultado es :" , resultado)
print("--------------------------------------------------------")
                    
"""
En los siguientes ejercicios, se explicará, formas un poco mas avanzadas de pasar parámetrosa las
funciones y de igual forma a la funcionalidad de return de las mismas.

El siguiente ejercicio, se trata de aprender cómo se le pueden pasar a una función
de Python un numero variable de parametros de entrada. En la definición de la función ,
se debe cambiar cómo se especifican los parámetros. Para ello se debe añadir asterisco delante de un parámetro
lo que representa que es un numero variable de parámetros. a la hora de utilizar la función se puede poner
tantos parámetros como se nececite entre parentesis y separados por coma.
"""
#**********************************************************************
print('----------------------------------------------------------------')
print('EJERCICIO 5 , PASAR UN NÚMERO VARIABLE DE PARÁMETROS A UNA FUNCIÓN')
print('----------------------------------------------------------------')

def Sumar (*valores):
    resultado = 0
    for item in valores:
        resultado = resultado + item
    return resultado

resultado = Sumar (6,4,8,89,777,45,5,15,35,25,78,95)
print('El resultado de la suma es: ', resultado)

print('----------------------------------------------------------------')

"""
El siguiente ejercicio es para aprender que es posible devolver mas de un  valor
con la sentencia return. Para esto, se debe agregar tantos elementos como se
nesecite a la sentencia return, separados por coma.Cuando se utiliza la función
y asignar resultado, se debe añadir el mismo número de elementos separados por
coma antes de el operador de asignación.
"""
print('----------------------------------------------------------------')
# EJERCICIO 6, DEVOLVER MAS DE UN VALOR CON LA SENTENCIA RETURN

print('EJERCICIO 6, DEVOLVER MAS DE UN VALOR CON LA SENTENCIA RETURN')

def SumarMultiplicar (*valores):
    resultadosuma = 0
    resultadomultiplicacion = 1

    for item in valores:
        resultadosuma = resultadosuma + item
        resultadomultiplicacion = resultadomultiplicacion * item
    return resultadosuma,resultadomultiplicacion
ressuma,resmulti = SumarMultiplicar (6,4,8,98,45,4,77,1)
print('El resultado de la suma es: ' , ressuma)
print('El resultado de la multiplicación es: ', resmulti)

print('----------------------------------------------------------------')

#EJERCICIO 7, UTILIZAR FUNCIONES DENTRO DE UNA FUNCIÓN

def SumarMultiplicar (param1,param2):
    return Sumar(param1,param2), Multiplicar(param1,param2)
def Sumar(sumando1,sumando2):
    return sumando1 + sumando2
def Multiplicar(multiplicando,multiplicador):
    return multiplicando * multiplicador

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
resultadosuma,resultadomultiplicacion = SumarMultiplicar(numero1,numero2)
print("El resultado de la suma es: ",resultadosuma)
print("El resultado de la multiplicación es: ",resultadomultiplicacion)
print('----------------------------------------------------------------')

# FUNCIONES CON VARIABLES GLOBALES

"""
Como se mencionabá, es necesario prestar atención a los nombres de las variables dentro
de las funciones y a las variables del programa.

En el siguiente ejercicio se declara una variable dentro de una función, con el mismo nombre
que otra variable del programa principal y se muestra en el programa principal como en función por
pantalla.
"""

# EJERCICIO 8, VARIABLES GLOBALES
print('VARIABLES GLOBALES')

def variables():
    variable =3
    print("Valor dentro de la función:"+ str(variable))

variable = 5
variables()
print("Variable en el programa principal: "+ str(variable))

print('----------------------------------------------------------------')

"""
Se mostrará un valor diferente cuando se ejecute, debido a que por defecto la definición de variables dentro de las
funciones tiene únicamente ámbito dentro de la función.
"""

#////////////////////////////////////////////////////////////////////////////////////////////////////

"""
Hay una forma para que las variables de las funciones, sean variables del programa principal. para esto
se debe añadir una sentencia dentro de la función y antes de definir la variable. Existen dos formas
para hacer esto:

    global NombreVariable
    nonlocal NombreVariable

La utilización de una u otra es indiferente.
"""
print('----------------------------------------------------------------')

# EJERCICIO 9, USO DE LA SENTENCIA global / nonlocal PARA VARIABLES.

print("USO DE SENTENCIA global / nonlocal PARA VARIABLES")

print('----------------------------------------------------------------')

def Variables():
    global variable
    print("Valor dentro de la función: " + str(variable))
    variable = 3
    print("Valor dentro de la función: " + str(variable))

variable = 5
print("Variable en el programa principal: " + str(variable))
Variables()
print("Variable en el programa principal: " + str (variable))

print('----------------------------------------------------------------')
































# PYTHON PRACTICO - TEMA - MANEJO DE EXCEPCIONES

"""
Una excepción es un error lógico que ocurre mientras se ejecuta un programa
y provoca su detención. La detención puede ser controlada y no producirce si
se realiza un control de excepciones correcto en el código fuente.

Controlar una excepción es guardar el estado en el que se encontraba el
programa en el momento justo del error e interrumpir el programa para ejecutar
un código fuente concreto. En muchos casos, dependiendo del error ocurrido, el
control de la excepción implicará, que el programa siga ejecutandose después
de controlarla, aunque en muchos casos esto no será posible.

El proceso de control de excepciones es similar en todos los lenguajes de
programación, en primer lugar es necesario incluir el código fuente de
ejecución normal dentro del bloque con la sentencia ...  try ... Posteriormente
se crea un bloque de código dentro de una sentencia ...  except ... que es
la que se ejecutará en caso de error.

El bloque except permite especificar el tipo de error que se controla con el
bloque de código, es por ello que se puede tener tantos bloques except como
errores se quiera controlar, aunque tambien es posible controloar un error
genérico que incluya a todos los errores. En el control de excepciones existe
la posibilidad de crear un bloque de código que se ejecute siempre al final,
independientemente de si ocurre error o no. Dicho bloque de código se escribe
como parte de la sentencia ...  finally ....

El aspecto del control de excepciones en Python se ve asi:

        try:
            BloqueInstrucciones
        except TipoError1 :
            BloqueInstruccionesError1
        except TipoError2
            BloqueInstruccionesError2
        except TipoErrorN:
            BloqueInstruccionesErrorN
        finally:
            BloqueCodigoFinally

    ---------------------------------------------

    try: indicador de comienzo del bloque de código fuente que se controlará

    BloqueInstruccionesPrograma : Conjunto de instrucciones que componen el
    programa

    except : Indicador de comienzo de excepción controlada.

    TipoError : Indicador del tipo de error que se controla con except. El
    parámetro es opcional, si no se especifica el tipo se controlara la
    excepción de forma genérica.

    BloqueInstruccionesError : Conjunto de instrucciones que se ejecuta si
    se produce el error indicado por tipo error.

    finally : Indicador de comienzo del bloque de código final. La sección
    es opcional.
    
    BloqueCodigoFinally : Conjunto de instrucciones que se ejecutarán al acabar
    cualquiera de los bloques de código anteriores.
"""
# TIPOS DE EXCEPCIONES

"""
En Python, existen diferentes tipos de excepciones que pueden controlarse, todas ellas
derivan de una serie de excepciones base.

    Las excepciones base son:

        Excepción : Tipo de excepción mas genérica, de esta derivan todas las excepciones
        de Python.

        ArithmeticError : Excepción genérica iapra errores aritméticos.

        BufferError : Genérica, para errores relacionados con buffers.

        LookupError : Genérica para errores relacionados con acceso a datos de colecciones.

        ---------------------------------------------------------------------------------

        El grupo de Excepcines anteriores da lugar a un grupo de excepciones concretas que son las siguientes:

            AssertionError : Excepción que se lanza cuando la instrucción assert falla.

            AttributeError : Se lanza cuando la instrucción input no devuelve datos leídos.

            FloatingPointError : Se lanza cuando se cierra una función de tipo generator o coroutine.

            ImportError : Se lanza cuando se intenta importar un módulo al programa y falla.

            ModuleNotFoundError : Se lanza cuando se intenta importar un modulo y no se encuentra. deriva del anterior

            IndexError : Se lanza cuando se intenta acceder a la clave de un diccionario y no se encuentra

            KeyError : Se lanza cuando se intenta acceder a la clave de un diccionario y no se encuentra.

            KeyboardInterrupt : Se lanza cuando el usuario utiliza el comando de interrupción con el teclado (Control-C o delete)

            MemoryError : Se lanza cuando el programa ejecuta una instrucción, y ésta supera el máximo de memoria disponible.

            NameError : Se lanza cuando el nombre local o global no se encuentra.

            NotImplementedError : Se lanza cuando un método de una clase no ha sido implementado todavia y tiene que
            hacerlo
            -------------------------------------------------------------------------------------------------
            OSError : Se lanza cuando el sistema operativo lanza una excepción, al ejecutar una instrucción.
            existen las siguientes excepciones específicas que pueden lanzar el sistema operativo.

                BlockingIOError : Se lanza cuando una operación se bloquea en un objeto que no debería bloquearse.

                ChildProsessError : Excepción que se lanza cuando una operación de un proceso hijo devuelve un error.

                ConnectionError : Excepción generica que se lanza para errores relacionados a conexión.

                BrokenPipeError : Se lanza cuando se intenta escribir un socket o pipe (tubería) y ya ha cido cerrado.

                ConnectionAbortedError : Se lanza cuando durante un intento de conexión ésta es abortada por el otro extremo.

                ConnectionRefusedError : Se lanza cuando durante un intento de conexión ésta es rechazada por el otro extremo.

                FileExistError : Se lanza cuando se intenta crear un fichero o directorio y éste ya existe.

                IsADirectoryError : Se lanza cuando se intenta ejecutar una operación relacionada con ficheros en
                un directorio.

                NotADirectoryError : Se kabza cuando se intenta ejecutar una operacion relacionada con directorios
                a algo que no es un directorio.

                PermissionError : Se lanza cuando se intenta ejecutar una operación y no se tiene los permisos
                suficientes.

                ProcessLookupError : Se lanza cuando se ejecuta un porceso que no existe y se ha indicado que si.

                TimeoutError : Se lanza cuando se sobrepasa el tiempo de espera en alguna función del sistema.

            -----------------------------------------------------------------------------------------------------------

            OverflowError : Se lanza cuando el resultado de una operación matemática es demaciando grande para ser representado.

            RecursionErrro : Se lanza cuando el número de recursividad supera el máximo permitido.

            ReferenceError : Se lanza al intentar acceder a ciertos atributos por parte de la clase proxy y que ya se
            encuentran en el recolector de basura.

            RuntumeError : Se lanza cuando el error que ocurre no puede ser categorizado en ninguno de los tipos existentes.

            StopIteration : Se lanza cuando se intenta acceder al siguiente elemento de un iterador y ya no tiene más elementos
            sobre los que iterar.

            StopAsyncIteration : Se lanza cuando se intenta acceder al siguiente elemento de un iterador asincrono y ya
            no se tiene más elementos sobre los que iterar.

            SyntaxError : Se lanza cuando el analizador sintactico encuentra un error de sintaxis.

            IndentationError : Excepción genérica que se lanza cuando se encuentran errores de indentación dle código
            fuente.

            TabError : Se lanza cuando se encuentran errores de uso de las tabulaciones, y espaciados del código fuente.
            La excepción deriva de la anterior.

            SystemError : Se lanza cuando el interprete de Python encuentra un error interno mientras ejecuta el programa.

            TypeError : Se lanza cuando una operación o función se usa con un tipo de dato incorrecto.

            UnbounLocalError : se lanza cuando se utiliza una variable local en una función o metodo y no ha sido
            asignado ningun valor previamente.

            UnicodeError : Se lanza cuando se produce un error a la hora de codificar o decodificar Unicode.

            UnicodeEncodeError : Se lanza cuando se produce un error a la hora de realizar una codificación Unicode.

            UnicodeDecodeErrror : Se lanza cuando se produce un erro a la hora de realizar una decodificación de Unicode.

            UnicodeTranslateError : Se lanza cuando se produce un error a la hora de traducir Unicode.

            ValueError : Se lanza cuando una operación o función recibe un parámetro del tipo correcto, pero con un valor incorrecto.

            ZeroDivisionError : Se lanza cuando se realiza una división por cero
            
"""

# EJERCICIOS

# Error divición por cero. 


# print (19 / 0) -> Este código lanza un erro de tipo ZeroDivisionError.

# EJERCICIO 2 , CONTROL DE EXCEPCIÓN LANZADA DIVISIÓN POR CERO .

try :
    print(str(19 /0))
except :
    print("Error : No existe la división por cero, ingresa un número valido")
print('---------------------------------------------------------------------------------------------')

# EJERCICIO 3 , UTILIZAR SECCIÓN finally , que añade un bloque de código que se ejecutará siempre indpendientemente
# se produzca o no una excepción.

print('---------------------------------------------------------------------------------------------')
    
print('Iniciando programa')
print("\n Ha comenzado la primera parte del programa")

try:
    print(str(17/0))
except :
    print('Error : División por cero')
finally :
    print('Segunda parte del programa acabada')
    
print('---------------------------------------------------------------------------------------------')

"""
En el control de excepciones es posible añadir bloques else , Para ejecutar un bloque de código concreto
que no se quiere ejecutar como parte  del bloque finally. 
"""

# EJERCICIO 4 , USO DE BLOQUE ELSE.
print("Uso de bloque else en control de excepciones")
print('---------------------------------------------------------------------------------------------')

print ("! Iniciando el programa !")
print ("\n comenzando la primera parte del programa")

try:
    print(11 /0)
except:
    print("Error : División por cero")
else :
    print("Info : No se ha producido errores")
finally :
    print('Primera parte del programa acabada')

print("\n Comenzando la segunda parte del programa")
try:
    print(str(11/1))
except :
    print("Error división por cero")
else :
    print("INfo : No se ha producid errores")
finally :
    print("Segunda parte del programa acabada")
print('---------------------------------------------------------------------------------------------')

# EJERCICIO 5 , CONTROLAR EXCEPCIONES DE UN TIPO ESPECIFICO, EN SECCIONES EXCEPT.

# AÑADIR UN CONTROL PARA EL TIPO DE EXCEPCIÓN ZERO DIVISION ERROR.
print('---------------------------------------------------------------------------------------------')
print("Control tipo especifico de exepcion")
print('---------------------------------------------------------------------------------------------')

print("Iniciando el programa")

try :
    print(str(10/0))
except ZeroDivisionError:
    print ("Error : División por cero")
except :
    print("Error : General")
else :
    print("No se ha producido errores")
finally :
    print("Programa acabado")
print('---------------------------------------------------------------------------------------------')


























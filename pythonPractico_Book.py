print("TEMA 1: TIPOS DE DATOS - SUBTEMA 1: DATOS NUMÉRICOS")
print(" ʕ•ᴥ•ʔ")

# Tipos de datos más básicos en Python relacionados con los números son tres:
# Entero: Número entero con límite de valor.
# Reales: Número compuesto por parte entera y parte decimal.
# Complejo: Número compuesto por parte real y parte imaginaria.

# Antes de la explicación se verán operadores aritméticos
"""
Suma: + suma dos valores tipo numérico,
Resta: - resta,
Multiplicación: * multiplica,
División: / divide, devuelve un número real con decimales si los tiene.
División entera: // realiza división entera de dos valores, es decir, que devuelve el resultado sin decimales.
Módulo: % realiza el módulo de dos valores numéricos, es decir, obtiene el resto de la división.
Exponente: ** realiza el exponente de dos valores numéricos.
Negación.
"""

"""
Números enteros: son números sin decimales, positivos o negativos, se indican con int.

"""

x = 987
x = -x
print("frase", x)

numero1 = int(input("Primer sumando: "))
numero2 = int(input("Segundo sumando: "))
print("Resultado: ", numero1 + numero2)

# División entera
print("División entera")
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
print("Resultado: ", dividendo // divisor)

print("Exponente")

base = int(input("Base: "))
exponente = int(input("Exponente: "))
print("Resultado", base ** exponente)

print("Números Reales")

"""
Números reales: tienen decimales. Se representan con float y se separan con ".".
"""
print("Ejemplo resta con números reales leídos mediante input")

minuendo = float(input("Minuendo: "))
sustraendo = float(input("Sustraendo: "))
print("Resultado: ", minuendo - sustraendo)

print("División con reales")

dividendo = float(input("Dividendo: "))
divisor = float(input("Divisor: "))
print("Resultado", dividendo / divisor)

print("Multiplicación numérica con reales input")

multiplicando = float(input("Multiplicando: "))
multiplicador = float(input("Multiplicador: "))
print("Resultado: ", multiplicando * multiplicador)

print("*********************************")
print("REDONDEO DE NÚMEROS REALES")
print("")

"""
Los números reales tienen un número infinito de decimales, pero Python tiene
la instrucción round que permite acortar el número de decimales.
"""
print("Ejemplo práctico")

print("********************")

multiplicando = float(input("Multiplicando: "))
multiplicador = float(input("Multiplicador: "))

# round recibe dos parámetros: 1. número a redondear, 2. número de decimales.
resultado = round(multiplicando * multiplicador, 1)
print("Resultado de la multiplicación: ", resultado)

print("NÚMEROS COMPLEJOS")

"""
Están compuestos por una parte real y otra imaginaria. Cada una de las partes
es un número decimal y se representan con complex.
"""
numero = complex(float(input("Parte real: ")), float(input("Parte imaginaria: ")))
print(numero)

print("///////////////////////////////////////////////////")
print("")
print("USO DE PARENTESIS EN OPERACIONES PARA ORDEN MANUAL")
# USO DE PARENTESIS EN OPERACIONES
# Se aconseja utilizar paréntesis para establecer el orden de ejecución de forma manual.

# Ejemplo

numero1 = float(input("Primer número: "))
numero2 = float(input("Segundo número: "))
numero3 = float(input("Tercer número: "))
numero4 = float(input("Cuarto número: "))
numero5 = float(input("Quinto número: "))
numero6 = float(input("Sexto número: "))

resultado = (numero5 + (numero3 * (numero1 ** numero6))) - (numero4 // numero2)
resultado2 = (8 + (7 * (5)))
print(resultado)














































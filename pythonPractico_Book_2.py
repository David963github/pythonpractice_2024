# TEMA: TIPOS DE DATOS EN PYTHON  * SUBTEMA: BOOLEANOS
"""
Los booleanos, también conocidos como datos lógicos, se caracterizan por tener
únicamente dos valores: True o False.
"""

print("Ejemplo de booleanos")
print("")

verdadero = True
falso = False
print("Valor de la variable verdadero:", verdadero)
print("Valor de la variable falso:", falso)

# OPERADORES LÓGICOS

"""
Permiten construir expresiones lógicas y tienen como resultado un valor
booleano (True o False). Pueden realizarse sobre variables booleanas, ya sean valores
independientes o provenientes de otras operaciones.
"""

# SON AND, OR Y NOT

"""
AND: Con este operador se realiza la operación lógica [Y] entre dos elementos.
El resultado será True si ambos son True; de lo contrario, será False.

OR: Con este operador se realiza la operación lógica [O] entre dos elementos.
El resultado será True si alguno de los dos elementos es True; caso contrario, será
False.

NOT: Con este operador se realiza la operación lógica [NO]. El resultado será True
si el elemento es False y será False si el elemento es True.

Al igual que con las operaciones aritméticas, se recomienda usar paréntesis
para construir operaciones lógicas complejas.
"""

print("*Ejercicio práctico*")

booleano1 = bool(input("Primer valor: "))
booleano2 = bool(input("Segundo valor: "))
booleano3 = bool(input("Tercer valor: "))
booleano4 = bool(input("Cuarto valor: "))
booleano5 = bool(input("Quinto valor: "))
print("Resultado:", booleano4 or ((booleano3 and not booleano2) and booleano1) or booleano5)

# OPERADORES RELACIONALES

"""
Permiten comparar dos valores entre sí, retornando un valor booleano (True o False).
Pueden realizarse a valores independientes o valores que provienen de otras operaciones.
valor1 [operador relacional valor2].

Operador ==: valor1 y valor2 son iguales.
         !=: valor1 y valor2 son diferentes.
         >: valor1 es mayor que valor2.
         <: valor1 es menor que valor2.
         >=: valor1 es mayor o igual a valor2.
"""

print("Ejercicio práctico operadores relacionales.")
print("")

print("****************************************")

numero1 = float(input("Primer número: "))
numero2 = float(input("Segundo número: "))
numero3 = float(input("Tercer número: "))
numero4 = float(input("Cuarto número: "))
print(numero1, "==", numero4, ":", numero1 == numero4)
print(numero2, "!=", numero3, ":", numero2 != numero3)
print(numero3, ">", numero2, ":", numero3 > numero2)
print(numero4, "<", numero1, ":", numero4 < numero1)
print(numero1, ">=", numero3, ":", numero1 >= numero3)
print(numero2, "<=", numero4, ":", numero2 <= numero4)


























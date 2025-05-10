# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 13:46:43 2023

@author: Eduardo
"""

#                  CLASE 01 - CTIC

# Bienvenidos  a la Primera clase 
# del curso de Python Basico 
# Profesor : Abraham Zamudio 




# Segunda celda 
# Definicion de variables 
NombreVariable = "Python101"
# Tercera celda : Para crear nuevas celdas de codigo podemos
# utilizar la combinacion de teclas CTRL + M + B
Var_x = 2023
var_y = 1303
VaR_Z = 1982.9




# Cuarta celda : 
    
  # Variables de tipo cadena de caracter: Se definen entre comillas dobles o 
  # comillas simples 

  # Variables numericas : 
    # int (integer)
    # float (numero punto flotante)

  # Variables booleanas :
    # Son variables que pueden tomar solo dos posibles valores : True / False

# Definamos dos variables numericas 
g = 9.81
j = 1
numero_e = 2.71
numero_pi = 3.14159
k = 100

# definamos 3 variables de tipo cadena de carcacter
Clase = "Primera"
Fecha = "13/03/2023"
Prof = 'Abraham Zamudio'

# Definamos un par de variables booleanas 
Uno = True
Cero = False 




# Funcion type : Conocer el tipo de variable
type(Var_x)
type(g)
type(Uno)
type(NombreVariable)




# Operadores aritmeticos
# + - * / 
# ** : potenciacion
# % : Calculo del residuo de la division entera
# // : Calcula el cociente de la division entera

# Operadores de comparacion
# < > <= >= == !=

# Operadores logicos 
# & : And logico 
# | : OR logico
# not : negacion


# Realicemos algunas operaciones aritmeticas y de comparacion

x = 12
y = 3.6
z = 45.9

c1 = (x/y)**(1/3)
c1

c2 = ((x*y)+ (z/9.81))**(0.7)
c2

b1 = True
b2 = False

c3 = b1 & b2
c3

c4 = b2 | b1
c4

# Hagamos una composicion de operaciones logicas 
c5 = not ((b1 & b1) | (b2 | b1) & (b2 & b1))
c5




# Operaciones de variables str (cadenas de caracteres)
curso = "Programacion Basica con Python"
cl = 'Clase1'
prof = 'Abraham Zamudio'
date = "13/03/2023"




# Operacion de concatenacion de str : +
msj1 = cl + " " + date
msj1




# Operador repeticion : *
msj2 = 3 * cl
msj2




# Acceso a las componentes de una cadena de caracteres

# Primera componente
msj1[0]

# En python los indices siempre inician en cero.

# Tercera componente
msj1[2]

# Si leemos una cadena de caracteres de derecha a izquierda
# sus indices inician en -1, continua con -2 , luego con -3

# Ultima componentes de msj1
msj1[-1]

# Penultima componentes 
msj1[-2]

# Numero de elementos de un str : funcion len
len(msj1)


#%%
#                  FUNCION PRINT

# Funcion print : Sirve para montrar mensajes en pantalla 
# Primera forma : Mostremos una cadena de caracteres

print("Curso : Programacion en Python - Nivel Basico")
print("Horario : Lunes - Miercoles - Viernes [8-11AM]")
print("Profesor : Abraham Zamudio")




# Segunda forma : Python hereda ciertas cosas de C
# \t : tab 
# \n : salto de linea 
print("El curso de Programacion \nen python (Nivel Basico) \ntiene una duracion total de \t 18Hrs.")



# tercera forma : Mostremos una variable con determinado formato 
x1 = 0.3
x2 = x1 ** (-0.9)
x3 = x2*666
print("La suma de %f con %f es %f" %(x1, x2, x1+x2 ))
print("Para ver los numeros con solo dos cifras decimales : %.2f")
print("La suma de %.3f con %.1f es %.4f" %(x1, x2, x1+x2 ))




# Mostremos algunas variables de tipo entero 
D = 2023
d = 13
r = D%d
q = D // d
print("Dividendo : %d \nDivisor : %d \n Residuo : %d \n Cociente : %d" %(D,d,r, q))



# Ejemplito :
# Consideremos comprar 3 productos en el mercado 
# 4.5 Kg de arroz 
# 6.5 Kg  de azucar
# 3 docenas de latas de atun 

# Precios : 
# azucar (kg) : 5.2
# Arroz (kg) : 4.5
# Docenas de latas de atun : 32

# Suponiendo que los precios no tienen grabado el IGV(18%).
# Mostrar el total a cancelar

# Definamos las variables 
Arroz = 4.5
Azucar = 6.5
Atun = 3

PrecioArroz =4.5
PrecioAzucr = 5.2
PrecioDocAtun = 32

MontoTotal = (Arroz*PrecioArroz + Azucar*PrecioAzucr + Atun*PrecioDocAtun)*1.18

# Cuarta forma de usar el print : Doc string
print("""
La lista de compras de 
4.5 Kg de arroz 
6.5 Kg  de azucar
3 docenas de latas de atun 
--------------------------
Total a pagar : %.1f
      .... Gracias por su compra.
 """ %(MontoTotal) )




# Rutina de Entrada / Lectura : Funcion input 
# input por defecto almacena las variables leidas del teclado 
# como variables de tipo cadena de caracter

nombre = input("Ingresa tu primer nombre : ")
apellido = input("Ingresa tu apellido materno : ")
edad = input("INgresa tu edad : ")
CodigoUNI = input("Ingresa tu codigo UNI : ")

print("""
      Los datos ingresados son :
      Primer Nombre : %s
      Apellido Materno : %s
      Edad : %s
      Cod. UNI : %s""" %(nombre, apellido, edad, CodigoUNI))
    
      
# Ley de Coulomb :
# F = k * q1*q2 / d**2

# Definamos la constante k 
k = 9*10**9

# lectura de los datos : los input/entradas de mi programa 
q1 = float(input( "Ingresa la primera carga [Coulombs] : " ))
q2 = float(input("Ingresa la segunda carga [Coulombs] : "))
d = float(input("Ingresa la distancia de separacion [metros] : "))

# Realizamos las operaciones para calcular la fuerza de coulomb
F = (k * q1*q2)/(d**2)

print("""
Ley de Coulomb
--------------
Datos :
    q1 = %f
    q2 = %f
    d = %f

Resultado : 
    Fuerza Electrica : %f""" %(q1, q2, d, F))
    



# Importacion de modulos 
# Modulo matematico : math
# Forma mas adecuada/usada de cargar un modulo es mediante un alias 

import math as m 


# Documentacion del modulo math (alias m)
help(m)

# Otra forma de conocer a las funciones que componen a un 
# modulo es mediante la funcion dir 
dir(m)

# Lectura de la documentacion de alguna de estas funciones 
help(m.prod)

# Documentacion de la funcion trunc
help(m.trunc)




# Datos/constantes
x1 = (m.pi)**(m.e)
print("""
Uso de las constantes del modulo matematico 
x1 = (m.pi)**(m.e) = %f""" %(x1))



# Calculemos el seno de un angulo en sexagesimales entregado 
# por el usuario 

angulo = float(input("Ingresa el angulo en sexagesimales "))

SenoAngulo = m.sin(m.radians(angulo))

print("""
      El angulo ingresado es : %f
      seno (%f) = %f""" %(angulo, angulo, SenoAngulo ))
      
      
      

# Otro modulo basico : random 
import random as rnd 


# Documentacion del modulo random 
help(rnd)


# Funciones que componen al modulo random
dir(rnd)


# Funciones que componen al modulo random 

# 'betavariate',
#  'choice',
#  'choices',
#  'expovariate',
#  'gammavariate',
#  'gauss',
#  'getrandbits',
#  'getstate',
#  'lognormvariate',
#  'normalvariate',
#  'paretovariate',
#  'randbytes',
#  'randint',
#  'random',
#  'randrange',
#  'sample',
#  'seed',
#  'setstate',
#  'shuffle',
#  'triangular',
#  'uniform',
#  'vonmisesvariate',
#  'weibullvariate'


# # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # # 
# Segunda  Tarea : 
# Leer/comprender/interpretar/probar  la documentacion de todas las funciones y
#  constantes del modulo random (alias rnd)
# # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # # 

# Documentacion de la funcion gauss del modulo rnd
help(rnd.gauss)


# Documentacion de la funcion randint del modulo random
help(rnd.randint)


Nota1 = rnd.randint(0,20)
Nota1
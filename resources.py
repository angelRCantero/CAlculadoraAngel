####aca va a ir el codigo de la calculadora
##Empiezo con codigo basico para entender sintaxis basicas
#comienzo con estructuras basadas en un video de internet que daba 
# informacion de como hacer una calculadora con semantica mas avanzada pero bien explicada
import sys

num1 = 0
num2 = 0

menu = """
1:Sumar
2:Restar
3:Multiplicar
4:Dividir
5:Potencia
6:Raiz
0:Salir
"""

def Sumar():
    print("ingrese el primer numero: ")
    try:
        num1 = float(input())
        print("ingresa el segundo numero: ")
        num2 = float(input())
        print("la suma de los numeros es igual a: ", num1 + num2)
    except ValueError:
        print("Ingresa solamente numeros")
        Sumar()    
    
def Restar():
    print("ingrese el primer numero: ")
    try:
        num1 = float(input())
        print("ingresa el segundo numero: ")
        num2 = float(input())
        print("la resta de los numeros es igual a: ", num1 - num2)
    except ValueError:
        print("Ingresa solamente numeros")
    
    
def Multiplicar():
    print("ingrese el primer numero: ")
    num1 = float(input())
    print("ingresa el segundo numero: ")
    num2 = float(input())
    print("el resultado de la multiplicacion es igual a: ", num1 * num2)
    
    
def Dividir():
    print("ingrese el primer numero: ")
    num1 = float(input())
    print("ingresa el segundo numero: ")
    num2 = float(input())
    print("el resultado de la division es igual a: ", num1 / num2)
    
    
def Potencia():
    print("ingrese el primer numero: ")
    num1 = float(input())
    print("ingresa el segundo numero: ")
    num2 = float(input())
    print("el resultado de la potencia es : ", num1 ** num2)
    
    
def Raiz():
    print("ingrese el primer numero: ")
    num1 = float(input())
    print("ingresa el segundo numero: ")
    num2 = float(input())
    print("el resultado de la raiz es : ", num1 ** (1/num2) )
    
print("bienvenido a la calculadora basica que pidio el profe juan...")
while True:
    print(menu)  #el valor de 'valE' es igual al valor de la entrada del usuario
    try:
        valE = int(input())
        if valE == 1:
            Sumar()
        elif valE == 2:
            Restar()
        elif valE == 3:
            Multiplicar()
        elif valE == 4:
            Dividir()
        elif valE == 5:
            Potencia()
        elif valE == 6:
            Raiz()
        elif valE == 0:
            sys.exit()
        else:
            print("ingresa una opcion disponible")
    except ValueError:
        print("ERROR!!! ingresa solo numeros")
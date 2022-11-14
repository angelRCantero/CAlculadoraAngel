####aca va a ir el codigo de la calculadora
##Empiezo con codigo basico para entender sintaxis basicas
#comienzo con estructuras basadas en un video de internet que daba 
# informacion de como hacer una calculadora con semantica mas avanzada pero bien explicada
import sys #EL SYS ES UNA LIBRERIA QUE IMPORTA LA RUTA DE SALIDA DESDE LAS OPCIONES DEL MENU DE LA CALCULADORA

num1 = 0 
num2 = 0

menu =  """
1: Sumar
2: Restar
3: Multiplicar
4: Dividir
5: Potencia
6: Raiz
0: Salir
""" 


def Sumar():
    print("ingrese el primer numero: ")
    try:#CON EL 'TRY' COMPRUEBO TIPOS DE ERRORES DE LOS DATOS DE ENTRADA Y EL 'EXCEPT' DA EL TIPO DE ERROR ESPECIFICO ###
        #CON VALORES YA PREESTABLECIDOS DENTRO DE SU LIBRERIA
        num1 = float(input())
        print("ingresa el segundo numero: ")
        num2 = float(input())
        print("la suma de los numeros es igual a: ", num1 + num2)
    except ValueError:#ACA SE VE EL ERROR TIPO 'VALUEERROR' QUE RECONOCE QUE EL VALOR DE ENTRADA ESTA CONDICIONADO POR EL 'FLOAT' ###
        #EXIGIENDO ESTE,UN VALOR DE TIPO NUMERICO DECIMAL,PARA ASI REACCIONAR A CUALQUIER TIPO DE ENTRADA INCORRECTA COMO POR EJEMPLO LETRAS.
        print("ERROR!!! Ingresa solamente numeros")#LUEGO DE LA VALIDACION INTERNA POR MEDIO DEL 'TRY' SE HACE UNA LLAMADA NUEVAMENTE HACIA LA VARIABLE QUE CREAMOS,###
        #COMO EN ESTE CASO LA VAR 'SUMAR' PARA QUE CON ESTE PROCESO NO SE CIERRE NUESTRA CALCULADORA
        Sumar()
        
def Restar():
    print("ingrese el primer numero: ")
    try:
        num1 = float(input())
        print("ingresa el segundo numero: ")
        num2 = float(input())
        print("la resta de los numeros es igual a: ", num1 - num2)
    except ValueError:
        print("ERROR!!! Ingresa solamente numeros")
        Restar()
        
def Multiplicar():
    print("ingrese el primer numero: ")
    try:
        num1 = float(input())
        print("ingresa el segundo numero: ")
        num2 = float(input())
        print("el resultado de la multiplicacion es igual a: ", num1 * num2)
    except ValueError:
        print("ERROR!!! ingrese solamente numeros")
        Multiplicar()
    
def Dividir():
    print("ingrese el primer numero: ")
    try:
        num1 = float(input())
        print("ingresa el segundo numero: ")
        num2 = float(input())
        try:#ESTE 'TRY' ES ESPECIFICO DE EL TIPO DE ENTRADA INCORRECTA DEBIDO AL ERROR MATEMATICO DE DIVIDIR POR 0 UN NUMERO,###
            #NO QUIERE DECIR QUE EL TIPO DE ENTRADA ESTE INCORRECTO PORQUE EL 0 ES UN NUMERO,SI NO QUE EN LA OPERACION 
            #NO ES POSIBLE REALIZARSE CON UN 0 COMO DIVIDENDO
            print("el resultado de la division es igual a: ", num1 / num2)
        except ZeroDivisionError:
            print("ERROR no se puede dividir sobre 0")
            Dividir()
    except ValueError:
        print("ERROR!!! ingrese solamente numeros")
        Dividir()
    
    
def Potencia():
    print("ingrese el primer numero: ")
    try:
        num1 = float(input())
        print("ingresa el segundo numero: ")
        num2 = float(input())
        print("el resultado de la potencia es : ", num1 ** num2)
    except ValueError:
        print("ERROR!!! ingrese solo numeros")
        Potencia()
    
    
def Raiz():
    print("ingrese el primer numero: ")
    try:
        num1 = float(input())
        print("ingresa el segundo numero: ")
        num2 = float(input())
        try:
            print("el resultado de la raiz es : ", num1 ** (1/num2) )
        except ZeroDivisionError:#EL MISMO CASO DONDE ENCONTRAMOS UNA OPERACION DE TIPO DIVIDIR CON UN DIVIDENDO 0 YA QUE LA RAIZ DIVIDE '1/NUM2'
            print("ERROR no es posible dividir en la raiz a la 0")
            Raiz()
    except ValueError:
        print("ERROR!!! ingrese solo numeros")
        Raiz()
    
print("bienvenido a la calculadora basica que pidio el profe juan...")
while True:
    print(menu)  #el valor de 'valE' es igual al valor de la entrada del usuario
    try:#ESTE 'TRY' COMPRUEBA QUE EL USUARIO ELIJA ENTRE LAS OPCIONES DISPONIBLES
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
            sys.exit()#EL SYS LE DARA EL ESCAPE DE RUTINA A LA CALCULADORA
        else:
            print("ingresa una opcion disponible")
    except ValueError:#EL 'EXCEPT GENERA EL TIPO DE ERROR DENTRO DE LOS VALORES DISPONIBLES DEL 'INT' CON LAS OPCIONES DISPONIBLES###
        print("ERROR!!! ingresa solo numeros")#DEL 1 AL 6 INCLUYENDO EL 0 COMO CIERRE DEL PROGRAMA,QUE DE NO SER UNA DE LAS DISPONIBLES###
        #O NO SEA UN NUMERO ENTERO USARA EL 'PRINT' PARA DAR EL MENSAJE QUE LA ENTRADA NO CONDICE CON UNA OPCION DISPONIBLE
        
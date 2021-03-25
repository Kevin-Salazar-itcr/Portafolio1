print(""" Cualquier funcion que aparezca aquí está en total operación
CorrimientoAEntero()
contarDigitosFlotante()
indiceNumero()
cortarNumero()
""")
"""
CorrimientoAEntero
E: num
S: Pasar los decimales a la parte entera
R: Número flotante
"""
def CorrimientoAEntero(num):
    if(isinstance(num, float)):
        return corrimiento_aux(num)
    else:
        print("Digite un número con al menos un decimal")

def corrimiento_aux(num):
    if(num%2==0):
        return num
    if(num%3==0):
        return num
    if(num%5==0):
        return num
    if(num%7==0):
        return num
    else:
        print(num)
        print("==========")
        return corrimiento_aux(num*10)
"==========================================="
"""
contarDigitosFlotante
E: num
S: cantidad de dígitos (incluyendo decimales)
R: número flotante
"""
def contarDigitosFlotante(num):
    if(isinstance(num, float)):
        res_int = corrimiento_aux(num)
        return flotante_aux(res_int)
    else:
        return "Ingrese un número que contenga decimales"
def flotante_aux(res_int):
    if(res_int<=9):
        return 1
    else:
        return 1+flotante_aux(res_int//10)
"======================================="
"""
IndiceNumero
E: num= numero cualquiera; indice= numero cualquiera
S: digito del numero (de izquierda a derecha) según el índice
R: Entero positivo
"""
def indiceNumero(num, indice):
     if isinstance(num, int) and (num>0):
          digitos =  longitud(num)
          if (digitos>indice):
               return indice_aux(num, indice, digitos-1)
          else:
               return "El índice está fuera del rango numérico"
     else:
          return "Error: Digite númeroos enteros positivos"
        
def indice_aux(num, indice, digitos):
     if (indice == digitos):
         return num%10
     else:
          return indice_aux(num//10, indice, digitos-1)

def longitud(num):
     if isinstance(num, int):
          if(num<=9):
               return 1
          else:
               return 1+longitud(num//10)
     else:
          print("Digite un número entero positivo")
"==============================================="
"""
cortarNunero
E: num, i1, i2} numeros enteros
S: un nuevo numero segun indices
    f(12763, 0, 3)= [0]=1 y  [3]=6 }16
R: numeros enteros
"""
def cortarNumero(num, i1, i2):
    if(isinstance(num, int)):
        digitos=longitud(num)
        if(digitos>i1):
            if(digitos>i2):
                primero=(indiceNumero(num, i1))*10**1
                segundo=(indiceNumero(num, i2))*10**0
                return primero+segundo
            else:
                return "El indice está fuera del rango numérico"
        else:
            return "El indice está fuera del rango numérico"
    else:
        print("Sólo números enteros")

"==========================================="

print("recursividad1()")
"Indicadores al pie del código:"
"=========================: código en total funcionamiento"
#=========================: Código sin terminar
"""
divisores
E: num
S: imprimir divisores de un número de manera descendente
R: numero entero positivo
"""
 
def divisores(num):
    if(isinstance(num, int) and num>0):
        return divisores_aux(num, 1)
    else: 
        return print("Error: Revise que el número sea entero positivo")
def divisores_aux(num, i):
    if(i>num):
        return 0
    if(num%i==0):
        print("===========")
        print(i)
        res= (1+divisores_aux(num, i+1))
        print("============")
        return (res)
    else:
        return divisores_aux(num, i+1)

"================================================"
"""
multiplicarRecursivo
E: num, factor } 2 números enteros positivos
S: Multipicación de entradas (sin usar operador *)
R: numeros enteros positivos
"""

def multiplicarRecursivo(num, factor):
    if(isinstance(num, int) and isinstance(factor, int)):
        if(num==0) or (factor==0):
            return 0
        else:
            return num+multiplicarRecursivo(num, factor-1)
    else:
        return "Los numeros deben ser enteros positivos"
"================================================"
"""
divisionRecursivo
E: dividendo, divisor } 2 numeros enteros positivos
S: división de dividendo entre divisor
R: divisor no puede ser 0
     no se puede usar operador /
"""
def divisionRecursivo(dividendo, divisor):
    if(isinstance(dividendo, int) and isinstance(divisor, int)):
        if(dividendo>=0) and (divisor>0):
            if(dividendo>= divisor):
                return divisionRecursivo_aux(dividendo, divisor)
            else:
                print("Dividendo debe ser mayor o igual al divisor")
        else:
            print("Verifique que el dividendo sea mayor o igual a 0, y el divisor sea mayor a 0.")
    else:
        print("Error: Ambos números deben ser enteros positivos.")
def divisionRecursivo_aux(dividendo, divisor):
    if(dividendo<=0):
        return 0
    if(dividendo==1):
        return 0    
    elif(dividendo==divisor):
        return 1
    else:
        return 1+divisionRecursivo_aux(dividendo-divisor, divisor)
"================================================"
def recursividad1():
    print("""
Opciones:
1-   divisores
2-   multiplicarRecursivo
3-   divisionRecursivo
4-   Salir
""")
    opcion=input("Digite la operación a realizar: ")
    if(isinstance(opcion, str)):
        if(opcion=="1"):
            num=int(input("Digite un número: "))
            return divisores(num)
        if(opcion=="2"):
            num=int(input("Digite un número: "))
            factor=int(input("Digite otro número: "))
            return multiplicarRecursivo(num, factor)
        if(opcion=="3"):
            dividendo=int(input("Ingrese un número: "))
            divisor=int( input("Digite otro número: "))
            return divisionRecursivo(dividendo, divisor)
        elif(opcion=="4"):
            return "Hasta luego"
        elif(opcion>"4"):
            return recursividad1()
        print("\n")
        recursividad1()
    else:
        print("Error")

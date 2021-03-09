def contarDigitos(num):
    if(num==0):
        return 0
    else:
        return 1+contarDigitos(num//10)

def inversaNum(num):
    if(isinstance(num, int)):
        if(num>=0):
            if (num<=10):
                return num
            else:
                return inversaNum_aux(num, contarDigitos(num))
        else:
            print("Error: numero deve ser positivo")
    else:
         print("Error: numero no entero")

def inversaNum_aux(num, largo):
    if largo==0:
        return 0
    else:
       return (num%10)*(10**(largo-1))+inversaNum_aux(num//10, largo-1)


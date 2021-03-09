def numeroPar(num):
    if(isinstance(num, int) and num>=0):
        if(num%2==0):
            return True
        else:
            return False
    else:
        print("Error: numero no es entero positivo")

def contarPares(num):
    if(isinstance(num,int) and num>=0):
        if (num==0):
            return 0
        if(num%2==0):
            return 1+contarPares(num//10)
        else:
            return contarPares(num//10)
    else:
        return "Digite un numero entero"

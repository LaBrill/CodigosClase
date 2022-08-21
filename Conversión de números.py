def conversion():
    numero = input ("Introduce un numero para pasarlo a decimal, especifica en que base esta como :2,3,16 : ")
    sistemaconv = int (input("introduce un sistema de conversion: "))
    print (int(numero,sistemaconv))
conversion()

def octal_decimal():
    numero = int(input("introduce un numero para pasarlo de decimal a octal: "))
    convertido = oct(numero)[2:]
    print(convertido)
octal_decimal()

def hexadecimal_a_decimal():
    numero =int(input("introduce un numero en base decimal para pasar a base hexadecimal: "))
    convertido = hex(numero)[2:]
    print(convertido)
hexadecimal_a_decimal()

def binario_a_decimal():
    numero=int(input("introduce un numero decimal para pasarlo a binario: "))
    convertido=bin(numero)[2:]
    print(convertido)
binario_a_decimal()

print ("si quieres convertir de decimal a acci introduce 10, si quieres pasar de binario a accsi introdice 2: ")
sistema =  int(input("introduce el numero: "))
if sistema == 10:
         
        x = int(input("si quieres saber el mensaje en codigo accsi introduce un numero en base decimal deacuerdo a los resultados previos (solo numeros del 97 al 122): "))
    
        while x != 1:

         if x == 97:
            print ("en accsi : a")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97 para finalizar")
            x = int(input())
               
         if x == 98:
            print ("en accsi : b")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 99:
            print ("en accsi : c")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
            
         if x == 100:
            print ("en accsi : d")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 101:
            print ("en accsi : e")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 102:
            print ("en accsi : f")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 103:
            print ("en accsi : g")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 104:
            print ("en accsi : h")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 105:
            print ("en accsi : i")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 106:
            print ("en accsi : j")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 107:
            print ("en accsi : k")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 108:
            print ("en accsi : l")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 109:
            print ("en accsi : m")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 110:
            print ("en accsi : n")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 164:
            print ("en accsi : ñ")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 111:
            print ("en accsi : o")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 112:
            print ("en accsi : p")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 113:
            print ("en accsi : q")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 114:
            print ("en accsi : r")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 115:
            print ("en accsi : s")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
               
         if x == 116:
            print ("en accsi : t")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 117:
            print ("en accsi : u")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 118:
            print ("en accsi : v")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 119:
            print ("en accsi : w")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 120:
            print ("en accsi : x")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 121:
            print ("en accsi : y")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 122:
            print ("en accsi : z")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())

if sistema == 2: 
         
        x = int(input("si quieres saber el mensaje en codigo accsi introduce un numero en base binario deacuerdo a los resultados previos : "))
    
        while x != 1:
         
         if x == 1100001:
               print ("en accsi : a")
               print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97 para finalizar")
               x = int(input())
               
         if x == 1100010:
            print ("en accsi : b")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1100011:
            print ("en accsi : c")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
            
         if x == 1100100:
            print ("en accsi : d")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1100101:
            print ("en accsi : e")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1100110:
            print ("en accsi : f")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1100111:
            print ("en accsi : g")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1101000:
            print ("en accsi : h")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1101001:
            print ("en accsi : i")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1101010:
            print ("en accsi : j")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1101011:
            print ("en accsi : k")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1101100:
            print ("en accsi : l")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1101101:
            print ("en accsi : m")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1101110:
            print ("en accsi : n")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1101111:
            print ("en accsi : o")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1110000:
            print ("en accsi : p")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1110001:
            print ("en accsi : q")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1110010:
            print ("en accsi : r")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1110011:
            print ("en accsi : s")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
               
         if x == 1110100:
            print ("en accsi : t")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1110101:
            print ("en accsi : u")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1110110:
            print ("en accsi : v")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1100111:
            print ("en accsi : w")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1101000:
            print ("en accsi : x")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1101001:
            print ("en accsi : y")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())
       
         if x == 1101010:
            print ("en accsi : z")
            print ("si quiere continuar inserte un numero entre 97 y 122 de lo contrario escriba un numero menor a 97")
            x = int(input())

from re import M
from machine import Pin, PWM , I2C, ADC
import utime 
from ssd1306 import SSD1306_I2C
import bluetooth
from BLE import BLEUART

#boton para empezar sin necesidad de el telefono

variableservo = 0
botoniniciar = Pin(13,Pin.IN)

#variables para los imanes y pines de entrada
valorsensorimanes = Pin(19,Pin.IN)
valorsensorcanica = Pin(28,Pin.IN)
valoriman = 0
casillaiman = 0

# decplaraciones para la pantalla
i2c = I2C(0, scl=Pin(22), sda=Pin(23))
oled = SSD1306_I2C(ancho, alto, i2c)
alto = 64
ancho = 128

# declaraciones para el motor y su funcionamiento 

i = 0   #contador para el motor
m1 = PWM(Pin (12),20000)
m2 = PWM(Pin (13),20000)



#Bluetooth
      
name= "EspSapos"
ble = bluetooth.BLE()
uart = BLEUART(ble,name)

#declaraciones servo 

servo = PWM(Pin(4), freq=50)

def iniciarprogramasinbluetooth():
  if botoniniciar.value()==0:
    variableservo = 1
    variableservo=int(mapear(variableservo,0,2,1150,8100))
    print (variableservo)
    servo.duty(variableservo)
    
    m1.duty(0)
    m2.duty(0)
      
    for i in range (400,1023,10):
      m1.duty(i)
      utime.sleep(0.2)

    for i in range (1023,400,-10):
      m1.duty(i)
      utime.sleep(0.2)
    
    posicioniman
    posicioncanica()


#funcion para ingresar el valor del servo e inciar el programa
def on_rx():
    print("servomotor funcionando")
    rx_recibe = uart.read().decode().strip()
    dato=float(rx_recibe)
    if dato>=0 and dato<=180:
        uart.write("Ingrese 1 para dejar que la bola caiga o 0 para que se mantenga igual")
        uart.write("angulo: "+str(dato) + "\n")
        print("angulo: " + str(dato) + "\n")
        m=int(mapear(dato,0,2,1150,8100))
        print (m)
        servo.duty_u16(m)
    else:
        uart.write("el valor no aplica")
        print("el valor no aplica")

   



#funcion mapear
def mapear(valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
  valoriman = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada - minimo_entrada) + minimo_salida
  return valoriman



#funcion para recorrer el numero de casillas
def posicioniman():
    
    if valorsensorimanes > 7:
      casillaiman += 1
      utime.sleep(0.1)

    if valorsensorimanes < 5:
      casillaiman += 1
      utime.sleep(0.1)



#funcion para saber en que posicion esta la canica
def posicioncanica():

  if casillaiman == 0 and valorsensorcanica > 7:
    print("La canica se encientra en el verde Negro N° 0")

    oled.text("---------------*", 0, 00,1)
    oled.text("|   Posicion:  |", 0, 8,1)
    oled.text("|              |", 0, 16,1)
    oled.text("|  Color Verde |", 0, 24,1)
    oled.text("|              |", 0, 32,1)
    oled.text("|   Numero 0   |", 0, 40,1)
    oled.text("|              |", 0, 48,1)
    oled.text("*--------------*", 0, 56,1)
    oled.show()
    utime.sleep(0.2)

  elif casillaiman == 1 and valorsensorcanica > 7:
    print("la canica se encuentra en el color Negro N° 4")

    oled.text("---------------*", 0, 00,1)
    oled.text("|   Posicion:  |", 0, 8,1)
    oled.text("|              |", 0, 16,1)
    oled.text("|  Color Negro |", 0, 24,1)
    oled.text("|              |", 0, 32,1)
    oled.text("|   Numero 4   |", 0, 40,1)
    oled.text("|              |", 0, 48,1)
    oled.text("*--------------*", 0, 56,1)
    oled.show()
    utime.sleep(0.2)    

  elif casillaiman == 2 and valorsensorcanica > 7:
    print("La canica se encuentra en el color Rojo N° 2")

    oled.text("---------------*", 0, 00,1)
    oled.text("|   Posicion:  |", 0, 8,1)
    oled.text("|              |", 0, 16,1)
    oled.text("|  Color Rojo  |", 0, 24,1)
    oled.text("|              |", 0, 32,1)
    oled.text("|   Numero 2   |", 0, 40,1)
    oled.text("|              |", 0, 48,1)
    oled.text("*--------------*", 0, 56,1)
    oled.show()
    utime.sleep(0.2)        

  elif casillaiman == 3 and valorsensorcanica > 7:
    print("La canica se encuentra en el color Negro N° 13")

    oled.text("---------------*", 0, 00,1)
    oled.text("|   Posicion:  |", 0, 8,1)
    oled.text("|              |", 0, 16,1)
    oled.text("|  Color Negro |", 0, 24,1)
    oled.text("|              |", 0, 32,1)
    oled.text("|   Numero 13  |", 0, 40,1)
    oled.text("|              |", 0, 48,1)
    oled.text("*--------------*", 0, 56,1)
    oled.show()
    utime.sleep(0.2)    

  elif casillaiman == 4 and valorsensorcanica > 7:
    print("La canica se encuentra en el color Rojo N° 9")

    oled.text("---------------*", 0, 00,1)
    oled.text("|   Posicion:  |", 0, 8,1)
    oled.text("|              |", 0, 16,1)
    oled.text("|  Color Rojo  |", 0, 24,1)
    oled.text("|              |", 0, 32,1)
    oled.text("|   Numero 9   |", 0, 40,1)
    oled.text("|              |", 0, 48,1)
    oled.text("*--------------*", 0, 56,1)
    oled.show()
    utime.sleep(0.2)    

  elif casillaiman == 5 and valorsensorcanica > 7:
    print("La canica se encuentra en el color Negro N° 1")

    oled.text("---------------*", 0, 00,1)
    oled.text("|   Posicion:  |", 0, 8,1)
    oled.text("|              |", 0, 16,1)
    oled.text("|  Color Negro |", 0, 24,1)
    oled.text("|              |", 0, 32,1)
    oled.text("|   Numero 1   |", 0, 40,1)
    oled.text("|              |", 0, 48,1)
    oled.text("*--------------*", 0, 56,1)
    oled.show()
    utime.sleep(0.2)
    
  elif casillaiman == 6 and valorsensorcanica > 7:
    print("La canica se encuentra en el color Rojo N° 7")

    oled.text("---------------*", 0, 00,1)
    oled.text("|   Posicion:  |", 0, 8,1)
    oled.text("|              |", 0, 16,1)
    oled.text("|  Color Rojo  |", 0, 24,1)
    oled.text("|              |", 0, 32,1)
    oled.text("|   Numero 7   |", 0, 40,1)
    oled.text("|              |", 0, 48,1)
    oled.text("*--------------*", 0, 56,1)
    oled.show()
    utime.sleep(0.2)    

  elif casillaiman == 7 and valorsensorcanica > 7:
    print("La canica se encuentra en el color Negro N° 15")

    oled.text("---------------*", 0, 00,1)
    oled.text("|   Posicion:  |", 0, 8,1)
    oled.text("|              |", 0, 16,1)
    oled.text("|  Color negro |", 0, 24,1)
    oled.text("|              |", 0, 32,1)
    oled.text("|   Numero 15  |", 0, 40,1)
    oled.text("|              |", 0, 48,1)
    oled.text("*--------------*", 0, 56,1)
    oled.show()
    utime.sleep(0.2)           

  elif casillaiman == 8 and valorsensorcanica > 7:
    print("La canica se encuentra en el color Rojo N° 12") 

    oled.text("---------------*", 0, 00,1)
    oled.text("|   Posicion:  |", 0, 8,1)
    oled.text("|              |", 0, 16,1)
    oled.text("|  Color Rojo  |", 0, 24,1)
    oled.text("|              |", 0, 32,1)
    oled.text("|   Numero 12  |", 0, 40,1)
    oled.text("|              |", 0, 48,1)
    oled.text("*--------------*", 0, 56,1)
    oled.show()
    utime.sleep(0.2)       


    
while True:

  on_rx()
  m1.duty(0)
  m2.duty(0)
    
  for i in range (400,1023,10):
    m1.duty(i)
    utime.sleep(0.2)

  for i in range (1023,400,-10):
    m1.duty(i)
    utime.sleep(0.2)
    


  print("Efecto hall: " )
  print ("valor sensores" + valorsensorimanes + "posicion imanes" + casillaiman + "Valor motor:" + i) 
  utime.sleep(0.2)
  valorsensorimanes = mapear(valorsensorimanes , 0 , 160 , 0 , 10)
  valorsensorcanica = mapear(valorsensorcanica , 0 , 160 , 0 , 10)

  posicioniman()
  posicioncanica()

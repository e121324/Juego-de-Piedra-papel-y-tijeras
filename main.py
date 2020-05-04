import random 
import time
import os

#Func (para limpiar la pantalla)
def clear():
  os.system("cmd")
#Variable que define si esta juagando
juego = "si"
#Define el score del Usuario
usuario = 0
#Define es scored del cpu
cpu = 0

#Te pregunta tu nombre y te da un cumplido
nombre = input("Como te llamas :")
clear()
print("Hola "+nombre+" vamos a jugar! \n")
time.sleep(1)
#Lista que define las opciones del cpu
opciones = ["piedra","papel","tijeras"]
#Bucle Principal del juego
while juego == "si" :
  bot = random.choice(opciones)
  #Define que escoje el usuario 
  opcion = input("Que escojes piedra , papel o tijera :")
  #Comprueba si el usuario escogio piedra
  if opcion == "piedra":
    #Comprueba la opcion del cpu
    if bot == "piedra":
      #Muestra el mensaje dependiendo si ganaste perdistte o empataste
      print("\nEmpate, el cpu escogio: "+bot+"\n")
      #Imprime es score
      print("Usuario : "+str(usuario)+" , cpu : "+str(cpu))
    elif bot == "papel":
      print("\nPerdiste, el cpu escogio: "+bot+"\n")
      cpu += 1
      print("Usuario : "+str(usuario)+" , cpu : "+str(cpu))
    elif bot == "tijeras":
      print("\nGanaste, el cpu escogio: "+bot+"\n")
      usuario += 1
      print("Usuario : "+str(usuario)+" , cpu : "+str(cpu))

  elif opcion == "papel":
    if bot == "piedra":
      print("\nGanaste, el cpu escogio: "+bot+"\n")
      usuario += 1
      print("Usuario : "+str(usuario)+" , cpu : "+str(cpu))
    elif bot == "papel":
      print("\nEmpate, el cpu escogio: "+bot+"\n")
    elif bot == "tijeras":
       print("\nPerdiste, el cpu escogio: "+bot+"\n")
       cpu += 1
       print("Usuario : "+str(usuario)+" , cpu : "+str(cpu))

  elif opcion == "tijeras" or opcion == "tijera":
    if bot == "piedra":
      print("\nPerdiste, el cpu escogio: "+bot+"\n")
      cpu += 1 
      print("Usuario : "+str(usuario)+" , cpu : "+str(cpu))
    elif bot == "papel":
      print("\nGanaste, el cpu escogio: "+bot+"\n")
      usuario += 1 
      print("Usuario : "+str(usuario)+" , cpu : "+str(cpu))
    elif bot == "tijeras":
      print("\nEmpate, el cpu escogio: "+bot+"\n")
  #Si el string introducido por el usuario no corresponde co las anteriores imprime lo siguiente
  else:
    print("Mal input")
  #Preguta si quieres jugar otra vez(si o no )
  a = input("\nQuieres volver a jugar (y/n):")
  if a == "n" :
    break
  clear()

clear()
#Imprime es score
print("\nUsuario : "+str(usuario)+" , cpu : "+str(cpu))
time.sleep(1)
#Despedida
print("\nHasta la proximaaaaaaa")
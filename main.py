import random 
import time
import os

#Func
def clear():
  os.system("clear")

juego = "si"
usuario = 0
cpu = 0

nombre = input("Como te llamas :")
clear()
print("Hola "+nombre+" vamos a jugar! \n")
time.sleep(1)

opciones = ["piedra","papel","tijeras"]

while juego == "si" :
  bot = random.choice(opciones)

  opcion = input("Que escojes piedra , papel o tijera :")
  if opcion == "piedra":
    if bot == "piedra":
      print("\nEmpate, el cpu escogio: "+bot+"\n")
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

  else:
    print("Mal input")
  
  a = input("\nQuieres volver a jugar (y/n):")
  if a == "n" :
    break
  clear()
clear()
print("\nUsuario : "+str(usuario)+" , cpu : "+str(cpu))
time.sleep(1)
print("\nHasta la proximaaaaaaa")
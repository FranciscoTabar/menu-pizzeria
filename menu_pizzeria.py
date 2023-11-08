print("PIZZERIA: Fran y Guille")
dinero= float(input("Hola indica el dinero que quieres gastar:\n"))
DINERO_INICIAL = dinero
total = 0 
pedido = []

# pizzas
margarita= 200
jamon_queso= 250
cuatro_quesos= 300

 # condimentos extras
extra_queso= 50
peperoni= 80
champiñones= 60

# titulo del programa
print("---> Pizzeria F & G <---")

#bucle infinito para pizza
while True:
  # menu de pizzas
  print(f"1- Margarita - {margarita}$")
  print(f"2- Jamon y Queso -{jamon_queso}$")
  print(f"3- Cuatro Quesos -{cuatro_quesos}$")

  # eleccion del usuario
  eleccion= int(input("Por favor seleccione su pizza:\n"))
  # calcula el cambio y el total, se indica la pizza

  match eleccion:
    case 1:
      print(f"Ha elegido la pizza margarita.\nTotal a pagar {margarita}")
      dinero -= margarita
      print(f"le queda {round(dinero,2)}$.")
      total += margarita
      pedido.append(f"margarita - {margarita}$") 
      break
    case 2:
      print(f"Ha elegido la pizza jamon y queso.\nTotal a pagar {jamon_queso}")
      dinero -= jamon_queso
      print(f"Le queda {round(dinero,2)}$.")
      total += jamon_queso
      pedido.append(f"Jamon y Queso - {margarita}$")
      break
    case 3:
      print(f"Ha elegido la pizza cuatro quesos.\nTotal a pagar {cuatro_quesos}")
      dinero -= cuatro_quesos
      print(f"Le queda {round(dinero,2)}$.")
      total += cuatro_quesos
      pedido.append(f"Jamon y Queso - {cuatro_quesos}$")
      break
    case _:
      print("Opcion incorecta. Vuelve a intentarlo")

# bucle infinito para ingredientes

while True:
  print(f"1- Extra queso - {extra_queso}$")
  print(f"2- Extra peperoni - {peperoni}$")
  print(f"3- Extra champiñones - {champiñones}$")
  print(f"4- No añadire nada extra.")

# almacena la eleccion del usuario
  eleccion = int(input("Eliga una opcion si desea algun ingrediente extra.\n"))

  match eleccion:
    case 1: 
      print(f"Ha elegido extra queso. \n extra a pagar {extra_queso}$.")
      dinero -= extra_queso
      total += extra_queso
      print(f"Total a pagar : {total}$.")
      print(f"Le quedan {round(dinero,2)}$.")
      pedido.append(f"Extra queso - {extra_queso}$")
    case 2: 
      print(f"Ha elegido extra peperoni. \n extra a pagar {peperoni}$.")
      dinero -= peperoni
      total += peperoni
      print(f"Total a pagar : {total}$.")
      print(f"Le quedan {round(dinero,2)}$.")
      pedido.append(f"Extra peperoni- {peperoni}$")  
    case 3: 
      print(f"Ha elegido extra champiñones. \n extra a pagar {champiñones}$.")
      dinero -= champiñones
      total += champiñones
      print(f"Total a pagar : {total}$.")
      print(f"Le quedan {round(dinero,2)}$.")
      pedido.append(f"Extra champiñones- {champiñones}$")
    case 4 : 
      print("De acuerdo no se agrega nada extra")
      break
    case _:
      print(f"Opcion incorrecta. vuelve a intentarlo")



if total <= DINERO_INICIAL:
  print("\n ----- SU PEDIDO-----")

  print (f"EL TOTAL DE SU PEDIDO ES : {total}$.total")
  print(f"SU CAMBIO: {dinero}$.\n")

  for i in pedido:
    print(f"- {i}.")

  print("\n ¡disfruta tu pedido!!!")

else:
  print("su dinero es insuficiente. porfavor vuelva a empezar")
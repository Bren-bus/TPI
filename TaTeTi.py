fila1 = []
fila2 = []
fila3= []
elemento = ["'''"]
posicion = []

for i in range(0, 3, 1):
        fila1.append(elemento)
for j in range(0,3,1):
        fila2.append(elemento)
for k in range (0,3,1):
        fila3.append(elemento)

def mostrarTablero(fila1,fila2,fila3):
    print(fila1)
    print(fila2)
    print(fila3)






jugador1 = input("Jugador 1 (X), ingrese su nombre")
jugador2 = input("Jugador 2 (O), ingrese su nombre")
mostrarTablero(fila1,fila2,fila3)


ganador = False

#Contador de todas las jugadas (de ambos jugadores)
jugadas = 0

# Ciclo para que el jugador elija la posición que desea elegir. Se repite 9 veces, es la cantidad de turnos entre los dos jugadores
while (jugadas< 9):
    print(jugador1)
    seleccionJugador1 = input("Ingrese la posicion que desea elegir")

    while seleccionJugador1 in posicion[0:9]:
        print("SELECCIÓN NO VÁLIDA. Intenta de nuevo.")
        seleccionJugador1 = input("Ingrese la posición que desea elegir")
    while int(seleccionJugador1) > 9 or int(seleccionJugador1) <1:
        print("SELECCIÓN NO VÁLIDA. Intenta de nuevo.")
        seleccionJugador1 = input("Ingrese la posición que desea elegir")




    if seleccionJugador1 != posicion[0:9]:
        posicion.append(seleccionJugador1)
        jugadas = jugadas + 1
    if seleccionJugador1 == "1":

        fila1[0] = "[X]"
    if seleccionJugador1 == "2":
        fila1[1] = "[X]"
    if seleccionJugador1 == "3":
        fila1[2] = "[X]"
    if seleccionJugador1 == "4":
        fila2[0] = "[X]"
    if seleccionJugador1 == "5":
        fila2[1] = "[X]"
    if seleccionJugador1 == "6" :
        fila2[2] = "[X]"
    if seleccionJugador1 == "7":
        fila3[0] = "[X]"
    if seleccionJugador1 == "8":
        fila3[1] = "[X]"
    if seleccionJugador1 == "9":
        fila3[2] = "[X]"

    # Se muestra el tablero cada vez que un jugador elige una opcion

    mostrarTablero(fila1,fila2,fila3)
    if jugadas == 9 and ganador == False:
        print("Empate")
        break

    if fila1[0] == "[X]" and fila2[0] == "[X]" and fila3[0] == "[X]":
        ganador = True
        print("Felicitaciones:", jugador1, " ¡GANASTE!")
        break

    if fila1[1] == "[X]" and fila2[1] == "[X]" and fila3[1] == "[X]":
        ganador = True
        print("Felicitaciones:", jugador1, " ¡GANASTE!")
        break
    if fila1[2] == "[X]" and fila2[2] == "[X]" and fila3[2] == "[X]":
        ganador = True
        print("Felicitaciones:", jugador1, " ¡GANASTE!")
        break

    if fila1[0] == "[X]" and fila1[1] == "[X]" and fila1[2] == "[X]":
        ganador = True
        print("Felicitaciones:", jugador1, " ¡GANASTE!")
        break

    if fila2[0] == "[X]" and fila2[1] == "[X]" and fila2[2] == "[X]":
        ganador = True
        print("Felicitaciones:", jugador1, " ¡GANASTE!")
        break
    if fila3[0] == "[X]" and fila2[1] == "[X]" and fila3[2] == "[X]":
        ganador = True
        print("Felicitaciones:", jugador1, " ¡GANASTE!")
        break
    if fila1[0] == "[X]" and fila2[1] == "[X]" and fila3[2] == "[X]":
        ganador = True
        print("Felicitaciones:", jugador1, " ¡GANASTE!")
        break
    print(jugador2)
    seleccionJugador2 = input("Ingrese posicion que desea elegir")


    while (seleccionJugador2 in posicion[0:9]):
        print("SELECCIÓN NO VÁLIDA. Intenta de nuevo.")
        mostrarTablero(fila1, fila2, fila3)
        seleccionJugador2 = input("Ingrese la posición que desea elegir")
    while int(seleccionJugador2) > 9 or int(seleccionJugador2) < 1:
        print("SELECCIÓN NO VÁLIDA. Intenta de nuevo.")
        mostrarTablero(fila1, fila2, fila3)
        seleccionJugador2 = input("Ingrese la posición que desea elegir")


    if seleccionJugador2 != posicion[0:9]:
        posicion.append(seleccionJugador2)
        jugadas = jugadas + 1

    if seleccionJugador2 == "1":
        fila1[0] = "[O]"
    if seleccionJugador2 == "2":
        fila1[1] = "[O]"

    if seleccionJugador2 == "3":
        fila1[2] = "[O]"
    if seleccionJugador2 == "4":
        fila2[0] = "[O]"
    if seleccionJugador2 == "5":
        fila2[1] = "[O]"
    if seleccionJugador2 == "6":
        fila2[2] = "[O]"
    if seleccionJugador2 == "7":
        fila3[0] = "[O]"
    if seleccionJugador2 == "8":
        fila3[1] = "[O]"
    if seleccionJugador2 == "9":
        fila3[2] = "[O]"

    mostrarTablero(fila1, fila2, fila3)


    if fila1[0] == "[O]" and fila2[0] == "[O]" and fila3[0] == "[O]":
        ganador = True
        print("Felicitaciones:", jugador2, " ¡GANASTE!")
        break

    if fila1[1] == "[O]" and fila2[1] == "[O]" and fila3[1] == "[O]":
        ganador = True
        print("Felicitaciones:", jugador2, " ¡GANASTE!")
        break
    if fila1[2] == "[O]" and fila2[2] == "[O]" and fila3[2] == "[O]":
        ganador = True
        print("Felicitaciones:", jugador2, " ¡GANASTE!")
        break

    if fila1[0] == "[O]" and fila1[1] == "[O]" and fila1[2] == "[O]":
        ganador = True
        print("Felicitaciones:", jugador2, " ¡GANASTE!")
        break

    if fila2[0] == "[O]" and fila2[1] == "[O]" and fila2[2] == "[O]":
        ganador = True
        print("Felicitaciones:", jugador2, " ¡GANASTE!")
        break
    if fila3[0] == "[O]" and fila2[1] == "[O]" and fila1[2] == "[O]":
        ganador = True
        print("Felicitaciones:", jugador2, " ¡GANASTE!")
        break
    if fila1[2] == "[O]" and fila2[1] == "[O]" and fila3[0] == "[O]":
        ganador = True
        print("Felicitaciones:", jugador2, " ¡GANASTE!")
        break
    if ganador == True:
        break
    if jugadas == 9 and ganador == False:
        print("¡Declaro empate!")
        break
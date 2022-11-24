def juego_uno():
    import random

    salir = True

    instrucciones = str("instrucciones...")


    escenario = \
        '''   
    ~~~~~~~~~|~
             |
     0123456 J    
    ~~~~~~~~~~~   
    '''

    simbolos = '><(((º>'



    # paso 1
    def inicializar_juego(diccionario):
        palabra = random.choice(diccionario).lower()
        tablero = ['_'] * len(palabra)
        return tablero, palabra, []

    # paso 2
    def mostrar_escenario(errores):
        escena = escenario
        for i in range(0, len(simbolos)):
            simbolo = simbolos[i] if i < errores else ' '
            escena = escena.replace(str(i), simbolo)
        print(escena)

    # paso 3
    def mostrar_tablero(tablero, letras_erroneas):
        for casilla in tablero:
            print(casilla, end=' ')
        print()
        print()
        if len(letras_erroneas) > 0:
            print('Letras erróneas:', *letras_erroneas)
            print()

    # paso 4
    def pedir_letra(tablero, letras_erroneas):
        valida = False
        while not valida:
            letra = input('Introduce una letra (a-z): ').lower()
            valida = 'a' <= letra <= 'z' and len(letra) == 1  # es una letra
            if not valida:
                print('Error, la letra tiene que estar entre a y z.')
            else:
                valida = letra not in tablero + letras_erroneas
                if not valida:
                    print('Letra repetida, prueba con otra.')

        return letra

    # paso 5
    def procesar_letra(letra, palabra, tablero, letras_erroneas):
        if letra in palabra:
            print('¡Genial! Has acertado una letra.')
            actualizar_tablero(letra, palabra, tablero)
        else:
            print('¡Oh! Has fallado.')
            letras_erroneas.append(letra)

    # paso 5 (auxiliar)
    def actualizar_tablero(letra, palabra, tablero):
        for indice, letra_palabra in enumerate(palabra):
            if letra == letra_palabra:
                tablero[indice] = letra

    # paso 6
    def comprobar_palabra(tablero):
        return '_' not in tablero

    # bucle principal de juego
    def jugar_al_ahorcado(diccionario):

        tablero, palabra, letras_erroneas = inicializar_juego(diccionario)  # paso 1
        while len(letras_erroneas) < len(simbolos):  # pasos 7 y 8
            mostrar_escenario(len(letras_erroneas))  # paso 2
            mostrar_tablero(tablero, letras_erroneas)  # paso 3
            letra = pedir_letra(tablero, letras_erroneas)  # paso 4
            procesar_letra(letra, palabra, tablero, letras_erroneas)  # paso 5
            if comprobar_palabra(tablero):  # paso 6
                print('¡Felicidades, lo has logrado!')
                break
        else:
            print(f'¡Lo siento! ¡perdiste! La palabra a adivinar era {palabra}.')
            mostrar_escenario(len(letras_erroneas))  # paso 7

        mostrar_tablero(tablero, letras_erroneas)

    def jugar_otra_vez():
        return input('Deseas jugar otra vez (introduce s para sí o cualquier otra cosa para no): ')

    if __name__ == '__main__':

        diccionario = ['casa', 'pescado', 'calamar', 'monigote', 'mundial']

        # bienvenida()
        while True:
            jugar_al_ahorcado(diccionario)
            if jugar_otra_vez() != 's': break

    while salir == True:  # Bucle PRINCIPAL.
        print("""
           ************************
                - AHORCADO -
           ************************ 
            ¡BIENVENIDOS!
           1- Instrucciones
           2- ¡A jugar!
           3- Salir 
           """)

        opcion = int(input("Ingrese la acción que desee realizar  "))
        while opcion < 1 or opcion > 4:  # Cuando el usuario no elije algunas de las opciones que mostramos
            print("Por favor ingrese alguna de las opciones mostradas:")
            opcion = int(input())

        if opcion == 1 or opcion == 2:  # controlar las indentaciones
            if opcion == 1:
                print(instrucciones)
                input("Presione enter para continuar")

            elif opcion == 2:  # empieza el juego
                print("A jugar")
                jugar_al_ahorcado()
                input()

        elif opcion == 3:  # elije la opción de sair
            volver()
            salir = False  # lo que decia antes


def juego_dos():
    # Preguntas que forman parte del juego
    preg1 = str("¿Es el continente más grande?")
    preg2 = str("El idioma más hablado es el chino?")
    preg3 = str("La religión más popular dentro de los paises de este continente es el Budismo")
    preg4 = str("Uno de los paises que conforman este continente es el creador del animé")
    preg5 = str(
        "El deporte más reconocido mundialmente de uno de estos paises que conforman el continenete, ¿Son las artes maricales?")
    preg6 = str("¿Es el segundo continenete más grande?")
    preg7 = str("¿Está dividido tridimencionalmente?")
    preg8 = str("¿Fue descubierto por los españoles en el año 1492?")
    preg9 = str("El idioma más hablado es el español?")
    preg10 = str("¿La mayoria de sus paises lograron independizarse dentro de los ultimos doscientos años?")
    preg11 = str("¿Es el continente más pequeño?")
    preg12 = str("¿Sus paises son insulares?")
    preg13 = str("¿El idioma más hablado es el inglés?")
    preg14 = str("¿El deporte caracteristico de uno de sus paises es el rugby?")
    preg15 = str("¿Uno de sus paises es el habitad natural de los canguros y otros animales considerados peligrosos?")
    preg16 = str("¿Es el tercer continenete más grande?")
    preg17 = str("¿El mar más conocido de esta zona es el mar Rojo?")
    preg18 = str("¿Hay piramides?")
    preg19 = str("¿La mayoria de sus paises fueron o son colonias inglesas?")
    preg20 = str("¿Su moneda principal es el Euro?")
    preg21 = str("¿Reconocido historicamente por sus monarquias y revoluciones?")
    preg22 = str("¿Cuna del arte")
    preg23 = str("¿Territorio donde se desarrollo ambas guerras mundiales?")
    preg24 = str("¿Origen de la filosofía y mitología griega?")
    preg25 = str("¿Es Asía?")
    preg26 = str("¿Es América?")
    preg27 = str("¿Es Europa?")
    preg28 = str("¿Es Oceania?")
    preg29 = str("¿Es África?")
    perdiste = str("Lo adiviné ¡PERDISTE! (/¯◡ ‿ ◡)/¯ ~ ┻━┻")
    ganaste = str("No lo adiviné, Ganaste... x⸑x")

    instrucciones = str(
        "Instrucciones:\n1- Pensar uno de los cinco contienetes para que el programa intente adivinarlo (América, Ásia, Árfica, Oceanía o Europa)\n2- El programa te irá haciendo preguntas sobre las caracteristicas de los continentes\n3- Si algunas de esas caracteristicas coinciden con el continenete que pensaste entonces debes marcar la opción SI\n4- Si algunas de esas caracteristicas NO coincicen con el continente que pensaste entonces debes marcas la opción NO\n5- Si el continente que te muestra el programa al finalizar el juego no coincide con el que vos pensaste entonces ¡felicitaciones! GANASTE\n6- Si al finaizal el programa si te muestra el continenete que pensaste entonces lo siento, has perdido\nGracias :) ¡Que te diviertas!")

    salir = True

    while salir == True:  # Bucle PRINCIPAL.
        print("""
        ************************
        - PIENSA UN CONTINENTE -
        ************************ 
         ¡BIENVENIDOS!
        1- Instrucciones
        2- ¡A jugar!
        3- Salir 
        """)

        opcion = int(input("Ingrese la acción que desee realizar "))
        while opcion < 1 or opcion > 4:  # Cuando el usuario no elije algunas de las opciones que mostramos
            print("Por favor ingrese alguna de las opciones mostradas:")
            opcion = int(input())

        if opcion == 1 or opcion == 2:  # controlar las indentaciones
            if opcion == 1:
                print(instrucciones)
                input("Presione enter para continuar")

            elif opcion == 2:  # empieza el juego
                print("A jugar")
                print("Piensa un continente")
                input()
                print(preg1, """
                1- SI
                2- NO 
                """)
                si_no = int(input())

                if si_no == 1:  # El SI general
                    print(preg2, """
                    1- SI
                    2- NO 
                    """)
                    si_no = int(input())
                    if si_no == 1:
                        print(preg25, """
                        1- SI
                        2- NO 
                        """)
                        si_no = int(input())
                        if si_no == 1:
                            print(perdiste)
                        elif si_no == 2:
                            print(ganaste)  # Fin del si-si
                    elif si_no == 2:
                        print(preg8, """
                        1- SI
                        2- NO 
                        """)
                        si_no = int(input())
                        if si_no == 1:
                            print(preg26, """
                            1- SI
                            2- NO 
                            """)
                            si_no = int(input())
                            if si_no == 1:
                                print(perdiste)
                            elif si_no == 2:
                                print(ganaste)
                        elif si_no == 2:
                            print(preg18, """
                            1- SI
                            2- NO 
                            """)
                            si_no = int(input())
                            if si_no == 1:
                                print(preg29, """
                                1- SI
                                2- NO 
                                """)
                                si_no = int(input())
                                if si_no == 1:
                                    print(perdiste)
                                elif si_no == 2:
                                    print(ganaste)
                            elif si_no == 2:
                                print(preg15, """
                                1- SI
                                2- NO 
                                """)
                                si_no = int(input())
                                if si_no == 1:
                                    print(preg28, """
                                    1- SI
                                    2- NO 
                                    """)
                                    si_no = int(input())
                                    if si_no == 1:
                                        print(perdiste)
                                    elif si_no == 2:
                                        print(ganaste)
                                elif si_no == 2:
                                    print(preg27, """
                                    1- SI
                                    2- NO 
                                    """)
                                    si_no = int(input())
                                    if si_no == 1:
                                        print(perdiste)
                                    elif si_no == 2:
                                        print(ganaste)
                elif si_no == 2:  # El NO general
                    print(preg11, """
                    1- SI
                    2- NO 
                    """)
                    si_no = int(input())
                    if si_no == 1:
                        print(preg15, """
                        1- SI
                        2- NO 
                        """)
                        si_no = int(input())
                        if si_no == 1:
                            print(preg28, """
                               1- SI
                               2- NO 
                               """)
                            si_no = int(input())
                            if si_no == 1:
                                print(perdiste)
                            elif si_no == 2:
                                print(ganaste)
                    elif si_no == 2:
                        print(preg20, """
                            1- SI
                            2- NO 
                            """)
                        si_no = int(input())
                        if si_no == 1:
                            print(preg27, """
                                1- SI
                                2- NO 
                                """)
                            si_no = int(input())
                            if si_no == 1:
                                print(perdiste)
                            elif si_no == 2:
                                print(ganaste)
                        elif si_no == 2:
                            print(preg8, """    
                                 1- SI
                                 2- NO  
                                 """)
                            si_no = int(input())
                            if si_no == 1:
                                print(preg26, """
                                    1- SI
                                    2- NO 
                                    """)
                                si_no = int(input())
                                if si_no == 1:
                                    print(perdiste)
                                elif si_no == 2:
                                    print(ganaste)
                            elif si_no == 2:
                                print(preg29, """
                                        1- SI
                                        2- NO 
                                        """)
                                si_no = int(input())
                                if si_no == 1:
                                    print(perdiste)
                                elif si_no == 2:
                                    print(ganaste)



                    elif si_no == 2:
                        print(preg18, """
                        1- SI
                        2- NO 
                        """)
                        si_no = int(input())
                        if si_no == 1:
                            print(preg29, """
                            1- SI
                            2- NO 
                            """)
                            si_no = int(input())
                            if si_no == 1:
                                print(perdiste)
                            elif si_no == 2:
                                print(ganaste)
                        elif si_no == 2:
                            print(preg20, """
                            1- SI
                            2- NO 
                            """)
                            si_no = int(input())
                            if si_no == 1:
                                print(preg27, """
                                1- SI
                                2-NO
                                """)
                                si_no = int(input())
                                if si_no == 1:
                                    print(perdiste)
                                elif si_no == 2:
                                    print(ganaste)
                            elif si_no == 2:
                                print(preg26, """
                                1- SI
                                2- NO
                                """)
                                si_no = int(input())
                                if si_no == 1:
                                    print(perdiste)
                                elif si_no == 2:
                                    print(ganaste)


        elif opcion == 3:  # elije la opción de salir
            volver()
            salir = False  # lo que decia antes


def juego_tres():

    instrucciones = str('instrucciones..')

    salir = True



    def inicio_tateti():
        fila1 = []
        fila2 = []
        fila3 = []
        elemento = ["'''"]
        for i in range(0, 3, 1):
            fila1.append(elemento)
        for j in range(0, 3, 1):
            fila2.append(elemento)
        for k in range(0, 3, 1):
            fila3.append(elemento)

        def mostrarTablero(fila1, fila2, fila3):
            print(fila1)
            print(fila2)
            print(fila3)

        jugador1 = input("Jugador 1 (X), ingrese su nombre")
        jugador2 = input("Jugador 2 (O), ingrese su nombre")

        ganador = False

        # Contador de todas las jugadas (de ambos jugadores)
        jugadas = 0

        # Ciclo para que el jugador elija la posición que desea elegir. Se repite 9 veces, es la cantidad de turnos entre los dos jugadores
        while (jugadas < 9):

            print(jugador1)
            seleccionJugador1 = input("Ingrese la posicion que desea elegir")
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
            if seleccionJugador1 == "6":
                fila2[2] = "[X]"
            if seleccionJugador1 == "7":
                fila3[0] = "[X]"
            if seleccionJugador1 == "8":
                fila3[1] = "[X]"
            if seleccionJugador1 == "9":
                fila3[2] = "[X]"

            # Se muestra el tablero cada vez que un jugador elige una opcion

            mostrarTablero(fila1, fila2, fila3)
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
            if jugadas == 8 and ganador == False:
                print("¡Declaro empate!")
                break

    while salir == True:  # Bucle PRINCIPAL.
        print("""
                ************************
                     - TA-TE-TI -
                ************************ 
                 ¡BIENVENIDOS!
                1- Instrucciones
                2- ¡A jugar!
                3- Salir 
                """)

        opcion = int(input("Ingrese la acción que desee realizar  "))
        while opcion < 1 or opcion > 4:  # Cuando el usuario no elije algunas de las opciones que mostramos
            print("Por favor ingrese alguna de las opciones mostradas:")
            opcion = int(input())

        if opcion == 1 or opcion == 2:  # controlar las indentaciones
            if opcion == 1:
                print(instrucciones)
                input("Presione enter para continuar")

            elif opcion == 2:  # empieza el juego
                print("A jugar")
                inicio_tateti()
                input()

        elif opcion == 3:  # elije la opción de sair
            volver()
            salir = False  # lo que decia antes



def volver():

    salir= True

    while salir==True: #Bucle PRINCIPAL.
        print("""
        ************************
           - SALA DE JUEGOS -
        ************************ 
         ¡BIENVENIDOS!
        1- Ahorcado
        2- Piensa un continente
        3- TA-TE-TI
        """)

        opcion = int(input("Ingrese la acción que desee realizar "))
        while opcion < 1 or opcion > 4:  # Cuando el usuario no elije algunas de las opciones que mostramos
            print("Por favor ingrese alguna de las opciones mostradas:")
            opcion = int(input())

        if opcion == 1 or opcion == 2 or opcion == 3:  # controlar las indentaciones
            if opcion == 1:  # selecciona el Ahorcado
                juego_uno()
                break

            elif opcion == 2:  # selecciona Piensa un continente
                juego_dos()
                break

            elif opcion == 3:  # selecciona TA-TE-TI
                juego_tres()
                break

    # elif opcion == 3: #elije la opción de sair
    #     salir = False #lo que decia antes


volver()
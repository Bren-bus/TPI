import random

salir= True

instrucciones = str("INSTRUCCIONES:\n 1-El jugador 1 (programa) piensa una palabra y coloca tantas espacios (guiones) como letras tenga ésta y el jugador 2 tiene que adivinarla diciendo letras.\n2-El jugador 2 dice una letra y el programa revisa si la letra se encuentra en la palabra que ha pensado.\n3-Si la letra está la anota en el lugar que corresponda de las rayas que ha puesto previamente. Si la letra no está escribe la letra para que el jugador 2 sepa las letras que ha dicho y dibuja una parte del pez del ahorcado.\n4-Se ha de mostrar un anzuelo sin el pez y un espacio para poner las letras que se van diciendo.  \n4-El pez que se va dibujando tiene siete partes, por lo que el jugador tiene siete opciones de fallar.\n5-Gana el jugador si consigue descifrar la palabra antes de que el muñeco este completo.")


escenario = \
    '''   
~~~~~~~~~|~
         |
 0123456 J    
~~~~~~~~~~~   
'''

simbolos = '><(((º>' #los símbolos que se irán reemplazando en las posiciones numeradas en "escenario"


# paso 1. Declaro una función encargada de seleccionar una de las palabras contenidas en el array "palabras", de manera aleatoria. Se generan los espacios donde irán las letras según la longitud de la palabra.
def inicializar_juego(palabras):
    palabra = random.choice(palabras).lower()
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
        valida = 'a' <= letra <= 'z' and len(letra) == 1 # es una letra
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
        print('Perdiste! La palabra a adivinar era {palabra}.')
        mostrar_escenario(len(letras_erroneas))  # paso 7

    mostrar_tablero(tablero, letras_erroneas)


#Opción de volver al menú del juego/menú principal
def opciones():
    return input('Deseas jugar otra vez (introduce s para sí o cualquier otra cosa para no): ')





if __name__ == '__main__':

    palabras = ['casa', 'pescado', 'calamar', 'monigote', 'mundial']


    while True:
        jugar_al_ahorcado(palabras)
        if opciones() != 's': break

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
            salir = False  # lo que decia antes
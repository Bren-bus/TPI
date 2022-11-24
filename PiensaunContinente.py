preg1 = str("¿Es el continente más grande?")
preg2 = str("El idioma más hablado es el chino?")
preg3 = str("La religión más popular dentro de los paises de este continente es el Budismo")
preg4 = str("Uno de los paises que conforman este continente es el creador del animé")
preg5 = str("El deporte más reconocido mundialmente de uno de estos paises que conforman el continenete, ¿Son las artes maricales?")
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
preg26= str("¿Es América?")
preg27 = str("¿Es Europa?")
preg28 = str("¿Es Oceania?")
preg29 = str("¿Es África?")
perdiste = str("¡PERDISTE!")
ganaste = str("Ganaste...")

instrucciones = str("Instrucciones:\n1- Pensar uno de los cinco contienetes para que el programa intente adivinarlo (América, Ásia, Árfica, Oceanía o Europa)\n2- El programa te irá haciendo preguntas sobre las caracteristicas de los continentes\n3- Si algunas de esas caracteristicas coinciden con el continenete que pensaste entonces debes marcar la opción SI\n4- Si algunas de esas caracteristicas NO coincicen con el continente que pensaste entonces debes marcas la opción NO\n5- Si el continente que te muestra el programa al finalizar el juego no coincide con el que vos pensaste entonces ¡felicitaciones! GANASTE\n6- Si al finaizal el programa si te muestra el continenete que pensaste entonces lo siento, has perdido\nGracias :) ¡Que te diviertas!")





salir= True

while salir==True: #Bucle PRINCIPAL. 
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

elif opcion == 3:  # elije la opción de sair
    salir = False  # lo que decia antes


import Interfaz as interfaz

from Vista import InterfazGrafica as ig

opcion = ""


while opcion != "1" and opcion != "2" and opcion != "0":
    print("Bienvenido al santuario de animales de Adrián y Sergio")
    print("\nSelecciona una opción de interfaz")
    print("\n1. Interfaz de Consola")
    print("2. Interfaz Grafica")
    print("0. Salir sin entrar en ninguna interfaz")
    opcion = input("\nIntroduce una opción")
    if opcion == "1":
        interfaz.ejecutar()
    elif opcion == "2":
        print("Abre la ventana gráfica. "
              "\nSe abrió una aplicación de python, en tu barra de escritorio")
        ig.mensajeBienvenida()
    elif opcion == "0":
        print("Saliste de la Aplicación")
    else:
        print("No has seleccionado una opcion correcta")







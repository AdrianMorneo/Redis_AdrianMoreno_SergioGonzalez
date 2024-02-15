import redis
from redis import connection

import Interfaz as interfaz
from Vista import InterfazGrafica as ig
import Conexion as con

opcion = ""
# Comprueba la conexión a redis
conexion = con.conectar()

try:
    pruebaArranque = conexion.get('Hay conexión')
    # Bucle para solicitar la opción de interfaz hasta que se elija una válida
    while opcion != "1" and opcion != "2" and opcion != "0":
        print("Bienvenido al santuario de animales de Adrián y Sergio")
        print("\nSelecciona una opción de interfaz")
        print("\n1. Interfaz de Consola")
        print("2. Interfaz Grafica")
        print("0. Salir sin entrar en ninguna interfaz")
        opcion = input("\nIntroduce una opción: ")

        # Verifica la opción seleccionada y ejecuta la interfaz correspondiente
        if opcion == "1":
            interfaz.ejecutar()  # Ejecutar la interfaz de consola
        elif opcion == "2":
            print("Abre la ventana gráfica. "
                  "\nSe abrió una aplicación de python, en tu barra de escritorio")
            ig.mensajeBienvenida()  # Mostrar la ventana gráfica de bienvenida
        elif opcion == "0":
            print("Saliste de la Aplicación")
        else:
            print("No has seleccionado una opción correcta")
except redis.ConnectionError:
    print("\nDebe de arrancar Redis para usar la Aplicacion")







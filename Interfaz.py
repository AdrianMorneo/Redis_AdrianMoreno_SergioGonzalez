#Importación de bibliotecas
from art import tprint
from colorama import Fore, Style, init
from pyfiglet import Figlet
import os

from Animal import Animal
from Colaborador import Colaborador
from Conexion import Conexion


colaborador = Colaborador()
animal = Animal()

conexion = Conexion()

init(autoreset=True) # Inicialización de Colorama -- init(autoreset=True) que automáticamente resetea los estilos de color después de cada impresión.

class Santuario: # Representa la aplicación principal del santuario de animales.

    #  Inicializa las listas de animales y colaboradores, así como las instancias de Figlet para diferentes estilos de fuentes.
    def __init__(self):
        self.animales = []
        self.colaboradores = []
        self.figlet = Figlet(font='slant')
        self.figlet_big = Figlet(font='block')

    # Imprime un mensaje de bienvenida utilizando la función tprint con el nombre del santuario y los nombres "Adrian y Sergio".
    def imprimir_bienvenida(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        tprint("Santuario de Animales")
        tprint("-**Adrian y Sergio**-")

    #Imprime el menú de operaciones para Animales.
    def imprimir_menu_principal(self):
        print("\n" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + self.figlet.renderText("Menu Principal") + Style.RESET_ALL)
        print("\t\t" + Fore.YELLOW + "╔═══════════════════════════════╗")
        print("\t\t"+Fore.YELLOW+"║╔═════════════════════════════╗║")
        print("\t\t"+Fore.YELLOW + "║║\t  "+Fore.LIGHTWHITE_EX+" 1. " + Fore.LIGHTYELLOW_EX + "Animales" + Style.RESET_ALL + Fore.YELLOW+"             ║║")
        print("\t\t"+Fore.YELLOW + "║║\t  "+Fore.LIGHTWHITE_EX+" 2. " + Fore.LIGHTYELLOW_EX + "Colaboradores" + Style.RESET_ALL + Fore.YELLOW+"        ║║")
        print("\t\t"+Fore.YELLOW + "║║\t  "+Fore.LIGHTWHITE_EX+" 0. " + Fore.RED + "Salir" + Style.RESET_ALL + Fore.YELLOW+"                ║║")
        print("\t\t"+Fore.YELLOW+"║╚═════════════════════════════╝║")
        print("\t\t" + Fore.YELLOW + "╚═══════════════════════════════╝")

    # Imprime el menú de operaciones para Animales.
    def imprimir_menu_animales(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + Fore.LIGHTGREEN_EX + Style.BRIGHT + self.figlet.renderText("Animales") + Style.RESET_ALL)
        print("\t\t" + Fore.GREEN + "╔═══════════════════════════════════════╗")
        print("\t\t"+ Fore.GREEN+"║╔═════════════════════════════════════╗║")
        print("\t\t"+Fore.GREEN + "║║\t"+Fore.LIGHTWHITE_EX+" 1. " + Fore.LIGHTGREEN_EX + "Agregar un animal" + Style.RESET_ALL + Fore.GREEN + "              ║║")
        print("\t\t"+Fore.GREEN + "║║\t"+Fore.LIGHTWHITE_EX+" 2. " + Fore.LIGHTGREEN_EX + "Eliminar un animal" + Style.RESET_ALL + Fore.GREEN + "             ║║")
        print("\t\t"+Fore.GREEN + "║║\t"+Fore.LIGHTWHITE_EX+" 3. " + Fore.LIGHTGREEN_EX + "Modificar un animal" + Style.RESET_ALL + Fore.GREEN + "            ║║")
        print("\t\t"+Fore.GREEN + "║║\t"+Fore.LIGHTWHITE_EX+" 4. " + Fore.LIGHTGREEN_EX + "Buscar un animal" + Style.RESET_ALL + Fore.GREEN + "               ║║")
        print("\t\t"+Fore.GREEN + "║║\t"+Fore.LIGHTWHITE_EX+" 5. " + Fore.LIGHTGREEN_EX + "Mostrar todos los animales" + Style.RESET_ALL + Fore.GREEN + "     ║║")
        print("\t\t"+Fore.GREEN + "║║\t"+Fore.LIGHTWHITE_EX+" 0. " + Fore.RED + "Volver al menú principal" + Style.RESET_ALL + Fore.GREEN + "       ║║")
        print("\t\t"+ Fore.GREEN+"║╚═════════════════════════════════════╝║")
        print("\t\t" + Fore.GREEN + "╚═══════════════════════════════════════╝")

    # Imprime Imprime el menú de operaciones para Colaboradores.
    def imprimir_menu_colaboradores(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + Fore.LIGHTBLUE_EX + Style.BRIGHT +self.figlet.renderText("Colaboradores") + Style.RESET_ALL)
        print("\t\t" + Fore.BLUE + "╔═══════════════════════════════════════════╗")
        print("\t\t"+Fore.BLUE + "║╔═════════════════════════════════════════╗║")
        print("\t\t"+Fore.BLUE + "║║\t"+Fore.LIGHTWHITE_EX+" 1. " + Fore.LIGHTBLUE_EX + "Agregar un colaborador" + Style.RESET_ALL + Fore.BLUE + "              ║║")
        print("\t\t"+Fore.BLUE + "║║\t"+Fore.LIGHTWHITE_EX+" 2. " + Fore.LIGHTBLUE_EX + "Eliminar un colaborador" + Style.RESET_ALL + Fore.BLUE + "             ║║")
        print("\t\t"+Fore.BLUE + "║║\t"+Fore.LIGHTWHITE_EX+" 3. " + Fore.LIGHTBLUE_EX + "Modificar un colaborador" + Style.RESET_ALL + Fore.BLUE + "            ║║")
        print("\t\t"+Fore.BLUE + "║║\t"+Fore.LIGHTWHITE_EX+" 4. " + Fore.LIGHTBLUE_EX + "Buscar un colaborador" + Style.RESET_ALL + Fore.BLUE + "               ║║")
        print("\t\t"+Fore.BLUE + "║║\t"+Fore.LIGHTWHITE_EX+" 5. " + Fore.LIGHTBLUE_EX + "Mostrar todos los colaboradores" + Style.RESET_ALL + Fore.BLUE + "     ║║")
        print("\t\t"+Fore.BLUE + "║║\t"+Fore.LIGHTWHITE_EX+" 0. " + Fore.RED + "Volver al menú principal" + Style.RESET_ALL + Fore.BLUE + "            ║║")
        print("\t\t"+Fore.BLUE + "║╚═════════════════════════════════════════╝║")
        print("\t\t" + Fore.BLUE + "╚═══════════════════════════════════════════╝")

#Punto de entrada principal de la aplicación.
#Utiliza bucles para permitir al usuario navegar por los diferentes menús y realizar operaciones.
#Imprime los menús y opciones, y realiza las operaciones que quiera el usuario.
    def ejecutar(self):
        global colaborador
        self.imprimir_bienvenida()
        while True:

            self.imprimir_menu_principal()
            opcion_principal = input("\n\t"+Fore.CYAN + Style.BRIGHT + "Seleccione una opción: " + Style.RESET_ALL)

            if opcion_principal == "0":
                tprint("HASTA PRONTO")
                break

            elif opcion_principal == "1":
                while True:
                    self.imprimir_menu_animales()
                    opcion_animales = input("\n\t"+Fore.CYAN + Style.BRIGHT + "Seleccione una opción: " + Style.RESET_ALL)

                    if opcion_animales == "0":
                        break
                    elif opcion_animales == "1":
                        print("")

                    elif opcion_animales == "2":
                        print("")

                    elif opcion_animales == "3":
                        print("")

                    elif opcion_animales == "4":
                        print("")

                    elif opcion_animales == "5":
                        print("")

                    else:
                        print(Fore.RED + "Opción no válida." + Style.RESET_ALL)

            elif opcion_principal == "2":
                while True:
                    self.imprimir_menu_colaboradores()
                    opcion_colaboradores = input("\n\t"+Fore.CYAN + Style.BRIGHT + "Seleccione una opción: " + Style.RESET_ALL)

                    if opcion_colaboradores == "0":
                        break

                    elif opcion_colaboradores == "1":
                        colaborador.nuevo()
                        print(Fore.GREEN + "Nuevo colaborador REGISTRADO" + Style.RESET_ALL)

                    elif opcion_colaboradores == "2":
                        colaborador.borrar()
                        print(Fore.GREEN + "Colaborador ELIMINADO" + Style.RESET_ALL)

                    elif opcion_colaboradores == "3":
                        colaborador.modificar()
                        print(Fore.GREEN + "Colaborador MODIFICADO" + Style.RESET_ALL)

                    elif opcion_colaboradores == "4":

                        print(Fore.GREEN + "Colaborador: " + Style.RESET_ALL)
                        colaborador = colaborador.buscar()

                    elif opcion_colaboradores == "5":
                        colaboradores = colaborador.mostrarTodos()
                        print(Fore.GREEN + "Colaboradores registrados:" + Style.RESET_ALL)
                        print(colaboradores)

                    else:
                        print(Fore.RED + "Opción no válida." + Style.RESET_ALL)

            else:
                print(Fore.RED + "Opción no válida." + Style.RESET_ALL)

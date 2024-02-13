from datetime import datetime

def validarTipoA(tipo):
    tipos_animales = ["MAMÍFERO", "AVE", "PEZ", "REPTIL", "ANFIBIO"]

    if tipo in tipos_animales:
        return True
    else:
        return False


def validarDNI(dni):
    # Validar DNI con 8 números y una letra al final
    """
    Comprueba que un DNI tenga el formato correcto
    :param dni: El DNI a validar
    :return: Devuelve si es correcto o no
    """
    return len(dni) == 9 and dni[:-1].isdigit() and dni[-1].isalpha()

def validarNombre(nombre):
    # Validar que el nombre tenga más de 2 caracteres
    """
    Comprueba que un nombre tenga al menos 2 caracteres
    :param nombre: EL nombre a validar
    :return: Si se cumple o no
    """
    return len(nombre) > 1

def validarTelefono(telefono):
    # Validar que el teléfono tenga 9 números
    """
    Metodo para validar el formato de un numero telefono
    :param telefono:
    :return:
    """
    return len(telefono) == 9 and telefono.isdigit()

def validarFecha(fecha):
    # Validar que la fecha de nacimiento sea anterior al 2020
    """
    Comprueba que una fecha sea valida
    :param fecha_nacimiento: Recibe la fecha
    :return: True o False en funcion de si es valida o no
    """
    try:
        fecha_nac = datetime.strptime(fecha, '%d-%m-%Y')
        return 2025 > fecha_nac.year > 1950
    except ValueError:
        return False

def fallo(fallos, mensaje):
    """
    Metodo que permite gestionar los intentos en las acciones del usuario
    Muestra los errores actuales y los incrementa en 1
    :param fallos: Los fallos en ese momento
    :param mensaje: El mensaje que se quiere mostrar junto al numero de fallos
    :return: Devuelve los errores incrementados en 1
    """
    print(f"\t\t{mensaje} \n\t\tIntentos: {fallos + 1} de 5")
    return fallos + 1

def validarEdad(edad):
    try:
        edad = int(edad)
        if 0 <= edad < 100:
            return True
        else:
            return False
    except ValueError:
        return False
def confirmacion(mensaje, tipo):
    """
    Metodo que permite la gestion de confirmaciones
    :param mensaje: La pregunta que se le hace al usuario
    :param tipo: Cadena para personalizar uno de los mensajes
    :return: True o False dependiendo de la eleccion del usuario
    """
    finConfirmacion = False
    fallos = 0
    while not finConfirmacion and fallos < 5:
        eleccion = input(f"{mensaje} [S/N]: ").lower()
        if eleccion == "s":
            finConfirmacion = True
            if tipo is not None:
                print(f"{tipo} realizada.")
            return True
        elif eleccion == "n":
            finConfirmacion = True
            if tipo is not None:
                print(f"{tipo} cancelada.")
            return False
        else:
            fallos = fallo (fallos, "Entrada no valida.")
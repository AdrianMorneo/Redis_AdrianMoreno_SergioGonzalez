
import Conexion as conect

cnt = conect.conectar()

def agregarAnimal():
    id = cnt.incr('idAnimal')
    tipo = input("Introduce el tipo del animal: ")
    nombre = input("Introduce el nombre del animal: ")
    edad = int(input("Introduce la edad del animal: "))
    apadrinado = False
    dniPadrino = ''

    animal = {
        'id': id,
        'tipo': tipo,
        'nombre': nombre,
        'edad': edad,
        'apadrinado': apadrinado,
        'dniPadrino': dniPadrino
    }

    cnt.set(f'animal:{animal["id"]}:tipo', animal['tipo'])
    cnt.set(f'animal:{animal["id"]}:nombre', animal['nombre'])
    cnt.set(f'animal:{animal["id"]}:edad', str(animal['edad']))
    cnt.set(f'animal:{animal["id"]}:apadrinado',str(animal['apadrinado']))
    cnt.set(f'animal:{animal["id"]}:dniPadrino', animal['dniPadrino'])
    print(f"Animal agregado correctamente con ID: {id}")

def mostrarTodosA():
    keys = cnt.keys('animal:*')

    if keys:
        print("Animales guardados en la base de datos:\n")
        for key in keys:
            # Recuperar los valores de cada animal
            tipo = cnt.get(f'{key}:tipo')
            nombre = cnt.get(f'{key}:nombre')
            #edad = int(cnt.get(f'{key}:edad'))
            #apadrinado = cnt.get(f'{key}:apadrinado')
            #dniPadrino = cnt.get(f'{key}:dniPadrino')

            # Mostrar la información del animal
            print(f"Tipo: {tipo}, Nombre: {nombre}")
    else:
        print("No hay animales guardados en la base de datos")
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
    cnt.set(f'animal:{animal["id"]}:apadrinado', str(animal['apadrinado']))
    cnt.set(f'animal:{animal["id"]}:dniPadrino', animal['dniPadrino'])

    print(f"Animal agregado correctamente con ID: {id}")

def devolverAnimal(id_animal):
    # Obtener los valores del animal desde Redis
    tipo = cnt.get(f'animal:{id_animal}:tipo')
    nombre = cnt.get(f'animal:{id_animal}:nombre')
    edad = int(cnt.get(f'animal:{id_animal}:edad'))
    apadrinado_str = cnt.get(f'animal:{id_animal}:apadrinado')
    apadrinado = apadrinado_str == b'True'
    dniPadrino = cnt.get(f'animal:{id_animal}:dniPadrino')

    # Devolver un diccionario con los valores del animal
    animal = {
        'id': id_animal,
        'tipo': tipo,
        'nombre': nombre,
        'edad': edad,
        'apadrinado': apadrinado,
        'dniPadrino': dniPadrino
    }
    return animal

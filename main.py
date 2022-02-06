from time import sleep


class Mesa:
    def __init__(self, id: int, capacidad: int, tiempo_restante: int = 0):
        self.id = id
        self.capacidad = capacidad
        self.tiempo_restante = tiempo_restante

    def __str__(self):
        return f"Mesa: {self.id}\nCapacidad: {self.capacidad}\nTiempo restante: {self.tiempo_restante}"


class Grupo:
    def __init__(self, posicion: int, comensales: int, tiempo: int = 7200):
        self.posicion = posicion
        self.comensales = comensales
        self.tiempo = tiempo


def mesas_disponibles(mesas: dict):
    mesas_libres = []
    for mesa in mesas:
        if mesas[mesa].tiempo_restante <= 0:
            mesas_libres.append(mesas[mesa])

    return mesas_libres


def mostrar_info(mesas: dict, colas: list, segundos: int):
    print(f"\n\nSegundo: {segundos}")
    print("\nCola atendida: ")
    if colas[1]:
        for grupo in colas[1]:
            print(f"Posicion: {grupo.posicion}\t\tNumero de personas: "
                  f"{grupo.comensales}\t\tTiempo para comer: {grupo.tiempo}")
    else:
        print("Vacia")

    print("\nCola sin atender: ")
    if colas[0]:
        for grupo in colas[0]:
            print(f"Posicion: {grupo.posicion}\t\tNumero de personas: "
                  f"{grupo.comensales}\t\tTiempo para comer: {grupo.tiempo}")
    else:
        print("Vacía")

    print("\nMesas: ")
    for mesa in mesas:
        if mesas[mesa].tiempo_restante <= 0:
            print(f"Id: {mesas[mesa].id}\t\tCapacidad: {mesas[mesa].capacidad}\t\tDisponibilidad: Disponible")
        else:
            print(f"Id: {mesas[mesa].id}\t\tCapacidad: {mesas[mesa].capacidad}\t\tDisponibilidad: Ocupada"
                  f"\t\t\tTiempo restante: {mesas[mesa].tiempo_restante}")


def main(mesas: dict, colas: list, tiempo: int = 300):
    segundos = 0

    while colas[0] or colas[1]:

        mesas_libres = mesas_disponibles(mesas)

        mostrar_info(mesas, colas, segundos)

        if colas[1]:
            for posicion, grupo in enumerate(colas[1]):
                for id, mesa in enumerate(mesas_libres):
                    if mesa.capacidad == grupo.comensales:
                        mesa.tiempo_restante = 7200
                        colas[1].pop(posicion)
                        mesas_libres.pop(id)
                        break
                else:
                    for id, mesa in enumerate(mesas_libres):
                        if mesa.capacidad == grupo.comensales + 1:
                            mesa.tiempo_restante = 7200
                            colas[1].pop(posicion)
                            mesas_libres.pop(id)
                            break

        if colas[0]:
            for posicion, grupo in enumerate(colas[0]):
                for id, mesa in enumerate(mesas_libres):
                    if mesa.capacidad == grupo.comensales:
                        mesa.tiempo_restante = 7200
                        colas[0].pop(posicion)
                        mesas_libres.pop(id)
                        break
                else:
                    for id, mesa in enumerate(mesas_libres):
                        if mesa.capacidad == grupo.comensales + 1:
                            mesa.tiempo_restante = 7200
                            colas[0].pop(posicion)
                            mesas_libres.pop(id)
                            break

        segundos += tiempo
        for mesa in mesas:
            if mesas[mesa].tiempo_restante >= 0:
                mesas[mesa].tiempo_restante -= tiempo

        sleep(1)


mesa1 = Mesa(1, 2, 7200)
mesa2 = Mesa(2, 3, 5400)
mesa3 = Mesa(3, 4)
mesa4 = Mesa(4, 5, 2400)
mesa5 = Mesa(5, 6, 4800)
mesa6 = Mesa(6, 8, 1200)
mesa7 = Mesa(7, 3)
mesa8 = Mesa(8, 5, 1800)
mesa9 = Mesa(9, 7, 3600)
mesa10 = Mesa(10, 1)
mesa11 = Mesa(11, 8)
mesa12 = Mesa(12, 9, 1200)
mesas_prueba = {
    1: mesa1,
    2: mesa2,
    3: mesa3,
    4: mesa4,
    5: mesa5,
    6: mesa6,
    7: mesa7,
    8: mesa8,
    9: mesa9,
    10: mesa10,
    11: mesa11,
    12: mesa12
}

grupo1 = Grupo(1, 2, 5400)
grupo2 = Grupo(2, 5, 3600)
grupo3 = Grupo(3, 8)
grupo4 = Grupo(4, 4, 9600)
grupo5 = Grupo(5, 6)
grupo6 = Grupo(6, 4)
grupo7 = Grupo(7, 3, 600)
grupo8 = Grupo(8, 7, 4800)
grupo9 = Grupo(9, 6, 8400)
grupo10 = Grupo(10, 1)

sin_atender = [
    grupo4,
    grupo5,
    grupo6,
    grupo7,
    grupo8,
    grupo9,
    grupo10
]
atendidos = [
    grupo1,
    grupo2,
    grupo3
]
colas_prueba = [sin_atender, atendidos]

tiempo_prueba = 600

main(mesas_prueba, colas_prueba, tiempo_prueba)

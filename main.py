"""
Primero se mirará la primera persona que llegó a la cola, después se mira si hay una mesa con misma capacidad o uno más
que el número de personas, y si no está reservado se asignará esa mesa a las personas.
El tiempo se medirá en minutos y se asumirá que todas las personas tardarán 120 minutos en comer
"""


# Mesa
class Mesa:
    def __init__(self, id: int, capacidad: int, tiempo_restante: int):
        self.id = id
        self.capacidad = capacidad
        self.tiempo_restante = tiempo_restante

    def libre(self):
        if self.tiempo_restante == 0:
            pass

    def __str__(self):
        return f"Mesa: {self.id}\nCapacidad: {self.capacidad}\nTiempo restante: {self.tiempo_restante}"


# Reserva
class Reserva:
    def __init__(self, personas: int, minuto: int):
        self.personas = personas
        self.minuto = minuto

    def __str__(self):
        return f"Personas: {self.personas}\nMinuto: {self.minuto}"


# Lista de las mesas disponibles
def mesas_disponibles(mesas: dict, reservas: list, minutos: int):
    mesas_libres = []
    reservas = hacer_reservas(reservas, mesas)
    for mesa in mesas:
        if mesas[mesa].tiempo_restante == 0:
            if mesas[mesa].id in reservas:
                if not minutos - 120 < reservas[mesas[mesa].id][0] < minutos + 120:
                    mesas_libres.append(mesas[mesa])
            else:
                mesas_libres.append(mesas[mesa])

    return mesas_libres


# Reservar la mesa con mejor optimización de sitios para la cantidad de personas que sean
def hacer_reservas(reservas: list, mesas: dict):
    diccionario_reservas = {}
    for reserva in reservas:
        for mesa in mesas:
            if mesas[mesa].capacidad == reserva.personas:
                if mesas[mesa].id in diccionario_reservas:
                    if not [reserva.minuto][0] - 120 < diccionario_reservas[mesas[mesa].id][0] < \
                           [reserva.minuto][0] + 120:
                        diccionario_reservas[mesas[mesa].id] += [reserva.minuto]
                        break
                else:
                    diccionario_reservas[mesas[mesa].id] = [reserva.minuto]
                    break
        else:
            for mesa in mesas:
                if mesas[mesa].capacidad == reserva.personas + 1:
                    if mesas[mesa].id in diccionario_reservas:
                        if not [reserva.minuto][0] - 120 < diccionario_reservas[mesas[mesa].id][0] < \
                               [reserva.minuto][0] + 120:
                            diccionario_reservas[mesas[mesa].id] += [reserva.minuto]
                            break
                    else:
                        diccionario_reservas[mesas[mesa].id] = [reserva.minuto]
                        break
            else:
                raise Exception("Reserva Inválida")
    return diccionario_reservas


# Mostrar la información del minuto, las colas y las mesas
def mostrar_info(mesas: dict, colas: list, minutos: int):
    print(f"\n\nMinuto: {minutos}")
    print("\nCola atendida: ")
    if colas[1]:
        for grupo in colas[1]:
            print(f"Id: {grupo[0]}\t\tNúmero de personas: {grupo[1]}")
    else:
        print("Vacía")

    print("\nCola sin atender: ")
    if colas[0]:
        for grupo in colas[0]:
            print(f"Id: {grupo[0]}\t\tNúmero de personas: {grupo[1]}")
    else:
        print("Vacía")

    print("\nMesas: ")
    for mesa in mesas:
        if mesas[mesa].tiempo_restante == 0:
            print(f"Id: {mesas[mesa].id}\t\tCapacidad: {mesas[mesa].capacidad}\t\tDisponibilidad: Disponible")
        else:
            print(f"Id: {mesas[mesa].id}\t\tCapacidad: {mesas[mesa].capacidad}\t\tDisponibilidad: Ocupada"
                  f"\t\t\tTiempo restante: {mesas[mesa].tiempo_restante}")


# Main
def main(mesas: dict, reservas: list, colas: list, minutos: int):

    while colas[0] or colas[1]:

        mesas_libres = mesas_disponibles(mesas, reservas, minutos)

        mostrar_info(mesas, colas, minutos)

        if colas[1]:
            for posicion, grupo in enumerate(colas[1]):
                for id, mesa in enumerate(mesas_libres):
                    if mesa.capacidad == grupo[1]:
                        mesa.tiempo_restante = 120
                        colas[1].pop(posicion)
                        mesas_libres.pop(id)
                        break
                else:
                    for id, mesa in enumerate(mesas_libres):
                        if mesa.capacidad == grupo[1] + 1:
                            mesa.tiempo_restante = 120
                            colas[1].pop(posicion)
                            mesas_libres.pop(id)
                            break

        if colas[0]:
            for posicion, grupo in enumerate(colas[0]):
                for id, mesa in enumerate(mesas_libres):
                    if mesa.capacidad == grupo[1]:
                        mesa.tiempo_restante = 120
                        colas[0].pop(posicion)
                        mesas_libres.pop(id)
                        break
                else:
                    for id, mesa in enumerate(mesas_libres):
                        if mesa.capacidad == grupo[1] + 1:
                            mesa.tiempo_restante = 120
                            colas[0].pop(posicion)
                            mesas_libres.pop(id)
                            break

        minutos += 10
        for mesa in mesas:
            if mesas[mesa].tiempo_restante != 0:
                mesas[mesa].tiempo_restante -= 10

        input()


# Datos de ejemplo
mesa1 = Mesa(1, 2, 120)
mesa2 = Mesa(2, 3, 90)
mesa3 = Mesa(3, 4, 0)
mesa4 = Mesa(4, 5, 40)
mesa5 = Mesa(5, 6, 80)
mesa6 = Mesa(6, 7, 20)
mesa7 = Mesa(7, 3, 0)
mesa8 = Mesa(8, 5, 30)
mesa9 = Mesa(9, 7, 60)
mesa10 = Mesa(10, 1, 0)
mesas_prueba = {1: mesa1, 2: mesa2, 3: mesa3, 4: mesa4, 5: mesa5, 6: mesa6, 7: mesa7, 8: mesa8, 9: mesa9, 10: mesa10}

reserva1 = Reserva(4, 150)
reserva2 = Reserva(4, 160)
reserva3 = Reserva(3, 130)
reservas_prueba = [reserva1, reserva2, reserva3]

sin_atender = [("1", 4), ("2", 6), ("3", 5), ("4", 2), ("5", 3)]
atendidos = []
colas_prueba = [sin_atender, atendidos]

minutos_prueba = 0

main(mesas_prueba, reservas_prueba, colas_prueba, minutos_prueba)

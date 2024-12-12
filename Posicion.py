import random

from Jugador import *


class Posicion():

    def __init__(self):

        self.posiciones = ["Delantero Centro", "Extremo Izquierdo", "Extremo Derecho", "Mediocentro Ofensivo",
                           "Mediocentro", "Mediocentro Defensivo", "Lateral Izquierdo", "Lateral Derecho",
                           "Defensa Central"]

    def listar_posiciones(self):
        for i, posicion in enumerate(self.posiciones, start=1):
            print(f"{i}. {posicion.title()}")

    def simular_partidos_jugados(self, jugador):
        """Método que se encarga de la simulación de los partidos jugados para los futbolistas virtuales"""
        max_partidos = 70

        if jugador.edad == 15:
            jugador.partidos_jugados = random.randint(1, 15)
            print(f"Partidos jugados: {jugador.partidos_jugados}")

        elif 16<= jugador.edad <=17:
            partidos_anteriores = jugador.partidos_jugados
            ajuste_partidos = random.randint(5, 12)
            jugador.partidos_jugados = max(0, partidos_anteriores + ajuste_partidos)
            print(f"Partidos jugados: {jugador.partidos_jugados}")

        elif jugador.edad == 18:
            partidos_anteriores = jugador.partidos_jugados
            ajuste_partidos = random.randint(5, 10)
            jugador.partidos_jugados = max(0, partidos_anteriores + ajuste_partidos)
            print(f"Partidos jugados: {jugador.partidos_jugados}")

        elif 19<= jugador.edad <=29:
            partidos_anteriores = jugador.partidos_jugados
            ajuste_partidos = random.randint(-3, 5)
            jugador.partidos_jugados = min(max_partidos, max(0, partidos_anteriores + ajuste_partidos))
            print(f"Partidos jugados: {jugador.partidos_jugados}")

        elif 30<= jugador.edad <=35:
            partidos_anteriores = jugador.partidos_jugados
            ajuste_partidos = random.randint(-4, 2)
            jugador.partidos_jugados = min(max_partidos, max(0, partidos_anteriores + ajuste_partidos))
            print(f"Partidos jugados: {jugador.partidos_jugados}")

        elif 36<= jugador.edad <=39:
            partidos_anteriores = jugador.partidos_jugados
            ajuste_partidos = random.randint(-7, 2)
            jugador.partidos_jugados = min(max_partidos, max(0, partidos_anteriores + ajuste_partidos))
            print(f"Partidos jugados: {jugador.partidos_jugados}")

        elif jugador.edad >=40:
            partidos_anteriores = jugador.partidos_jugados
            ajuste_partidos = random.randint(-5, 0)
            jugador.partidos_jugados = max(0, partidos_anteriores + ajuste_partidos)
            print(f"Partidos jugados: {jugador.partidos_jugados}")

        elif jugador.edad == 45:
            pass

    def simular_goles(self, jugador):

        ratios_goles = {
            "Delantero Centro": (0.20, 2.25),
            "Extremo Izquierdo": (0.15, 1.80),
            "Extremo Derecho": (0.15, 1.80),
            "Mediocentro Ofensivo": (0.15, 1.50),
            "Mediocentro": (0.05, 1.20),
            "Mediocentro Defensivo": (0.00, 0.50),
            "Defensa Central": (0.00, 0.40),
            "Lateral Izquierdo": (0.00, 0.45),
            "Lateral Derecho": (0.00, 0.45),
        }

        min_ratio, max_ratio = ratios_goles.get(jugador.posicion, (0.00, 0.00))

        # Genera un ratio inicial
        if not hasattr(jugador, 'ratio_goles'):

            probabilidad = random.random()  # Genera un número entre 0 y 1 para calcular probabilidades

            if probabilidad <= 0.2:  # 20% de probabilidad para obtener un ratio inicial alto.
                min_ratio_avanzado = (max_ratio - min_ratio) / 2
                jugador.ratio_goles = round(random.uniform(min_ratio_avanzado, max_ratio), 2)

            else:  # 80% de probabilidad para obtener un ratio inicial más bajo.
                jugador.ratio_goles = round(random.uniform(min_ratio, (max_ratio - min_ratio) / 3), 2)


        # Calcular goles en función del ratio y los partidos jugados
        jugador.goles = round(jugador.partidos_jugados * jugador.ratio_goles)
        print(f"Goles: {jugador.goles}")

        # Ajustar ratio para próximas temporadas
        ajuste_ratio = random.uniform(-0.05, 0.10)  # Ajuste entre -0.05 y 0.10
        jugador.ratio_goles = max(min_ratio, min(max_ratio, jugador.ratio_goles + ajuste_ratio))

    def simular_asistencias(self, jugador):

        ratios_asistencias = {
            "Delantero Centro": (0.05, 1.00),
            "Extremo Izquierdo": (0.15, 2.00),
            "Extremo Derecho": (0.15, 2.00),
            "Mediocentro Ofensivo": (0.15, 2.10),
            "Mediocentro": (0.15, 2.10),
            "Mediocentro Defensivo": (0.05, 0.80),
            "Defensa Central": (0.05, 0.50),
            "Lateral Izquierdo": (0.05, 0.85),
            "Lateral Derecho": (0.05, 0.85),
        }

        min_ratio, max_ratio = ratios_asistencias.get(jugador.posicion, (0.00, 0.00))

        # Genera un ratio inicial
        if not hasattr(jugador, 'ratio_asistencias'):

            probabilidad = random.random()  # Genera un número entre 0 y 1 para calcular probabilidades

            if probabilidad <= 0.2:  # 20% de probabilidad para obtener un ratio inicial alto.
                min_ratio_avanzado = (max_ratio - min_ratio) / 2
                jugador.ratio_asistencias = round(random.uniform(min_ratio_avanzado, max_ratio), 2)

            else:  # 80% de probabilidad para obtener un ratio inicial más bajo.
                jugador.ratio_asistencias = round(random.uniform(min_ratio, (max_ratio - min_ratio) / 3), 2)


        # Calcular asistencias en función del ratio y los partidos jugados
        jugador.asistencias = round(jugador.partidos_jugados * jugador.ratio_asistencias)
        print(f"Asistencias: {jugador.asistencias}")

        # Ajustar ratio para próximas temporadas
        ajuste_ratio = random.uniform(-0.05, 0.10)  # Ajuste entre -0.05 y 0.10
        jugador.ratio_asistencias = max(min_ratio, min(max_ratio, jugador.ratio_asistencias + ajuste_ratio))


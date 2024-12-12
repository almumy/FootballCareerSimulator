import random
from Jugador import *


class Equipo():

    def __init__(self, nombre_equipo, nacionalidad_equipo, elo_equipo):

        self.nombre_equipo = nombre_equipo
        self.nacionalidad_equipo = nacionalidad_equipo
        self.elo_equipo = elo_equipo

    def __str__(self):
        return f"{self.nombre_equipo}, País: {self.nacionalidad_equipo.capitalize()}"

    def generar_oferta_primer_club(self, equipos, jugador):
        equipos_filtrados = []
        for equipo in equipos:
            if equipo.nacionalidad_equipo.lower() == jugador.nacionalidad.lower():
                equipos_filtrados.append(equipo)

        primera_oferta = random.sample(equipos_filtrados, 4)
        print(f"¡Comienza tu carrera como profesional con {jugador.edad} años en {jugador.nacionalidad.capitalize()}!")
        print(f"{jugador.nombre.capitalize()}, elige el equipo del que has sido canterano y en el que vas a debutar.")

        for i, oferta in enumerate(primera_oferta, start=1):
            # Categorías de ofertas económicas basadas en el ELO de los equipos existentes
            if oferta.elo_equipo >= 1700:
                probabilidad = random.random()
                if probabilidad <= 0.1:
                    valor_oferta = round(random.randint(50_000_000, 70_000_000) / 100) * 100
                    sueldo_oferta = round(random.randint(1_000_000, 8_000_000) / 100) * 100
                else:
                    valor_oferta = round(random.randint(20_000_000, 50_000_000) / 100) * 100
                    sueldo_oferta = round(random.randint(700_000, 1_000_000) / 100) * 100
            elif oferta.elo_equipo >= 1400:
                valor_oferta = round(random.randint(10_000_000, 20_000_000) / 100) * 100
                sueldo_oferta = round(random.randint(500_000, 700_000) / 100) * 100
            elif oferta.elo_equipo >= 1100:
                valor_oferta = round(random.randint(5_000_000, 10_000_000) / 100) * 100
                sueldo_oferta = round(random.randint(300_000, 500_000) / 100) * 100
            elif oferta.elo_equipo >= 800:
                valor_oferta = round(random.randint(1_000_000, 5_000_000) / 100) * 100
                sueldo_oferta = round(random.randint(200_000, 300_000) / 100) * 100
            elif oferta.elo_equipo >= 500:
                valor_oferta = round(random.randint(500_000, 1_000_000) / 100) * 100
                sueldo_oferta = round(random.randint(150_000, 250_000) / 100) * 100
            elif oferta.elo_equipo >= 200:
                valor_oferta = round(random.randint(100_000, 500_000) / 100) * 100
                sueldo_oferta = round(random.randint(50_000, 150_000) / 100) * 100
            else:
                valor_oferta = round(random.randint(10_000, 100_000) / 100) * 100
                sueldo_oferta = round(random.randint(21_000, 50_000) / 100) * 100

            valor_oferta_formateado = f"{valor_oferta:,}".replace(",", ".")
            sueldo_oferta_formateado = f"{sueldo_oferta:,}".replace(",", ".")
            print(f"{i}. {oferta} ---> {valor_oferta_formateado}€ de transferencia | {sueldo_oferta_formateado}€ de salario anual.")

        while True:
            try:
                seleccion = int(input("Introduce el número del equipo en el que vas a debutar (1-4): "))
                if seleccion < 1 or seleccion > 4:
                    raise ValueError("Por favor, ingresa un valor entre 1 y 4.")
                jugador.equipo = primera_oferta[seleccion - 1]  # Indentamos -1 para evitar el 0.
                jugador.valor_mercado = valor_oferta
                jugador.sueldo = sueldo_oferta
                print(f"¡Felicidades! vas a debutar en el primer equipo del {jugador.equipo}.")
                break
            except ValueError as e:
                print(f"Error: {e}")

    def generar_oferta(self, equipos, jugador):
        equipos_filtrados = []
        margen_elo = 100

        # Filtrar equipos según el margen de ELO
        for equipo in equipos:
            if abs(equipo.elo_equipo - jugador.elo) <= margen_elo and equipo != jugador.equipo:
                equipos_filtrados.append(equipo)

        # Si hay equipos filtrados, generamos las ofertas
        if equipos_filtrados:
            # Aseguramos que no haya duplicados en las ofertas
            equipos_filtrados = list(set(equipos_filtrados))

            # Seleccionamos un máximo de 3 ofertas
            ofertas = random.sample(equipos_filtrados, min(3, len(equipos_filtrados)))

            print("Han llegado algunas ofertas de clubes que están interesados en ti:")
            for i, oferta in enumerate(ofertas, start=1):
                # Categorías de ofertas económicas basadas en el ELO de los equipos existentes
                if oferta.nombre_equipo == "Real Madrid CF":
                    # Ofertas del Real Madrid: más bajas pero con mayor prestigio
                    valor_oferta = round(random.randint(80_000_000, 150_000_000) / 100) * 100  # Ofertas entre 80M y 150M
                    sueldo_oferta = round(random.randint(8_000_000, 40_000_000) / 100) * 100  # Sueldo anual entre 8M y 30M
                else:
                    # Condiciones generales basadas en el ELO del equipo
                    if oferta.elo_equipo >= 1700:
                        probabilidad = random.random()
                        if probabilidad <= 0.1:
                            valor_oferta = round(random.randint(120_000_000, 300_000_000) / 100) * 100
                            sueldo_oferta = round(random.randint(120_000_000, 260_000_000) / 100) * 100
                        else:
                            valor_oferta = round(random.randint(75_000_000, 120_000_000) / 100) * 100
                            sueldo_oferta = round(random.randint(10_000_000, 120_000_000) / 100) * 100
                    elif oferta.elo_equipo >= 1400:
                        valor_oferta = round(random.randint(50_000_000, 75_000_000) / 100) * 100
                        sueldo_oferta = round(random.randint(3_000_000, 10_000_000) / 100) * 100
                    elif oferta.elo_equipo >= 1100:
                        valor_oferta = round(random.randint(25_000_000, 50_000_000) / 100) * 100
                        sueldo_oferta = round(random.randint(1_000_000, 5_000_000) / 100) * 100
                    elif oferta.elo_equipo >= 800:
                        valor_oferta = round(random.randint(5_000_000, 25_000_000) / 100) * 100
                        sueldo_oferta = round(random.randint(500_000, 2_000_000) / 100) * 100
                    elif oferta.elo_equipo >= 500:
                        valor_oferta = round(random.randint(1_000_000, 5_000_000) / 100) * 100
                        sueldo_oferta = round(random.randint(200_000, 1_000_000) / 100) * 100
                    elif oferta.elo_equipo >= 200:
                        valor_oferta = round(random.randint(100_000, 1_000_000) / 100) * 100
                        sueldo_oferta = round(random.randint(50_000, 200_000) / 100) * 100
                    else:
                        valor_oferta = round(random.randint(10_000, 100_000) / 100) * 100
                        sueldo_oferta = round(random.randint(21_000, 200_000) / 100) * 100

                valor_oferta_formateado = f"{valor_oferta:,}".replace(",", ".")
                sueldo_oferta_formateado = f"{sueldo_oferta:,}".replace(",", ".")

                print(f"{i}. {oferta} ---> {valor_oferta_formateado}€ de transferencia | {sueldo_oferta_formateado}€ de salario anual.")
            print(f"{len(ofertas) + 1}. Quedarte en tu equipo actual: {jugador.equipo}")

            while True:
                try:
                    seleccion = int(input("Introduce el número de la oferta que deseas aceptar: "))
                    if seleccion < 1 or seleccion > len(ofertas) + 1:
                        raise ValueError("Por favor, ingresa un valor válido.")

                    if seleccion == len(ofertas) + 1:
                        print(f"Has decidido quedarte en tu club actual: {jugador.equipo}.")
                    else:
                        nuevo_equipo = ofertas[seleccion - 1]  # Restamos 1 porque las listas comienzan en 0
                        jugador.equipo = nuevo_equipo
                        jugador.valor_mercado = valor_oferta
                        jugador.sueldo = sueldo_oferta
                        print(f"¡Felicidades! Has aceptado un nuevo contrato con el {jugador.equipo}.")
                        print(
                            f"La transferencia se ha cerrado por {valor_oferta}€ y vas a ganar {sueldo_oferta}€ al año.")
                    break
                except ValueError as e:
                    print(f"Error: {e}. Inténtalo de nuevo.")
        else:
            print("No hay nuevas ofertas disponibles, te quedarás en tu equipo actual por defecto.")


equipos = [
    # ALEMANIA PRIMERA DIVISIÓN ELO > 225
    Equipo("FC Bayern Múnich", "alemania", 1800),
    Equipo("Bayer 04 Leverkusen", "alemania", 1350),
    Equipo("RB Leipzig", "alemania", 850),
    Equipo("Borussia Dortmund", "alemania", 1450),
    Equipo("VfB Stuttgart", "alemania", 600),
    Equipo("Eintracht Fráncfort", "alemania", 750),
    Equipo("VfL Wolfsburgo", "alemania", 625),
    Equipo("SC Friburgo", "alemania", 370),
    Equipo("TSG 1899 Hoffenheim", "alemania", 380),
    Equipo("1.FC Unión Berlín", "alemania", 370),
    Equipo("SV Werder Bremen", "alemania", 320),
    Equipo("FC Augsburgo", "alemania", 300),
    Equipo("1.FSV Mainz 05", "alemania", 290),
    Equipo("1.FC Heidenheim 1846", "alemania", 265),
    Equipo("VfL Bochum", "alemania", 260),
    Equipo("FC St. Pauli", "alemania", 240),
    Equipo("Holstein Kiel", "alemania", 225),
    # FRANCIA PRIMERA DIVISIÓN ELO > 220
    Equipo("París Saint-Germain FC", "francia", 1750),
    Equipo("AS Mónaco", "francia", 1250),
    Equipo("LOSC Lille", "francia", 750),
    Equipo("Olympique de Marsella", "francia", 800),
    Equipo("Olympique de Lyon", "francia", 600),
    Equipo("OGC Niza", "francia", 550),
    Equipo("Racing Club de Estrasburgo", "francia", 350),
    Equipo("Stade Rennais FC", "francia", 450),
    Equipo("RC Lens", "francia", 280),
    Equipo("Stade de Reims", "francia", 380),
    Equipo("Stade Brestois 29", "francia", 260),
    Equipo("FC Nantes", "francia", 300),
    Equipo("Toulouse FC", "francia", 250),
    Equipo("Montpellier HSC", "francia", 245),
    Equipo("Le Havre AC", "francia", 250),
    Equipo("AJ Auxerre", "francia", 240),
    Equipo("AS Saint-Étienne", "francia", 225),
    Equipo("Angers SCO", "francia", 220),
    # ESPAÑA PRIMERA DIVISIÓN ELO > 300
    Equipo("Real Madrid CF", "españa", 2000),
    Equipo("FC Barcelona", "españa", 1750),
    Equipo("Atlético de Madrid", "españa", 1450),
    Equipo("Sevilla FC", "españa", 750),
    Equipo("Real Betis Balompié", "españa", 700),
    Equipo("Real Sociedad", "españa", 800),
    Equipo("Athletic Club", "españa", 820),
    Equipo("Girona FC", "españa", 550),
    Equipo("Valencia CF", "españa", 600),
    Equipo("Villarreal CF", "españa", 700),
    Equipo("UD Las Palmas", "españa", 500),
    Equipo("RCD Mallorca", "españa", 450),
    Equipo("Deportivo Alavés", "españa", 425),
    Equipo("RC Celta de Vigo", "españa", 450),
    Equipo("CD Leganés", "españa", 370),
    Equipo("Real Valladolid CF", "españa", 345),
    Equipo("Getafe CF", "españa", 365),
    Equipo("RCD Espanyol", "españa", 325),
    # ESPAÑA SEGUNDA DIVISIÓN ELO < 300
    Equipo("UD Almería", "españa", 260),
    Equipo("Granada CF", "españa", 270),
    Equipo("Real Zaragoza", "españa", 200),
    Equipo("Real Oviedo", "españa", 180),
    Equipo("Elche CF", "españa", 180),
    Equipo("Cádiz CF", "españa", 210),
    Equipo("Real Racing Club", "españa", 200),
    Equipo("Real Sporting de Gijón", "españa", 170),
    Equipo("Levante UD", "españa", 170),
    Equipo("Burgos CF", "españa", 160),
    Equipo("SD Eibar", "españa", 180),
    Equipo("RC Deportivo de La Coruña", "españa", 180),
    Equipo("CD Tenerife", "españa", 170),
    Equipo("SD Huesca", "españa", 145),
    Equipo("Albacete Balompié", "españa", 140),
    Equipo("Málaga CF", "españa", 165),
    Equipo("CD Castellón", "españa", 140),
    Equipo("Racing Club de Ferrol", "españa", 130),
    Equipo("CD Eldense", "españa", 130),
    Equipo("FC Cartagena", "españa", 130),
    Equipo("CD Mirandés", "españa", 120),
    Equipo("Córdoba CF", "españa", 135),
]

from Jugador import *
from Equipo import *
from Posicion import *


def limpiar_consola():
    print("\n" * 100)

def main():
    jugador = Jugador()
    jugador.crear_jugador()
    limpiar_consola()
    equipos[0].generar_oferta_primer_club(equipos, jugador)
    jugador.asignar_elo_base()
    while jugador.edad < 40:
        limpiar_consola()
        print(f"-----Simulando tu temporada {jugador.temporada}. Edad {jugador.edad}. Equipo actual: {jugador.equipo}.-----")
        jugador.gestor_posiciones.simular_partidos_jugados(jugador)
        jugador.gestor_posiciones.simular_goles(jugador)
        jugador.gestor_posiciones.simular_asistencias(jugador)
        jugador.temporada += 1
        jugador.edad += 1
        jugador.aumentar_elo_por_rendimiento()
        print(f"-----Fin de la temporada-----")
        equipos[0].generar_oferta(equipos, jugador)


if __name__ == "__main__":
    main()

"""Funciones auxiliares para la red de ciudades de la Unidad 3."""


def crear_red_ciudades():
    """Crea una red no dirigida y ponderada de seis ciudades."""
    return {
        "Quito": [("Latacunga", 90), ("Riobamba", 250)],
        "Latacunga": [("Quito", 90), ("Ambato", 45)],
        "Ambato": [
            ("Latacunga", 45),
            ("Riobamba", 55),
            ("Guaranda", 100),
        ],
        "Riobamba": [("Quito", 250), ("Ambato", 55), ("Cuenca", 140)],
        "Guaranda": [("Ambato", 100), ("Cuenca", 170)],
        "Cuenca": [("Riobamba", 140), ("Guaranda", 170)],
    }


def calcular_grados(grafo):
    """Devuelve la cantidad de conexiones directas de cada ciudad."""
    # R1 - Calcular el grado de todos los vertices: O(V).
    return {ciudad: len(vecinos) for ciudad, vecinos in grafo.items()}


if __name__ == "__main__":
    # Prueba independiente del requerimiento R1.
    red_ciudades = crear_red_ciudades()
    grados = calcular_grados(red_ciudades)

    print("RED DE CIUDADES")
    for ciudad, conexiones in red_ciudades.items():
        print(f"\n{ciudad}:")
        for ciudad_vecina, distancia in conexiones:
            print(f"  -> {ciudad_vecina}: {distancia} km")

    print("\nGRADO DE CADA CIUDAD")
    for ciudad, grado in grados.items():
        print(f"{ciudad}: grado {grado}")

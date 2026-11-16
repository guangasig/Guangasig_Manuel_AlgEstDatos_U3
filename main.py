from utilidades import (
    bfs,
    calcular_grados,
    ciudades_extremas,
    comparar_rutas,
    crear_red_ciudades,
    dijkstra,
    red_esta_conectada,
)


def mostrar_menu():
    """Muestra las opciones disponibles en el sistema."""
    print("\nRED DE CIUDADES CARUPS")
    print("1. Mostrar red de ciudades")
    print("2. Mostrar grado de cada ciudad")
    print("3. Ejecutar BFS desde una ciudad")
    print("4. Ejecutar Dijkstra desde una ciudad")
    print("5. Comparar rutas Quito - Riobamba")
    print("0. Salir")


def obtener_ciudad(grafo, mensaje):
    """Solicita una ciudad existente sin distinguir mayusculas."""
    nombres = {ciudad.lower(): ciudad for ciudad in grafo}
    ciudad_ingresada = input(mensaje).strip().lower()
    return nombres.get(ciudad_ingresada)


def mostrar_red(grafo):
    """Muestra todas las ciudades, conexiones y distancias."""
    print("\nRED DE CIUDADES")
    for ciudad, conexiones in grafo.items():
        print(f"\n{ciudad}:")
        for ciudad_vecina, distancia in conexiones:
            print(f"  -> {ciudad_vecina}: {distancia} km")


def mostrar_grados(grafo):
    """Muestra la cantidad de conexiones directas de cada ciudad."""
    grados = calcular_grados(grafo)

    print("\nGRADO DE CADA CIUDAD")
    for ciudad, grado in grados.items():
        print(f"{ciudad}: grado {grado}")


def ejecutar_bfs(grafo):
    """Ejecuta BFS desde una ciudad seleccionada por el usuario."""
    origen = obtener_ciudad(grafo, "Ciudad de origen: ")

    if origen is None:
        print("La ciudad no existe en la red.")
        return

    escalas, _ = bfs(grafo, origen)

    print(f"\nESCALAS DESDE {origen.upper()}")
    for ciudad, cantidad_escalas in escalas.items():
        print(f"{ciudad}: {cantidad_escalas}")

    if red_esta_conectada(grafo, escalas):
        print("La red esta completamente conectada.")
    else:
        ciudades_aisladas = set(grafo) - set(escalas)
        print("Ciudades no alcanzables:", ", ".join(sorted(ciudades_aisladas)))


def ejecutar_dijkstra(grafo):
    """Ejecuta e interpreta Dijkstra desde una ciudad seleccionada."""
    origen = obtener_ciudad(grafo, "Ciudad de origen: ")

    if origen is None:
        print("La ciudad no existe en la red.")
        return

    distancias = dijkstra(grafo, origen)
    ciudad_cercana, ciudad_lejana = ciudades_extremas(distancias, origen)

    print(f"\nDISTANCIAS MINIMAS DESDE {origen.upper()}")
    for ciudad, distancia in distancias.items():
        if distancia == float("inf"):
            print(f"{ciudad}: no alcanzable")
        else:
            print(f"{ciudad}: {distancia} km")

    if ciudad_cercana is None:
        print("No existen otras ciudades alcanzables.")
        return

    print(
        f"Ciudad mas cercana: {ciudad_cercana} "
        f"({distancias[ciudad_cercana]} km)"
    )
    print(
        f"Ciudad mas lejana: {ciudad_lejana} "
        f"({distancias[ciudad_lejana]} km)"
    )


def ejecutar_comparacion(grafo):
    """Compara las rutas entre Quito y Riobamba para el R4."""
    origen = "Quito"
    destino = "Riobamba"
    comparacion = comparar_rutas(grafo, origen, destino)

    print("\nCOMPARACION QUITO - RIOBAMBA")
    print("Ruta con menos escalas:")
    print(" -> ".join(comparacion["ruta_bfs"]))
    print("Cantidad de escalas:", comparacion["escalas_bfs"])

    print("\nRuta de menor distancia:")
    print(" -> ".join(comparacion["ruta_dijkstra"]))
    print("Distancia minima:", comparacion["distancia_dijkstra"], "km")

    print(
        "\nLas rutas no coinciden porque BFS minimiza la cantidad de "
        "tramos, mientras Dijkstra minimiza la suma de kilometros."
    )


def main():
    """Inicia el menu principal con la red de ejemplo cargada."""
    grafo = crear_red_ciudades()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            mostrar_red(grafo)
        elif opcion == "2":
            mostrar_grados(grafo)
        elif opcion == "3":
            ejecutar_bfs(grafo)
        elif opcion == "4":
            ejecutar_dijkstra(grafo)
        elif opcion == "5":
            ejecutar_comparacion(grafo)
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    main()

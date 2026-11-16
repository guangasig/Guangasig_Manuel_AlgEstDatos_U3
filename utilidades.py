"""Funciones auxiliares para la red de ciudades de la Unidad 3."""

import heapq
from collections import deque


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


def bfs(grafo, origen):
    """Calcula escalas y padres desde una ciudad de origen."""
    # R2 - BFS visita cada vertice y cada arista: O(V + E).
    distancias = {origen: 0}
    padres = {origen: None}
    cola = deque([origen])

    while cola:
        ciudad = cola.popleft()

        for ciudad_vecina, _ in grafo[ciudad]:
            if ciudad_vecina not in distancias:
                distancias[ciudad_vecina] = distancias[ciudad] + 1
                padres[ciudad_vecina] = ciudad
                cola.append(ciudad_vecina)

    return distancias, padres


def red_esta_conectada(grafo, distancias_bfs):
    """Indica si BFS pudo alcanzar todas las ciudades de la red."""
    # Comparar las cantidades de vertices: O(1).
    return len(distancias_bfs) == len(grafo)


def reconstruir_camino(padres, destino):
    """Reconstruye una ruta desde el origen hasta el destino."""
    # Reconstruir como maximo V vertices: O(V).
    if destino not in padres:
        return []

    camino = []
    ciudad = destino

    while ciudad is not None:
        camino.append(ciudad)
        ciudad = padres[ciudad]

    return camino[::-1]


# R3 - Dijkstra con cola de prioridad: O((V + E) log V).
def dijkstra(grafo, origen):
    """Devuelve {ciudad: distancia_minima_desde_origen}."""
    dist = {ciudad: float('inf') for ciudad in grafo}
    dist[origen] = 0
    heap = [(0, origen)]          # cola de prioridad
    while heap:
        d, u = heapq.heappop(heap)      # el mas cercano pendiente
        if d > dist[u]:
            continue                    # ya teniamos una ruta mejor
        for vecino, peso in grafo[u]:
            if dist[u] + peso < dist[vecino]:    # relajacion
                dist[vecino] = dist[u] + peso
                heapq.heappush(heap, (dist[vecino], vecino))
    return dist


def ciudades_extremas(distancias, origen):
    """Devuelve las ciudades alcanzables mas cercana y mas lejana."""
    # Revisar las distancias de todos los vertices: O(V).
    alcanzables = {
        ciudad: distancia
        for ciudad, distancia in distancias.items()
        if ciudad != origen and distancia != float("inf")
    }

    if not alcanzables:
        return None, None

    ciudad_cercana = min(alcanzables, key=alcanzables.get)
    ciudad_lejana = max(alcanzables, key=alcanzables.get)
    return ciudad_cercana, ciudad_lejana


def reconstruir_ruta_dijkstra(grafo, distancias, origen, destino):
    """Reconstruye una ruta minima usando las distancias de Dijkstra."""
    # Examinar vecinos durante la reconstruccion: O(V + E).
    if destino not in distancias or distancias[destino] == float("inf"):
        return []

    ruta_inversa = [destino]
    ciudad_actual = destino

    while ciudad_actual != origen:
        ciudad_anterior = None

        for ciudad_vecina, distancia in grafo[ciudad_actual]:
            if distancias[ciudad_vecina] + distancia == distancias[ciudad_actual]:
                ciudad_anterior = ciudad_vecina
                break

        if ciudad_anterior is None:
            return []

        ruta_inversa.append(ciudad_anterior)
        ciudad_actual = ciudad_anterior

    return ruta_inversa[::-1]


def comparar_rutas(grafo, origen, destino):
    """Compara la ruta de menos escalas con la de menor distancia."""
    # R4 - Dominada por Dijkstra: O((V + E) log V).
    escalas, padres = bfs(grafo, origen)
    distancias = dijkstra(grafo, origen)

    return {
        "ruta_bfs": reconstruir_camino(padres, destino),
        "escalas_bfs": escalas.get(destino),
        "ruta_dijkstra": reconstruir_ruta_dijkstra(
            grafo,
            distancias,
            origen,
            destino,
        ),
        "distancia_dijkstra": distancias.get(destino, float("inf")),
    }


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

    # Prueba independiente del requerimiento R2.
    escalas, padres = bfs(red_ciudades, "Quito")

    print("\nESCALAS DESDE QUITO")
    for ciudad, cantidad_escalas in escalas.items():
        print(f"{ciudad}: {cantidad_escalas}")

    if red_esta_conectada(red_ciudades, escalas):
        print("\nLa red esta completamente conectada.")
    else:
        print("\nLa red tiene ciudades aisladas.")

    # Prueba independiente de los requerimientos R3 y R4.
    distancias = dijkstra(red_ciudades, "Quito")
    ciudad_cercana, ciudad_lejana = ciudades_extremas(distancias, "Quito")

    print("\nDISTANCIAS MINIMAS DESDE QUITO")
    for ciudad, distancia in distancias.items():
        print(f"{ciudad}: {distancia} km")

    print(f"\nCiudad mas cercana: {ciudad_cercana}")
    print(f"Ciudad mas lejana: {ciudad_lejana}")

    comparacion = comparar_rutas(red_ciudades, "Quito", "Riobamba")

    print("\nCOMPARACION QUITO - RIOBAMBA")
    print("Ruta con menos escalas:", " -> ".join(comparacion["ruta_bfs"]))
    print("Cantidad de escalas:", comparacion["escalas_bfs"])
    print(
        "Ruta de menor distancia:",
        " -> ".join(comparacion["ruta_dijkstra"]),
    )
    print("Distancia minima:", comparacion["distancia_dijkstra"], "km")

# Red de ciudades CarUPS

El programa modela una red de ciudades conectadas mediante carreteras, realiza un recorrido BFS y calcula distancias mínimas con Dijkstra.

## Ejecución

Desde la carpeta `unidad_3`, ejecute:

```bash
python main.py
```

La red de seis ciudades está cargada automáticamente para facilitar las pruebas.

## Funcionalidades

### R1 Modelado del grafo

La red se representa mediante una lista de adyacencia: un diccionario donde cada ciudad contiene una lista de tuplas con la ciudad vecina y la distancia en kilómetros. El programa también calcula el grado de cada ciudad.

### R2 Recorrido BFS

BFS recorre la red por niveles mediante una cola. Desde una ciudad de origen muestra las escalas necesarias para alcanzar las demás ciudades y determina si toda la red está conectada.

### R3 Ruta más barata con Dijkstra

El programa integra el algoritmo de Dijkstra proporcionado en la actividad. Muestra la distancia mínima desde una ciudad de origen hasta las demás e identifica la ciudad alcanzable más cercana y la más lejana.

### R4 Comparación de rutas

La comparación se realiza entre Quito y Riobamba:

```text
Menos escalas: Quito -> Riobamba
Distancia de la carretera directa: 250 km

Menor distancia: Quito -> Latacunga -> Ambato -> Riobamba
Distancia acumulada: 90 + 45 + 55 = 190 km
```

Las rutas no coinciden porque BFS minimiza el número de tramos, sin considerar sus pesos. Dijkstra suma los kilómetros y elige la ruta con menor distancia total, aunque tenga más tramos.

## Complejidad temporal

| Requerimiento | Operación                               |      Complejidad |
| ------------- | --------------------------------------- | ---------------: |
| R1            | Calcular el grado de todas las ciudades |             O(V) |
| R2            | Recorrer la red con BFS                 |         O(V + E) |
| R3            | Calcular distancias con Dijkstra        | O((V + E) log V) |
| R4            | Comparar las rutas                      | O((V + E) log V) |

El factor logarítmico de Dijkstra aparece porque utiliza una cola de prioridad. Cada inserción o extracción del montículo cuesta O(log V).

## Estructura del proyecto

```text
unidad_3/
├── main.py
├── utilidades.py
├── README.md
└── .gitignore
```

- `main.py`: contiene el menú e integra los cuatro requerimientos.
- `utilidades.py`: contiene la red, BFS, Dijkstra y las funciones de análisis.
- `.gitignore`: excluye archivos temporales de Python y la carpeta local `docs/`.

# Datos del portafolio

Archivos de datos que usan las visualizaciones de los temas 6 y 9. Los `.js` son los que carga la página; los `.csv` contienen los mismos datos en formato abierto para revisarlos sin leer código.

## Tema 6 — Frenado regenerativo

| Archivo | Contenido | Origen |
|---|---|---|
| `ciclo_udds.csv` | Velocidad (mph) segundo a segundo del ciclo urbano UDDS, 0–1369 s | EPA, *Urban Dynamometer Driving Schedule*, 40 CFR Parte 86, Apéndice I (a). Copia digital tomada del repositorio de NREL FASTSim (`python/fastsim/resources/cycles/udds.csv`, rama `fastsim-2`). |
| `ciclo_hwfet.csv` | Velocidad (mph) segundo a segundo del ciclo de carretera HWFET, 0–765 s | EPA, *Highway Fuel Economy Test Driving Schedule*, 40 CFR Parte 600, Apéndice I. Misma copia de NREL FASTSim (`hwfet.csv`). |
| `epa_testcar_2025_seleccion.csv` | Peso de prueba equivalente, coeficientes de carga A, B, C y rendimiento medido (MPGe sin ajustar) de dos vehículos eléctricos | EPA, *Data on Cars used for Testing Fuel Economy*, archivo del año modelo 2025 (`25-testcar-2026-01-21.xlsx`). Filas de las pruebas RTSL10086702, RTSL10086700 (Tesla Model 3 Long Range RWD) y JNSX10050525, JNSX10050513 (Nissan LEAF). |
| `ciclos-epa.js` | Los mismos ciclos (en décimas de mph) y vehículos, listos para la página | Generado a partir de los archivos anteriores |

Comprobación de los ciclos: el UDDS reconstruido dura 1369 s, recorre 11,99 km (7,45 mi), tiene velocidad media de 19,59 mph y máxima de 56,7 mph; el HWFET dura 765 s, recorre 16,51 km (10,26 mi), con media de 48,3 mph y máxima de 59,9 mph. Son los valores de referencia de ambos ciclos.

## Tema 9 — Asistencia gravitatoria

| Archivo | Contenido | Origen |
|---|---|---|
| `voyager1_horizons.csv` | Rapidez respecto al Sol (km/s) y distancia al Sol (UA) de la Voyager 1, 1977–1990 | NASA/JPL Horizons, objetivo `-31`, efeméride de observador, cantidades 19 (r) y 22 (VmagSn). |
| `voyager2_horizons.csv` | Lo mismo para la Voyager 2 | NASA/JPL Horizons, objetivo `-32` (trayectoria `Voyager_2_ST+refit2022_m`). |
| `voyager-horizons.js` | Las dos series más la tabla de encuentros, listas para la página | Generado a partir de las mismas consultas |

Las consultas se hicieron el 30 de octubre de 2026 con la API de Horizons (`https://ssd.jpl.nasa.gov/api/horizons.api`), con `EPHEM_TYPE='OBSERVER'`, `CENTER='500@399'` y `QUANTITIES='19,22'`. `VmagSn` es, según la propia documentación de Horizons, la magnitud de la velocidad del objeto respecto al Sol, de modo que no depende del observador elegido. Se pidió un paso de 5 días entre 1977 y 1991 y un paso de 3 horas en los 6 días alrededor de cada encuentro planetario; para aligerar la página se conservaron todos los puntos a menos de 2 días de cada encuentro, uno cada 12 horas hasta 8 días, uno cada 5 días hasta 40 días y uno cada 15 días en el resto del vuelo.

La tabla de encuentros (marco del Sol frente a marco del planeta) usa consultas adicionales a Horizons con el centro en cada planeta (`CENTER='500@599'`, `'500@699'`, `'500@799'`, `'500@899'`), 40 días antes y 40 días después de cada máximo acercamiento. Las fechas y distancias de máximo acercamiento son las de NASA NSSDCA (*Voyager 1/2 Closest Approach Distances/Times*).

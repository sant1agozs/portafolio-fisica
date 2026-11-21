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

### Caso numérico de la Voyager 2 en Júpiter (entrega final)

Para separar la magnitud del cambio del vector velocidad, |Δv|, del cambio de rapidez, Δ|v|, se consultaron el 21 de noviembre de 2026 dos estados vectoriales en el máximo acercamiento (1979-07-09 22:30 TDB), con `EPHEM_TYPE='VECTORS'`, `VEC_TABLE=2`, `OUT_UNITS='KM-S'`, `REF_PLANE='ECLIPTIC'`:

| Consulta | Resultado (posición en km, velocidad en km/s) |
|---|---|
| `COMMAND='-32'`, `CENTER='500@599'` (Voyager 2 respecto a Júpiter) | r = (438 860,9; 565 977,1; −86 334,2), v = (−16,0016; 12,3745; −0,2410) |
| `COMMAND='599'`, `CENTER='500@10'` (Júpiter respecto al Sol) | v = (−8,9716; −9,0553; 0,2382) |

Con GM de Júpiter = 1,26687 × 10⁸ km³/s², la órbita hiperbólica da v∞ = 7,62 km/s, e = 1,330, δ = 97,5°, |Δv| = 11,45 km/s, rapidez heliocéntrica asintótica de entrada 9,59 km/s y de salida 19,50 km/s, es decir Δ|v| = 9,91 km/s. El cálculo está en `voyager2_jupiter_vectores.py`.

## Tema 12 — Medición del período en el video de Tacoma Narrows

| Archivo | Contenido | Origen |
|---|---|---|
| `tacoma_toma_0040_0046.csv` | 150 cuadros de la toma desde la calzada (0:39,9 a 0:45,9 del video). Por cuadro: tiempo en el video y brillo medio (0–255) de una cuadrícula de 4 × 4 zonas de la imagen | Muestreado cuadro a cuadro del video de British Pathé, *Tacoma Bridge Collapse: The Wobbliest Bridge in the World? (1940)*, https://www.youtube.com/watch?v=XggxeuFDaDU, reproducido a velocidad normal |
| `tacoma_periodo.py` | Calcula la inclinación como la primera componente principal de las 16 series de brillo, y de ahí los mínimos, los cruces por cero y el período en el video | Script propio |

Resultado: mínimos en 41,92 s y 44,96 s, cruces por cero de subida en 42,58 s y 45,56 s; período en el video de unos 3,0 s, frente a los 5 s que midió F. B. Farquharson con cronómetro el 7 de noviembre de 1940. La diferencia viene de la velocidad de la película (ver el Tema 12).

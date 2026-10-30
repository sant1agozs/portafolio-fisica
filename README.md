# Física en el Software — Portafolio de evidencias

Portafolio individual del curso **Física I (FUN-18)**, Universidad CENFOTEC, periodo 2026-C3.
Autor: Santiago Hernández Quirós · Docente: Andrés Castro Núñez.

**Sitio publicado:** https://sant1agozs.github.io/portafolio-fisica/

El portafolio documenta cómo la mecánica clásica aparece en el desarrollo de software real. Es acumulativo: cada avance conserva lo anterior y agrega temas nuevos.

## Avance 1 — Cinemática y Dinámica

| # | Tema | Recurso |
|---|------|---------|
| 1 | Rastreo y navegación de un dron de reparto | Visualización de datos |
| 2 | El salto del personaje: cómo los motores de juego falsean la gravedad | Simulación interactiva |
| 3 | Gravedad artificial por rotación en hábitats espaciales | Diagrama |
| 4 | Llantas de Fórmula 1: la ventana de temperatura y el agarre | Visualización de datos |
| 5 | El resorte virtual detrás de un control háptico | Multimedia con análisis |

## Avance 2 — Leyes de conservación y Gravitación

| # | Tema | Recurso |
|---|------|---------|
| 6 | Frenado regenerativo en un vehículo eléctrico | Visualización de datos (ciclos de manejo y vehículos de prueba de la EPA) |
| 7 | El coeficiente de restitución en un motor de videojuego: por qué la pelota rebota mal | Simulación interactiva |
| 8 | Ruedas de reacción: cómo un satélite se gira sin empujarse contra nada | Diagrama |
| 9 | Asistencia gravitatoria: cómo la Voyager ganó velocidad sin gastar combustible | Visualización de datos (NASA/JPL Horizons) |

## Estructura

- `index.html`: sitio de una sola página. Las gráficas usan Chart.js y las ecuaciones KaTeX. Las simulaciones de los temas 2 y 7 recalculan la física cada vez que se mueve un control, y los diagramas de los temas 3 y 8 son SVG elaborados para este portafolio.
- `data/`: datos de terceros que usan los temas 6 y 9 (EPA y NASA/JPL), en `.csv` para revisarlos y en `.js` para que los cargue la página. La procedencia de cada archivo y las consultas exactas están en [`data/README.md`](data/README.md).
- Las gráficas de los temas del Avance 1 se calculan en la propia página a partir de las ecuaciones y fuentes citadas en cada tema.

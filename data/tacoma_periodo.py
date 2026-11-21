"""Tema 12: período de oscilación del puente de Tacoma Narrows medido en el video.

Entrada: tacoma_toma_0040_0046.csv, la toma desde la calzada entre 0:40 y 0:46 del video
de British Pathé (https://www.youtube.com/watch?v=XggxeuFDaDU). Cada fila es un cuadro del
video: su tiempo y el brillo medio (0-255) de una cuadrícula de 4 x 4 zonas de la imagen.
Cuando el tablero se inclina, el horizonte y las barandas se mueven y el brillo de las zonas
cambia; la primera componente principal de esas 16 series resume esa inclinación.

Salida: tiempos de los mínimos y de los cruces por cero de subida, y el período en el video.
"""
import csv
import numpy as np

with open('tacoma_toma_0040_0046.csv') as f:
    filas = list(csv.reader(f))[1:]
t = np.array([float(r[0]) for r in filas])
X = np.array([[float(v) for v in r[1:]] for r in filas])

X = X - X.mean(axis=0)
_, _, vt = np.linalg.svd(X, full_matrices=False)
senal = X @ vt[0]                                   # primera componente principal
senal = np.convolve(senal, np.ones(5) / 5, 'same')  # suavizado de 5 cuadros
if senal[np.argmax(np.abs(senal))] > 0:             # el signo de la componente es arbitrario
    senal = -senal

ti = np.arange(t[2], t[-3], 0.01)
y = np.interp(ti, t, senal)
# mínimo local: el valor más bajo en una ventana de ±0,5 s y claramente negativo
w = 50
minimos = [ti[i] for i in range(w, len(y) - w) if y[i] == y[i - w:i + w + 1].min() and y[i] < 0.6 * y.min()]
cruces = [ti[i] for i in range(1, len(y)) if y[i - 1] < 0 <= y[i]]

print('Mínimos de inclinación (s del video):', [float(round(m, 2)) for m in minimos])
print('Cruces por cero de subida (s del video):', [float(round(c, 2)) for c in cruces])
for nombre, serie in (('mínimos', minimos), ('cruces', cruces)):
    if len(serie) > 1:
        print(f'Período en el video entre {nombre}: {np.mean(np.diff(serie)):.2f} s')
print('Período real medido por Farquharson con cronómetro: 5 s (12 ciclos por minuto)')

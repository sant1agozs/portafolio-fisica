"""Genera las dos muestras del Tema 11: misma nota (La3, 220 Hz), distinto timbre.

Síntesis aditiva: y(t) = env(t) * sum_n A_n sin(2 pi n f0 t).
  - muestra_impares.wav: solo armónicos impares, A_n = 1/n (forma cercana a una onda cuadrada,
    timbre "hueco", parecido al clarinete).
  - muestra_todos.wav: todos los armónicos, A_n = 1/n (forma cercana a un diente de sierra,
    timbre "brillante", parecido a una cuerda frotada o un metal).
Las dos usan la misma envolvente y se normalizan al mismo valor RMS, para que la única
diferencia sea el contenido armónico (no el volumen ni la duración).
"""
import json, wave
import numpy as np

FS = 44100          # muestras por segundo
F0 = 220.0          # frecuencia fundamental (La3)
DUR = 2.0           # segundos
NMAX = 15           # armónicos hasta 15 x 220 = 3300 Hz
RMS = 0.18          # mismo nivel eficaz para las dos muestras

t = np.arange(int(FS * DUR)) / FS
# envolvente: ataque 30 ms, sostenido, caída de 300 ms al final
env = np.ones_like(t)
a = int(0.03 * FS); r = int(0.30 * FS)
env[:a] = np.linspace(0, 1, a)
env[-r:] = np.linspace(1, 0, r)

def amplitudes(solo_impares):
    return {n: (1.0 / n) for n in range(1, NMAX + 1) if (n % 2 == 1 or not solo_impares)}

def sintetiza(amps):
    y = sum(A * np.sin(2 * np.pi * n * F0 * t) for n, A in amps.items())
    sostenido = y[int(0.1 * FS):int(1.6 * FS)]
    y = y * (RMS / np.sqrt(np.mean(sostenido ** 2)))
    return y * env

def guarda(nombre, y):
    pcm = np.clip(y, -1, 1)
    pcm = (pcm * 32767).astype('<i2')
    with wave.open(nombre, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(FS); w.writeframes(pcm.tobytes())

info = {}
for nombre, impares in [('muestra_impares.wav', True), ('muestra_todos.wav', False)]:
    amps = amplitudes(impares)
    guarda(nombre, sintetiza(amps))
    potencia = {n: A * A for n, A in amps.items()}
    centroide = sum(n * F0 * p for n, p in potencia.items()) / sum(potencia.values())
    info[nombre] = {'f0_Hz': F0, 'armonicos': {str(n): round(A, 4) for n, A in amps.items()},
                    'centroide_espectral_Hz': round(centroide, 1)}
json.dump(info, open('muestras.json', 'w'), indent=1, ensure_ascii=False)
print(json.dumps({k: v['centroide_espectral_Hz'] for k, v in info.items()}))

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 1. Configuración de parámetros de la señal
fs = 1000  # Frecuencia de muestreo (Hz)
t = np.linspace(0, 0.5, int(fs * 0.5), endpoint=False)  # 0.5 segundos de duración
N = len(t)
freqs = np.fft.rfftfreq(N, 1/fs)

# 2. Generación de componentes frecuenciales (5 Hz, 50 Hz, 120 Hz) + Ruido
np.random.seed(42)  # Para resultados reproducibles
f1, f2, f3 = 5, 50, 120
s1 = np.sin(2 * np.pi * f1 * t)
s2 = 0.5 * np.sin(2 * np.pi * f2 * t)
s3 = 0.4 * np.sin(2 * np.pi * f3 * t)
ruido = 0.5 * np.random.normal(size=len(t))

# Señal de entrada combinada
x = s1 + s2 + s3 + ruido  # Definición correcta de 'x'

# 3. Diseño de Filtros con SciPy (Butterworth)
# Pasa Bajos (LPF - 15 Hz)
sos_lpf = signal.butter(4, 15, btype='low', fs=fs, output='sos')
y_lpf = signal.sosfiltfilt(sos_lpf, x)

# Pasa Altos (HPF - 80 Hz)
sos_hpf = signal.butter(4, 80, btype='high', fs=fs, output='sos')
y_hpf = signal.sosfiltfilt(sos_hpf, x)

# Pasa Bandas (BPF - 40 a 60 Hz)
sos_bpf = signal.butter(4, [40, 60], btype='bandpass', fs=fs, output='sos')
y_bpf = signal.sosfiltfilt(sos_bpf, x)

# 4. Cálculo de Transformadas Rápida de Fourier (FFT)
X_fft = np.abs(np.fft.rfft(x)) * (2 / N)
Y_lpf_fft = np.abs(np.fft.rfft(y_lpf)) * (2 / N)
Y_hpf_fft = np.abs(np.fft.rfft(y_hpf)) * (2 / N)
Y_bpf_fft = np.abs(np.fft.rfft(y_bpf)) * (2 / N)

# 5. Visualización de Resultados (8 Paneles)
fig, axs = plt.subplots(4, 2, figsize=(10, 8), sharex='col')
fig.suptitle('Análisis y Evaluación de Filtros Digitales en Python', fontsize=12)

# Señal de Entrada
axs[0, 0].plot(t, x, color='gray')
axs[0, 0].set_title('Señal de Entrada (Tiempo)', fontsize=9)
axs[0, 0].set_ylabel('Amplitud', fontsize=8)
axs[0, 0].grid(True)

axs[0, 1].plot(freqs, X_fft, color='gray')
axs[0, 1].set_title('Espectro Entrada', fontsize=9)
axs[0, 1].set_ylabel('Magnitud', fontsize=8)
axs[0, 1].grid(True)

# Pasa Bajos
axs[1, 0].plot(t, y_lpf, color='blue')
axs[1, 0].set_title('Salida Pasa Bajos (Aísla 5 Hz)', fontsize=9)
axs[1, 0].set_ylabel('Amplitud', fontsize=8)
axs[1, 0].grid(True)

axs[1, 1].plot(freqs, Y_lpf_fft, color='blue')
axs[1, 1].set_title('Espectro LPF', fontsize=9)
axs[1, 1].set_ylabel('Magnitud', fontsize=8)
axs[1, 1].grid(True)

# Pasa Altos
axs[2, 0].plot(t, y_hpf, color='red')
axs[2, 0].set_title('Salida Pasa Altos (Aísla 120 Hz)', fontsize=9)
axs[2, 0].set_ylabel('Amplitud', fontsize=8)
axs[2, 0].grid(True)

axs[2, 1].plot(freqs, Y_hpf_fft, color='red')
axs[2, 1].set_title('Espectro HPF', fontsize=9)
axs[2, 1].set_ylabel('Magnitud', fontsize=8)
axs[2, 1].grid(True)

# Pasa Bandas
axs[3, 0].plot(t, y_bpf, color='green')
axs[3, 0].set_title('Salida Pasa Bandas (Aísla 50 Hz)', fontsize=9)
axs[3, 0].set_xlabel('Tiempo [s]', fontsize=8)
axs[3, 0].set_ylabel('Amplitud', fontsize=8)
axs[3, 0].grid(True)

axs[3, 1].plot(freqs, Y_bpf_fft, color='green')
axs[3, 1].set_title('Espectro BPF', fontsize=9)
axs[3, 1].set_xlabel('Frecuencia [Hz]', fontsize=8)
axs[3, 1].set_ylabel('Magnitud', fontsize=8)
axs[3, 1].grid(True)

plt.tight_layout()
plt.savefig('filtros_digitales.png', dpi=300)

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# 1. SEÑAL DE ENTRADA
fs = 1000                                      
nyquist = 0.5 * fs                             
t = np.linspace(0, 0.5, int(fs * 0.5))        

s1 = 1.0 * np.sin(2 * np.pi * 5 * t)           
s2 = 0.8 * np.sin(2 * np.pi * 50 * t)          
s3 = 0.5 * np.sin(2 * np.pi * 120 * t)         
ruido = np.random.normal(0, 0.2, len(t))

x = s1 + s2 + s3 + ruido                      

# 2. FILTROS
b_lpf, a_lpf = signal.butter(4, 15 / nyquist, btype='low')
y_lpf = signal.filtfilt(b_lpf, a_lpf, x)

b_hpf, a_hpf = signal.butter(4, 80 / nyquist, btype='high')
y_hpf = signal.filtfilt(b_hpf, a_hpf, x)

b_bpf, a_bpf = signal.butter(4, [35 / nyquist, 65 / nyquist], btype='bandpass')
y_bpf = signal.filtfilt(b_bpf, a_bpf, x)

# 3. ESPECTROS (FFT)
N = len(t)
freqs = np.fft.rfftfreq(N, d=1/fs)

X_fft = np.abs(np.fft.rfft(x)) * (2/N)
LPF_fft = np.abs(np.fft.rfft(y_lpf)) * (2/N)
HPF_fft = np.abs(np.fft.rfft(y_hpf)) * (2/N)
BPF_fft = np.abs(np.fft.rfft(y_bpf)) * (2/N)

# 4. FIGURA COMPACTA (figsize 9 x 7.5 para evitar el recorte)
plt.rc('font', size=7)
fig, axes = plt.subplots(4, 2, figsize=(9, 7.5))
fig.suptitle('Análisis y Comparación de Filtros Digitales', fontsize=10, fontweight='bold')

# FILA 1
axes[0, 0].plot(t, x, color='gray', linewidth=0.8)
axes[0, 0].set_title('Señal de Entrada (Tiempo)', fontsize=8)
axes[0, 0].grid(True)

axes[0, 1].plot(freqs, X_fft, color='gray', linewidth=0.8)
axes[0, 1].set_title('Espectro Entrada', fontsize=8)
axes[0, 1].grid(True)

# FILA 2
axes[1, 0].plot(t, x, color='gray', alpha=0.3, linewidth=0.7, label='Entrada')
axes[1, 0].plot(t, y_lpf, color='blue', label='Salida LPF', linewidth=1.2)
axes[1, 0].set_title('Pasa Bajos (5 Hz)', fontsize=8)
axes[1, 0].grid(True)
axes[1, 0].legend(loc='upper right', fontsize=6)

axes[1, 1].plot(freqs, X_fft, color='gray', alpha=0.3, linewidth=0.7)
axes[1, 1].plot(freqs, LPF_fft, color='blue', linewidth=1)
axes[1, 1].set_title('Espectro LPF', fontsize=8)
axes[1, 1].grid(True)

# FILA 3
axes[2, 0].plot(t, x, color='gray', alpha=0.3, linewidth=0.7, label='Entrada')
axes[2, 0].plot(t, y_hpf, color='red', label='Salida HPF', linewidth=1)
axes[2, 0].set_title('Pasa Altos (120 Hz)', fontsize=8)
axes[2, 0].grid(True)
axes[2, 0].legend(loc='upper right', fontsize=6)

axes[2, 1].plot(freqs, X_fft, color='gray', alpha=0.3, linewidth=0.7)
axes[2, 1].plot(freqs, HPF_fft, color='red', linewidth=1)
axes[2, 1].set_title('Espectro HPF', fontsize=8)
axes[2, 1].grid(True)

# FILA 4
axes[3, 0].plot(t, x, color='gray', alpha=0.3, linewidth=0.7, label='Entrada')
axes[3, 0].plot(t, y_bpf, color='green', label='Salida BPF', linewidth=1.2)
axes[3, 0].set_title('Pasa Bandas (50 Hz)', fontsize=8)
axes[3, 0].set_xlabel('Tiempo [s]', fontsize=7)
axes[3, 0].grid(True)
axes[3, 0].legend(loc='upper right', fontsize=6)

axes[3, 1].plot(freqs, X_fft, color='gray', alpha=0.3, linewidth=0.7)
axes[3, 1].plot(freqs, BPF_fft, color='green', linewidth=1)
axes[3, 1].set_title('Espectro BPF', fontsize=8)
axes[3, 1].set_xlabel('Frecuencia [Hz]', fontsize=7)
axes[3, 1].grid(True)

plt.tight_layout()
plt.savefig('filtros_digitales.png', dpi=120)
print("¡Listo! La figura ahora se ajusta al alto máximo del visor.")
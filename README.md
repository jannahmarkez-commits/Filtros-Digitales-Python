 # 📡 Diseño e Implementación de Filtros Digitales (FIR vs. IIR)

Este repositorio contiene la implementación en Python para el diseño, simulación y evaluación de filtros digitales pasa bajos, pasa altos y pasa bandas aplicados al procesamiento de señales y biopotenciales.

---

## 📂 Archivos del Repositorio

* `main_9_senales.py`: Código principal con la simulación completa y análisis de las 9 configuraciones de señales.
* `main_comparativo_2_senales.py`: Código focalizado en la comparación directa y superposición de 2 señales clave.
* `tipos de señales.png`: Gráfica del análisis espectral en tiempo y frecuencia.
* `final de comparacion 2.png`: Gráfica comparativa de señales superpuestas.

---

## 📊 Resultados y Análisis Gráfico

### 1. Análisis Espectral Completo
![Análisis Espectral](tipos%20de%20señales.png)

### 2. Comparativa Directa de Señales
![Comparativa](final%20de%20comparacion%202.png)



## 📌 Conclusiones del Proyecto

* **Dominio Teórico:** Se analizó la diferencia entre filtros FIR (estables y de fase lineal) e IIR (eficientes a menor orden computacional), así como la importancia del filtrado bidireccional (`filtfilt`) para preservar la morfología en biopotenciales sensibles como el electrocardiograma (ECG).
* **Análisis Espectral:** Mediante la Transformada Rápida de Fourier (FFT), se validó la separación espectral del sistema, logrando aislar con precisión las componentes frecuenciales requeridas (5 Hz, 50 Hz y 120 Hz).
* **Estabilidad Numérica:** Se implementaron Secciones de Segundo Orden (SOS) para garantizar estabilidad en los filtros IIR y mitigar errores de cuantización en el código.

---

## 📚 Referencias Bibliográficas

* **Oppenheim, A. V., & Schafer, R. W.** (2010). *Discrete-time signal processing* (3rd ed.). Pearson Higher Education.
* **Proakis, J. G., & Manolakis, D. G.** (2007). *Digital signal processing: Principles, algorithms, and applications* (4th ed.). Pearson Prentice Hall.
* **SciPy Community.** (2024). *Signal processing (scipy.signal)*. SciPy Reference Guide.

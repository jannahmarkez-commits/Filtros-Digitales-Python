 Diseño e Implementación de Filtros Digitales (FIR vs. IIR)

Este repositorio contiene la implementación en Python para el diseño, simulación y evaluación de filtros digitales aplicados al procesamiento de señales y biopotenciales.


 Archivos del Repositorio

* **`main_9_senales.py`**: Código principal con la simulación y análisis espectral completo.
* **`main_comparativo_2_senales.py`**: Código enfocado en la comparación directa de 2 señales.

---

 Resultados Gráficos

 1. Análisis Espectral de Señales
![Análisis Completo](tipos%20de%20señales.png)

 2. Comparativa Directa
![Comparativa](final%20de%20comparacion%202.png)




 Conclusiones
Dominio Teórico y Algorítmico:** Se analizó la diferencia entre filtros FIR (estables y de fase lineal) e IIR (eficientes a menor orden computacional), así como la importancia del filtrado bidireccional (`filtfilt`) para preservar la morfología del ECG sin distorsión de fase.
Análisis Espectral de Señales:** Mediante la Transformada Rápida de Fourier (FFT), se validó la separación espectral del sistema, logrando aislar con precisión las componentes frecuenciales requeridas.
Retos de Desarrollo Superados:** A pesar de la complejidad inicial para interpretar señales inmersas en ruido estocástico, se implementaron Secciones de Segundo Orden (SOS) para garantizar estabilidad numérica y mitigar errores de cuantización en el código.

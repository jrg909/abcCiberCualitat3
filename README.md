# Lenguajes/librerías usadas

* Python 3.5+
* NiaPy 1.0.2
* Matplotlib 3.0.2

# Instalación de NiaPy y Matplotlib en Linux

Suponiendo que una versión de python 3.5+ está instalada, se ejecuta el siguiente comando:

```bash
python3 -m pip install NiaPy matplotlib
```

# Instrucciones para ejecución en Linux y sus resultados
Abrir una terminal en el directorio raíz del repositorio y ejecutar:

```bash
python3 main.py
```

## Resultados
La ejecución producirá lo siguiente:
- Imprimirá en la consola el promedio y la desviación estándar del mejor punto solución y de su valor en la función a optimizar de 30 ejecuciones del algoritmo.
- Generará una imagen de extensión **.png** en la carpeta **figuras**, la cual grafica la evolución del promedio del valor de la función a optimizar en el punto solución vs. el número de iteraciones internas del algoritmo para 30 ejecuciones del mismo.
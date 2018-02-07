# Instalación de Python 3

## Instalación en Windows

Para instalar *Python* en Windows lo más sencillo es hacerlo descargando e instalando **Anaconda** ya que incluye muchos paquetes que vamos a estar utilizando.

### Paso a paso

Pueden seguir el paso a paso o usar el video [Tutorial de instalación](https://www.youtube.com/watch?v=A91AB14BIz8)

 - [Descargar el Instalador de Anaconda](https://www.continuum.io/downloads)

Escoger la versión para **Python 3.6** en `64-Bit` o `32-Bit` según tu equipo.

![][conda_1]

[conda_1]: ../.images/anaconda_downloader.png

 - Una vez descargado dar click para Instalar
 - Dar Siguiente
 - Aceptar Términos y Condiciones
 - Selecciona la instalación única ("Just Me") y da click en Siguiente
 - Selecciona el folder de instalación y presiona Siguiente

![][conda_2]

[conda_2]: ../.images/anaconda_file.png
 - Deselecciona *Agregar a Anaconda el PATH de variables de entorno*
 - Selecciona únicamente la Opción de usar Anaconda como default de Python 3.6

![][conda_3]

[conda_3]: ../.images/anaconda_conf.png

 - Click en Instalar
 - Y una vez terminado el proceso presiona Finalizar.

## Instalación en Ubuntu 

*Python* está instalado nativamente sobre las distribuciones de Ubuntu, únicamente es importante revisar la versión que tiene ya instalada. Para esto simplemente abran una terminal con las teclas `Ctrl + Alt  + T` o entrando al buscador de Ubuntu, tecleando `terminal` y seleccionando el ícono marcado en la imagen de abajo.

![][term_1]

[term_1]: ../.images/terminal_ss.png

Y ahora una vez abierta la consola, ejecutar `python3` y se desplegará la terminal interactiva donde se puede revisar la versión que está corriendo de *Python*. 

```bash
	Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
	[GCC 5.4.0 20160609] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> 
```

¡Todo listo!, para salir de la terminal interactiva escribe `exit()` y teclea `Enter` o presiona `Ctrl + D`.

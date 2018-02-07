# Instalación de Ubuntu en Máquina Virtual para Windows 10

Tutorial en video completo [aquí](https://www.youtube.com/watch?v=uV5boDESAe0)

## Descarga de la imagen ISO de Ubuntu 14.04

 - Ir al [sitio](http://releases.ubuntu.com/14.04/) para descargar la imágen ISO de Ubuntu Desktop 14.04 LTS. 
 - Descargar la opción `amd64` para máquinas de 64 bits y `i386` para máquinas de 32 bits.

## Instalación Virtualbox

Para poder correr Ubuntu 14.04 LTS por medio de una máquina virtual, se necesita primero instalar [VirtualBox](https://www.virtualbox.org/) .

 - Descargar archivos para Windows desde la página de [VirtualBox](https://www.virtualbox.org/)
   - Seleccionar Windows Hosts (Automáticamente descarga archivo .exe)
 - Ejecutar archivo .exe para instalar VirtualBox
 - Una vez instalado abrir la aplicación de Virtualbox.

## Crear nueva máquina virtual

*VM - Virtual Machine*

 - Dentro de VirtualBox dar click en el botón `New`
 - Escribir el *Nombre* de la VM, *Tipo*: Linux, *Version*: Ubuntu (32 ó 64), Click en `Next`
 - Asignar Memoria RAM según el tamaño de su máquina, mínimo 512 MB. Click en `Next`
 - Seleccionar la opción, Crear un disco duro virtual ahora. Click en `Next`
 - Escoger VirtaulBox Disk Image. Click en `Next`
 - Escoger Tamaño fijo. Click en `Next`
 - Definir nombre al Disco Duro Virtual y tamaño. Mínimo 10GB. Click en `Crear`
 - Selecciona la VM recién creada, y ve a Settings/Configuración.
 - Ve a Almacenamiento, ahora en Controlador IDE presiona en el disco superior derecho para agregar una Unidad. 
   - Navega hasta la ubicación de la Imagen descargada de ISO de Ubuntu y da click en aceptar.
 - Una vez agregada la imagen ISO, da click en Iniciar.
 - Ahora qué estes en la pantalla de configuración de Ubuntu, selecciona Instalar Ubuntu.
 - Da Click en siguiente para las configuraciones preestablecidas
 - Escoge Borrar disco e instalar Ubuntu, y click en Instalar ahora.
 - Por último, configura el nombre del equipo, usuario y contraseña a tu gusto y espera a qué termine de instalar.

Es probable que se reinicie un par de veces la ventana de VirtualBox antes de abrir la pantalla de Log In de Ubuntu.
Si llegaste al Login, la instalación fue hecha correctamente.



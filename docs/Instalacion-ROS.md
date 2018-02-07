# Instalación de ROS

Éste archivo incluye los procesos de instalación de ROS Indigo para en Ubuntu 14.04.

--- 

### Para [Ubuntu 14.04](http://wiki.ros.org/indigo/Installation/Ubuntu)

 - Configurar lista de fuentes para aceptar *packages.ros.org*

```
	sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

 - Agregar Llaves del servidor

```
	sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
```

En caso de tener errores de conexión, cambiar el parámetro `--keyserver` por `hkp://pgp.mit.edu:80` ó `hkp://keyserver.ubuntu.com:80`

---

---


### ROS en VM

<http://nootrix.com/diy-tutos/virtualizing-ros/>
<http://nootrix.com/downloads/#RosVM>
<http://nootrix.com/diy-tutos/getting-started-ros/>

## Documento pendiente por terminar ...


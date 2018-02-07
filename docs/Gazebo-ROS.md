# Gazebo ROS

Documento para utilizar ROS con Gazebo. (Versión verificada para ROS Indigo y Ubuntu 14.04).

>>>

Revisar el funcionamiento de Gazebo con el siguiente comando:

```bash
    gazebo
```

 - En caso de ver errores en la consola o sólo visualizar la pantalla negra dentro del simulador de Gazebo. Ejecutar lo siguiente:

```bash
    cd ~/
    cp <RUTA_AL_REPOSITORIO>/code/bash-scripts/gazebo_mod.sh ~/
    source gazebo_mod.sh
```
*Éste archivo descargará todos los modelos de Gazebo y puede tardar unos 30 min.*


>>>

Ahora instalar los siguientes paquetes de ROS externos:

```bash
    sudo apt-get install ros-indigo-urdf-sim-tutorial
    sudo apt-get install ros-indigo-controller-manager
    sudo apt-get install ros-indigo-join-state-publisher
    sudo apt-get install ros-indigo-join-state-controller
    sudo apt-get install ros-indigo-robot-state-publisher
``` 

>>>

Y ejecutar el siguiente comando para poder visualizar el robot R2D2 y moverlo a través del UI que despliega:

```bash
    roslaunch urdf_sim_tutorial 13-diffdrive.launch
```





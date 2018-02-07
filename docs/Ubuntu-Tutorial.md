
# Manejo básico de Ubuntu

Descripción a detallo de sistemas [Unix](https://www.tutorialspoint.com/unix/)

## Comandos básicos

```bash
	ls  #  Lista los elementos de un directorio
	ls -a # Lista todos los elementos de un directorio (incluso ocultos)
	ls -l  # Lista elementos con permisos, número de elementos, usuario, tamaño y fecha

	whoami  # Muesta usuario loggeado
	users   # Lista los usuarios
	pwd  # Imprime localización actual (Current path)

	halt  # Apaga el sistema inmediatamente
	poweroff   # Apaga el sistema
	reboot  # Reinicia el sistema

	clear  # Limpia pantalla
	man [comando] # Abre el manual del comando

	find Archivo.* # Busca archivos

	vi [nombre_archivo]  # Crea y abre el editor vi
	nano [nombre_archivo] # Crea y abre editor nano

	cat # Muestra contenido de un archivo

	wc # Cuenta palabras de un archivo

	cp [origen] [destino] # Copiar archivos e origen a destino
	mv [origen] [destino]  # Mueve o renombra archivos o directorios
	rm [archivo] # Borrar archivos
	

	cd [directorio]  # Cambio de directorio
	mkdir [directorio] # Crear directorio
	rm -r ó rmdir [directorio] # Borrar directorio
	cp -r [origen] [destino]  # Copia directorios con contenido
	chmod a+x [file]  # Cambiar permisos para (a, o, g, u) y agregar accesos (x,r,w)

	echo [argumento] # Muestra argumento

	grep [argumento] #  Imprime lo que cumpla con la expresión regular
```

## Variables de entorno

```bash
	$TEST="UNIX ENV VAR" # Asigna variable de entorno
	export TEST="UNIX VAR" # Asigna variable de entorno
	echo $TEST  # Muestra contenido de variable de entorno

```

## Procesos

```bash
	ls -l & ## Corre comando en el Background
	ps  # Lista procesos corriendo
	kill [PID]  # Terminar Procesos
```

## Redes

```bash
	ping [hostname]   # Echo request a un host
```

## Bash Scripts

Los archivos de Shell tienen extension `.sh` y es necesario cambiar los permisos de ejecución para poderlos correr.

*Ejemplo:*

Escribe el siguienet snippet en un archivo con nombre `escribe-ip.sh`.

```bash
	originalAddress=@(ifconfig | grep “inet addr” | head –n 1 | cut –d “:” –f 2 | cut –d “ “ –f 1)
 
	echo $originalAddress 
```

o éste otro

```bash
	#!/bin/sh

	# Author : Jorge Viz 
	# Script follows here:

	echo "What is your name?"
	read PERSON
	echo "Hello, $PERSON"
```

Ahora cambia los permisos para habilitar la ejecución.

```bash
	chmod a+x escribe-ip.sh
```

### Bash Syntaxis

```bash
	NAME="hola"   # Asignar variable
	echo $NAME    # Mostrar variable
	readonly NAME   # Asignar de solo lectura
	unset NAME  # Liberar variable de memoria

	# Parametros del Shell
	#!/bin/sh

	echo "File Name: $0"
	echo "First Parameter : $1"
	echo "Second Parameter : $2"
	echo "Quoted Values: $@"
	echo "Quoted Values: $*"
	echo "Total Number of Parameters : $#"

	# If else
	#!/bin/sh

	a=10
	b=20

	if [ $a == $b ]
	then
	   echo "a is equal to b"
	elif [ $a -gt $b ]
	then
	   echo "a is greater than b"
	elif [ $a -lt $b ]
	then
	   echo "a is less than b"
	else
	   echo "None of the condition met"
	fi

	# For loop
	#!/bin/sh

	for TOKEN in $*
	do
	   echo $TOKEN
	done

	# Arrays 
	#!/bin/sh

	NAME[0]="Zara"
	NAME[1]="Qadir"
	NAME[2]="Mahnaz"
	NAME[3]="Ayan"
	NAME[4]="Daisy"
	echo "First Index: ${NAME[0]}"
	echo "Second Index: ${NAME[1]}"
```

#### Bash Operations

[Arithmetic & Boolean Operations](https://www.tutorialspoint.com/unix/unix-basic-operators.htm)

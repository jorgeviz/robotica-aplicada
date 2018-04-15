#!/bin/bash

NAME="hola"   # Asignar variable
echo $NAME    # Mostrar variable
#readonly NAME   # Asignar de solo lectura
#unset NAME  # Liberar variable de memori

echo "-----------------"

# parametros del script
echo "File Name: $0"
echo "First Param: $1"
echo "Second Param: $2"
echo "Quoted Values as String: $@"
echo "Quoted Values as Array: $*"
echo "Total Number of Parameters: $#"

echo "-----------------"

echo "If else"
# If else
a=$1
b=$2

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

echo "-----------------"
echo "For each loop"
# For loop
for TOKEN in $*
do
   echo $TOKEN
done

echo "-----------------"
echo "For loop"
for ((i=0; i<4; i++))
do
	echo $i
done


# Arrays 
NAME[0]="Zara"
NAME[1]="Qadir"
NAME[2]="Mahnaz"
NAME[3]="Ayan"
NAME[4]="Daisy"
echo "First Index: ${NAME[0]}"
echo "Second Index: ${NAME[1]}"
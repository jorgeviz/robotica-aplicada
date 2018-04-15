#!/bin/bash
# Esta linea parsea la IP local
originalAddress=$(ifconfig | grep "inet" | grep "addr" | head -n 1 | cut -d ":" -f 2 | cut -d " " -f 1)
# Muestra la Variable con la IP
echo $originalAddress 
